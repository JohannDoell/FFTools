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
        self.assign_value_change_listen_function()

    def load_text_edit_into_list(self):
        """Adds each text entry object into the Python list text_edit_buttons"""
        self.text_edit_buttons.append(self.ui.textEdit_1)
        self.text_edit_buttons.append(self.ui.textEdit_2)
        self.text_edit_buttons.append(self.ui.textEdit_3)
        self.text_edit_buttons.append(self.ui.textEdit_4)
        self.text_edit_buttons.append(self.ui.textEdit_5)
        self.text_edit_buttons.append(self.ui.textEdit_6)
        self.text_edit_buttons.append(self.ui.textEdit_7)
        self.text_edit_buttons.append(self.ui.textEdit_8)
        self.text_edit_buttons.append(self.ui.textEdit_9)

    def assign_value_change_listen_function(self):
        """Assigns the function compute_cactpot_matrix to each text entry object"""
        for x in range(len(self.text_edit_buttons)):
            self.text_edit_buttons[x].textChanged.connect(self.compute_cactpot_matrix)

    def compute_cactpot_matrix(self):
        """
        Takes the values from the UI and sends the cactpot board to solver.py
        """

        def sanitize_matrix(textbox_entries):
            """
            Sanitizes the cactpot matrix for use with solver.py
            :param textbox_entries: The list of textbox values from the UI with this index form:
            0 1 2
            3 4 5
            6 7 8
            :return: The sanitized matrix.
            """
            # cactpot_matrix = to_matrix(textbox_values, 3)
            matrix_to_sanitize = textbox_entries.copy()
            for i in range(len(matrix_to_sanitize)):
                if matrix_to_sanitize[i] == '':
                    matrix_to_sanitize[i] = 0
                else:
                    matrix_to_sanitize[i] = int(matrix_to_sanitize[i])
            # print(cactpot_matrix)
            return matrix_to_sanitize

        # Get values from the UI
        textbox_values = [''] * 9
        for x in range(len(self.text_edit_buttons)):
            textbox_values[x] = self.text_edit_buttons[x].toPlainText()

        cactpot_matrix = sanitize_matrix(textbox_values)

        # Remove the blanks from the original non-sanitized matrix for validity checks.
        test_array = textbox_values.copy()
        test_array = [value for value in test_array if value != '']

        if has_duplicates(test_array):
            self.ui.textBrowser.setText("Has duplicates")
        elif too_many_elements(test_array, 4):
            self.ui.textBrowser.setText("Too many scratches")
        else:
            self.ui.textBrowser.setText("")
            cactpot_solver = Solver()
            cactpot_solver.feed_input(cactpot_matrix)
            print(cactpot_solver.calculate_expected_line_values())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
