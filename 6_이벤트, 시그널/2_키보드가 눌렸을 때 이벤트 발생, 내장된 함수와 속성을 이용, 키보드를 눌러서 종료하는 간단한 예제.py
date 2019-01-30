# 키보드가 눌렸을 때 발생하는 메소드(함수) 추가
# 내장된 Qt.Key_xxx 를 이용해서 키보드의 입력값을 지정해줄 수 있음.
# 간단한게 키보드 키를 눌러서 종료하는 방법.

import sys
from PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Event Handler')         # 창이름
        self.show()

    # 이미 정의되어 있는 함수를 재정의 함 !!
    # keyPressEvent : 어떤 키보드가 눌렸을 때 발생하는 메소드(Method)
    def keyPressEvent(self, QKeyEvent):         # QkeyEvent : 내가 값을 눌렀을때 값을 전달하는 객체.
        if QKeyEvent.key() == Qt.Key_Escape:    # 키보드의 'ESC'가 눌릴 때 이벤트 발생
            self.close()                        # 종료.

    def keyPressEvent(self, QKeyEvent):         # QkeyEvent : 내가 값을 눌렀을때 값을 전달하는 객체.
        if QKeyEvent.key() == Qt.Key_F4:        # 키보드의 'F4'가 눌릴 때 이벤트 발생
            self.close()

    def keyPressEvent(self, QKeyEvent):         # QkeyEvent : 내가 값을 눌렀을때 값을 전달하는 객체.
        if QKeyEvent.key() == Qt.Key_8:         # 키보드의 '8'이 눌릴 때 이벤트 발생
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())