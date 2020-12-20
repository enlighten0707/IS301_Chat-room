# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import struct
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_total = QtWidgets.QFrame(self.centralwidget)
        self.frame_total.setGeometry(QtCore.QRect(10, 20, 981, 721))
        self.frame_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_total.setObjectName("frame_total")
        self.frame_buttons = QtWidgets.QFrame(self.frame_total)
        self.frame_buttons.setGeometry(QtCore.QRect(10, 30, 121, 481))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.login_button = QtWidgets.QPushButton(self.frame_buttons)
        self.login_button.setGeometry(QtCore.QRect(20, 0, 90, 90))
        self.login_button.setStyleSheet("border-image: url(source/icon/Interface.png);")
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
        self.logout_button.setStyleSheet("border-image: url(source/icon/Forbidden.png);")
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
        self.clear_button.setStyleSheet("border-image: url(source/icon/Clear.png);")
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
        self.exit_button.setStyleSheet("border-image: url(source/icon/Exit.png);")
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
        self.frame_info = QtWidgets.QFrame(self.frame_total)
        self.frame_info.setGeometry(QtCore.QRect(150, 440, 831, 281))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.info = QtWidgets.QTextBrowser(self.frame_info)
        self.info.setGeometry(QtCore.QRect(20, 50, 350, 220))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.info_label = QtWidgets.QLabel(self.frame_info)
        self.info_label.setGeometry(QtCore.QRect(20, 0, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.user_list = QtWidgets.QTextBrowser(self.frame_info)
        self.user_list.setGeometry(QtCore.QRect(450, 50, 350, 220))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.user_list.setFont(font)
        self.user_list.setObjectName("user_list")
        self.user_list_label = QtWidgets.QLabel(self.frame_info)
        self.user_list_label.setGeometry(QtCore.QRect(450, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.user_list_label.setFont(font)
        self.user_list_label.setObjectName("user_list_label")
        self.frame_send = QtWidgets.QFrame(self.frame_total)
        self.frame_send.setGeometry(QtCore.QRect(150, 190, 831, 241))
        self.frame_send.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send.setObjectName("frame_send")
        self.message_edit = QtWidgets.QTextEdit(self.frame_send)
        self.message_edit.setGeometry(QtCore.QRect(450, 70, 341, 151))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.message_edit.setFont(font)
        self.message_edit.setObjectName("message_edit")
        self.frame_edit = QtWidgets.QFrame(self.frame_send)
        self.frame_edit.setGeometry(QtCore.QRect(10, 10, 391, 61))
        self.frame_edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edit.setObjectName("frame_edit")
        self.recv_edit = QtWidgets.QLineEdit(self.frame_edit)
        self.recv_edit.setGeometry(QtCore.QRect(90, 14, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.recv_edit.setFont(font)
        self.recv_edit.setObjectName("recv_edit")
        self.recv_label = QtWidgets.QLabel(self.frame_edit)
        self.recv_label.setGeometry(QtCore.QRect(10, 10, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.recv_label.setFont(font)
        self.recv_label.setObjectName("recv_label")
        self.message_label = QtWidgets.QLabel(self.frame_send)
        self.message_label.setGeometry(QtCore.QRect(450, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")
        self.frame_file = QtWidgets.QFrame(self.frame_send)
        self.frame_file.setGeometry(QtCore.QRect(10, 80, 411, 61))
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.file_edit = QtWidgets.QLineEdit(self.frame_file)
        self.file_edit.setGeometry(QtCore.QRect(90, 14, 201, 41))
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
        self.file_button.setGeometry(QtCore.QRect(310, 14, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.file_button.setFont(font)
        self.file_button.setObjectName("file_button")
        self.send_file_button = QtWidgets.QPushButton(self.frame_send)
        self.send_file_button.setGeometry(QtCore.QRect(10, 170, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.send_file_button.setFont(font)
        self.send_file_button.setObjectName("send_file_button")
        self.send_message_button = QtWidgets.QPushButton(self.frame_send)
        self.send_message_button.setGeometry(QtCore.QRect(250, 170, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.send_message_button.setFont(font)
        self.send_message_button.setObjectName("send_message_button")
        self.frame_log = QtWidgets.QFrame(self.frame_total)
        self.frame_log.setGeometry(QtCore.QRect(150, 29, 831, 151))
        self.frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log.setObjectName("frame_log")
        self.frame_ip = QtWidgets.QFrame(self.frame_log)
        self.frame_ip.setGeometry(QtCore.QRect(10, 80, 361, 61))
        self.frame_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ip.setObjectName("frame_ip")
        self.ip_edit = QtWidgets.QLineEdit(self.frame_ip)
        self.ip_edit.setGeometry(QtCore.QRect(140, 14, 201, 41))
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
        self.frame_port.setGeometry(QtCore.QRect(440, 80, 351, 61))
        self.frame_port.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_port.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_port.setObjectName("frame_port")
        self.port_edit = QtWidgets.QLineEdit(self.frame_port)
        self.port_edit.setGeometry(QtCore.QRect(150, 14, 201, 41))
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
        self.username_edit.setGeometry(QtCore.QRect(140, 14, 201, 41))
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
        self.line_v = QtWidgets.QFrame(self.frame_total)
        self.line_v.setGeometry(QtCore.QRect(130, 0, 20, 721))
        self.line_v.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v.setObjectName("line_v")
        self.line_h2 = QtWidgets.QFrame(self.frame_total)
        self.line_h2.setGeometry(QtCore.QRect(140, 430, 841, 16))
        self.line_h2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h2.setObjectName("line_h2")
        self.line_h1 = QtWidgets.QFrame(self.frame_total)
        self.line_h1.setGeometry(QtCore.QRect(140, 180, 841, 16))
        self.line_h1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1.setObjectName("line_h1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear_button.clicked.connect(self.info.clear)
        self.exit_button.clicked.connect(self.exit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.login_button.clicked.connect(self.log_in)
        self.logout_button.clicked.connect(self.log_out)
        self.send_message_button.clicked.connect(self.send)
        self.send_file_button.clicked.connect(self.sendfile)
        self.file_button.clicked.connect(self.slot_btn_chooseFile)

        self.connectFlag = False
        self.socketDict = {}

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_label.setText(_translate("MainWindow", "Log in"))
        self.logout_label.setText(_translate("MainWindow", "Log out"))
        self.clear_label.setText(_translate("MainWindow", "Clear"))
        self.exit_label.setText(_translate("MainWindow", "Exit"))
        self.info_label.setText(_translate("MainWindow", "Info"))
        self.user_list_label.setText(_translate("MainWindow", "Online users"))
        self.recv_label.setText(_translate("MainWindow", "To"))
        self.message_label.setText(_translate("MainWindow", "Message"))
        self.file_label.setText(_translate("MainWindow", "File"))
        self.file_button.setText(_translate("MainWindow", "Select"))
        self.send_file_button.setText(_translate("MainWindow", "Send File"))
        self.send_message_button.setText(_translate("MainWindow", "Send Message"))
        self.ip_label.setText(_translate("MainWindow", "IP"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.username_label.setText(_translate("MainWindow", "Username"))

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
            self.info.append("you are already inline\n")

    def log_out(self):
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
            del self.socketDict[self.name]
            print(self.user_list)
            self.user_list.clear()
            print(self.user_list)
            self.name = "<anonymous user>"
        else:
            self.info.append("you are already offline\n")

    def exit(self):
        # 在关闭客户端时也能够发送消息给服务端，让服务端的线程结束
        if self.connectFlag:
            self.connectFlag = False
            self.socketDict[self.name].send("exit".encode('utf-8'))
            self.socketDict[self.name].close()
        else:
            self.info.append("you are already offline\n")
        MainWindow.Close()

    def send(self):
        if self.connectFlag:
            if self.message_edit.toPlainText() and self.recv_edit.text():
                self.socketDict[self.name].send(("sendmess").encode('utf-8'))
                self.socketDict[self.name].send(("<" + self.recv_edit.text() + ">" + "-*-" +
                                                 self.message_edit.toPlainText()).encode('utf-8'))

                # self.message_edit.clear()
        else:
            self.info.append("you are offline!\n")

    def sendfile(self):
        if self.connectFlag:
            self.socketDict[self.name].send("sendfile".encode('utf-8'))
            self.socketDict[self.name].send(("<"+self.recv_edit.text()+">").encode('utf-8'))
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
        else:
            self.info.append("you are offline!\n")

    def group(self,event):
        if self.connectFlag:
            if self.message_edit.toPlainText():
                self.socketDict[self.name].send(("group").encode('utf-8'))
                self.socketDict[self.name].send(("<" + self.name + ">" + "-*-" +
                                                 self.message_edit.toPlainText()).encode('utf-8'))
                # self.message_edit.Clear()
            else:
                self.info.append("wrong")
        else:
            self.info.append("you are offline!\n")

    def handle(self):
        while True:
            if self.connectFlag:
                mode = self.socketDict[self.name].recv(1024).decode('utf-8')

                print(mode)

                if mode == "message":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')
                    print(messtext)
                    self.info.append(messtext)
                elif mode == "userupdate":
                    messtext = self.socketDict[self.name].recv(1024).decode('utf-8')

                    # print(messtext)
                    # self.user_list.clear()
                    # print(messtext)
                    self.user_list.append(messtext)
                    # print(messtext)

                elif mode == "sendfile":
                    send_user_name = self.socketDict[self.name].recv(1024).decode('utf-8')
                    fileinfo_size = struct.calcsize('128sl')
                    buf = self.socketDict[self.name].recv(fileinfo_size)
                    if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        fn = filename.strip(b'\00')
                        new_filename = os.path.join('./', 'new2_' + fn.decode('utf-8'))
                        self.info.append(send_user_name + "sended you a file\n")
                        self.info.append('Filesize is {0}\n'.format(filesize))
                        recvd_size = 0  # 定义已接收文件的大小
                        fp = open(new_filename, 'wb')
                        self.info.append('start receiving...\n')

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

    def slot_btn_chooseFile(self):
        fileName, _ = QFileDialog.getOpenFileName()
        self.file_edit.setText(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
