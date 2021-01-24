#!/usr/bin/env python3

import unicodedata

if __name__ == "__main__":
    # 7-1
    mystery = '\U0001f4a9'
    print(mystery)
    m_name = unicodedata.name(mystery)
    print(m_name)

    # 7-2
    pop_bytes = bytes(mystery, 'utf-8')
    print(pop_bytes)

    # 7-3
    pop_string = pop_bytes.decode('utf-8')
    print(pop_string)

    # 7-4
    letter: str = '''
    Dear {salutation} {name},

    Thank you for your letter. We are sorry that our {product} {verbed} in your 
    {room}. Please note that it should never be used in a {room}, especially
    near any {animals}.

    Send us your receipt and {amount} for shipping and handling. We will send
    you another {product} that, i our tests, is {percent}% less likery to
    have {verbed}.

    Thank you for your support.

    Sincerely.
    {spokeman}
    {job_title}
    '''

    # 7-5
    response = {
        'salutation': 'what?',
        'name': 'miyako',
        'product': 'enough',
        'verbed': 'verbed',
        'room': '103',
        'animals': 'gnu',
        'amount': 'big',
        'percent': '2500',
        'spokeman': 'Hi',
        'job_title': 'I fine thank you'
    }
    
    print(letter.format(**response))