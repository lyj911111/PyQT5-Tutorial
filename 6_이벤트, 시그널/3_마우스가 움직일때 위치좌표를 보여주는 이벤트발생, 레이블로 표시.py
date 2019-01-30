# 마우스가 움직일 때 발생하는 메소드(함수) 추가
# 마우스가 움직일 떄 x,y 좌표를 label로 보여줌.

import sys
from PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()    # grid 레이아웃 객체 할당.
        grid.setSpacing(10)     # grid 10씩 띄움.

        # 초기값 지정.
        x = 0
        y = 0

        # text객체 생성, 포멧 지정. -> 예) x: 12 y: 35 이런식의 포멧을 지정함.
        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)            # 생성된 text객체를 label 에 삽입.
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)   # label을 첫번째 grid에 집어넣음.

        self.setMouseTracking(True)          # True : 창내의 마우스의 화살표 위치를 계속 추적
                                             # False : 창내 마우스의 클릭이벤트가 있을때 좌표 추적 (창내에 클릭이벤트 발생시 외부까지 드레그하면 추적이 가능.

        self.setLayout(grid)                 # 메인 레이아웃을 Grid 레이아웃 세팅 활성화.

        self.setGeometry(300, 300, 250, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Event object')         # 창이름
        self.show()

    # 마우스가 움직일때 발생하는 이벤트
    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()                 # 움직일때 발생하는 마우스의 x값을 대입
        y = QMouseEvent.y()                 # 움직일때 발생하는 마우스의 y값을 대입

        text = "x: {0}, y: {1}".format(x, y)    # 위에 있는 텍스트 포멧과 동일하게 지정 ※※
        self.label.setText(text)                # 위에 있는 self.label 객체에 포멧을 세팅함. 반드시 지정 ※※

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())