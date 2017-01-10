#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license

# Title: PyQt5 Gui                    Version: 1.0
# Date: 08-01-17                      Language: python3
# Description: pyqt5 simple example of empty window
#
###############################################################

# do something
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle('pyQt Tuts')

window.show()
sys.exit(app.exec_())