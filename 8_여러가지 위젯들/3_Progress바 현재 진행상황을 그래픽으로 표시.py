# Progress Bar 진행상황을 그래픽으로 표시

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)              # ProgressBar를 만듦 (진행상황 %바)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('start', self)       # start 버튼 만들기
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)     # 버튼을 눌렀을 때, doAction 함수를 수행.

        self.timer = QBasicTimer()      # 아래 timeEvent 함수가 수행됨.
        self.step = 30                  # 버튼을 눌렀을때 시작하는 지점, (0: 0%부터 시작, 50: 50%부터 시작)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QProgressBar")
        self.show()

    # 버튼이 활성화 되어있을 때 함수 pressed 눌려있으면 True 아니면 False
    def timerEvent(self, e):

        # 최대로 찰 수 있는 %양/100% 중.
        if self.step >= 80:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 5       # 타이머 증가량.
        self.pbar.setValue(self.step)

    def doAction(self):

        # 버튼을 눌렀을때, active이면 timer를 멈추고, 버튼text를 'start'로 바꿈
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        # 아니면 다시 타이머를 진행시키고, 버튼 text는 'stop'으로 만듦
        else:
            self.timer.start(1000, self)     # 100 : 0.1초를 의미, 0.1초마다 증가.  (1000은 1초)
            self.btn.setText('stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())