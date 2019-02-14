# 대화상자 만들기.
# 버튼을 클릭 후, 입력 대화상자를 누르고,
# Cancel을 누를 경우 취소, 값을 입력하고 OK를 누르면 값이 입력됨.


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)          # 버튼추가
        self.btn.move(20, 20)                           # 위치 지정,
        self.btn.clicked.connect(self.showDialog)       # 버튼 클릭시 함수(메서드)와 연결.

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Input Dialog')      # 창이름
        self.show()

    # Dialog 대화장자를 만듦.
    def showDialog(self):
        # 사용자가 입력한 문자는 text객체에 문자열(String)로 return / 사용자가 버튼 ok를 누르면 ok값에 True가 return
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')    # 대화상자 제목설정 / 입력 Prompt 설정.

        if ok:
            self.le.setText(text)      # ok값이 True일 경우, text에 입력한 문자열을 le에 넣어라.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())