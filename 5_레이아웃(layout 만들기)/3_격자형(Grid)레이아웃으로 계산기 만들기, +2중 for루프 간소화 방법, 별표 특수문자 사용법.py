# Grid 격자형으로 버튼 계산기 만들기 (레이아웃)

import sys
from  PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()        # 격자형태의 레이아웃 객체 생성.
        self.setLayout(grid)        # 격자의 레이아웃 세팅.

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '*', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]     # i 가 [0]일때, j 는 [0~3]까지, i가 [1]일때 j는 [0~3]까지 ... 이런식으로 2중 루프 진행.
                                                                     # 그럼 postions는 [0,0] [0,1] [0,2] [0,3]
                                                                     #                 [1,0] [1,1] [1,2] [1,3]...  으로 행렬이 만들어짐.

        for position, name in zip(positions, names):                   # ** zip : (동일한 갯수로 이루어진 자료형을 묶어줌.) / 2개의 리스트를 하나의 튜플로 묶어줌.
            if name == '':                                             # 즉, (0, 0) 을 넘기고, 'Cls'를 넘김. / (0, 1)을 넘기고, 'Bck'를 넘김 / 빈칸제외 / (0, 3)을 넘기고, 'Close'를 넘김
                continue                                               # 빈칸인 경우를 제외하고
            btn = QPushButton(name)                                    # name 에 버튼기능을 추가.
            grid.addWidget(btn, *position)                             # *position 의 '*'의미 =>  posion에서는 예) 튜플값(0,2)가 날라오게 되는데, 이를 0, 2 로 바꿔줌.
                                                                       # 즉, grid.addWidget(btn, 0, 2) 이런식으로 받을 수 있도록 만들어 주는 것임.
        self.move(300, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Calculator')         # 창이름
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())