import wx
import socket
import threading
import os
import struct

class MyFrameClient(wx.Frame):
    """ We simply derive a new class of Frame. """

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, pos=(100, 20), size=(550, 590))
        panel = wx.Panel(self)
        self.name = "<anonymous user>"

        #self.panel=wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

        self.font1 = wx.Font(28, wx.ROMAN, wx.ITALIC, wx.NORMAL, False)
        self.text1 = wx.StaticText(panel, -1, "ip：", (50, 75))
        self.text2 = wx.StaticText(panel, -1, "port：", (50, 105))
        self.text3 = wx.StaticText(panel, -1, "chatclient", (200, 10))
        self.text3.SetFont(self.font1)
        #self.text4 = wx.StaticText(panel, -1, "----------------------------------------------", (50, 10))
        self.text4 = wx.StaticText(panel, -1, "----------------------------------------------", (50, 50))
        #self.text4 = wx.StaticText(panel, -1, "----------------------------------------------", (250, 10))
        self.text4 = wx.StaticText(panel, -1, "-----------------------------------------------------", (250, 50))
        self.name_text = wx.StaticText(panel, -1, "username:", (50, 135))
        self.to_who_mess = wx.StaticText(panel, -1, "to: ", (50, 375))

        '''new'''
        self.to_who_file = wx.StaticText(panel, -1, "to: ", (50, 226))

        self.who_online = wx.StaticText(panel, -1, "online users:", (50, 410))
        # text window
        self.server_ip_input = wx.TextCtrl(panel, pos=(100, 70), size=(110, 25))
        self.server_port_input = wx.TextCtrl(panel, pos=(100, 100), size=(110, 25))
        self.name_input = wx.TextCtrl(panel, pos=(120, 130), size=(90, 25))
        self.send_to = wx.TextCtrl(panel, pos=(70, 370), size=(80, 30))

        '''new'''
        self.file_path_show = wx.TextCtrl(panel, pos=(50, 192), size=(100, 28))
        self.send_to2 = wx.TextCtrl(panel, pos=(70, 222), size=(80, 28))

        self.message_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(50, 260), size=(160, 100))
        self.message_output = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, pos=(250, 70),
                                          size=(270, 430))
        self.user_show = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(50, 435), size=(160, 110))
        # buttons
        self.send_button = wx.Button(panel, label=u'send message', pos=(160, 370), size=(90, 30))

        self.group_button = wx.Button(panel,label=u'group',pos=(160,405),size=(90,30))

        self.login_button = wx.Button(panel, label=u'log in', pos=(50, 163), size=(70, 25))
        self.logout_button = wx.Button(panel, label=u'log out', pos=(140, 163), size=(70, 25))
        self.exit_button = wx.Button(panel, label=u'quit', pos=(430, 510), size=(100, 30))
        self.clear_button = wx.Button(panel, label=u'clear all', pos=(250, 510), size=(170, 30))

        '''new'''
        self.select_file_button = wx.Button(panel, label=u'file upload', pos=(160, 190), size=(90, 30))
        self.send_file_button = wx.Button(panel, label=u'send files', pos=(160, 220), size=(90, 30))

        # bind the buttons with functions
        self.Bind(wx.EVT_BUTTON, self.exit, self.exit_button)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_button)
        self.Bind(wx.EVT_BUTTON, self.sendfile, self.send_file_button)
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_button)
        self.Bind(wx.EVT_BUTTON, self.log_in, self.login_button)
        self.Bind(wx.EVT_BUTTON, self.log_out, self.logout_button)
        self.Bind(wx.EVT_BUTTON, self.selectfile, self.select_file_button)

        self.Bind(wx.EVT_BUTTON,self.group,self.group_button)
        # print("\033[41;1m write something here \033[0m")

        self.connectFlag = False
        self.socketDict = {}
        self.Show(True)

    def OnEraseBack(self,event):
        dc=event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect=self.GetUpdateRegion().GetBox()
            dc.SetclippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("1_1.jpg")
        dc.DrawBitmap(bmp,0,0)


    def log_in(self, event):
        if not self.connectFlag:
            self.connectFlag = True
            self.name = "<" + self.name_input.GetValue() + ">"
            self.socketDict[self.name] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketDict[self.name].connect((self.server_ip_input.GetValue(), int(self.server_port_input.GetValue())))
            self.socketDict[self.name].send(self.name.encode('utf-8'))
            t1 = threading.Thread(target=self.handle, args=())
            t1.start()
        else:
            self.message_output.AppendText("you are already inline\n")

    # 要加上event参数

    def log_out(self, event):
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
            del self.socketDict[self.name]
            # self.message_output.AppendText(self.name+"logged out!\n")
            self.user_show.Clear()
            self.name = "<anonymous user>"
        else:
            self.message_output.AppendText("you are already offline\n")

    def exit(self, event):
        # 在关闭客户端时也能够发送消息给服务端，让服务端的线程结束
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
            #del self.socketDict[self.name]
            # self.message_output.AppendText(self.name+"logged out!\n")
            #self.user_show.Clear()
            #self.name = "<anonymous user>"
        else:
            self.message_output.AppendText("you are already offline\n")
        self.Close(True)

    def send(self, event):
        if self.connectFlag:
            # self.message_output.AppendText(self.name+":")
            # self.message_output.AppendText(self.message_input.GetValue()+"\n")
            # self.message_input.Clear()
            if self.message_input.GetValue() and self.send_to.GetValue():
                self.socketDict[self.name].send(("sendmess").encode('utf-8'))
                self.socketDict[self.name].send(("<" + self.send_to.GetValue() + ">" + "-*-" +
                                                 self.message_input.GetValue()).encode('utf-8'))
                self.message_input.Clear()
        else:
            self.message_output.AppendText("you are offline!\n")

    def group(self,event):
        if self.connectFlag:
            if self.message_input.GetValue():
                self.socketDict[self.name].send(("group").encode('utf-8'))
                #self.socketDict[self.name].send((self.message_input.GetValue()).encode('utf-8'))
                self.socketDict[self.name].send(("<" + self.name + ">" + "-*-" +
                                                 self.message_input.GetValue()).encode('utf-8'))
                self.message_input.Clear()
            else:
                self.message_output.AppendText("wrong")
        else:
            self.message_output.AppendText("you are offline!\n")


    def sendfile(self, event):
        if self.connectFlag:
            self.socketDict[self.name].send("sendfile".encode('utf-8'))
            self.socketDict[self.name].send(("<"+self.send_to2.GetValue()+">").encode('utf-8'))
            filepath = self.file_path_show.GetValue()
            if os.path.isfile(filepath):
                fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'),
                                    os.stat(filepath).st_size)
                self.socketDict[self.name].send(fhead)
                #self.message_output.AppendText('client filepath: {0}\n'.format(filepath))

                fp = open(filepath, 'rb')
                while 1:
                    data = fp.read(1024)
                    if not data:
                        self.message_output.AppendText('{0} file send over...\n'.format(filepath))
                        break
                    self.socketDict[self.name].send(data)
        else:
            self.message_output.AppendText("you are offline!\n")

    def handle(self):
        while True:
            if self.connectFlag:
                mode = self.socketDict[self.name].recv(1024).decode('utf-8')
                if mode == "message":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')
                    self.message_output.AppendText(messtext)
                elif mode == "userupdate":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')
                    self.user_show.Clear()
                    self.user_show.AppendText(messtext)
                elif mode == "sendfile":
                    send_user_name = self.socketDict[self.name].recv(1024).decode('utf-8')
                    fileinfo_size = struct.calcsize('128sl')
                    buf = self.socketDict[self.name].recv(fileinfo_size)
                    if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        # self.message_output.AppendText(str(type(filename)))
                        fn = filename.strip(b'\00')
                        new_filename = os.path.join('./', 'new2_' + fn.decode('utf-8'))
                        self.message_output.AppendText(send_user_name+"sended you a file\n")
                        self.message_output.AppendText('Filesize is {0}\n'.format(filesize))
                        recvd_size = 0  # 定义已接收文件的大小
                        fp = open(new_filename, 'wb')
                        self.message_output.AppendText('start receiving...\n')

                        while not recvd_size == filesize:
                            if filesize - recvd_size > 1024:
                                data = self.socketDict[self.name].recv(1024)
                                recvd_size += len(data)
                            else:
                                data = self.socketDict[self.name].recv(filesize - recvd_size)
                                recvd_size = filesize
                            fp.write(data)
                        fp.close()
                        self.message_output.AppendText('end receive...\n')
            else:
                break

    def selectfile(self, event):

        dlg = wx.FileDialog(self, u"选择文件", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.file_path_show.AppendText(dlg.GetPath())  # 文件夹路径

        dlg.Destroy()

    def clear(self, event):
        self.message_output.Clear()


app = wx.App(False)
frame = MyFrameClient(None, "client")
app.MainLoop()


