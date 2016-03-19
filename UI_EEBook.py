#!/src/bin/env python
# -*- coding:utf-8 -*-

import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QIcon
from src.gui.ui import MainWindow
from src.resources import qrc_resources

reload(sys)
sys.setdefaultencoding('utf8')


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icon.png"))

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()