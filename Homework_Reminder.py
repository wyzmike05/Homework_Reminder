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
        self.setWindowTitle("item Reminder")
        self.resize(400, 600)
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

        # display item to do
        self.item_to_do_label = QLabel("item To Do:")
        layout.addWidget(self.item_to_do_label)

        self.item_to_do = QListWidget()
        layout.addWidget(self.item_to_do)
        # TODO

        # connect save button with add_item
        self.save_button.clicked.connect(self.add_item)

        # set layout
        self.setLayout(layout)

        # load item
        self.load_item()

    def set_window_position(self):
        """
        set window position
        """
        qr = self.frameGeometry()
        central_point = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(central_point)
        self.move(qr.topLeft())

    def add_item(self):
        """
        write the file with input
        """
        subject = self.subject_input.toPlainText().strip()
        assignment_date = self.assignment_date_input.dateTime()
        content = self.assignment_content_input.toPlainText().strip()
        due_time = self.due_time_input.dateTime()

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

        item_data = {
            "subject": subject,
            "assignment_date": assignment_date,
            "content": content,
            "due_time": due_time,
        }

        if os.path.exists("item_data.json"):
            with open("item_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(item_data)

        data = sorted(data, key=lambda x: x["due_time"])

        with open("item_data.json", "w") as file:
            json.dump(data, file, indent=4)

        self.subject_input.clear()
        self.assignment_content_input.clear()

        self.load_item()

        # TODO

    def load_item(self):
        # 清空当前显示的列表
        self.item_to_do.clear()

        # 检查文件是否存在
        if os.path.exists("item_data.json"):
            with open("item_data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

            # 遍历数据并将每条任务显示在列表中
            for item_data in data:
                subject = item_data["subject"]
                assignment_date = item_data["assignment_date"]
                due_time = item_data["due_time"]
                content = item_data["content"]

                # 将任务内容组合成一个可视化的字符串
                item_text = f"Subject: {subject}\nContent: {content}\nAssigned:{assignment_date}\nDue: {due_time}"

                # 创建QListWidgetItem并添加到QListWidget
                list_item = QListWidgetItem(item_text)
                self.item_to_do.addItem(list_item)
        # TODO

    def finish_item(self):
        pass
        # TODO

    def delete_item(self):
        pass
        # TODO

    def remind_item(self):
        pass
        # TODO

    def edit_item(self):
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
