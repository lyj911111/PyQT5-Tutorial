# 채크박스 활성화 유무에 따른 이벤트

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox("show title", self)          # 체크박스 옆에 표시할 text 지정.
        cb.move(20, 20)                             # 체크박스 위치 지정.
        cb.toggle()                                 # 체크박스에 Default로 V자 표시함. (이 줄을 제거하면 Default는 빈 박스)
        cb.stateChanged.connect(self.changeTitle)   # 체크박스 활성화시 changeTitle 함수로 이동.

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("QcheckBox")
        self.show()

    # 체크박스가 활성화 되어있을 때 함수
    def changeTitle(self, state):

        # state값이 체크가 했는지 안되어있는지 판단,
        if state == Qt.Checked:
            self.setWindowTitle("QcheckBox")
        else:
            self.setWindowTitle('  ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())