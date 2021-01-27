#!/usr/bin/env python3

if __name__ == "__main__":

    # xml
    xml_text = """<?xml version="1.0"?>
<menu>
    <breakfast hours='7-11'>
        <item price='$6.00'>breakfast burriros</item>
        <item price='$4.00'>pancakes</item>
    </breakfast>
    <lunch hours='11-3'>
        <item price='$5.00'>hamburger</item>
    </lunch>
    <dinner hours='3-10'>
        <item price='8.00'>spaghetti</item>
    </dinner>
</menu>
    """

    with open('menu.xml', 'wt') as fout:
        fout.write(xml_text)

    import xml.etree.ElementTree as et
    tree = et.ElementTree(file='menu.xml')
    root = tree.getroot()
    print('root.tag', root.tag)

    for child in root:
        print('tag:', child.tag, ', attributes:', child.attrib)
        for grandchild in child:
            print('\ttag:', grandchild.tag, ', attributes:', grandchild.attrib)

    print('root(menu)セクションの数', len(root))
    print('root[0](breakfast)の項目の数', len(root[0]))

    