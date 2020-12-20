# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import struct


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_total = QtWidgets.QFrame(self.centralwidget)
        self.frame_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_total.setObjectName("frame_total")
        self.frame_buttons = QtWidgets.QFrame(self.frame_total)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 30, 121, 481))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.start_button = QtWidgets.QPushButton(self.frame_buttons)
        self.start_button.setGeometry(QtCore.QRect(20, 10, 70, 70))
        self.start_button.setStyleSheet("border-image: url(source/icon/Start.png);")
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
        self.stop_button = QtWidgets.QPushButton(self.frame_buttons)
        self.stop_button.setGeometry(QtCore.QRect(20, 110, 70, 70))
        self.stop_button.setStyleSheet("border-image: url(source/icon/Stop.png);")
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
        self.clear_button = QtWidgets.QPushButton(self.frame_buttons)
        self.clear_button.setGeometry(QtCore.QRect(20, 220, 70, 70))
        self.clear_button.setStyleSheet("border-image: url(source/icon/Clear.png);")
        self.clear_button.setText("")
        self.clear_button.setObjectName("clear_button")
        self.clear_button_2 = QtWidgets.QLabel(self.frame_buttons)
        self.clear_button_2.setGeometry(QtCore.QRect(30, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.clear_button_2.setFont(font)
        self.clear_button_2.setTextFormat(QtCore.Qt.RichText)
        self.clear_button_2.setObjectName("clear_button_2")
        self.exit_button = QtWidgets.QPushButton(self.frame_buttons)
        self.exit_button.setGeometry(QtCore.QRect(20, 340, 70, 70))
        self.exit_button.setStyleSheet("border-image: url(source/icon/Exit.png);")
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
        self.frame_info = QtWidgets.QFrame(self.frame_total)
        self.frame_info.setGeometry(QtCore.QRect(160, 160, 701, 361))
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
        self.frame_ip = QtWidgets.QFrame(self.frame_info)
        self.frame_ip.setGeometry(QtCore.QRect(10, 50, 291, 61))
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
        self.ip_label.setObjectName("ip_label")
        self.frame_port = QtWidgets.QFrame(self.frame_info)
        self.frame_port.setGeometry(QtCore.QRect(360, 50, 301, 61))
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
        self.info_label = QtWidgets.QLabel(self.frame_info)
        self.info_label.setGeometry(QtCore.QRect(20, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.gridLayout_2.addWidget(self.frame_total, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.clear_button.clicked.connect(self.info.clear)
        self.exit_button.clicked.connect(self.exit)

        self.listenFlag = False
        self.user_change_flag = False
        self.serverDic = {}
        self.socketDic = {}

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_label.setText(_translate("MainWindow", "Start"))
        self.stop_label.setText(_translate("MainWindow", "Stop"))
        self.clear_button_2.setText(_translate("MainWindow", "Clear"))
        self.exit_label.setText(_translate("MainWindow", "Exit"))
        self.ip_label.setText(_translate("MainWindow", "IP"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.info_label.setText(_translate("MainWindow", "Info"))

    def exit(self):
        self.stop()
        MainWindow.close()

    def stop(self):
        if self.serverDic:
            self.serverDic["Server"].close()
            del self.serverDic["Server"]
            self.info.append("stop listening...\n")
            self.listenFlag = False
        else:
            self.info.append("has already stopped listening\n")

    def start(self):
        self.serverDic["Server"] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverDic["Server"].bind((self.ip_edit.text(), int(self.port_edit.text())))
        if not self.listenFlag:
            self.listenFlag = True
            self.serverDic["Server"].listen(5)
            self.info.append('Waiting for connection...\n')
            # 开始创建一个线程来监听客户端的连接
            t1 = threading.Thread(target=self.listen, args=())
            t1.start()

    def listen(self):
        while True:
            # 接受一个新连接:accept函数会一直等待直到接收到连接
            sock, addr = self.serverDic["Server"].accept()
            # 创建一个新线程来处理与客户端的连接:
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

    def tcplink(self, sock, addr):
        sock_name = sock.recv(1024).decode('utf-8')
        self.socketDic[sock_name] = sock
        self.info.append("%s logged in successfully!\n" % sock_name)

        tem = ""  # 存储在线人的id
        for Key in self.socketDic.keys():
            tem = tem + Key + "\n"
        for Key in self.socketDic.keys():
            self.socketDic[Key].send("userupdate".encode('utf-8'))
            self.socketDic[Key].send(tem.encode('utf-8'))

        while True:
            # mode: sendmess-----发送消息
            # mode: sendfile-----发送文件
            # mode: exit-----退出

            mode = sock.recv(1024).decode('utf-8')

            # 当用户下线时，他会向服务端发送exit信息
            if mode == "exit":
                break
            elif mode == "group":
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

        self.info.append("%s logged out!\n" % sock_name)
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
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
