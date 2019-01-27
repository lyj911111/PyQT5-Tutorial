# Grid 격자형으로 버튼 계산기 만들기 (레이아웃)

import sys
from  PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget,
                              QLineEdit, QGridLayout, QLabel)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('title')         # 순서대로 레이블을 만듬
        author = QLabel('Author')
        review = QLabel('review')

        titleEdit = QLineEdit()     # QLine 한줄짜리 쓸 수 있는 text상자
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()    # QText 한줄이상 여러줄을 쓸 수 있는 text상자

        grid = QGridLayout()
        grid.setSpacing(10)         # 각 객체들 사이에 10의 공간 여백을 줌.

        grid.addWidget(title, 1, 0)         # (1,0) 위치에 title 레이블
        grid.addWidget(titleEdit, 1, 1)     # (1,1) 위치에 text입력 상자 생성. (두 칸의 사이 간격은 10)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)                # (3,0)에 review 레이블
        grid.addWidget(reviewEdit, 3, 1, 5, 1)      # (3,1)에 review Text상자 삽입. 5는 레이블의 기본 위치에 대한 정보와 크기를 키우면 text상자가 커짐
                                                    # 뒤 5,1 을 지우면 레이블이 가운데 위치함.
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Review')         # 창이름
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())