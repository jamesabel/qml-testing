import sys
import time
import threading
from PyQt5 import QtCore, QtGui, QtQml


class LoginManager(QtCore.QObject):
    loginSuccess = QtCore.pyqtSignal(QtCore.QVariant)
    loginFailure = QtCore.pyqtSignal(QtCore.QVariant)
    
    serverNames = QtCore.pyqtSignal(QtCore.QVariant)
    lastLogin = QtCore.pyqtSignal(QtCore.QVariant)
    lastServer = QtCore.pyqtSignal(QtCore.QVariant)
    
    @QtCore.pyqtSlot(str, str, str)
    def Login(self, Login, Password, ServerName):
        def thread(Login, Password, ServerName):
            if Password != "user":
                self.loginFailure.emit("Invalid Credentials")
            else:
                self.loginSuccess.emit("SUCCESS!")
            
        threading.Thread(target=thread, args=(Login, Password, ServerName)).start()
    
    @QtCore.pyqtSlot()
    def GetServerNames(self):
        def go():
            serverNames = ["one", "two", "three"]
            self.serverNames.emit(serverNames)
        threading.Thread(target=go).start()
    
    @QtCore.pyqtSlot()
    def GetLastLogin(self):
        def go():
            login = "user"
            self.lastLogin.emit(login)
        threading.Thread(target=go).start()
    
    @QtCore.pyqtSlot()
    def GetLastServerName(self):
        def go():
            serverName = "three"
            self.lastServer.emit(serverName)
        threading.Thread(target=go).start()


app = QtGui.QGuiApplication(sys.argv)
QtQml.qmlRegisterType(LoginManager, 'LoginManager', 1, 0, 'LoginManager')
engine = QtQml.QQmlApplicationEngine("Main.qml")
app.exec_()
