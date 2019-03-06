# 이미지를 나타낼 수 있는 위젯.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)     # Lable을 설정
        qle = QLineEdit(self)       # text입력 상자를 만듦

        qle.move(60, 100)           # text입력 상자를 옮김 (좌표지정)
        self.lbl.move(60, 10)       # 출력되는 lable의 위치를 지정 (좌표지정)

        # 문자가 변경될 경우, 그 문자[str]을 onChanged 함수와 연결함.
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QLineEdit")
        self.show()

    # 변경된[str]이 입력 인자 text으로 전달됨.
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()       # 문자를 입력할 때마다 size를 늘리면서 lable로 전달 (이것이 없을 경우 실시간 업데이트가 안됨)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())