from socket import *
s = socket()
s.bind(("0.0.0.0",8008))
s.listen(5)
c,addr = s.accept()
# print(addr)
data = c.recv(4096)
# print(data.decode())


data2 ="""HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello</h1>
"""
c.send(data2.encode())

c.close()
s.close()