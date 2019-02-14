# 글자 폰트 설정창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy, QVBoxLayout, QLabel, QFontDialog

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()    # 세로방향 레이아웃 설정.

        # 버튼명 입력과 생성, 버튼사이즈 고정.
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        btn.move(20, 20)    # 버튼 위치 이동

        vbox.addWidget(btn) # 세로방향 첫번째에 버튼을 추가.

        btn.clicked.connect(self.showDialog) # 버튼을 누르면 함수와 연결.

        # 레이블을 생성. 위치 이동
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        # 생성한 글자를 세로방향 두번째 라벨로 생성.
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Font Dialog")
        self.show()

    # 버튼을 눌렀을 때 작동하는 함수
    def showDialog(self):
        font, ok = QFontDialog.getFont()    # 폰트를 어떤것을 선택했는지, ok버튼을 눌렀는지를 return함.

        # ok버튼을 눌렀을때 해당 세팅한 폰트값을 lbl 글자에 적용.
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())