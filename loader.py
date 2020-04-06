#coding: utf-8
import os
import socket

def load(title, text, classificator, link='', img=None):
    text_record = f"""
    \t<!-- record -->
    \t
    \t<div class='record-text'>
    \t\t<rtitle>{title}</rtitle>
    \t\t<rtext>{text}</rtext>
    \t\t<rlink>{link}</rlink>
    \t</div>
    """.encode('utf-8')

    img_record = f"""
    \t\t\t<div class='record-text'>
        \t\t\t\t<rtitle>{title}</rtitle>
        \t\t\t\t<rtext>{text}</rtext>
        \t\t\t\t<rimg><img src='{img}'></rimg>
        \t\t\t\t<rlink>ссылка</rlink>
    \t\t\t</div>
  
    """

    if classificator == 1:
        data = text_record
    else:
        data = img_record

    with open('scroll/index.html', 'r', encoding='utf-8') as source:
        lines = source.readlines()
        for i, line in enumerate(lines):
            if line.strip() == '<!-- record -->':
                insert_index = i
    
        lines.pop(insert_index)
        lines.insert(insert_index, data.decode('utf-8'))

    os.remove('scroll/index.html')
    with open('scroll/index.html', 'w', encoding='utf-8') as result:
        result.writelines(lines)

sock = socket.socket()
sock.bind(('90.156.201.47', 8080))
sock.listen(1)
conn, addr = sock.accept()

while True:
    title, text, classificator, *kwargs = conn.recv(8096).decode('utf-8').split()

    load(title, text, classificator)
    conn.send("success")

sock.close()
