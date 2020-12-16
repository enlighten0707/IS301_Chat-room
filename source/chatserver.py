import wx
import socket
import threading
import struct


class MyFrameServer(wx.Frame):
    # We simply derive a new class of Frame.
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, pos=(100, 20), size=(400, 600))
        panel = wx.Panel(self)

        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        self.font1 = wx.Font(40, wx.ROMAN, wx.ITALIC, wx.NORMAL, False)
        self.ipshuru = wx.StaticText(panel, -1, "Ip: ", (20, 105))
        self.portshuru = wx.StaticText(panel, -1, "port：", (200, 105))
        self.show_text = wx.StaticText(panel, -1, "SERVER", (100, 23))
        self.show_text.SetFont(self.font1)


        # text window
        self.ip_input = wx.TextCtrl(panel, pos=(50, 100), size=(110, 25))
        self.port_input = wx.TextCtrl(panel, pos=(250, 100), size=(80, 25))

        self.message_output = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(10, 180), size=(365, 345))
        # buttons
        self.start_button = wx.Button(panel, label=u'start', pos=(20, 130), size=(160, 35))
        self.stop_button = wx.Button(panel, label=u'stop', pos=(200, 130), size=(160, 35))
        self.exit_button = wx.Button(panel, label=u'quit', pos=(280, 530), size=(100, 30))

        self.clear_button = wx.Button(panel, label=u'clear all', pos=(10, 530), size=(250, 30))

        # bind the buttons with functions
        self.Bind(wx.EVT_BUTTON, self.exit, self.exit_button)
        self.Bind(wx.EVT_BUTTON, self.start, self.start_button)
        self.Bind(wx.EVT_BUTTON, self.stop, self.stop_button)
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_button)

        self.listenFlag = False
        self.user_change_flag = False
        self.serverDic = {}
        self.socketDic = {}

        self.Show(True)

    def OnEraseBack(self,event):
        dc=event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect=self.GetUpdateRegion().GetBox()
            dc.SetclippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("./pic/2_1.jpg")
        dc.DrawBitmap(bmp,0,0)

    # 要加上event参数
    def exit(self, event):
        self.Close(True)

    # 创建一个新的thread进程来执行监听中的accept函数，等待客户端的连接
    def start(self, event):
        self.serverDic["Server"] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverDic["Server"].bind((self.ip_input.GetValue(), int(self.port_input.GetValue())))
        if not self.listenFlag:
            self.listenFlag = True
            self.serverDic["Server"].listen(5)
            self.message_output.AppendText('Waiting for connection...\n')
            # 开始创建一个线程来监听客户端的连接
            t1 = threading.Thread(target=self.listen, args=())
            t1.start()

    def stop(self, event):
        if self.serverDic:
            self.serverDic["Server"].close()
            del self.serverDic["Server"]
            self.message_output.AppendText("stop listening...\n")
        else:
            self.message_output.AppendText("has already stopped listening\n")

    def listen(self):
        while True:
            # 接受一个新连接:accept函数会一直等待直到接收到连接
            sock, addr = self.serverDic["Server"].accept()
            # 创建一个新线程来处理与客户端的连接:
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

    def clear(self, event):
        self.message_output.Clear()

    # 创建一个sock来处理与客户端的连接
    def tcplink(self, sock, addr):
        sock_name = sock.recv(1024).decode('utf-8')
        self.socketDic[sock_name] = sock
        self.message_output.AppendText("%s logged in successfully!\n" % sock_name)

        tem = ""# 存储在线人的id
        for Key in self.socketDic.keys():
            tem = tem + Key + "\n"
        for Key in self.socketDic.keys():
            self.socketDic[Key].send("userupdate".encode('utf-8'))
            self.socketDic[Key].send(tem.encode('utf-8'))

        while True:
            #mode: sendmess-----发送消息
            #mode: sendfile-----发送文件
            #mode: exit-----退出

            mode = sock.recv(1024).decode('utf-8')

            # 当用户下线时，他会向服务端发送exit信息
            if mode == "exit":
                break
            elif mode == "group":
                # groupmessage=sock.recv(1024).decode('utf-8')
                # for onlinename in self.socketDic.keys():
                #     self.socketDic[onlinename].send((groupmessage).encode('utf-8'))
                #     self.socketDic[onlinename].send((sock_name+": "+groupmessage+"\n").encode('utf-8'))
                towho_message = sock.recv(1024).decode('utf-8')
                towho, message = towho_message.split("-*-")
                for onlinename in self.socketDic.keys():
                    if onlinename != towho:
                        self.socketDic[onlinename].send("message".encode('utf-8'))
                        self.socketDic[onlinename].send((sock_name + ": " + message + "\n").encode('utf-8'))

            elif mode == "sendmess":
                towho_message = sock.recv(1024).decode('utf-8')
                towho, message = towho_message.split("-*-")
                for onlinename in self.socketDic.keys():
                    if onlinename == towho:
                        self.socketDic[onlinename].send("message".encode('utf-8'))
                        self.socketDic[onlinename].send((sock_name + ": " + message + "\n").encode('utf-8'))

            elif mode == "sendfile":
                towho = sock.recv(1024).decode('utf-8')
                for onlinename in self.socketDic.keys():
                    if onlinename == towho:
                        self.socketDic[onlinename].send("sendfile".encode('utf-8'))
                        self.socketDic[onlinename].send(sock_name.encode('utf-8'))
                        fileinfo_size = struct.calcsize('128sl')
                        buf = sock.recv(fileinfo_size)
                        self.socketDic[onlinename].send(buf)
                        if buf:
                            filename, filesize = struct.unpack('128sl', buf)
                            recvd_size = 0  # 定义已接收文件的大小
                            while not recvd_size == filesize:

                                if filesize - recvd_size > 1024:
                                    data = sock.recv(1024)
                                    self.socketDic[onlinename].send(data)
                                    recvd_size += len(data)
                                else:
                                    data = sock.recv(filesize - recvd_size)
                                    self.socketDic[onlinename].send(data)
                                    recvd_size = filesize

        self.message_output.AppendText("%s logged out!\n" % sock_name)
        # 生成新的在线人ID
        tem = ""
        for Key in self.socketDic.keys():
            if Key != sock_name:
                tem = tem + Key + "\n"
        # 当一个用户下线时，像其它所有的在线用户发送新的在线人信息
        for Key in self.socketDic.keys():
            if Key != sock_name:
                self.socketDic[Key].send("userupdate".encode('utf-8'))
                self.socketDic[Key].send(tem.encode('utf-8'))

        sock.close()
        del self.socketDic[sock_name]


app = wx.App(False)
frame = MyFrameServer(None, "server")
app.MainLoop()

