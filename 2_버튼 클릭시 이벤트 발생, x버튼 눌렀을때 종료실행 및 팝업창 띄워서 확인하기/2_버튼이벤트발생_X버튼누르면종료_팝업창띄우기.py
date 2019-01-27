# python version : 3.6
# QT version     : PyQT5

# 기본 임포트
import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 사용할 임포트
# 버튼추가 / 메시지박스 추가 /
from PyQt5.QtWidgets import QPushButton, QMessageBox
# 버튼을 눌렀을때 슬롯을 발생 또는 이벤트 발생
from PyQt5.QtCore import QCoreApplication


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("Push Button", self)          # 버튼 생성.
        btn.resize(btn.sizeHint())                      # 버튼을 좌우 간격에 맞게 조정. 정가운데로
        btn.move(20, 50)                                # 왼쪽상단 기점으로 부터 x,y좌표로 버튼 이동.

        self.resize(500, 500)                       # 위젯 창의 크기를 500 x 500 으로만듦.
        self.setWindowTitle('위젯의 창 이름')       		# 위젯의 창 이름 설정

        # 버튼이 클릭이 되었다(clicked) 그리고 연결한다. (API 인스턴스를 종료시킨다.)
        btn.clicked.connect(QCoreApplication.instance().quit)  # 버튼을 눌렀을 때 종료( quit() )시킴.

        self.show()

    # 버튼 x를 눌렀을때 발생하는 이벤트
    def closeEvent(self, QCloseEvent):
        print("x눌렀을때") # 확인용

        # 메세지박스를 띄움. ( 창 제목 / Prompt / yes스위치 또는 No 스위치 / Default 선택활성화), Yes 또는 No를 ans로 리턴시킬수 있음
        ans = QMessageBox.question(self, "종료 확인", "종료 하실래요?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # 만약 Yes값이 입력 된다면 (상수임)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()        # 이벤트 발생을 승인함.
        else:
            QCloseEvent.ignore()        # 이벤트 발생을 무시함.


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())