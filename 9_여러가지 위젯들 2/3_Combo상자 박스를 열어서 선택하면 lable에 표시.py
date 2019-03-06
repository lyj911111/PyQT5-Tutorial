# 이미지를 나타낼 수 있는 위젯.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("ubuntu", self)       # 초기 lable에 나와있는 text

        # 콤보상자를 만들어서 아래 리스트를 추가.
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Centos")

        # 콤보상자와 lable의 좌표이동
        combo.move(50, 50)
        self.lbl.move(50, 150)

        # 콤보상자가 활성화 되었을때 str을 전달해서 onActivated함수로 전달
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Q Combo Box")
        self.show()

    # 변경된[str]이 입력 인자 text으로 전달됨.
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()       # 문자를 입력할 때마다 size를 늘리면서 lable로 전달 (이것이 없을 경우 실시간 업데이트가 안됨)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())