import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel,
    QDateTimeEdit,
    QListWidget,
    QListWidgetItem,
    QDesktopWidget,
    QHBoxLayout,
    QCheckBox,
    QMessageBox,
)
from PyQt5.QtCore import QDateTime


class W_Reminder(QWidget):
    def __init__(self):
        super().__init__()

        # set window title window size and window position
        self.setWindowTitle("task Reminder")
        self.resize(1000, 1000)
        self.set_window_position()

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
        # connect save button with add_task
        self.save_button.clicked.connect(self.add_task)

        # display task to do
        self.task_todo_label = QLabel("task To Do:")
        layout.addWidget(self.task_todo_label)

        self.task_todo = QListWidget()
        layout.addWidget(self.task_todo)

        # display task done
        self.task_done_label = QLabel("task done:")
        layout.addWidget(self.task_done_label)

        self.task_done = QListWidget()
        layout.addWidget(self.task_done)
        # TODO

        # set layout
        self.setLayout(layout)

        # load task
        self.load_task()

    def set_window_position(self):
        """
        set window position
        """
        qr = self.frameGeometry()
        # get central point
        central_point = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(central_point)
        self.move(qr.topLeft())

    def add_task(self):
        """
        write the file with input
        """

        subject = self.subject_input.toPlainText().strip()
        assignment_date = self.assignment_date_input.dateTime()
        content = self.assignment_content_input.toPlainText().strip()
        due_time = self.due_time_input.dateTime()
        done = False

        if not subject or not content:
            QMessageBox.warning(self, "Error", "Subject and content cannot be empty!")
            return

        if due_time < assignment_date:
            QMessageBox.warning(
                self, "Error", "Assignment time must be earlier than due time!"
            )
            return
        assignment_date = assignment_date.toString("yyyy-MM-dd HH:mm")
        due_time = due_time.toString("yyyy-MM-dd HH:mm")

        task_data = {
            "subject": subject,
            "assignment_date": assignment_date,
            "content": content,
            "due_time": due_time,
            "done": done,
        }

        if os.path.exists("task_data.json"):
            with open("task_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(task_data)

        data = sorted(data, key=lambda x: x["due_time"])

        with open("task_data.json", "w") as file:
            json.dump(data, file, indent=4)

        self.subject_input.clear()
        self.assignment_content_input.clear()

        self.load_task()

        # TODO

    def load_task(self):
        """
        with state todo (False) and done (True)
        """
        # clear the lists
        self.task_todo.clear()
        self.task_done.clear()

        if os.path.exists("task_data.json"):
            with open("task_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

            for task_data in data:
                # read file
                subject = task_data["subject"]
                assignment_date = task_data["assignment_date"]
                due_time = task_data["due_time"]
                content = task_data["content"]
                done = task_data["done"]

                task_widget = QWidget()
                task_layout = QHBoxLayout()
                task_widget.setLayout(task_layout)
                list_task = QListWidgetItem()

                # task label
                task_label = QLabel(
                    f"Subject: {subject}\nContent: {content}\nAssigned: {assignment_date}\nDue: {due_time}"
                )
                task_layout.addWidget(task_label)

                # edit button
                edit_button = QPushButton("Edit")
                edit_button.clicked.connect(lambda: self.edit_task(task_data))
                task_layout.addWidget(edit_button)

                # delete button
                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda: self.delete_task(task_data))
                task_layout.addWidget(delete_button)

                if done:
                    uncomplete_button = QPushButton("Uncomplete")
                    uncomplete_button.clicked.connect(
                        lambda: self.uncomplete_task(task_data)
                    )
                    task_layout.addWidget(uncomplete_button)

                    self.task_done.addItem(list_task)

                    self.task_done.setItemWidget(list_task, task_widget)
                else:
                    complete_button = QPushButton("Complete")
                    complete_button.clicked.connect(
                        lambda: self.complete_task(task_data)
                    )
                    task_layout.addWidget(complete_button)

                    self.task_todo.addItem(list_task)

                    self.task_todo.setItemWidget(list_task, task_widget)

                list_task.setSizeHint(task_widget.sizeHint())
        # TODO

    def complete_task(self, task_data):
        if os.path.exists("task_data.json"):
            with open("task_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
            try:
                index = data.index(task_data)
            except ValueError:
                print("Task Not Found...")
                return
            data[index]["done"] = True

            with open("task_data.json", "w") as file:
                json.dump(data, file, indent=4)

        # TODO

        self.load_task()

    def uncomplete_task(self, task_data):
        if os.path.exists("task_data.json"):
            with open("task_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
            try:
                index = data.index(task_data)
            except ValueError:
                print("Task Not Found...")
                return
            data[index]["done"] = False

            with open("task_data.json", "w") as file:
                json.dump(data, file, indent=4)
        # TODO
        self.load_task()

    def delete_task(self, task_data):
        if os.path.exists("task_data.json"):
            with open("task_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
            try:
                data.remove(task_data)
            except ValueError:
                return

            with open("task_data.json", "w") as file:
                json.dump(data, file, indent=4)

        # TODO
        self.load_task()

    def remind_task(self):
        pass
        # TODO

    def edit_task(self):
        pass
        # TODO

    def alert(self):
        pass
        # TODO


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create main window
    window = W_Reminder()
    window.show()

    # execution
    sys.exit(app.exec_())
