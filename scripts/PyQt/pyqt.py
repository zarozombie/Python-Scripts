import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("This is an example of PyQt GUI\n I do think special char work")
   w.setGeometry(100,100,400,200)
   b.move(50,20)
   w.setWindowTitle('Example Window')
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
