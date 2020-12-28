# -*- coding: utf-8 -*-
import sys
import socket
import threading
import struct
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    # 实现了聊天程序中的服务器类
    def setupUi(self, Server):
        # UI界面设计
        Server.setObjectName("Server")
        Server.resize(900, 560)
        Server.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_total = QtWidgets.QFrame(self.centralwidget)
        self.frame_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_total.setObjectName("frame_total")

        # 界面左边按钮栏frame设计
        self.frame_buttons = QtWidgets.QFrame(self.frame_total)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 30, 121, 481))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        # Start按钮
        self.start_button = QtWidgets.QPushButton(self.frame_buttons)
        self.start_button.setGeometry(QtCore.QRect(20, 10, 70, 70))
        self.start_button.setStyleSheet("border-image: url(icon/Start.png);")
        self.start_button.setText("")
        self.start_button.setObjectName("start_button")
        self.start_label = QtWidgets.QLabel(self.frame_buttons)
        self.start_label.setGeometry(QtCore.QRect(30, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.start_label.setFont(font)
        self.start_label.setTextFormat(QtCore.Qt.RichText)
        self.start_label.setObjectName("start_label")
        # Stop按钮
        self.stop_button = QtWidgets.QPushButton(self.frame_buttons)
        self.stop_button.setGeometry(QtCore.QRect(20, 110, 70, 70))
        self.stop_button.setStyleSheet("border-image: url(icon/Stop.png);")
        self.stop_button.setText("")
        self.stop_button.setObjectName("stop_button")
        self.stop_label = QtWidgets.QLabel(self.frame_buttons)
        self.stop_label.setGeometry(QtCore.QRect(30, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.stop_label.setFont(font)
        self.stop_label.setTextFormat(QtCore.Qt.RichText)
        self.stop_label.setObjectName("stop_label")
        # clear按钮
        self.clear_button = QtWidgets.QPushButton(self.frame_buttons)
        self.clear_button.setGeometry(QtCore.QRect(20, 220, 70, 70))
        self.clear_button.setStyleSheet("border-image: url(icon/Clear.png);")
        self.clear_button.setText("")
        self.clear_button.setObjectName("clear_button")
        self.clear_label = QtWidgets.QLabel(self.frame_buttons)
        self.clear_label.setGeometry(QtCore.QRect(30, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.clear_label.setFont(font)
        self.clear_label.setTextFormat(QtCore.Qt.RichText)
        self.clear_label.setObjectName("clear_label")
        # exit按钮
        self.exit_button = QtWidgets.QPushButton(self.frame_buttons)
        self.exit_button.setGeometry(QtCore.QRect(20, 340, 70, 70))
        self.exit_button.setStyleSheet("border-image: url(icon/Exit.png);")
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.exit_label = QtWidgets.QLabel(self.frame_buttons)
        self.exit_label.setGeometry(QtCore.QRect(30, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.exit_label.setFont(font)
        self.exit_label.setTextFormat(QtCore.Qt.RichText)
        self.exit_label.setObjectName("exit_label")

        # 界面右边frame设计
        self.frame_info = QtWidgets.QFrame(self.frame_total)
        self.frame_info.setGeometry(QtCore.QRect(140, 120, 701, 361))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.info = QtWidgets.QTextBrowser(self.frame_info)
        self.info.setGeometry(QtCore.QRect(90, 130, 601, 221))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info.setFont(font)
        self.info.setObjectName("info")
        # 填入IP
        self.frame_ip = QtWidgets.QFrame(self.frame_info)
        self.frame_ip.setGeometry(QtCore.QRect(10, 40, 291, 61))
        self.frame_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ip.setObjectName("frame_ip")
        self.ip_edit = QtWidgets.QLineEdit(self.frame_ip)
        self.ip_edit.setGeometry(QtCore.QRect(80, 14, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.ip_edit.setFont(font)
        self.ip_edit.setObjectName("ip_edit")
        self.ip_label = QtWidgets.QLabel(self.frame_ip)
        self.ip_label.setGeometry(QtCore.QRect(10, 10, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.ip_label.setFont(font)
        self.ip_label.setStyleSheet("\n"
                                    "")
        self.ip_label.setObjectName("ip_label")
        # 填入port
        self.frame_port = QtWidgets.QFrame(self.frame_info)
        self.frame_port.setGeometry(QtCore.QRect(360, 40, 301, 61))
        self.frame_port.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_port.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_port.setObjectName("frame_port")
        self.port_edit = QtWidgets.QLineEdit(self.frame_port)
        self.port_edit.setGeometry(QtCore.QRect(90, 14, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.port_edit.setFont(font)
        self.port_edit.setObjectName("port_edit")
        self.port_label = QtWidgets.QLabel(self.frame_port)
        self.port_label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        # Info信息显示栏
        self.info_label = QtWidgets.QLabel(self.frame_info)
        self.info_label.setGeometry(QtCore.QRect(20, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")

        # “Server” title设计
        self.label = QtWidgets.QLabel(self.frame_total)
        self.label.setGeometry(QtCore.QRect(390, 40, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.frame_total, 0, 0, 1, 1)
        Server.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Server)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 30))
        self.menubar.setObjectName("menubar")
        Server.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Server)
        self.statusbar.setObjectName("statusbar")
        Server.setStatusBar(self.statusbar)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

        # 定义信号函数
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.clear_button.clicked.connect(self.info.clear)
        self.exit_button.clicked.connect(self.exit)

        # 其他变量
        self.listenFlag = False
        self.user_change_flag = False
        self.serverDic = {}
        self.socketDic = {}
        self.Server = Server
        self.Link_list = []

    def retranslateUi(self, Server):
        # 在将xxx.ui文件转换为ui_xxx.h文件的系统，uic工具为.h文件添加了retranslateUi(QWidget *)函数，
        # 就是专门做的一个重新设置翻译文件的操作，不需要关闭或者隐藏任何一个窗体
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.start_label.setText(_translate("Server", "Start"))
        self.stop_label.setText(_translate("Server", "Stop"))
        self.clear_label.setText(_translate("Server", "Clear"))
        self.exit_label.setText(_translate("Server", "Exit"))
        self.ip_label.setText(_translate("Server", "IP"))
        self.port_label.setText(_translate("Server", "Port"))
        self.info_label.setText(_translate("Server", "Info"))
        self.label.setText(_translate("Server", "Server"))

    def exit(self):
        self.stop()
        for i in range(len(self.Link_list)):
            self.Link_list[i].stop()
        self.listenFlag = False
        self.serverDic["Server"].close()
        del self.serverDic["Server"]
        Server.close()

    def stop(self):
        if self.listenFlag:
            self.info.append("stop listening...")
            self.listenFlag = False
        else:
            self.info.append("has already stopped listening")

    def start(self):
        if "Server" not in self.serverDic.keys():
            self.serverDic["Server"] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverDic["Server"].bind((self.ip_edit.text(), int(self.port_edit.text())))

        if not self.listenFlag:
            self.listenFlag = True
            self.serverDic["Server"].listen(5)
            self.info.append('Waiting for connection...')

            # 开始创建一个线程来监听客户端的连接
            t1 = threading.Thread(target=self.listen, args=())
            t1.start()
            self.Link_list.append(t1)

    def listen(self):
        while self.listenFlag:
            # 接受一个新连接:accept函数会一直等待直到接收到连接
            sock, addr = self.serverDic["Server"].accept()
            # 创建一个新线程来处理与客户端的连接:
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

    def tcplink(self, sock, addr):
        sock_name = sock.recv(1024).decode('utf-8')
        self.socketDic[sock_name] = sock
        self.info.append("%s logged in successfully!" % sock_name)

        tem = ""  # 存储在线人的id
        for Key in self.socketDic.keys():
            tem = tem + Key + "\n"
        for Key in self.socketDic.keys():
            self.socketDic[Key].send("userupdate".encode('utf-8'))
            self.socketDic[Key].send(tem.encode('utf-8'))

        while True:
            # mode: exit-----退出
            # mode: sendmess-----发送消息
            # mode: sendmess_group-----群发消息
            # mode: sendfile-----发送文件
            # mode: sendfile_group-----群发文件，实际运行时有一些问题

            mode = sock.recv(1024).decode('utf-8')

            if mode == "exit":  # 当用户下线时，他会向服务端发送exit信息
                break

            elif mode == "sendmess":
                towho_message = sock.recv(1024).decode('utf-8')
                towho, message = towho_message.split("-*-")
                for onlinename in self.socketDic.keys():
                    if onlinename == towho:
                        self.socketDic[onlinename].send("sendmess".encode('utf-8'))
                        self.socketDic[onlinename].send((sock_name + ": " + message + "\n").encode('utf-8'))

            elif mode == "sendmess_group":
                towho_message = sock.recv(1024).decode('utf-8')
                towho, message = towho_message.split("-*-")
                for onlinename in self.socketDic.keys():
                    if onlinename != towho:
                        self.socketDic[onlinename].send("sendmess".encode('utf-8'))
                        self.socketDic[onlinename].send((sock_name + ": " + message + "\n").encode('utf-8'))

            elif mode == "sendfile":
                towho = sock.recv(1024).decode('utf-8')
                for onlinename in self.socketDic.keys():
                    if onlinename == towho:
                        self.socketDic[onlinename].send("sendfile".encode('utf-8'))
                        self.socketDic[onlinename].send(sock_name.encode('utf-8'))
                        fileinfo_size = struct.calcsize('128sl')
                        buf = sock.recv(fileinfo_size) # 读取文件路径和文件信息
                        self.socketDic[onlinename].send(buf)
                        if buf:
                            filename, filesize = struct.unpack('128sl', buf)
                            recvd_size = 0  # 定义已接收文件的大小
                            while not recvd_size == filesize:
                                if filesize - recvd_size > 1024:
                                    data = sock.recv(1024)
                                    self.socketDic[onlinename].send(data) #分段转发数据
                                    recvd_size += len(data)
                                else:
                                    data = sock.recv(filesize - recvd_size)
                                    self.socketDic[onlinename].send(data)
                                    recvd_size = filesize

            '''
            # sendfile_group 在尝试之后，有bug没有解决
            elif mode == "sendfile_group":
                towho = sock.recv(1024).decode('utf-8')
                fileinfo_size = struct.calcsize('128sl')
                buf = sock.recv(fileinfo_size)

                if buf:
                    for onlinename in self.socketDic.keys():
                        if onlinename != towho:
                            self.socketDic[onlinename].send("sendfile".encode('utf-8'))
                            self.socketDic[onlinename].send(sock_name.encode('utf-8'))
                            self.socketDic[onlinename].send(buf)

                    filename, filesize = struct.unpack('128sl', buf)
                    recvd_size = 0  # 定义已接收文件的大小
                    while not recvd_size == filesize:
                        if filesize - recvd_size > 1024:
                            data = sock.recv(1024)
                            for onlinename in self.socketDic.keys():
                                if onlinename != towho:
                                    self.socketDic[onlinename].send(data)
                            recvd_size += len(data)
                        else:
                            data = sock.recv(filesize - recvd_size)
                            for onlinename in self.socketDic.keys():
                                if onlinename != towho:
                                    self.socketDic[onlinename].send(data)
                            recvd_size = filesize
            '''

        self.info.append("%s logged out!" % sock_name)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Server = QMainWindow()
    ui = Ui_Server()
    ui.setupUi(Server)
    Server.show()
    sys.exit(app.exec_())
