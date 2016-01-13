#!user/bin/python
#-*- coding:utf-8 -*-

import GlobalVar
import threading
import time
from PyQt5 import QtCore
import random

#线程启动时间计算，讲时间转换为Fabonacci数值
#num 线程运行次数，0 ：无限运行 -1:停止运行
#interval 线程间隔时间
class ThreadCalFaboTime(threading.Thread, QtCore.QObject):
    signalChangeColor = QtCore.pyqtSignal()
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self)
        self.num = num
        self.threadStop = False
        self.interval = interval

    def run(self):
        while not self.threadStop:
            self.calFaboTime()
            if self.interval != 0:
                time.sleep(self.interval)

    def stop(self):
        self.threadStop = True

    def calFaboTime(self):
        GlobalVar.resetGlobalVar()
        localTime = time.localtime(time.time())
        #计算时
        hour = localTime[3] if localTime[3] <= 12 else localTime[3] - 12
        exec("self.num%d(1,%d)" % (hour, random.randint(0, 2)))

        #计算分
        exec("self.num%d(2,%d)" % (localTime[4] / 5, random.randint(0, 2)))

        #计算秒
        if localTime[5] == 0:
            key = "S"
        else:
            key = "S_%s"%(localTime[5])
        GlobalVar.labelS[key] = 3
        #发射信号
        self.signalChangeColor.emit()

    #时分的数字
    def num0(self, flag, type):
        print("0")
    def num1(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F_1"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 2

    def num2(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F1_1"] += 2
            elif type == 1:
                GlobalVar.labelF["F_2"] += 2

    def num3(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_2"] += 1
            elif type == 1:
                GlobalVar.labelF["F_3"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2
            elif type == 1:
                GlobalVar.labelF["F_3"] += 2

    def num4(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_3"] += 1
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_3"] += 1
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_2"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_3"] += 2
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_3"] += 2
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2

    def num5(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_3"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
            elif type == 2:
                GlobalVar.labelF["F_5"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_3"] += 2
            elif type == 1:
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2
            elif type == 2:
                GlobalVar.labelF["F_5"] += 2

    def num6(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
            elif type == 3:
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2
            elif type == 3:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2

    def num7(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2

    def num8(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 2:
                GlobalVar.labelF["F_5"] += 1
                GlobalVar.labelF["F_3"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 2:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_5"] += 2

    def num9(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 2:
                GlobalVar.labelF["F_5"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F1_1"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 2:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2

    def num10(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F1_2"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F_5"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F1_2"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2

    def num11(self, flag, type):
        #时
        if flag == 1:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 1
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F_5"] += 1
            elif type == 1:
                GlobalVar.labelF["F_2"] += 1
                GlobalVar.labelF["F_3"] += 1
                GlobalVar.labelF["F_5"] += 1
                GlobalVar.labelF["F1_2"] += 1
        #分
        elif flag == 2:
            if type == 0:
                GlobalVar.labelF["F1_1"] += 2
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2
            elif type == 1:
                GlobalVar.labelF["F_2"] += 2
                GlobalVar.labelF["F_3"] += 2
                GlobalVar.labelF["F_5"] += 2
                GlobalVar.labelF["F1_2"] += 2