# 위에 메뉴바 만들기
# ** 주의사항: 만들 때 메뉴의 코드의 구조: - 서브그룹
#                                           - 서브 메뉴 추가
#                                           - 주 메뉴추가 (그룹)
# 이 순서로 안하면 코드가 꼬일 수 도 있다.

import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow # <= 위젯이 아니고 메인윈도우로 임포트
from  PyQt5.QtWidgets import QAction, QMenu            # <= Action이 되도록 불러옴. /
from  PyQt5.QtCore import QCoreApplication          # 엑션 트리거 만들때사용

# 상속인자를  Qwidget이 아니고 QMainWindow 로 해야함.
class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()                                    # 상태 표시창을 생성.
        self.statusBar().showMessage("안녕상태표시줄")      # 상태 표시줄 생성. (어떠한 상태인지 설명해줌)

        menu = self.menuBar()                   # 메뉴창을 생성함.
        menu_File = menu.addMenu('File')        # 파일바에 그룹생성.
        menu_Edit = menu.addMenu('Edit')
        menu_View = menu.addMenu('View')

        # 메모리상에 이러한 기능을 만든것임 (실제 GUI가 아니고)
        file_exit = QAction('Exit', self)               # 메뉴 객체 생성.
        file_exit.setShortcut('Ctrl+Q')                 # 단축키를 지정해줌 (set Shortcut)
        file_exit.setStatusTip("누르면 영원히 빠이")    # 상태표시줄 생성.

        # file_exit를 누를때 트리거 실행. 위에서 기능을 추가하고 실행하도록 만들어줌
        file_exit.triggered.connect(QCoreApplication.instance().quit)

        new_txt = QAction("텍스트 파일", self)
        new_py = QAction("파이썬 파일", self)


        # Sub 그룹을 만듦.
        file_new = QMenu('New', self)

        # Sub 그룹의 하위 목록으로 2가지 Action 메뉴가 생성됨.
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        #  Main 메뉴추가(전체 그룹)
        menu_File.addMenu(file_new)             # 하위 sub메뉴를 갖고있는 메뉴를 등록.
        menu_File.addAction(file_exit)          # 누르면 Action하는 메뉴를 등록함.

        self.resize(450, 400)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())