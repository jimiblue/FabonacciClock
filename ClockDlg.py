from PyQt5 import QtWidgets, QtCore
from ClockUi import Ui_Dialog as ClockDlg
import GlobalVar
import CalFabonacciTime

#类重载，用于显示继承在Object的Qt UI文件，并添加相关的界面操作，信号与槽等
class ShowDlg(QtWidgets.QWidget, ClockDlg):
    def __init__(self):
        super(ShowDlg, self).__init__()
        self.setupUi(self)
        #开始时间转换
        self.calTime = CalFabonacciTime.ThreadCalFaboTime(0, 1)
        #绑定信号
        self.calTime.signalChangeColor.connect(self.changeColor)
        self.calTime.start()
        #主界面GridLayout全覆盖
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        #label布局GridLayout设置边距
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        #窗口设置
        self.setWindowTitle("FabonacciClock")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:black;")
        self.resize(460, 320)
        #self.setWindowState(QtCore.Qt.WindowFullScreen)
        #self.setWindowState(QtCore.Qt.WindowMaximized)

    def setLabelColor(self, label, type):
        if type == 0:
            self.color = "white"
        elif type == -1:
            self.color = "black"
        elif type == 1:
            self.color = "red"
        elif type == 2:
            self.color = "green"
        elif type == 3:
            self.color = "blue"

        self.command = "self.%s.setStyleSheet(\"background-color:%s;\")" % (label, self.color)
        exec(self.command)

    def changeColor(self):
        for (label, type) in GlobalVar.labelS.items():
            self.setLabelColor(label, type)
        for (label, type) in GlobalVar.labelF.items():
            self.setLabelColor(label, type)

    def test(self):
        print("hello emit ")



