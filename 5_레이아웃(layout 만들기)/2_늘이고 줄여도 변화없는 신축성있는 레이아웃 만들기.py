# 창을 늘리고 줄여도 항상 같은 위치에 버튼이 위치함. 창에 신축성을 부여

import sys
from  PyQt5.QtWidgets import (QApplication, QPushButton, QWidget,
                              QHBoxLayout, QVBoxLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okbtn = QPushButton("OK")
        cancelbtn = QPushButton("cancel")

        hbox = QHBoxLayout()				# 객체생성.
        hbox.addStretch(1)                  # hbox버튼이 차지하고 있지 않은 수평좌표 공간(x축 좌표)이 늘었다 줄었다 신축성이 생김. 사용자가 창을 키워도 같이 늘어남.

        hbox.addWidget(okbtn)               # ok 버튼 추가
        hbox.addWidget(cancelbtn)           # cancel 버튼 추가 ( 수평방향으로 -> Stretch공간/ OK / Cancel 이렇게 생성됨.)

        vbox = QVBoxLayout()				# 객체생성.
        vbox.addStretch(1)					# hbox버튼이 차지하고 있지 않은 수직좌표 공간(y축 좌표)이 늘었다 줄었다 신축성이 생김. 사용자가 창을 키워도 같이 늘어남.
        vbox.addLayout(hbox)                # hbox 있기 전까지 모든 수직좌표(y좌표)를 눌어나거나 줄어들거나 할 수 있음. ( 수직방향으로 -> stretch공간 / hbox버튼 이렇게 구조를 이룸)

        self.setLayout(vbox)				# **반드시 vbox가 있어야 올바르게 생성 (공식처럼 기억)

        self.setGeometry(300, 300, 300, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Buttons')         # 창이름
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())