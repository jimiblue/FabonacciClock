#!user/bin/python
#-*- coding:utf-8 -*-

import GlobalVar
import threading
import time
from PyQt5 import QtCore

#线程启动时间计算，讲时间转换为Fabonacci数值
#num 线程运行次数，0 ：无限运行 -1:停止运行
#interval 线程间隔时间
class ThreadCalFaboTime(threading.Thread):

    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.num = num
        self.threadStop = False
        self.interval = interval
        self.signal = GlobalVar.Signal()

    def run(self):
        while not self.threadStop:
            self.calFaboTime()
            if self.interval != 0:
                time.sleep(self.interval)

    def stop(self):
        self.threadStop = True

    def calFaboTime(self):
        localTime = time.localtime(time.time())
        hour = localTime[3]
        minutes = localTime[4]
        seconds = localTime[5]
        #计算时
        faboHour = hour % 5

        #计算分

        #计算秒
        if seconds == 0:
            key = "S"
        else:
            key = "S_%s"%(seconds)
        GlobalVar.labelS[key] = 3
        #发射信号
        self.signal.emitChangeColor()

