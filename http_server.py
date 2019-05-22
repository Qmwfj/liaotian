"""
将浏览器发送给网页展示
"""

from socket import *

def handle(coonfd):
    print("请求来自",coonfd.getpeername())
    request = coonfd.recv(4096)  #接受http请求
    #防止客户端断开
    if not request:
        return
    #将request按行分割
    request_line = request.splitlines()[0].decode()
    #获取请求内容
    info = request_line.split(" ")[1]
    if info == "/":
        f = open("../day3/index.html")
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>sorry</h1>"
    coonfd.send(response.encode())

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8880))
    sockfd.listen(5)
    while True:
        coonfd,addr = sockfd.accept()
        handle(coonfd)
        coonfd.close()
        print(addr)
if __name__ == '__main__':
    main()