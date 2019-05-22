"""
广播收
1创建套接字
2 选择接受端口
3 设置套接字可以接受广播
"""
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind(("0.0.0.0",9999))
while True:
    try:
        data,addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    else:
        print(data.decode(),addr)

s.close()