# 이미지를 나타낼 수 있는 위젯.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)                # 이미지가 하나일땐 HBox나 VBox나 별 의미 없음, hBox이므로 가로방향으로 추가
        pixmap1 = QPixmap('./img/Pistol.jpg')   # 이미지를 불러오는 위젯 (현재파일 -> img -> 이미지) 디렉터리
        pixmap2 = QPixmap('./img/shotgun.jpg')

        # 첫번째 이미지를 lable에 layout
        lbl = QLabel(self)      # lable을 만듦.
        lbl.setPixmap(pixmap1)  # lable에 pixmap에서 가저온 이미지를 넣음. (문자도 숫자도 아닌 이미지를 넣었음)
        hbox.addWidget(lbl)     # 세팅된 lable을 hbox에 넣음
        self.setLayout(hbox)    # 그리고 hbox를 Layout시킴.

        # 두번째 이미지를 lable에 layout
        lbl = QLabel(self)
        lbl.setPixmap(pixmap2)  # lable에 pixmap에서 가저온 이미지를 넣음. (문자도 숫자도 아닌 이미지를 넣었음)
        hbox.addWidget(lbl)     # 세팅된 lable을 hbox에 넣음
        self.setLayout(hbox)    # 그리고 hbox를 Layout시킴.

        self.move(300, 200)
        self.setWindowTitle("guns")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())