#!/user/bin/python
#-*- coding:utf-8 -*-
from PyQt5 import QtCore

#信号类，存储所有跨线程非QObject父类的信号
class Signal(QtCore.QObject):
    signalChangeColor = QtCore.pyqtSignal()

    def emitChangeColor(self):
        self.signalChangeColor.emit()

#存储F label的状态字典
labelF = {"F1_1": 0,
          "F1_2": 0,
          "F_3": 0,
          "F_5": 0,
          "F_2": 0
          }
#存储S label的状态字典
labelS = {"S": 0,
          "S_1": 0,
          "S_2": 0,
          "S_3": 0,
          "S_4": 0,
          "S_5": 0,
          "S_6": 0,
          "S_7": 0,
          "S_8": 0,
          "S_9": 0,

          "S_10": 0,
          "S_11": 0,
          "S_12": 0,
          "S_13": 0,
          "S_14": 0,
          "S_15": 0,
          "S_16": 0,
          "S_17": 0,
          "S_18": 0,
          "S_19": 0,

          "S_20": 0,
          "S_21": 0,
          "S_22": 0,
          "S_23": 0,
          "S_24": 0,
          "S_25": 0,
          "S_26": 0,
          "S_27": 0,
          "S_28": 0,
          "S_29": 0,

          "S_30": 0,
          "S_31": 0,
          "S_32": 0,
          "S_33": 0,
          "S_34": 0,
          "S_35": 0,
          "S_36": 0,
          "S_37": 0,
          "S_38": 0,
          "S_39": 0,

          "S_40": 0,
          "S_41": 0,
          "S_42": 0,
          "S_43": 0,
          "S_44": 0,
          "S_45": 0,
          "S_46": 0,
          "S_47": 0,
          "S_48": 0,
          "S_49": 0,

          "S_51": 0,
          "S_52": 0,
          "S_53": 0,
          "S_54": 0,
          "S_55": 0,
          "S_56": 0,
          "S_57": 0,
          "S_58": 0,
          "S_59": 0,
          "S_50": 0
          }

def resetGlobalVar():
    labelS["S"] = 0
    for x in range(1, 60):
        key = "S_%d"%(x)
        labelS[key] = 0

    labelF["F1_1"] = 0
    labelF["F1_2"] = 0
    labelF["F_2"] = 0
    labelF["F_3"] = 0
    labelF["F_5"] = 0
