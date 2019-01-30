# 슬라이더 (올리고, 내리고) 생성과
# 슬라이더 값이 변경될때 이벤트 발생. (LCD 숫자 값)

import sys
from PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import (QApplication, QVBoxLayout, QWidget,
                              QLCDNumber, QSlider)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)                  # LCD 에 숫자 출력 객체 할당.
        sld = QSlider(Qt.Horizontal, self)      # 슬라이더(올리고 내리고 하는것)을 가로로 만듦, 객체 생성.

        vbox = QVBoxLayout()        # 세로로 아래쪽으로 하나씩 layout을 추가한다.
        vbox.addWidget(sld)         # 첫번째로 Slider생성.
        vbox.addWidget(lcd)         # 두번쨰로 LCD숫자 생성.
        self.setLayout(vbox)                    # 세팅 완료된 레이아웃을 배치.

        sld.valueChanged.connect(lcd.display)   # 슬라이더에 값이 변경 됬을 때, 연결, LCD Display에 있는 값을

        self.setGeometry(300, 300, 250, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Signal and slot')         # 창이름
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())