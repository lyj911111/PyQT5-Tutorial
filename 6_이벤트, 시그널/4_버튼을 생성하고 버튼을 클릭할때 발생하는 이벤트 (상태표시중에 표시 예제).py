# 버튼을 생성하고, 버튼이 눌렸을 때 발생하는 이벤트.

import sys
from PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼1,2 을 추가하고, 버튼의 위치를 지정. (레이아웃 없이, 절대좌표로 지정)
        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        # 버튼이 눌렸을 때 메서드(함수)와 연결)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()        # 아래 상태창.

        self.setGeometry(300, 300, 290, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Event sender')         # 창이름
        self.show()

    def buttonClicked(self):
        sender = self.sender()  # 왼쪽의 sender는 변수명, 오른쪽 sender()는 함수를 호출한 '객체'를 가져오는 놈. / 여기서는 btn2 가 sender()으로 들어감.
        self.statusBar().showMessage(sender.text() + ' was pressed')     # 아래 상태창에, sender가 갖고있는 text값을 보여줌.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())