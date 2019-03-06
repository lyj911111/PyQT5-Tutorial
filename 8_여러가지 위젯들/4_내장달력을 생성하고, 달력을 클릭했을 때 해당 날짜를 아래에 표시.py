# 내장된 달력을 출력

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)                    # 세로방향으로 첫번째 Box를 생성

        cal = QCalendarWidget(self)                 # Box에 달력 위젯을 추가
        cal.setGridVisible(True)                    # Grid형식의 달력을 세팅
        cal.clicked[QDate].connect(self.showDate)   # 클릭했을 때 showDate함수로 들어가서 클릭한 날짜[QDate] 를 출력

        vbox.addWidget(cal)

        self.lbl = QLabel(self)                     # 레이블 객체생성
        date = cal.selectedDate()                   # 선택한 날짜를 date 변수에 저장.
        self.lbl.setText(date.toString())           # 그 date를 문자열로 변환해서 lbl으로 보냄

        vbox.addWidget(self.lbl)                    # 세로방향으로 두번째 Box를 생성, 위에서 lbl을 받으면 위젯 추가.

        self.setLayout(vbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Calender")
        self.show()

    # 달력의 날짜를 클릭했을 때 [QDate]의 값이 인자로 전달
    def showDate(self, date):
        self.lbl.setText(date.toString())           # 받은 date를 문자열로 변경


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())