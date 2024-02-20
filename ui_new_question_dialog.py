from PyQt5 import QtWidgets

from PyQt5.QtCore import QMetaObject, QMetaObject, QCoreApplication, QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame, QLabel, QGroupBox, QPlainTextEdit, QRadioButton, QPushButton, QSpacerItem


class Ui_NewQuestion_Dialog(object):
    def setupUi(self, Dialog):
        # dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 800)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(500, 800))
        Dialog.setStyleSheet(
            "background-color: rgb(240, 240, 240);"
        )
        self.dialog_layout = QVBoxLayout(Dialog)
        self.dialog_layout.setContentsMargins(0, 0, 0, 0)
        self.dialog_layout.setSpacing(0)
        self.dialog_layout.setObjectName("dialog_layout")





        # title frame
        self.title_frame = QFrame(Dialog)
        self.title_frame.setMinimumSize(QSize(0, 80))
        self.title_frame.setMaximumSize(QSize(16777215, 80))
        self.title_frame.setStyleSheet(
            "background-color: rgb(59, 84, 188);\n"
            "color: white;"
        )
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.titleFrame_layout = QVBoxLayout(self.title_frame)
        self.titleFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame_layout.setSpacing(0)
        self.titleFrame_layout.setObjectName("titleFrame_layout")

        # title label
        self.title_label = QLabel(self.title_frame)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.titleFrame_layout.addWidget(self.title_label)
        self.dialog_layout.addWidget(self.title_frame)





        # body frame
        self.body_frame = QFrame(Dialog)
        self.body_frame.setStyleSheet(
            "QPlainTextEdit {\n"
                "background-color: white;\n"
            "}"
        )
        self.body_frame.setFrameShape(QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.bodyFrame_layout = QVBoxLayout(self.body_frame)
        self.bodyFrame_layout.setContentsMargins(24, 24, 24, 0)
        self.bodyFrame_layout.setSpacing(0)
        self.bodyFrame_layout.setObjectName("bodyFrame_layout")

        # body plain text edit
        self.body_plain_text_edit = QPlainTextEdit(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        self.body_plain_text_edit.setFont(font)
        self.body_plain_text_edit.setFrameShape(QFrame.NoFrame)
        self.body_plain_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.body_plain_text_edit.setObjectName("body_plain_text_edit")
        self.bodyFrame_layout.addWidget(self.body_plain_text_edit)
        self.dialog_layout.addWidget(self.body_frame)





        # actions frame
        self.actions_frame = QFrame(Dialog)
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.actionsFrame_layout = QVBoxLayout(self.actions_frame)
        self.actionsFrame_layout.setContentsMargins(24, 24, 24, 24)
        self.actionsFrame_layout.setSpacing(6)
        self.actionsFrame_layout.setObjectName("actionsFrame_layout")

        # question type group box
        self.question_type_group_box = QGroupBox(self.actions_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.question_type_group_box.setFont(font)
        self.question_type_group_box.setStyleSheet(
            "QGroupBox {\n"
                "border: 1px solid rgb(220, 220, 220);\n"
                "border-radius: 20px;\n"
                "padding-top: 15px;\n"
                "color: rgb(59, 84, 188);\n"
            "}"
        )
        self.question_type_group_box.setAlignment(Qt.AlignCenter)
        self.question_type_group_box.setFlat(False)
        self.question_type_group_box.setObjectName("question_type_group_box")
        self.questionTypeGroupBox_layout = QHBoxLayout(self.question_type_group_box)
        self.questionTypeGroupBox_layout.setContentsMargins(15, 5, 15, 5)
        self.questionTypeGroupBox_layout.setSpacing(0)
        self.questionTypeGroupBox_layout.setObjectName("questionTypeGroupBox_layout")

        # general question radio button
        self.general_question_radio_button = QRadioButton(self.question_type_group_box)
        self.general_question_radio_button.setObjectName("general_question_radio_button")
        self.questionTypeGroupBox_layout.addWidget(self.general_question_radio_button)

        # spacer item
        question_type_group_box_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.questionTypeGroupBox_layout.addItem(question_type_group_box_left_spacer)

        # technical question radio button
        self.technical_question_radio_button = QRadioButton(self.question_type_group_box)
        self.technical_question_radio_button.setObjectName("technical_question_radio_button")
        self.questionTypeGroupBox_layout.addWidget(self.technical_question_radio_button)

        # spacer item
        question_type_group_box_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.questionTypeGroupBox_layout.addItem(question_type_group_box_right_spacer)

        # coding question radio button
        self.coding_question_radio_button = QRadioButton(self.question_type_group_box)
        self.coding_question_radio_button.setObjectName("coding_question_radio_button")
        self.questionTypeGroupBox_layout.addWidget(self.coding_question_radio_button)
        self.actionsFrame_layout.addWidget(self.question_type_group_box)

        # error frame
        self.error_frame = QFrame(self.actions_frame)
        self.error_frame.setStyleSheet(
            "color: red;"
        )
        self.error_frame.setFrameShape(QFrame.StyledPanel)
        self.error_frame.setFrameShadow(QFrame.Raised)
        self.error_frame.setObjectName("error_frame")
        self.errorFrame_layout = QVBoxLayout(self.error_frame)
        self.errorFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.errorFrame_layout.setSpacing(0)
        self.errorFrame_layout.setObjectName("errorFrame_layout")

        # error label
        self.error_label = QLabel(self.error_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.errorFrame_layout.addWidget(self.error_label)
        self.actionsFrame_layout.addWidget(self.error_frame)

        # button frame
        self.button_frame = QFrame(self.actions_frame)
        self.button_frame.setStyleSheet(
            "QPushButton {\n"
                "padding: 15px 35px;\n"
                "border: none;\n"
                "border-radius: 5px;\n"
                "background-color: rgb(46, 196, 89);\n"
                "color: white;\n"
            "}\n"
            "QPushButton:Hover {\n"
                "background-color: rgb(25, 110, 50);\n"
            "}\n"
            "QPushButton:Pressed {\n"
                "background-color: rgb(33, 150, 243);\n"
            "}"
        )
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.buttonFrame_layout = QHBoxLayout(self.button_frame)
        self.buttonFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.buttonFrame_layout.setSpacing(0)
        self.buttonFrame_layout.setObjectName("buttonFrame_layout")

        # spacer item
        button_frame_left_spacer = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.buttonFrame_layout.addItem(button_frame_left_spacer)

        # add question button
        self.add_question_button = QPushButton(self.button_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_question_button.setFont(font)
        self.add_question_button.setObjectName("add_question_button")
        self.buttonFrame_layout.addWidget(self.add_question_button)

        # spacer item
        button_frame_right_spacer = QSpacerItem(173, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.buttonFrame_layout.addItem(button_frame_right_spacer)

        # 
        self.actionsFrame_layout.addWidget(self.button_frame)
        self.dialog_layout.addWidget(self.actions_frame)




        #
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "NEW QUESTION"))
        self.question_type_group_box.setTitle(_translate("Dialog", "Question Type"))
        self.general_question_radio_button.setText(_translate("Dialog", "General"))
        self.technical_question_radio_button.setText(_translate("Dialog", "Technical"))
        self.coding_question_radio_button.setText(_translate("Dialog", "Coding"))
        self.error_label.setText(_translate("Dialog", ""))
        self.add_question_button.setText(_translate("Dialog", "Add"))
