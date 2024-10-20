import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QDateTimeEdit,
    QMessageBox,
    QApplication,
    QDesktopWidget,
)
from PyQt5.QtCore import QDateTime


class W_Reminder(QWidget):
    def __init__(self):
        super().__init__()

        # set window title window size and window position
        self.setWindowTitle("Homework Reminder")
        self.resize(400, 600)
        self.initialize_window_position()

        # create layout
        layout = QVBoxLayout()

        # subject
        self.subject_label = QLabel("Subject:")
        layout.addWidget(self.subject_label)

        self.subject_input = QTextEdit()
        layout.addWidget(self.subject_input)

        # assignment date input
        self.assignment_date_label = QLabel("Assignment Date:")
        layout.addWidget(self.assignment_date_label)

        self.assignment_date_input = QDateTimeEdit()
        self.assignment_date_input.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.assignment_date_input)

        # assignment content input
        self.assignment_content_label = QLabel("Assignment Content:")
        layout.addWidget(self.assignment_content_label)

        self.assignment_content_input = QTextEdit()
        layout.addWidget(self.assignment_content_input)

        # input due time
        self.due_time_label = QLabel("Due Time:")
        layout.addWidget(self.due_time_label)

        self.due_time_input = QDateTimeEdit()
        self.due_time_input.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.due_time_input)

        # save button
        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)

        # display item to do
        self.item_to_do_label = QLabel("item To Do:")
        layout.addWidget(self.item_to_do_label)

        self.item_to_do_display = QTextEdit()
        self.item_to_do_display.setReadOnly(True)
        layout.addWidget(self.item_to_do_display)

        # connect save button with add_item
        self.save_button.clicked.connect(self.add_item)

        # set layout
        self.setLayout(layout)

        # load item
        self.load_item()

    def initialize_window_position(self):
        qr = self.frameGeometry()
        central_point = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(central_point)
        self.move(qr.topLeft())

    def add_item(self):
        pass  # TODO

    def load_item(self):
        pass  # TODO

    def finish_item(self):
        pass  # TODO

    def delete_item(self):
        pass  # TODO

    def remind_item(self):
        pass  # TODO

    def edit_item(self):
        pass  # TODO

    def alert(self):
        pass  # TODO


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create main window
    window = W_Reminder()
    window.show()

    # execution
    sys.exit(app.exec_())
