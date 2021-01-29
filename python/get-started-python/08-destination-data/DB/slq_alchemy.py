""" Test Module """

#!/usr/bin/env python3

if __name__ == "__main__":
    import sqlalchemy as sa
    # DBを作り，メモリ内にその記憶領域(storage)を作る．
    # 引数の文字列は，"sqlite:///:memory:'でもよい

    ### エンジンレイヤ
    conn = sa.create_engine('sqlite://')

    # 3つの列を持つzooテーブルを作る
    print(conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)'''))

    # データ挿入のためのプレースホルダーと，3件の挿入
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    conn.execute(ins, 'duck', 10, 0.0)
    conn.execute(ins, 'bear', 2, 1000.0)
    conn.execute(ins, 'weasel', 1, 20000.0)

    # データ取得
    # SQLAlchemyでは，rowsはリストではなく，直接表示できないResultProxyというものになっている
    rows = conn.execute('SELECT * FROM zoo')

    print(rows)

    # iterableなので，ループで処理できる
    for row in rows:
        print(row)

    ### SQL表現言語
    meta = sa.MetaData()
    zoo2 = sa.Table('zoo2', meta,
        sa.Column('critter', sa.String, primary_key=True),
        sa.Column('count', sa.Integer),
        sa.Column('damages', sa.Float)
    )

    # zoo2はSQLデータベースの世界とPythonデータ構造の世界を橋渡しする
    meta.create_all(conn)

    # データ挿入 zoo2の定義がここで生きるようだ
    conn.execute(zoo2.insert(('bear', 2, 1000.0)))
    conn.execute(zoo2.insert(('weasel', 1, 2000.0)))
    conn.execute(zoo2.insert(('duck', 10, 0)))

    result = conn.execute(zoo2.select())

    rows = result.fetchall()
    print(rows)
    for row in rows:
        print(row)

    ### ORM
    # ORMではもう一つimportが必要になる
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Zoo3(Base):
        """ Test Class """
        # Table name
        __tablename__= 'zoo3'

        # column
        critter = sa.Column('critter', sa.String, primary_key=True)
        count = sa.Column('count', sa.Integer)
        damages = sa.Column('damages', sa.Float)

        def __init__(self, critter, count, damages):
            self.critter = critter
            self.count = count
            self.damages = damages

        def __repr__(self):
            return "<Zoo3({}, {}, {})>".format(self.critter, self.count, self.damages)

        def __str__(self):
            return "this is not str object"

    # 次の行で手品のようにデータベースとテーブルが作られる
    Base.metadata.create_all(conn)

    first = Zoo3('duck', 10, 0.0)
    second = Zoo3('bear', 2, 1000.0)
    third = Zoo3('weasel', 1, 2000.0)
    print('farst', first)

    # マジックメソッドでちょっと遊ぶ
    print("What is this - " + str(first))

    # データベースとのやり取りするためのセッションを作る
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=conn)
    ses = Session()

    # セッション内で先程作った3つのオブジェクトをDBに書き込む
    # add() 関数は1個のオブジェクトを追加し，add_all()関数はリストを追加する
    print(type(ses.add))
    ses.add(instance=first)
    ses.add_all([second, third])

    # 最後にcommitして処理を完了させる
    ses.commit()
