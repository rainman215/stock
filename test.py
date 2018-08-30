#! /usr/bin/env python
#coding=GB18030
import sys
from PyQt4 import QtGui,QtCore
import daily_data as dd
import jigou as jg
class winForm(QtGui.QWidget):
    def __init__(self):
        super(winForm,self).__init__()
        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        self.setToolTip('this is a <b>QWidget</b> widget')
        btn=QtGui.QPushButton(u'每日数据搜集',self)
        btn.clicked.connect(dd._start)
        btn.setToolTip('this is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        

        btn1=QtGui.QPushButton(u'龙虎榜分析',self)
        btn1.clicked.connect(jg.analysis)
        btn1.resize(btn1.sizeHint())
        btn1.move(150,50)
        
        self.setGeometry(300,300,400,300)
        self.setWindowTitle(u'股票查询')
        self.setWindowIcon(QtGui.QIcon())
        self.center()
        self.show()
    def oclick(self):
        print("PyQt5 button click")
        
    def closeEvent(self,event):
        res=QtGui.QMessageBox.question(self,'info',
                "Quit?",QtGui.QMessageBox.Yes |
                                       QtGui.QMessageBox.No)
        if res==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr=self.frameGeometry()
        cp=QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app=QtGui.QApplication(sys.argv)
    ex=winForm()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()