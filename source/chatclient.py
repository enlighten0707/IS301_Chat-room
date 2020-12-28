# -*- coding: utf-8 -*-

import sys
import socket
import threading
import struct
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    # 实现了聊天程序中的客户端类
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(Client)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_total = QtWidgets.QFrame(self.centralwidget)
        self.frame_total.setGeometry(QtCore.QRect(10, 20, 981, 721))
        self.frame_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_total.setObjectName("frame_total")

        # 界面左边部分按钮设计
        self.frame_buttons = QtWidgets.QFrame(self.frame_total)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 30, 121, 481))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.login_button = QtWidgets.QPushButton(self.frame_buttons)
        self.login_button.setGeometry(QtCore.QRect(20, 0, 90, 90))
        self.login_button.setStyleSheet("border-image: url(icon/Interface.png);")
        self.login_button.setText("")
        self.login_button.setObjectName("login_button")
        self.login_label = QtWidgets.QLabel(self.frame_buttons)
        self.login_label.setGeometry(QtCore.QRect(20, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.login_label.setFont(font)
        self.login_label.setTextFormat(QtCore.Qt.RichText)
        self.login_label.setObjectName("login_label")
        self.logout_button = QtWidgets.QPushButton(self.frame_buttons)
        self.logout_button.setGeometry(QtCore.QRect(20, 110, 70, 70))
        self.logout_button.setStyleSheet("border-image: url(icon/Forbidden.png);")
        self.logout_button.setText("")
        self.logout_button.setObjectName("logout_button")
        self.logout_label = QtWidgets.QLabel(self.frame_buttons)
        self.logout_label.setGeometry(QtCore.QRect(20, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.logout_label.setFont(font)
        self.logout_label.setTextFormat(QtCore.Qt.RichText)
        self.logout_label.setObjectName("logout_label")
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
        self.exit_button = QtWidgets.QPushButton(self.frame_buttons)
        self.exit_button.setGeometry(QtCore.QRect(20, 340, 70, 70))
        self.exit_button.setStyleSheet("border-image: url(icon/Exit.png);")
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.exit_label = QtWidgets.QLabel(self.frame_buttons)
        self.exit_label.setGeometry(QtCore.QRect(40, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.exit_label.setFont(font)
        self.exit_label.setTextFormat(QtCore.Qt.RichText)
        self.exit_label.setObjectName("exit_label")

        # 界面后边部分设计
        self.frame_info = QtWidgets.QFrame(self.frame_total)
        self.frame_info.setGeometry(QtCore.QRect(600, 210, 381, 491))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.info = QtWidgets.QTextBrowser(self.frame_info)
        self.info.setGeometry(QtCore.QRect(10, 70, 350, 401))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.info_label = QtWidgets.QLabel(self.frame_info)
        self.info_label.setGeometry(QtCore.QRect(10, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.frame_send = QtWidgets.QFrame(self.frame_total)
        self.frame_send.setGeometry(QtCore.QRect(150, 180, 431, 511))
        self.frame_send.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send.setObjectName("frame_send")
        self.frame_edit = QtWidgets.QFrame(self.frame_send)
        self.frame_edit.setGeometry(QtCore.QRect(10, 20, 421, 61))
        self.frame_edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edit.setObjectName("frame_edit")

        # 接收者选择列表
        self.recv_label = QtWidgets.QLabel(self.frame_edit)
        self.recv_label.setGeometry(QtCore.QRect(10, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.recv_label.setFont(font)
        self.recv_label.setObjectName("recv_label")
        self.receiver_choose = QtWidgets.QComboBox(self.frame_edit)
        self.receiver_choose.setGeometry(QtCore.QRect(110, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.receiver_choose.setFont(font)
        self.receiver_choose.setObjectName("receiver_choose")
        self.receiver_choose.addItem("all_users")

        # 选择待发送和文件，编辑待发送消息
        self.frame_file = QtWidgets.QFrame(self.frame_send)
        self.frame_file.setGeometry(QtCore.QRect(10, 90, 421, 61))
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.file_edit = QtWidgets.QLineEdit(self.frame_file)
        self.file_edit.setGeometry(QtCore.QRect(110, 14, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.file_edit.setFont(font)
        self.file_edit.setObjectName("file_edit")
        self.file_label = QtWidgets.QLabel(self.frame_file)
        self.file_label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")
        self.file_button = QtWidgets.QPushButton(self.frame_file)
        self.file_button.setGeometry(QtCore.QRect(330, 14, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.file_button.setFont(font)
        self.file_button.setObjectName("file_button")
        self.send_file_button = QtWidgets.QPushButton(self.frame_send)
        self.send_file_button.setGeometry(QtCore.QRect(10, 450, 171, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.send_file_button.setFont(font)
        self.send_file_button.setObjectName("send_file_button")
        self.send_message_button = QtWidgets.QPushButton(self.frame_send)
        self.send_message_button.setGeometry(QtCore.QRect(250, 450, 171, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.send_message_button.setFont(font)
        self.send_message_button.setObjectName("send_message_button")
        self.message_edit = QtWidgets.QTextEdit(self.frame_send)
        self.message_edit.setGeometry(QtCore.QRect(120, 170, 301, 261))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.message_edit.setFont(font)
        self.message_edit.setObjectName("message_edit")
        self.message_label = QtWidgets.QLabel(self.frame_send)
        self.message_label.setGeometry(QtCore.QRect(20, 160, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")
        self.frame_log = QtWidgets.QFrame(self.frame_total)
        self.frame_log.setGeometry(QtCore.QRect(150, 29, 831, 151))
        self.frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log.setObjectName("frame_log")

        # 填入IP，端口号，用户名等信息
        self.frame_ip = QtWidgets.QFrame(self.frame_log)
        self.frame_ip.setGeometry(QtCore.QRect(10, 80, 361, 61))
        self.frame_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ip.setObjectName("frame_ip")
        self.ip_edit = QtWidgets.QLineEdit(self.frame_ip)
        self.ip_edit.setGeometry(QtCore.QRect(140, 14, 221, 41))
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
        self.ip_label.setObjectName("ip_label")
        self.frame_port = QtWidgets.QFrame(self.frame_log)
        self.frame_port.setGeometry(QtCore.QRect(440, 80, 371, 61))
        self.frame_port.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_port.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_port.setObjectName("frame_port")
        self.port_edit = QtWidgets.QLineEdit(self.frame_port)
        self.port_edit.setGeometry(QtCore.QRect(140, 14, 221, 41))
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
        self.frame_user = QtWidgets.QFrame(self.frame_log)
        self.frame_user.setGeometry(QtCore.QRect(10, 10, 361, 61))
        self.frame_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user.setObjectName("frame_user")
        self.username_edit = QtWidgets.QLineEdit(self.frame_user)
        self.username_edit.setGeometry(QtCore.QRect(140, 14, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.username_edit.setFont(font)
        self.username_edit.setObjectName("username_edit")
        self.username_label = QtWidgets.QLabel(self.frame_user)
        self.username_label.setGeometry(QtCore.QRect(10, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.title = QtWidgets.QLabel(self.frame_log)
        self.title.setGeometry(QtCore.QRect(530, 0, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")

        # 界面分割线
        self.line_v1 = QtWidgets.QFrame(self.frame_total)
        self.line_v1.setGeometry(QtCore.QRect(130, 0, 20, 721))
        self.line_v1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v1.setObjectName("line_v1")
        self.line_h1 = QtWidgets.QFrame(self.frame_total)
        self.line_h1.setGeometry(QtCore.QRect(140, 180, 841, 16))
        self.line_h1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1.setObjectName("line_h1")
        self.line_v2 = QtWidgets.QFrame(self.frame_total)
        self.line_v2.setGeometry(QtCore.QRect(580, 190, 20, 531))
        self.line_v2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v2.setObjectName("line_v2")
        self.frame_buttons.raise_()
        self.frame_info.raise_()
        self.frame_send.raise_()
        self.frame_log.raise_()
        self.line_v1.raise_()
        self.line_h1.raise_()
        self.frame_edit.raise_()
        self.line_v2.raise_()
        Client.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Client)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menubar.setObjectName("menubar")
        Client.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Client)
        self.statusbar.setObjectName("statusbar")
        Client.setStatusBar(self.statusbar)

        self.retranslateUi(Client)

        # 定义信号函数
        self.clear_button.clicked.connect(self.info.clear)
        self.exit_button.clicked.connect(Client.close)
        QtCore.QMetaObject.connectSlotsByName(Client)
        self.login_button.clicked.connect(self.log_in)
        self.logout_button.clicked.connect(self.log_out)
        self.send_message_button.clicked.connect(self.sendmess)
        self.send_file_button.clicked.connect(self.sendfile)
        self.file_button.clicked.connect(self.choosefile)

        # 定义其他变量
        self.connectFlag = False
        self.socketDict = {}
        self.Client = Client

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "Client"))
        self.login_label.setText(_translate("Client", "Log in"))
        self.logout_label.setText(_translate("Client", "Log out"))
        self.clear_label.setText(_translate("Client", "Clear"))
        self.exit_label.setText(_translate("Client", "Exit"))
        self.info_label.setText(_translate("Client", "Received Message"))
        self.recv_label.setText(_translate("Client", "Send to"))
        self.file_label.setText(_translate("Client", "File"))
        self.file_button.setText(_translate("Client", "Select"))
        self.send_file_button.setText(_translate("Client", "Send File"))
        self.send_message_button.setText(_translate("Client", "Send Message"))
        self.message_label.setText(_translate("Client", "Message"))
        self.ip_label.setText(_translate("Client", "IP"))
        self.port_label.setText(_translate("Client", "Port"))
        self.username_label.setText(_translate("Client", "Username"))
        self.title.setText(_translate("Client", "Client"))

    def log_in(self):
        if not self.connectFlag:
            self.connectFlag = True
            self.name = "<" + self.username_edit.text() + ">"
            self.socketDict[self.name] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketDict[self.name].connect(
                (self.ip_edit.text(), int(self.port_edit.text())))
            self.socketDict[self.name].send(self.name.encode('utf-8'))
            t1 = threading.Thread(target=self.handle, args=())
            t1.start()
        else:
            self.info.append("you are already inline")

    def log_out(self):
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
            del self.socketDict[self.name]
            self.name = "<anonymous user>"
        else:
            self.info.append("you are already offline")

    def exit(self):
        # 在关闭客户端时也能够发送消息给服务端，让服务端的线程结束
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
        else:
            self.info.append("you are already offline")
        self.Client.Close()

    def sendmess(self):
        if self.connectFlag:
            if self.message_edit.toPlainText() and self.receiver_choose.currentText():
                if self.receiver_choose.currentIndex() == 0:
                    # 选择消息接收者为“all_users”，群发消息
                    self.socketDict[self.name].send(("sendmess_group").encode('utf-8'))
                    self.socketDict[self.name].send((self.name+ "-*-" +
                                                     self.message_edit.toPlainText()).encode('utf-8'))
                else:
                    # 否则，单发消息
                    self.socketDict[self.name].send(("sendmess").encode('utf-8'))
                    self.socketDict[self.name].send(("<" + self.receiver_choose.currentText() + ">" + "-*-" +
                                                     self.message_edit.toPlainText()).encode('utf-8'))

                self.message_edit.clear()

        else:
            self.info.append("you are offline!")

    def sendfile(self):
        if self.connectFlag:
            if self.receiver_choose.currentIndex() != 0:
                # 单发文件
                self.socketDict[self.name].send("sendfile".encode('utf-8'))
                self.socketDict[self.name].send(("<" + self.receiver_choose.currentText() + ">").encode('utf-8'))
                filepath = self.file_edit.text()
                if os.path.isfile(filepath):
                    fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'),
                                        os.stat(filepath).st_size)
                    self.socketDict[self.name].send(fhead)

                    fp = open(filepath, 'rb')
                    while 1:
                        data = fp.read(1024)
                        if not data:
                            self.info.append('{0} file send over...\n'.format(filepath))
                            break
                        self.socketDict[self.name].send(data)
            '''
            # 群发文件，在尝试之后，有bug没有解决
            else:
                # 选择消息接收者为“all_users”，群发文件
                self.socketDict[self.name].send("sendfile_group".encode('utf-8'))
                self.socketDict[self.name].send((self.name).encode('utf-8'))
                filepath = self.file_edit.text()
                if os.path.isfile(filepath):
                    fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'),
                                        os.stat(filepath).st_size)
                    self.socketDict[self.name].send(fhead)

                    fp = open(filepath, 'rb')
                    while 1:
                        data = fp.read(1024)
                        if not data:
                            self.info.append('{0} file send over...\n'.format(filepath))
                            break
                        self.socketDict[self.name].send(data)
            '''

        else:
            self.info.append("you are offline!")

    def handle(self):
        while True:
            if self.connectFlag:
                mode = self.socketDict[self.name].recv(1024).decode('utf-8')

                if mode == "sendmess":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')
                    self.info.insertPlainText(messtext)
                elif mode == "userupdate":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')
                    messtext_split = messtext.split('\n')

                    # 维护目前在线用户信息，并更新可供选择的接收者列表
                    i = 0
                    j = 1
                    while i < len(messtext_split) and j < self.receiver_choose.count():
                        user = messtext_split[i]
                        if user != self.name:
                            user = user.strip('<')
                            user = user.strip('>')
                            self.receiver_choose.setItemText(j, user)
                            j += 1
                        i += 1
                    while i < len(messtext_split):
                        user = messtext_split[i]
                        if user != self.name:
                            user = user.strip('<')
                            user = user.strip('>')
                            self.receiver_choose.addItem(user)
                        i += 1

                elif mode == "sendfile":
                    send_user_name = self.socketDict[self.name].recv(1024).decode('utf-8',errors='ignore')
                    fileinfo_size = struct.calcsize('128sl')
                    buf = self.socketDict[self.name].recv(fileinfo_size) # 读取文件路径和文件信息
                    if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        fn = filename.strip(b'\00')
                        # fn = fn.decode('utf-8')
                        # fn = fn.split('\\')[-1]
                        new_filename = os.path.join('./', fn)
                        if os.path.exists(new_filename): #文件若已经存在，重新命名
                            new_filename = os.path.join('./', 'new_' + fn)
                        self.info.append(send_user_name + "sended you a file")
                        self.info.append('Filesize is {0}'.format(filesize))
                        recvd_size = 0  # 定义已接收文件的大小
                        fp = open(new_filename, 'wb')
                        self.info.append('start receiving...')

                        while not recvd_size == filesize:
                            if filesize - recvd_size > 1024:
                                data = self.socketDict[self.name].recv(1024)
                                recvd_size += len(data)
                            else:
                                data = self.socketDict[self.name].recv(filesize - recvd_size)
                                recvd_size = filesize
                            fp.write(data)
                        fp.close()
                        self.info.append('end receive...\n')
            else:
                break

    def choosefile(self):
        # 调用 QFileDialog，在资源管理器中选择文件路径
        fileName, _ = QFileDialog.getOpenFileName()
        self.file_edit.setText(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Client = QMainWindow()
    ui = Ui_Client()
    ui.setupUi(Client)
    Client.show()
    sys.exit(app.exec_())
