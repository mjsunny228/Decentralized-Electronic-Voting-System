from PyQt5.QtWidgets import *
import sys

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.form_layout = QFormLayout()

        self.button1 = QPushButton('게시')
        self.button2 = QPushButton('초기화')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.line_edit4 = QLineEdit()


        self.form_layout.addRow('질문: ', self.line_edit1)
        self.form_layout.addRow('선택지: ', self.line_edit2)
        self.form_layout.addRow('', self.line_edit3)
        self.form_layout.addRow('', self.line_edit4)
        self.form_layout.addRow('', self.hbox_layout)


        self.setLayout(self.form_layout)

class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목') #이거 외에는 다 고정코드

        self.group_box1 = QGroupBox('메뉴')

        self.button1 = QPushButton('투표 조회')


        self.hbox_layout=QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.group_box2 = QGroupBox('투표 결과')

        self.progressbar1 = QProgressBar()
        self.progressbar2 = QProgressBar()
        self.progressbar3 = QProgressBar()

        self.progressbar1.setRange(0, 100)
        self.progressbar2.setRange(0, 100)
        self.progressbar3.setRange(0, 100)

        self.value1 = 50
        self.progressbar1.setValue(self.value1)

        self.value2 = 25
        self.progressbar2.setValue(self.value2)

        self.value3 = 25
        self.progressbar3.setValue(self.value3)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.progressbar1)
        self.vbox_layout.addWidget(self.progressbar2)
        self.vbox_layout.addWidget(self.progressbar3)

        self.group_box3 = QGroupBox('투표')

        self.button1 = QPushButton('A1')
        self.button2 = QPushButton('A2')
        self.button3 = QPushButton('A3')

        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.button1)
        self.vbox_layout2.addWidget(self.button2)
        self.vbox_layout2.addWidget(self.button3)

        self.vote_list_group_box = QGroupBox('투표 목록')

        self.vote_list = QListWidget()
        self.vote_list.addItem('투표1')
        self.vote_list.addItem('투표2')

        self.vote_list_vbox_layout = QVBoxLayout()
        self.vote_list_vbox_layout.addWidget(self.vote_list)


        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)
        self.group_box3.setLayout(self.vbox_layout2)
        self.vote_list_group_box.setLayout(self.vote_list_vbox_layout)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.group_box1, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.group_box3, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.group_box2, 3, 0, 1, 2)
        self.grid_layout.addWidget(self.vote_list_group_box,2,0,1,1)

        self.setLayout(self.grid_layout)




class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목') #이거 외에는 다 고정코드

        self.tab1 =Tab1()
        self.tab2 = Tab2()

        self. tabs = QTabWidget()
        self.tabs.addTab(self.tab1, '투표 생성')
        self.tabs.addTab(self.tab2, '투표')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)

        self.setLayout(self.vbox_layout)

def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook=exception_hook
    app = QApplication(sys.argv)
    gui=GUI()
    gui.show()
    sys.exit(app.exec())
