from ClockDlg  import ShowDlg
from PyQt5 import QtWidgets
import sys

# #显示
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    showDlg = ShowDlg()
    showDlg.show()
    sys.exit(app.exec_())