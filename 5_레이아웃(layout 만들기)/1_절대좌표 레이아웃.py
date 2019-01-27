# 절대 좌표입력으로 고정된 위치에 레이아웃 만들기. (창이 변경되어도 항상 같은자리에 있음)

import sys
from  PyQt5.QtWidgets import QApplication, QLabel, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)  # 레이블을 만듬.
        lbl1.move(15, 10)               # 왼쪽 상단기준으로 x, y만큼 떨어진곳에서 만들어짐.

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Absolute')         # 창이름
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())