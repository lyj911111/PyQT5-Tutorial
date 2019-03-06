# 이미지를 나타낼 수 있는 위젯.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    # 인자 title 에는 'button'이라는 str이 들어올 것이고, parent에는 아래 상속받는 self 가 들어올것이다.
    def __init__(self, title, parent):
        super().__init__(title, parent)     # 'button'과 아래 self를 상속받아 새로운 push버튼을 정의

    # ** e 매개변수 : event 매서드에는 항상 e라는 매서드가 필요,해당 이벤트가 발생한 객체. 예) 버튼이 눌렸을 때 발생하는 하나의 이벤트, 객체를 다르게 하여 다른 버튼이 눌렸을 때 나타나는 효과를 만들 수 있음
    # 버튼 위에서 마우스가 움직이고 있을 때 발생하는 이벤트
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:       # 오른쪽 버튼이 눌린상태가 아니면 종료
            return

        mimeData = QMimeData()              # Mime는 다양한 멀티미디어 데이터를 다룰 수 있음.

        # 버튼에는 드레그 기능이 없기 떄문에 추가함.
        drag = QDrag(self)          # 드레그 객체 생성
        drag.setMimeData(mimeData)  # 이 객체가 건들 수 있는 객체(mimeData)를 지정.

        drag.exec_(Qt.MoveAction)   # 드레그 객체 활성화. (움직임 action) - 오른쪽이 눌렸을 때

    def mousePressEvent(self, e):

        # 상의 클레스를 상속받지 않으면, "버튼 클릭 효과"가 나타나지 않음 (왼쪽 마우스로 눌렸을때 눌린자국 표시)
        super().mousePressEvent(e)

        # 마우스가 왼쪽이 클릭 되었을 때 출력
        if e.button() == Qt.LeftButton:
            print('press')

# 먼저 수행.
class Example(QWidget):
    def __init__(self):
        super().__init__()                      # super으로 상속 받은 초기화 진행
        self.initUI()                           # initUI 매서드를 호출

    def initUI(self):
        self.setAcceptDrops(True)               # Drop Event를 활성화 (마우스를 drag한 후 때었을 때 Drop)

        # Button 클레스에 'Button' 인수를 넘김.
        self.button = Button('Button', self)    # 버튼 객체생성 및 추가
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')    # 윈도우 이름 생성 / 좌표, 크기 지정
        self.setGeometry(300, 300, 300, 200)

    # 내장 매서드를 재정의함 (파이참 왼쪽에 파랑색으로 표시됨)
    # ** 마우스를 Drag 할 때 발생하는 이벤트
    def dragEnterEvent(self, e):
        e.accept()        # 데이터가 이동되는 매서드에는 반드시 '허용 여부'를 해야함

    # ** 마우스 드레그를 하다가 마우를 놓았을 때 drop이 발생하는 이벤트!
    # (때에 따라서 if문을 이용해 데이터 종류를 제한할 수 있음)
    def dropEvent(self, e):
        position = e.pos()                      # 그때의 마우스가 위치한 좌표
        self.button.move(position)              # 그 position에 버튼을 이동시킴

        e.accept()        # 데이터가 이동되는 매서드에는 반드시 '허용 여부'를 해야함

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()                  # 먼저 수행.
    ex.show()
    sys.exit(app.exec_())