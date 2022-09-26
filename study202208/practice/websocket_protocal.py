from websocket import create_connection
def webscoket_protcoal():
    #连接websocket服务时会收获第一次响应信息
    ws_obj=create_connection("ws://tech01.ceba.ceshiren.com:10000/websocket")
    #对websocket服务发起请求，会获取第二次响应信息
    ws_obj.send("hello,Hogwarts ~~~")
    ws_obj.send("hello,Hogwarts2 ~~~")
    #获取响应信息
    print(ws_obj.recv())
    print(ws_obj.recv())
    print(ws_obj.recv())
    #关闭连接
    ws_obj.close()

if __name__=='__main__':
    webscoket_protcoal()