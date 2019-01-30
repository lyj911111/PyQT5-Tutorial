# 신호를 보낼 수 있는 객체를 생성하기. (QObject를 상속받은 pyqtSignal)

# 1. 마우스클릭
# 2. mousePressEvent가 발생.
# 3. closeApp 객체에 신호가 방출되었으면 한다.Emit()
# 4. closeApp 과 연결된(.connect) self.close를 실행 시킨다.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow

class Communicate(QObject):
    closeApp = pyqtSignal()     # pyqtSignal()을 쓰기 위해서 위에서 QObject를 상속 받음.
                                # pyqtSignal() : 신호를 보낼 수 있는 객체를 생성한다.
                                # 이제 "closeApp"은 신호를 보낼 수 있는 객체가 되었다.
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()                  # c 객체는 위에 메서드의 기능을 갖음.
        self.c.closeApp.connect(self.close)     # c 의 closeApp 에 "창을 닫는 이벤트(self.close)"를 연결.

        self.setGeometry(300, 300, 290, 150)    # 초기 창 위치좌표와 크기 설정.
        self.setWindowTitle('Emit signal')      # 창이름
        self.show()

    # 마우스를 눌렀을 때 이벤트.
    def mousePressEvent(self, event):
        self.c.closeApp.emit()                  # 이벤트가 발생하면(emit), closeApp과 연결된 slot에 신호를 줌.
                                                # 결론: closeApp과 연결된 메서드(함수)를 호출하라.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())