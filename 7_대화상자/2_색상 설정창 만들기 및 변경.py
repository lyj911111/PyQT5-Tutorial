# 색상 설정창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)	# R, G, B 값 초기값. (0, 0, 0) 이므로 검정색. 객체 생성.

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)	# 클릭시 showDialog함수와 연결(호출)

		# 색상을 디스플레이할 프레임을 추가 (창내 사각형 색상 표시)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("background-color: {0};".format(col.name()))
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle("Color Dialog")
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()	# 내장된 컬러 선택창을 호출함.

		# isValid란, 사용자가 OK를 눌렀을때. True, Cancel을 눌렀을 때 False가 입력됨.
        if col.isValid():
            print(col.name())
            self.frm.setStyleSheet("background-color: {0};".format(col.name()))	# 색상을 선택하면 col.name() 에 값이 들어가게 되고, 그 값이 전달됨.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())