import sqlite3

from PyQt5.QtCore import QSize, QRect, QDate, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QDialog, QWidget,
    QFrame, QGroupBox,
    QLabel, QSpacerItem,
    QPushButton, QLineEdit, QDateEdit, QComboBox, QPlainTextEdit,
    QHBoxLayout, QVBoxLayout, QSizePolicy,
    QScrollArea
    )

class Ui_NewApplication_Dialog(object):
    def setupUi(self, dialog):
        print("Setting up Ui_NewApplication_Dialog")
        # dialog window
        dialog.setObjectName("Dialog")
        dialog.resize(500, 800)
        dialog.setMinimumSize(QSize(500, 400))
        dialog.setMaximumSize(QSize(500, 800))
        self.verticalLayout_19 = QVBoxLayout(dialog)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")

        # scroll area
        self.scrollArea = QScrollArea(dialog)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -177, 481, 975))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")





        # title frame
        self.title_frame = QFrame(self.scrollAreaWidgetContents)
        self.title_frame.setMinimumSize(QSize(0, 80))
        self.title_frame.setMaximumSize(QSize(16777215, 80))
        self.title_frame.setStyleSheet(
            "QFrame {\n"
                "color: white;\n"
                "background-color: rgb(33, 150, 243);\n"
            "}"
        )
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.verticalLayout = QVBoxLayout(self.title_frame)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # title label
        self.title_label = QLabel(self.title_frame)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.verticalLayout_22.addWidget(self.title_frame)





        # body frame
        self.body_frame = QFrame(self.scrollAreaWidgetContents)
        self.body_frame.setStyleSheet(
            "#body_frame {\n"
                "background-color: rgb(240, 240, 240);\n"
            "}\n"
            "QGroupBox {\n"
                "border: 1px solid rgb(220, 220, 220);\n"
                "border-radius: 20px;\n"
                "padding-top: 15px;\n"
                "color: rgb(33, 150, 243);\n"
            "}\n"
            "QLineEdit, QComboBox, QPlainTextEdit, QTableWidget {\n"
                "border: 0px;\n"
            "}"
        )
        self.body_frame.setFrameShape(QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.verticalLayout_23 = QVBoxLayout(self.body_frame)
        self.verticalLayout_23.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_23.setSpacing(24)
        self.verticalLayout_23.setObjectName("verticalLayout_23")





        # company details group box
        self.company_details_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.company_details_group_box.setFont(font)
        self.company_details_group_box.setFlat(True)
        self.company_details_group_box.setObjectName("company_details_group_box")
        self.verticalLayout_5 = QVBoxLayout(self.company_details_group_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # company frame
        self.company_frame = QFrame(self.company_details_group_box)
        self.company_frame.setFrameShape(QFrame.StyledPanel)
        self.company_frame.setFrameShadow(QFrame.Raised)
        self.company_frame.setObjectName("company_frame")
        self.verticalLayout_2 = QVBoxLayout(self.company_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # company label
        self.company_label = QLabel(self.company_frame)
        self.company_label.setObjectName("company_label")
        self.verticalLayout_2.addWidget(self.company_label)

        # company line edit
        self.company_line_edit = QLineEdit(self.company_frame)
        self.company_line_edit.setMinimumSize(QSize(0, 25))
        self.company_line_edit.setMaximumSize(QSize(16777215, 25))
        self.company_line_edit.setObjectName("company_line_edit")
        self.verticalLayout_2.addWidget(self.company_line_edit)
        self.verticalLayout_5.addWidget(self.company_frame)

        # city frame
        self.city_frame = QFrame(self.company_details_group_box)
        self.city_frame.setFrameShape(QFrame.StyledPanel)
        self.city_frame.setFrameShadow(QFrame.Raised)
        self.city_frame.setObjectName("city_frame")
        self.verticalLayout_3 = QVBoxLayout(self.city_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # city label
        self.city_label = QLabel(self.city_frame)
        self.city_label.setObjectName("city_label")
        self.verticalLayout_3.addWidget(self.city_label)

        # city line edit
        self.city_line_edit = QLineEdit(self.city_frame)
        self.city_line_edit.setMinimumSize(QSize(0, 25))
        self.city_line_edit.setMaximumSize(QSize(16777215, 25))
        self.city_line_edit.setObjectName("city_line_edit")
        self.verticalLayout_3.addWidget(self.city_line_edit)
        self.verticalLayout_5.addWidget(self.city_frame)

        # state frame
        self.state_frame = QFrame(self.company_details_group_box)
        self.state_frame.setFrameShape(QFrame.StyledPanel)
        self.state_frame.setFrameShadow(QFrame.Raised)
        self.state_frame.setObjectName("state_frame")
        self.verticalLayout_4 = QVBoxLayout(self.state_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # state label
        self.state_label = QLabel(self.state_frame)
        self.state_label.setObjectName("state_label")
        self.verticalLayout_4.addWidget(self.state_label)

        # state combo box
        self.state_combo_box = QComboBox(self.state_frame)
        self.state_combo_box.setMinimumSize(QSize(0, 25))
        self.state_combo_box.setMaximumSize(QSize(16777215, 25))
        self.state_combo_box.setObjectName("state_combo_box")
        for _ in range(51):
            self.state_combo_box.addItem("")
        self.verticalLayout_4.addWidget(self.state_combo_box)
        self.verticalLayout_5.addWidget(self.state_frame)
        self.verticalLayout_23.addWidget(self.company_details_group_box)





        # position group box
        self.position_details_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.position_details_group_box.setFont(font)
        self.position_details_group_box.setFlat(True)
        self.position_details_group_box.setObjectName("position_details_group_box")
        self.verticalLayout_10 = QVBoxLayout(self.position_details_group_box)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        # position frame
        self.position_frame = QFrame(self.position_details_group_box)
        self.position_frame.setFrameShape(QFrame.StyledPanel)
        self.position_frame.setFrameShadow(QFrame.Raised)
        self.position_frame.setObjectName("position_frame")
        self.verticalLayout_6 = QVBoxLayout(self.position_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # position label
        self.position_label = QLabel(self.position_frame)
        self.position_label.setObjectName("position_label")
        self.verticalLayout_6.addWidget(self.position_label)
        self.position_line_edit = QLineEdit(self.position_frame)
        self.position_line_edit.setMinimumSize(QSize(0, 25))
        self.position_line_edit.setMaximumSize(QSize(16777215, 25))
        self.position_line_edit.setObjectName("position_line_edit")
        self.verticalLayout_6.addWidget(self.position_line_edit)
        self.verticalLayout_10.addWidget(self.position_frame)

        # work style frame
        self.work_style_frame = QFrame(self.position_details_group_box)
        self.work_style_frame.setFrameShape(QFrame.StyledPanel)
        self.work_style_frame.setFrameShadow(QFrame.Raised)
        self.work_style_frame.setObjectName("work_style_frame")
        self.verticalLayout_7 = QVBoxLayout(self.work_style_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # work style label
        self.work_style_label = QLabel(self.work_style_frame)
        self.work_style_label.setObjectName("work_style_label")
        self.verticalLayout_7.addWidget(self.work_style_label)

        # work style combo box
        self.work_style_combo_box = QComboBox(self.work_style_frame)
        self.work_style_combo_box.setMinimumSize(QSize(0, 25))
        self.work_style_combo_box.setMaximumSize(QSize(16777215, 25))
        self.work_style_combo_box.setObjectName("work_style_combo_box")
        for _ in range(4):
                self.work_style_combo_box.addItem("")
        self.verticalLayout_7.addWidget(self.work_style_combo_box)
        self.verticalLayout_10.addWidget(self.work_style_frame)

        # employment status frame
        self.employment_status_frame = QFrame(self.position_details_group_box)
        self.employment_status_frame.setFrameShape(QFrame.StyledPanel)
        self.employment_status_frame.setFrameShadow(QFrame.Raised)
        self.employment_status_frame.setObjectName("employment_status_frame")
        self.verticalLayout_8 = QVBoxLayout(self.employment_status_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # employment status label
        self.employment_status_label = QLabel(self.employment_status_frame)
        self.employment_status_label.setObjectName("employment_status_label")
        self.verticalLayout_8.addWidget(self.employment_status_label)

        # employment status combo box
        self.employment_status_combo_box = QComboBox(self.employment_status_frame)
        self.employment_status_combo_box.setMinimumSize(QSize(0, 25))
        self.employment_status_combo_box.setMaximumSize(QSize(16777215, 25))
        self.employment_status_combo_box.setObjectName("employment_status_combo_box")
        for _ in range(7):
                self.employment_status_combo_box.addItem("")
        self.verticalLayout_8.addWidget(self.employment_status_combo_box)
        self.verticalLayout_10.addWidget(self.employment_status_frame)

        # job description frame
        self.job_description_frame = QFrame(self.position_details_group_box)
        self.job_description_frame.setFrameShape(QFrame.StyledPanel)
        self.job_description_frame.setFrameShadow(QFrame.Raised)
        self.job_description_frame.setObjectName("job_description_frame")
        self.verticalLayout_9 = QVBoxLayout(self.job_description_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        # job description label
        self.job_description_label = QLabel(self.job_description_frame)
        self.job_description_label.setObjectName("job_description_label")
        self.verticalLayout_9.addWidget(self.job_description_label)

        # job description plain text edit
        self.job_description_plain_text_edit = QPlainTextEdit(self.job_description_frame)
        self.job_description_plain_text_edit.setMinimumSize(QSize(0, 250))
        self.job_description_plain_text_edit.setMaximumSize(QSize(16777215, 250))
        font = QFont()
        font.setPointSize(10)
        self.job_description_plain_text_edit.setFont(font)
        self.job_description_plain_text_edit.setObjectName("job_description_plain_text_edit")
        self.verticalLayout_9.addWidget(self.job_description_plain_text_edit)
        self.verticalLayout_10.addWidget(self.job_description_frame)
        self.verticalLayout_23.addWidget(self.position_details_group_box)





        # application status history group box
        self.application_status_history_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.application_status_history_group_box.setFont(font)
        self.application_status_history_group_box.setFlat(True)
        self.application_status_history_group_box.setObjectName("application_status_history_group_box")
        self.verticalLayout_20 = QVBoxLayout(self.application_status_history_group_box)
        self.verticalLayout_20.setObjectName("verticalLayout_20")

        # application status history actions frame
        self.application_status_history_actions_frame = QFrame(self.application_status_history_group_box)
        self.application_status_history_actions_frame.setStyleSheet(
             "QPushButton {\n"
                "padding: 5px 15px;\n"
                "border: none;\n"
                "border-radius: 5px;\n"
                "background-color: rgb(33, 150, 243);\n"
                "color: white;\n"
            "}\n"
            "QPushButton:Hover {\n"
                "background-color: rgb(25, 105, 170);\n"
            "}\n"
            "QPushButton:Pressed {\n"
                "background-color: rgb(33, 150, 243);\n"
            "}"
        )
        self.application_status_history_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.application_status_history_actions_frame.setFrameShadow(QFrame.Raised)
        self.application_status_history_actions_frame.setObjectName("application_status_history_actions_frame")
        self.horizontalLayout_5 = QHBoxLayout(self.application_status_history_actions_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # application status line edit
        self.application_status_line_edit = QLineEdit(self.application_status_history_actions_frame)
        self.application_status_line_edit.setMinimumSize(QSize(0, 25))
        self.application_status_line_edit.setMaximumSize(QSize(200, 25))
        self.application_status_line_edit.setReadOnly(True)
        self.application_status_line_edit.setObjectName("application_status_line_edit")
        self.horizontalLayout_5.addWidget(self.application_status_line_edit)

        # application status date edit
        self.application_status_date_edit = QDateEdit(self.application_status_history_actions_frame)
        self.application_status_date_edit.setMinimumSize(QSize(0, 25))
        self.application_status_date_edit.setMaximumSize(QSize(16777215, 25))
        self.application_status_date_edit.setMaximumDate(QDate(2124, 12, 31))
        self.application_status_date_edit.setMinimumDate(QDate(2024, 1, 1))
        self.application_status_date_edit.setCalendarPopup(True)
        self.application_status_date_edit.setObjectName("application_status_date_edit")
        self.horizontalLayout_5.addWidget(self.application_status_date_edit)
        self.verticalLayout_20.addWidget(self.application_status_history_actions_frame)
        self.verticalLayout_23.addWidget(self.application_status_history_group_box)





        # actions outter frame
        self.actions_outter_frame = QFrame(self.body_frame)
        self.actions_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_outter_frame.setFrameShadow(QFrame.Raised)
        self.actions_outter_frame.setObjectName("actions_outter_frame")
        self.verticalLayout_21 = QVBoxLayout(self.actions_outter_frame)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")

        # error frame
        self.error_frame = QFrame(self.actions_outter_frame)
        self.error_frame.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.error_frame.setFont(font)
        self.error_frame.setStyleSheet(
             "QFrame {\n"
                "color: red;\n"
            "}"
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
        self.verticalLayout_21.addWidget(self.error_frame)

        # action frame
        self.actions_frame = QFrame(self.actions_outter_frame)
        self.actions_frame.setStyleSheet(
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
        self.actions_frame.setFrameShape(QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.actionsFrame_layout = QHBoxLayout(self.actions_frame)
        self.actionsFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.actionsFrame_layout.setSpacing(0)
        self.actionsFrame_layout.setObjectName("actionsFrame_layout")

        # spacer item
        spacerItem = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.actionsFrame_layout.addItem(spacerItem)

        # create button
        self.create_button = QPushButton(self.actions_frame)
        self.create_button.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.actionsFrame_layout.addWidget(self.create_button)

        # spacer item
        spacerItem1 = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.actionsFrame_layout.addItem(spacerItem1)
        self.verticalLayout_21.addWidget(self.actions_frame)
        self.verticalLayout_23.addWidget(self.actions_outter_frame)
        self.verticalLayout_22.addWidget(self.body_frame)





        # scroll area
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_19.addWidget(self.scrollArea)

        self.retranslateUi(dialog)
        QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "NEW APPLICATION"))
        self.company_details_group_box.setTitle(_translate("Dialog", "Company Details"))
        self.company_label.setText(_translate("Dialog", "Company:"))
        self.city_label.setText(_translate("Dialog", "City:"))
        self.state_label.setText(_translate("Dialog", "State:"))

        us_states = [
            "-", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
            "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
            "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
            "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
            "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
            "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
            "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]
        for index in range(51):
                self.state_combo_box.setItemText(index, _translate("Dialog", us_states[index]))
        
        self.position_details_group_box.setTitle(_translate("Dialog", "Position Details"))
        self.position_label.setText(_translate("Dialog", "Position:"))
        self.work_style_label.setText(_translate("Dialog", "Work Style:"))

        work_styles = [ "-", "On-Site", "Remote", "Hybrid" ]
        for index in range(4):
              self.work_style_combo_box.setItemText(index, _translate("Dialog", work_styles[index]))

        self.employment_status_label.setText(_translate("Dialog", "Employment Status:"))

        employment_statuses = [ "-", "Full-Time", "Part-Time", "Contract", "Temporary", "Co-Op", "Intern"]
        for index in range(7):
              self.employment_status_combo_box.setItemText(index, _translate("Dialog", employment_statuses[index]))

        self.job_description_label.setText(_translate("Dialog", "Job Description:"))
        self.application_status_history_group_box.setTitle(_translate("Dialog", "Application Status History"))
        self.application_status_line_edit.setText(_translate("Dialog", "Application Submitted"))
        self.error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))
        self.create_button.setText(_translate("Dialog", "Create"))
