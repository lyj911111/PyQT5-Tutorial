#  체크표시된 메뉴만들기 (메뉴에 활성화)
#  컨텍스트 메뉴 (오른쪽 마우스 클릭하면 생기는 메뉴)

import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow # <= 위젯이 아니고 메인윈도우로 임포트

from  PyQt5.QtWidgets import qApp       # <== 위젯종료를 간단하게 할 수 있는 모듈 임포트**

from  PyQt5.QtWidgets import QAction, QMenu            # <= Action이 되도록 불러옴. /



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
        menu_View = menu.addMenu('View')        # <== View 메뉴를 추가함!

        # 메모리상에 이러한 기능을 만든것임 (실제 GUI가 아니고)
        file_exit = QAction('Exit', self)               # 메뉴 객체 생성.
        file_exit.setShortcut('Ctrl+Q')                 # 단축키를 지정해줌 (set Shortcut)
        file_exit.setStatusTip("누르면 영원히 빠이")    # 상태표시줄 생성.
        view_stat = QAction(" 상태표시줄", self, checkable=True)     #  <== 상태표시줄 (체크박스를 활성화하기 위해  checkable이 필요)
        view_stat.setChecked(True)                                   #  <== 상태표시줄에 이미 체크된 상태로 둠. (Default)

        # file_exit를 누를때 트리거 실행. 위에서 기능을 추가하고 실행하도록 만들어줌
        file_exit.triggered.connect(qApp.quit)                       #  <== qApp을 이용해서 간단하게 종료 트리거를 만듦
        view_stat.triggered.connect(self.toggle_stat)                #  <== 상태표시줄이 활성화 될때 이 toggle_stat 함수(메서드)를 실행(triiger)

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
        menu_View.addAction(view_stat)      # <== View메뉴에 상태표시줄 체크박스를 추가함 ( 선택하는 양식 )

        self.resize(450, 400)
        self.show()

    # <== 토글을 할떄 상태(state)를 저장한다해서 이부분이 들어가야함.
    def toggle_stat(self, state):
        if state == True:                                   # <== 만일 V체크 박스가 활성화 되어있다면 show()
            self.statusBar().show()
            self.statusBar().showMessage("나 활성화 됨")    # <== 아랫쪽에 상태표시줄의 메시지를 확인.
        else:                                               # <== 만일 체크가 없다면, 숨겨라.
            self.statusBar().hide()

    # 마우스 오른쪽 버튼누르면 뜨는 메뉴, 이미정의 되어있는 내장함수를 그데로 가져와서 사용.(상속받아서)
    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)                                              # <== 새로운 메뉴를 만들어 객체에 할당.
        quit = cm.addAction("Quit")                                   # <== 메뉴에 실제로 디스플레이될 Text
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))   # <==  메뉴가 클릭되면 / mapToGlobal 마우스를 어느 좌표에서 눌렀는지 확인.

        if action == quit:                                              # <== 오른쪽마우스의  quit 가 눌렸을때.
            qApp.quit()                                                 # <== 엡을 종료하라.

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())