# text창에 있는 문자열을 드레그해서 버튼으로 옮길 경우, 버튼의 글자가 그것으로 바뀜.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Button(QPushButton):
    # 인자 title 에는 'button'이라는 str이 들어올 것이고, parent에는 아래 상속받는 self 가 들어올것이다.
    def __init__(self, title, parent):
        super().__init__(title, parent)     # 'button'과 아래 self를 상속받아 새로운 push버튼을 정의

        self.setAcceptDrops(True)           # 버튼 자체에 Drop기능을 활성화함. (드레그 후 드롭기능을 받아들임)

    # 드레그가 들어왔을 때
    def dragEnterEvent(self, e):
        # 일반적인 text 포멧을 받아들이고, 그 외 무시
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 마우스 드롭 이벤트가 발생했을 때
    def dropEvent(self, e):
        # 드레그 했던(text)를 self(버튼) 자체의 text로 설정을 하겠다.
        self.setText(e.mimeData().text())

# 먼저 수행.
class Example(QWidget):
    def __init__(self):
        super().__init__()                      # super으로 상속 받은 초기화 진행
        self.initUI()                           # initUI 매서드를 호출

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')    # 윈도우 이름 생성 / 좌표, 크기 지정
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()                  # 먼저 수행.
    ex.show()
    sys.exit(app.exec_())