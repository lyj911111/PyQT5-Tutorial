# 버튼 활성화 유무에 따른 동작

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QPushButton
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 컬러를 지정하기 위한 컬러 객체 생성 초기값 (0, 0, 0)검정
        self.col = QColor(0, 0, 0)

        # 'Red'라는 버튼생성, 위치지정 / checkable 누른상태, 땐 상태를 구분해줌 / 위치지정.
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        # 버튼을 클릭했을때 setColor 함수와 연결
        redb.clicked.connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked.connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked.connect(self.setColor)

        # 사각형 Frame을 생성해서 디스플레이 / x,y좌표 가로세로길이 / setColor함수의 값이 변하면 여기 값에 인자전달하여 이벤트
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("background-color: {0}".format(self.col.name()))

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QcheckBox")
        self.show()

    # 버튼이 활성화 되어있을 때 함수 pressed 눌려있으면 True 아니면 False
    def setColor(self, pressed):

        source = self.sender()      # 호출했던 버튼의 객체를 불러와서 전달함.

        # 눌렸을 경우 255, 아닐경우 0
        if pressed:
            val = 255
        else:
            val = 0

        # 불러온 객체 sourse의 text가 일치할경우
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("background-color: {0}".format(self.col.name()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())