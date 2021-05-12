import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import MiniCactpot
from helper import *
from solver.solver import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = MiniCactpot.Ui_MainWindow()
        self.ui.setupUi(self)

        self.text_edit_buttons = []
        self.load_text_edit_into_list()
        self.assign_value_change_function()

    def load_text_edit_into_list(self):
        self.text_edit_buttons.append(self.ui.textEdit_1)
        self.text_edit_buttons.append(self.ui.textEdit_2)
        self.text_edit_buttons.append(self.ui.textEdit_3)
        self.text_edit_buttons.append(self.ui.textEdit_4)
        self.text_edit_buttons.append(self.ui.textEdit_5)
        self.text_edit_buttons.append(self.ui.textEdit_6)
        self.text_edit_buttons.append(self.ui.textEdit_7)
        self.text_edit_buttons.append(self.ui.textEdit_8)
        self.text_edit_buttons.append(self.ui.textEdit_9)

    def assign_value_change_function(self):
        for x in range(len(self.text_edit_buttons)):
            self.text_edit_buttons[x].textChanged.connect(self.compute_cactpot_matrix)

    def compute_cactpot_matrix(self):

        def sanitize_matrix():
            pass

        textbox_values = [''] * 9
        for x in range(len(self.text_edit_buttons)):
            textbox_values[x] = self.text_edit_buttons[x].toPlainText()

        # cactpot_matrix = to_matrix(textbox_values, 3)
        cactpot_matrix = textbox_values.copy()
        for x in range(len(cactpot_matrix)):
            if cactpot_matrix[x] == '':
                cactpot_matrix[x] = 0
            else:
                cactpot_matrix[x] = int(cactpot_matrix[x])
        print(cactpot_matrix)

        array = textbox_values.copy()
        # Remove all blanks.
        array = [value for value in array if value != '']
        # print(array)

        if has_duplicates(array):
            self.ui.textBrowser.setText("Has duplicates")
        elif too_many_elements(array, 4):
            self.ui.textBrowser.setText("Too many scratches")
        else:
            self.ui.textBrowser.setText("")
            cactpot_solver = Solver()
            cactpot_solver.feed_input(cactpot_matrix)
            cactpot_solver.calculate_expected_line_values()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
