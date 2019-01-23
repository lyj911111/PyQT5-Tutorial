import sys      # 기본적으로 가져와야함, 시스템 쉘 정보등을 담고있음.

# QTWidgets 에 대부분의 기본 기능을 갖고있음. 버튼, 툴팁텍스트 추가 등등
from PyQt5.QtWidgets import QApplication, QWidget   # 기본적으로 가져와야 할 2가지 모듈

# QWidget 을 상속받아 클래스 생성. (나만의 창을 만들기 위한)
class Exam(QWidget):
    # 생성자 만들기
    def __init__(self):
        super().__init__()           # super(): 상위 계층이 생성됨.
        self.initUI()                # 내가 사용할 함수, Method 매서드를 만듬
    def initUI(self):
        self.show()                 # 사용자가 볼 수 있도록 출력 (기본적으로 만들기)

# app : 어플리케이션 객체생성
# sys.argv : 시스템의 명령을 받아서 진행할때
app = QApplication(sys.argv)        # 모든 Qt5의 어플리케이션은 반드시 QApplication object를 생성해야 한다. (기본적인 사항)

w = Exam()      # w라는 객체 생성 내가만든 class를 이용해서

# app.exec_() : Main 루프를 실행 이벤트가 발생할 때까지 실행. 사용자가 프로그램을 종료를하면  sys.exit() 으로 깨끗하게 종료시킴.
sys.exit(app.exec_())
