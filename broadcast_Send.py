"""
发送广播
"""
from socket import *
from time import *

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
dest = ("176.209.104.255",9999)
data = "大家好我是张文虎,我 很帅，我很嫩"

while True:
    sleep(1)
    s.sendto(data.encode(),dest)

s.close()


