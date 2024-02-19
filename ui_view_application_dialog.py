from PyQt5.QtCore import QSize, QRect, QDate, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget,
    QFrame, QGroupBox, QScrollArea, QTableWidget, QTableWidgetItem,
    QLabel,
    QDateEdit, QPushButton, QComboBox, QLineEdit, QPlainTextEdit,
    QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem,
    QAbstractItemView
)


class Ui_ViewApplication_Dialog(object):
    def setupUi(self, Dialog):
        # dialog window
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 800)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(500, 800))
        self.dialogWindowLayout = QVBoxLayout(Dialog)
        self.dialogWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.dialogWindowLayout.setSpacing(0)
        self.dialogWindowLayout.setObjectName("dialogWindowLayout")

        # scroll area
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -498, 481, 1746))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")





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
        self.titleFrameLayout = QVBoxLayout(self.title_frame)
        self.titleFrameLayout.setContentsMargins(0, -1, 0, 0)
        self.titleFrameLayout.setSpacing(0)
        self.titleFrameLayout.setObjectName("titleFrameLayout")

        # title label
        self.title_label = QLabel(self.title_frame)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.titleFrameLayout.addWidget(self.title_label)
        self.scrollAreaLayout.addWidget(self.title_frame)





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
        self.bodyFrameLayout = QVBoxLayout(self.body_frame)
        self.bodyFrameLayout.setContentsMargins(24, 24, 24, 24)
        self.bodyFrameLayout.setSpacing(24)
        self.bodyFrameLayout.setObjectName("bodyFrameLayout")





        # company details group box
        self.company_details_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.company_details_group_box.setFont(font)
        self.company_details_group_box.setFlat(True)
        self.company_details_group_box.setObjectName("company_details_group_box")
        self.companyDetailsGroupBoxLayout = QVBoxLayout(self.company_details_group_box)
        self.companyDetailsGroupBoxLayout.setObjectName("companyDetailsGroupBoxLayout")

        # company frame
        self.company_frame = QFrame(self.company_details_group_box)
        self.company_frame.setFrameShape(QFrame.StyledPanel)
        self.company_frame.setFrameShadow(QFrame.Raised)
        self.company_frame.setObjectName("company_frame")
        self.companyFrameLayout = QVBoxLayout(self.company_frame)
        self.companyFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.companyFrameLayout.setObjectName("companyFrameLayout")

        # company label
        self.company_label = QLabel(self.company_frame)
        self.company_label.setObjectName("company_label")
        self.companyFrameLayout.addWidget(self.company_label)

        # company line edit
        self.company_line_edit = QLineEdit(self.company_frame)
        self.company_line_edit.setMinimumSize(QSize(0, 25))
        self.company_line_edit.setMaximumSize(QSize(16777215, 25))
        self.company_line_edit.setReadOnly(True)
        self.company_line_edit.setObjectName("company_line_edit")
        self.companyFrameLayout.addWidget(self.company_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.company_frame)

        # city frame
        self.city_frame = QFrame(self.company_details_group_box)
        self.city_frame.setFrameShape(QFrame.StyledPanel)
        self.city_frame.setFrameShadow(QFrame.Raised)
        self.city_frame.setObjectName("city_frame")
        self.cityFrameLayout = QVBoxLayout(self.city_frame)
        self.cityFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.cityFrameLayout.setObjectName("cityFrameLayout")

        # city label
        self.city_label = QLabel(self.city_frame)
        self.city_label.setObjectName("city_label")
        self.cityFrameLayout.addWidget(self.city_label)

        # city line edit
        self.city_line_edit = QLineEdit(self.city_frame)
        self.city_line_edit.setMinimumSize(QSize(0, 25))
        self.city_line_edit.setMaximumSize(QSize(16777215, 25))
        self.city_line_edit.setReadOnly(True)
        self.city_line_edit.setObjectName("city_line_edit")
        self.cityFrameLayout.addWidget(self.city_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.city_frame)

        # state frame
        self.state_frame = QFrame(self.company_details_group_box)
        self.state_frame.setFrameShape(QFrame.StyledPanel)
        self.state_frame.setFrameShadow(QFrame.Raised)
        self.state_frame.setObjectName("state_frame")
        self.stateFrameLayout = QVBoxLayout(self.state_frame)
        self.stateFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.stateFrameLayout.setObjectName("stateFrameLayout")

        # state label
        self.state_label = QLabel(self.state_frame)
        self.state_label.setObjectName("state_label")
        self.stateFrameLayout.addWidget(self.state_label)

        # state line edit
        self.state_line_edit = QLineEdit(self.state_frame)
        self.state_line_edit.setMinimumSize(QSize(0, 25))
        self.state_line_edit.setMaximumSize(QSize(16777215, 25))
        self.state_line_edit.setReadOnly(True)
        self.state_line_edit.setObjectName("state_line_edit")
        self.stateFrameLayout.addWidget(self.state_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.state_frame)
        self.bodyFrameLayout.addWidget(self.company_details_group_box)





        # position details group box
        self.position_details_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.position_details_group_box.setFont(font)
        self.position_details_group_box.setFlat(True)
        self.position_details_group_box.setObjectName("position_details_group_box")
        self.positionDetailsGroupBoxLayout = QVBoxLayout(self.position_details_group_box)
        self.positionDetailsGroupBoxLayout.setObjectName("positionDetailsGroupBoxLayout")

        # position frame
        self.position_frame = QFrame(self.position_details_group_box)
        self.position_frame.setFrameShape(QFrame.StyledPanel)
        self.position_frame.setFrameShadow(QFrame.Raised)
        self.position_frame.setObjectName("position_frame")
        self.positionFrameLayout = QVBoxLayout(self.position_frame)
        self.positionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.positionFrameLayout.setObjectName("positionFrameLayout")

        # position label
        self.position_label = QLabel(self.position_frame)
        self.position_label.setObjectName("position_label")
        self.positionFrameLayout.addWidget(self.position_label)

        # position line edit
        self.position_line_edit = QLineEdit(self.position_frame)
        self.position_line_edit.setMinimumSize(QSize(0, 25))
        self.position_line_edit.setMaximumSize(QSize(16777215, 25))
        self.position_line_edit.setReadOnly(True)
        self.position_line_edit.setObjectName("position_line_edit")
        self.positionFrameLayout.addWidget(self.position_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.position_frame)

        # work style frame
        self.work_style_frame = QFrame(self.position_details_group_box)
        self.work_style_frame.setFrameShape(QFrame.StyledPanel)
        self.work_style_frame.setFrameShadow(QFrame.Raised)
        self.work_style_frame.setObjectName("work_style_frame")
        self.workStyleLayout = QVBoxLayout(self.work_style_frame)
        self.workStyleLayout.setContentsMargins(0, 0, 0, 0)
        self.workStyleLayout.setObjectName("workStyleLayout")

        # work style label
        self.work_style_label = QLabel(self.work_style_frame)
        self.work_style_label.setObjectName("work_style_label")
        self.workStyleLayout.addWidget(self.work_style_label)

        # work style line edit
        self.work_style_line_edit = QLineEdit(self.work_style_frame)
        self.work_style_line_edit.setMinimumSize(QSize(0, 25))
        self.work_style_line_edit.setMaximumSize(QSize(16777215, 25))
        self.work_style_line_edit.setReadOnly(True)
        self.work_style_line_edit.setObjectName("work_style_line_edit")
        self.workStyleLayout.addWidget(self.work_style_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.work_style_frame)

        # employment status frame
        self.employment_status_frame = QFrame(self.position_details_group_box)
        self.employment_status_frame.setFrameShape(QFrame.StyledPanel)
        self.employment_status_frame.setFrameShadow(QFrame.Raised)
        self.employment_status_frame.setObjectName("employment_status_frame")
        self.employmentStatusFrameLayout = QVBoxLayout(self.employment_status_frame)
        self.employmentStatusFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.employmentStatusFrameLayout.setObjectName("employmentStatusFrameLayout")

        # employment status label
        self.employment_status_label = QLabel(self.employment_status_frame)
        self.employment_status_label.setObjectName("employment_status_label")
        self.employmentStatusFrameLayout.addWidget(self.employment_status_label)

        # employment status line edit
        self.employment_status_line_edit = QLineEdit(self.employment_status_frame)
        self.employment_status_line_edit.setMinimumSize(QSize(0, 25))
        self.employment_status_line_edit.setMaximumSize(QSize(16777215, 25))
        self.employment_status_line_edit.setReadOnly(True)
        self.employment_status_line_edit.setObjectName("employment_status_line_edit")
        self.employmentStatusFrameLayout.addWidget(self.employment_status_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.employment_status_frame)

        # job description frame
        self.job_description_frame = QFrame(self.position_details_group_box)
        self.job_description_frame.setFrameShape(QFrame.StyledPanel)
        self.job_description_frame.setFrameShadow(QFrame.Raised)
        self.job_description_frame.setObjectName("job_description_frame")
        self.jobDescriptionFrameLayout = QVBoxLayout(self.job_description_frame)
        self.jobDescriptionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.jobDescriptionFrameLayout.setObjectName("jobDescriptionFrameLayout")

        # job description label
        self.job_description_label = QLabel(self.job_description_frame)
        self.job_description_label.setObjectName("job_description_label")
        self.jobDescriptionFrameLayout.addWidget(self.job_description_label)

        # job description plain text edit
        self.job_description_plain_text_edit = QPlainTextEdit(self.job_description_frame)
        self.job_description_plain_text_edit.setMinimumSize(QSize(0, 250))
        self.job_description_plain_text_edit.setMaximumSize(QSize(16777215, 250))
        font = QFont()
        font.setPointSize(10)
        self.job_description_plain_text_edit.setFont(font)
        self.job_description_plain_text_edit.setReadOnly(True)
        self.job_description_plain_text_edit.setObjectName("job_description_plain_text_edit")
        self.jobDescriptionFrameLayout.addWidget(self.job_description_plain_text_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.job_description_frame)

        # skills frame
        self.skills_frame = QFrame(self.position_details_group_box)
        self.skills_frame.setFrameShape(QFrame.StyledPanel)
        self.skills_frame.setFrameShadow(QFrame.Raised)
        self.skills_frame.setObjectName("skills_frame")
        self.skillsFrameLayout = QVBoxLayout(self.skills_frame)
        self.skillsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.skillsFrameLayout.setObjectName("skillsFrameLayout")

        # skills label
        self.skill_label = QLabel(self.skills_frame)
        self.skill_label.setObjectName("skill_label")
        self.skillsFrameLayout.addWidget(self.skill_label)

        # skills table
        self.skills_table = QTableWidget(self.skills_frame)
        self.skills_table.setMinimumSize(QSize(0, 200))
        self.skills_table.setMaximumSize(QSize(16777215, 200))
        self.skills_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.skills_table.setObjectName("skills_table")
        self.skills_table.setColumnCount(1)
        self.skills_table.setRowCount(0)
        item = QTableWidgetItem()
        self.skills_table.setHorizontalHeaderItem(0, item)
        self.skills_table.horizontalHeader().setVisible(True)
        self.skills_table.verticalHeader().setVisible(False)
        self.skillsFrameLayout.addWidget(self.skills_table)

        # skill action outter frame
        self.skill_action_outter_frame = QFrame(self.skills_frame)
        self.skill_action_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.skill_action_outter_frame.setFrameShadow(QFrame.Raised)
        self.skill_action_outter_frame.setObjectName("skill_action_outter_frame")
        self.skillActionOutterFrameLayout = QVBoxLayout(self.skill_action_outter_frame)
        self.skillActionOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.skillActionOutterFrameLayout.setSpacing(0)
        self.skillActionOutterFrameLayout.setObjectName("skillActionOutterFrameLayout")

        # skill error frame
        self.skill_error_frame = QFrame(self.skill_action_outter_frame)
        self.skill_error_frame.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.skill_error_frame.setFont(font)
        self.skill_error_frame.setStyleSheet(
            "QFrame {\n"
                "color: red;\n"
            "}"
        )
        self.skill_error_frame.setFrameShape(QFrame.StyledPanel)
        self.skill_error_frame.setFrameShadow(QFrame.Raised)
        self.skill_error_frame.setObjectName("skill_error_frame")
        self.skillErrorFrameLayout = QHBoxLayout(self.skill_error_frame)
        self.skillErrorFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.skillErrorFrameLayout.setSpacing(0)
        self.skillErrorFrameLayout.setObjectName("skillErrorFrameLayout")

        # spacer item
        spacerItem = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.skillErrorFrameLayout.addItem(spacerItem)

        # skill error label
        self.skill_error_label = QLabel(self.skill_error_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.skill_error_label.setFont(font)
        self.skill_error_label.setAlignment(Qt.AlignCenter)
        self.skill_error_label.setObjectName("skill_error_label")
        self.skillErrorFrameLayout.addWidget(self.skill_error_label)
        self.skillActionOutterFrameLayout.addWidget(self.skill_error_frame)

        # add skill frame
        self.add_skill_frame = QFrame(self.skill_action_outter_frame)
        self.add_skill_frame.setStyleSheet(
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
        self.add_skill_frame.setFrameShape(QFrame.StyledPanel)
        self.add_skill_frame.setFrameShadow(QFrame.Raised)
        self.add_skill_frame.setObjectName("add_skill_frame")
        self.addSkillFrameLayout = QHBoxLayout(self.add_skill_frame)
        self.addSkillFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.addSkillFrameLayout.setObjectName("addSkillFrameLayout")

        # spacer item
        spacerItem1 = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.addSkillFrameLayout.addItem(spacerItem1)

        # add skill line edit
        self.add_skill_line_edit = QLineEdit(self.add_skill_frame)
        self.add_skill_line_edit.setMinimumSize(QSize(0, 25))
        self.add_skill_line_edit.setMaximumSize(QSize(16777215, 25))
        self.add_skill_line_edit.setObjectName("add_skill_line_edit")
        self.addSkillFrameLayout.addWidget(self.add_skill_line_edit)

        # add skill button
        self.add_skill_button = QPushButton(self.add_skill_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_skill_button.setFont(font)
        self.add_skill_button.setObjectName("add_skill_button")
        self.addSkillFrameLayout.addWidget(self.add_skill_button)
        self.skillActionOutterFrameLayout.addWidget(self.add_skill_frame)
        self.skillsFrameLayout.addWidget(self.skill_action_outter_frame)
        self.positionDetailsGroupBoxLayout.addWidget(self.skills_frame)
        self.bodyFrameLayout.addWidget(self.position_details_group_box)

        



        # contact information group box
        self.contact_information_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.contact_information_group_box.setFont(font)
        self.contact_information_group_box.setFlat(True)
        self.contact_information_group_box.setObjectName("contact_information_group_box")
        self.contactInformationGroupBoxLayout = QVBoxLayout(self.contact_information_group_box)
        self.contactInformationGroupBoxLayout.setObjectName("contactInformationGroupBoxLayout")

        # contact table widget
        self.contact_table_widget = QTableWidget(self.contact_information_group_box)
        self.contact_table_widget.setMinimumSize(QSize(0, 150))
        self.contact_table_widget.setMaximumSize(QSize(16777215, 150))
        self.contact_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contact_table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.contact_table_widget.setShowGrid(False)
        self.contact_table_widget.setObjectName("contact_table_widget")
        self.contact_table_widget.setColumnCount(5)
        self.contact_table_widget.setRowCount(0)
        item = QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(4, item)
        self.contact_table_widget.verticalHeader().setVisible(False)
        self.contactInformationGroupBoxLayout.addWidget(self.contact_table_widget)

        # add contact frame
        self.add_contact_frame = QFrame(self.contact_information_group_box)
        self.add_contact_frame.setFrameShape(QFrame.StyledPanel)
        self.add_contact_frame.setFrameShadow(QFrame.Raised)
        self.add_contact_frame.setObjectName("add_contact_frame")
        self.addContactFrameLayout = QVBoxLayout(self.add_contact_frame)
        self.addContactFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.addContactFrameLayout.setSpacing(0)
        self.addContactFrameLayout.setObjectName("addContactFrameLayout")

        # position outter frame
        self.position_outter_frame = QFrame(self.add_contact_frame)
        self.position_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.position_outter_frame.setFrameShadow(QFrame.Raised)
        self.position_outter_frame.setObjectName("position_outter_frame")
        self.positionOutterFrameLayout = QHBoxLayout(self.position_outter_frame)
        self.positionOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.positionOutterFrameLayout.setSpacing(0)
        self.positionOutterFrameLayout.setObjectName("positionOutterFrameLayout")

        # contact position frame
        self.contact_position_frame = QFrame(self.position_outter_frame)
        self.contact_position_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_position_frame.setFrameShadow(QFrame.Raised)
        self.contact_position_frame.setObjectName("contact_position_frame")
        self.contactPositionFrameLayout = QVBoxLayout(self.contact_position_frame)
        self.contactPositionFrameLayout.setContentsMargins(0, 0, 9, 0)
        self.contactPositionFrameLayout.setSpacing(6)
        self.contactPositionFrameLayout.setObjectName("contactPositionFrameLayout")

        # contact position label
        self.contact_position_label = QLabel(self.contact_position_frame)
        self.contact_position_label.setObjectName("contact_position_label")
        self.contactPositionFrameLayout.addWidget(self.contact_position_label)

        # contact position line edit
        self.contact_position_line_edit = QLineEdit(self.contact_position_frame)
        self.contact_position_line_edit.setMinimumSize(QSize(0, 25))
        self.contact_position_line_edit.setMaximumSize(QSize(16777215, 25))
        self.contact_position_line_edit.setObjectName("contact_position_line_edit")
        self.contactPositionFrameLayout.addWidget(self.contact_position_line_edit)
        self.positionOutterFrameLayout.addWidget(self.contact_position_frame)

        # spacer item
        spacerItem2 = QSpacerItem(206, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.positionOutterFrameLayout.addItem(spacerItem2)
        self.addContactFrameLayout.addWidget(self.position_outter_frame)

        # contact name outter frame
        self.contact_name_outter_frame = QFrame(self.add_contact_frame)
        self.contact_name_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_name_outter_frame.setFrameShadow(QFrame.Raised)
        self.contact_name_outter_frame.setObjectName("contact_name_outter_frame")
        self.contactNameOutterFrame = QHBoxLayout(self.contact_name_outter_frame)
        self.contactNameOutterFrame.setContentsMargins(0, 0, 0, 0)
        self.contactNameOutterFrame.setSpacing(0)
        self.contactNameOutterFrame.setObjectName("contactNameOutterFrame")

        # contact first name frame
        self.contact_first_name_frame = QFrame(self.contact_name_outter_frame)
        self.contact_first_name_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_first_name_frame.setFrameShadow(QFrame.Raised)
        self.contact_first_name_frame.setObjectName("contact_first_name_frame")
        self.contactFirstNameFrameLabel = QVBoxLayout(self.contact_first_name_frame)
        self.contactFirstNameFrameLabel.setContentsMargins(0, 0, -1, 0)
        self.contactFirstNameFrameLabel.setObjectName("contactFirstNameFrameLabel")

        # contact first name label
        self.contact_first_name_label = QLabel(self.contact_first_name_frame)
        self.contact_first_name_label.setObjectName("contact_first_name_label")
        self.contactFirstNameFrameLabel.addWidget(self.contact_first_name_label)

        # contact first name line edit
        self.contact_first_name_line_edit = QLineEdit(self.contact_first_name_frame)
        self.contact_first_name_line_edit.setMinimumSize(QSize(0, 25))
        self.contact_first_name_line_edit.setMaximumSize(QSize(16777215, 25))
        self.contact_first_name_line_edit.setObjectName("contact_first_name_line_edit")
        self.contactFirstNameFrameLabel.addWidget(self.contact_first_name_line_edit)
        self.contactNameOutterFrame.addWidget(self.contact_first_name_frame)

        # contact last name frame
        self.contact_last_name_frame = QFrame(self.contact_name_outter_frame)
        self.contact_last_name_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_last_name_frame.setFrameShadow(QFrame.Raised)
        self.contact_last_name_frame.setObjectName("contact_last_name_frame")
        self.contactLastNameFrameLayout = QVBoxLayout(self.contact_last_name_frame)
        self.contactLastNameFrameLayout.setContentsMargins(9, 0, 0, 0)
        self.contactLastNameFrameLayout.setObjectName("contactLastNameFrameLayout")

        # contact last name label
        self.contact_last_name_label = QLabel(self.contact_last_name_frame)
        self.contact_last_name_label.setObjectName("contact_last_name_label")
        self.contactLastNameFrameLayout.addWidget(self.contact_last_name_label)

        # contact last name line edit
        self.contact_last_name_line_edit = QLineEdit(self.contact_last_name_frame)
        self.contact_last_name_line_edit.setMinimumSize(QSize(0, 25))
        self.contact_last_name_line_edit.setMaximumSize(QSize(16777215, 25))
        self.contact_last_name_line_edit.setObjectName("contact_last_name_line_edit")
        self.contactLastNameFrameLayout.addWidget(self.contact_last_name_line_edit)
        self.contactNameOutterFrame.addWidget(self.contact_last_name_frame)
        self.addContactFrameLayout.addWidget(self.contact_name_outter_frame)

        # contact reachback outter frame
        self.contact_reachback_outter_frame = QFrame(self.add_contact_frame)
        self.contact_reachback_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_reachback_outter_frame.setFrameShadow(QFrame.Raised)
        self.contact_reachback_outter_frame.setObjectName("contact_reachback_outter_frame")
        self.contactReachbackOutterFrameLayout = QHBoxLayout(self.contact_reachback_outter_frame)
        self.contactReachbackOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactReachbackOutterFrameLayout.setSpacing(0)
        self.contactReachbackOutterFrameLayout.setObjectName("contactReachbackOutterFrameLayout")

        # contact phone frame
        self.contact_phone_frame = QFrame(self.contact_reachback_outter_frame)
        self.contact_phone_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_phone_frame.setFrameShadow(QFrame.Raised)
        self.contact_phone_frame.setObjectName("contact_phone_frame")
        self.contactPhoneFrameLayout = QVBoxLayout(self.contact_phone_frame)
        self.contactPhoneFrameLayout.setContentsMargins(0, 0, -1, 0)
        self.contactPhoneFrameLayout.setObjectName("contactPhoneFrameLayout")

        # contact phone label
        self.contact_phone_label = QLabel(self.contact_phone_frame)
        self.contact_phone_label.setObjectName("contact_phone_label")
        self.contactPhoneFrameLayout.addWidget(self.contact_phone_label)

        # contact phone line edit
        self.contact_phone_line_edit = QLineEdit(self.contact_phone_frame)
        self.contact_phone_line_edit.setMinimumSize(QSize(0, 25))
        self.contact_phone_line_edit.setMaximumSize(QSize(16777215, 25))
        self.contact_phone_line_edit.setObjectName("contact_phone_line_edit")
        self.contactPhoneFrameLayout.addWidget(self.contact_phone_line_edit)
        self.contactReachbackOutterFrameLayout.addWidget(self.contact_phone_frame)

        # contact email frame
        self.contact_email_frame = QFrame(self.contact_reachback_outter_frame)
        self.contact_email_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_email_frame.setFrameShadow(QFrame.Raised)
        self.contact_email_frame.setObjectName("contact_email_frame")
        self.contactEmailFrameLayout = QVBoxLayout(self.contact_email_frame)
        self.contactEmailFrameLayout.setContentsMargins(-1, 0, 0, 0)
        self.contactEmailFrameLayout.setObjectName("contactEmailFrameLayout")

        # contact email label
        self.contact_email_label = QLabel(self.contact_email_frame)
        self.contact_email_label.setObjectName("contact_email_label")
        self.contactEmailFrameLayout.addWidget(self.contact_email_label)

        # contact email line edit
        self.contact_email_line_edit = QLineEdit(self.contact_email_frame)
        self.contact_email_line_edit.setMinimumSize(QSize(0, 25))
        self.contact_email_line_edit.setMaximumSize(QSize(16777215, 25))
        self.contact_email_line_edit.setObjectName("contact_email_line_edit")
        self.contactEmailFrameLayout.addWidget(self.contact_email_line_edit)
        self.contactReachbackOutterFrameLayout.addWidget(self.contact_email_frame)
        self.addContactFrameLayout.addWidget(self.contact_reachback_outter_frame)

        # contact error frame
        self.contact_error_frame = QFrame(self.add_contact_frame)
        self.contact_error_frame.setMaximumSize(QSize(16777215, 25))
        self.contact_error_frame.setStyleSheet(
            "QFrame {\n"
                "color: red;\n"
            "}"
        )
        self.contact_error_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_error_frame.setFrameShadow(QFrame.Raised)
        self.contact_error_frame.setObjectName("contact_error_frame")
        self.contactErrorFrameLayout = QVBoxLayout(self.contact_error_frame)
        self.contactErrorFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactErrorFrameLayout.setSpacing(0)
        self.contactErrorFrameLayout.setObjectName("contactErrorFrameLayout")

        # contact error label
        self.contact_error_label = QLabel(self.contact_error_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.contact_error_label.setFont(font)
        self.contact_error_label.setAlignment(Qt.AlignCenter)
        self.contact_error_label.setObjectName("contact_error_label")
        self.contactErrorFrameLayout.addWidget(self.contact_error_label)
        self.addContactFrameLayout.addWidget(self.contact_error_frame)

        # contact action frame
        self.contact_action_frame = QFrame(self.add_contact_frame)
        self.contact_action_frame.setStyleSheet(
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
        self.contact_action_frame.setFrameShape(QFrame.StyledPanel)
        self.contact_action_frame.setFrameShadow(QFrame.Raised)
        self.contact_action_frame.setObjectName("contact_action_frame")
        self.contactActionFrameLayout = QHBoxLayout(self.contact_action_frame)
        self.contactActionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactActionFrameLayout.setSpacing(0)
        self.contactActionFrameLayout.setObjectName("contactActionFrameLayout")

        # spacer item
        spacerItem3 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.contactActionFrameLayout.addItem(spacerItem3)

        # add contact button
        self.add_contact_button = QPushButton(self.contact_action_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_contact_button.setFont(font)
        self.add_contact_button.setObjectName("add_contact_button")
        self.contactActionFrameLayout.addWidget(self.add_contact_button)

        # spacer item
        spacerItem4 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.contactActionFrameLayout.addItem(spacerItem4)
        self.addContactFrameLayout.addWidget(self.contact_action_frame)
        self.contactInformationGroupBoxLayout.addWidget(self.add_contact_frame)
        self.bodyFrameLayout.addWidget(self.contact_information_group_box)
        self.application_status_history_group_box = QGroupBox(self.body_frame)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)





        # application status history group box
        self.application_status_history_group_box.setFont(font)
        self.application_status_history_group_box.setFlat(True)
        self.application_status_history_group_box.setObjectName("application_status_history_group_box")
        self.applicationStatusHistoryGroupBoxLayout = QVBoxLayout(self.application_status_history_group_box)
        self.applicationStatusHistoryGroupBoxLayout.setObjectName("applicationStatusHistoryGroupBoxLayout")

        # application status history table widget
        self.application_status_history_table_widget = QTableWidget(self.application_status_history_group_box)
        self.application_status_history_table_widget.setMinimumSize(QSize(0, 150))
        self.application_status_history_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.application_status_history_table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.application_status_history_table_widget.setShowGrid(False)
        self.application_status_history_table_widget.setWordWrap(True)
        self.application_status_history_table_widget.setObjectName("application_status_history_table_widget")
        self.application_status_history_table_widget.setColumnCount(2)
        self.application_status_history_table_widget.setRowCount(0)
        item = QTableWidgetItem()
        self.application_status_history_table_widget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.application_status_history_table_widget.setHorizontalHeaderItem(1, item)
        self.application_status_history_table_widget.verticalHeader().setVisible(False)
        self.applicationStatusHistoryGroupBoxLayout.addWidget(self.application_status_history_table_widget)

        # application status actions outter frame
        self.application_status_actions_outter_frame = QFrame(self.application_status_history_group_box)
        self.application_status_actions_outter_frame.setFrameShape(QFrame.StyledPanel)
        self.application_status_actions_outter_frame.setFrameShadow(QFrame.Raised)
        self.application_status_actions_outter_frame.setObjectName("application_status_actions_outter_frame")
        self.applicationStatusActionsOutterFrame = QVBoxLayout(self.application_status_actions_outter_frame)
        self.applicationStatusActionsOutterFrame.setContentsMargins(0, 0, 0, 0)
        self.applicationStatusActionsOutterFrame.setSpacing(0)
        self.applicationStatusActionsOutterFrame.setObjectName("applicationStatusActionsOutterFrame")

        # applicaiton status error frame
        self.application_status_error_frame = QFrame(self.application_status_actions_outter_frame)
        self.application_status_error_frame.setStyleSheet(
            "QFrame {\n"
                "color: red;\n"
            "}"
        )
        self.application_status_error_frame.setFrameShape(QFrame.StyledPanel)
        self.application_status_error_frame.setFrameShadow(QFrame.Raised)
        self.application_status_error_frame.setObjectName("application_status_error_frame")
        self.applicationStatusErrorFrameLayout = QVBoxLayout(self.application_status_error_frame)
        self.applicationStatusErrorFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.applicationStatusErrorFrameLayout.setSpacing(0)
        self.applicationStatusErrorFrameLayout.setObjectName("applicationStatusErrorFrameLayout")

        # applicaiton status error label
        self.application_status_error_label = QLabel(self.application_status_error_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.application_status_error_label.setFont(font)
        self.application_status_error_label.setAlignment(Qt.AlignCenter)
        self.application_status_error_label.setObjectName("application_status_error_label")
        self.applicationStatusErrorFrameLayout.addWidget(self.application_status_error_label)
        self.applicationStatusActionsOutterFrame.addWidget(self.application_status_error_frame)

        # application status history actions frame
        self.application_status_history_actions_frame = QFrame(self.application_status_actions_outter_frame)
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
        self.applicationStatusHistoryActionsFrameLayout = QHBoxLayout(self.application_status_history_actions_frame)
        self.applicationStatusHistoryActionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.applicationStatusHistoryActionsFrameLayout.setObjectName("applicationStatusHistoryActionsFrameLayout")

        # application status combo box
        self.application_status_combo_box = QComboBox(self.application_status_history_actions_frame)
        self.application_status_combo_box.setMinimumSize(QSize(0, 25))
        self.application_status_combo_box.setMaximumSize(QSize(16777215, 25))
        self.application_status_combo_box.setObjectName("application_status_combo_box")

        for _ in range(5):
            self.application_status_combo_box.addItem("")

        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.application_status_combo_box)

        # application status date edit
        self.application_status_date_edit = QDateEdit(self.application_status_history_actions_frame)
        self.application_status_date_edit.setMinimumSize(QSize(0, 25))
        self.application_status_date_edit.setMaximumSize(QSize(16777215, 25))
        self.application_status_date_edit.setMaximumDate(QDate(2124, 12, 31))
        self.application_status_date_edit.setMinimumDate(QDate(2024, 1, 1))
        self.application_status_date_edit.setCalendarPopup(True)
        self.application_status_date_edit.setObjectName("application_status_date_edit")
        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.application_status_date_edit)

        # add application status button
        self.add_application_status_button = QPushButton(self.application_status_history_actions_frame)
        self.add_application_status_button.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_application_status_button.setFont(font)
        self.add_application_status_button.setObjectName("add_application_status_button")

        



        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.add_application_status_button)
        self.applicationStatusActionsOutterFrame.addWidget(self.application_status_history_actions_frame)
        self.applicationStatusHistoryGroupBoxLayout.addWidget(self.application_status_actions_outter_frame)
        self.bodyFrameLayout.addWidget(self.application_status_history_group_box)
        self.scrollAreaLayout.addWidget(self.body_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.dialogWindowLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "VIEW APPLICATION"))
        self.company_details_group_box.setTitle(_translate("Dialog", "Company Details"))
        self.company_label.setText(_translate("Dialog", "Company:"))
        self.city_label.setText(_translate("Dialog", "City:"))
        self.state_label.setText(_translate("Dialog", "State:"))
        self.position_details_group_box.setTitle(_translate("Dialog", "Position Details"))
        self.position_label.setText(_translate("Dialog", "Position:"))
        self.work_style_label.setText(_translate("Dialog", "Work Style:"))
        self.employment_status_label.setText(_translate("Dialog", "Employment Status:"))
        self.job_description_label.setText(_translate("Dialog", "Job Description:"))
        self.skill_label.setText(_translate("Dialog", "Skills:"))
        item = self.skills_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Skill"))
        self.skill_error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))
        self.add_skill_button.setText(_translate("Dialog", "Add"))
        self.contact_information_group_box.setTitle(_translate("Dialog", "Contact Information"))

        contact_table_columns = ["Position", "First Name", "Last Name", "Email", "Phone"]
        for index in range(5):
            item = self.contact_table_widget.horizontalHeaderItem(index)
            item.setText(_translate("Dialog", contact_table_columns[index]))

        self.contact_position_label.setText(_translate("Dialog", "Position:"))
        self.contact_first_name_label.setText(_translate("Dialog", "*First Name:"))
        self.contact_last_name_label.setText(_translate("Dialog", "*Last Name:"))
        self.contact_phone_label.setText(_translate("Dialog", "Phone Number:"))
        self.contact_email_label.setText(_translate("Dialog", "Email Address:"))
        self.contact_error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))
        self.add_contact_button.setText(_translate("Dialog", "Add Contact"))
        self.application_status_history_group_box.setTitle(_translate("Dialog", "Application Status History"))

        application_status_history_table_columns = ["Status", "Date"]
        for index in range(2):
            item = self.application_status_history_table_widget.horizontalHeaderItem(index)
            item.setText(_translate("Dialog", application_status_history_table_columns[index]))

        self.application_status_error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))

        application_statuses = ["-", "Screening Interview", "Technical Interview", "Job Offer", "Application Rejected"]
        for index in range(5):
            self.application_status_combo_box.setItemText(index, _translate("Dialog", application_statuses[index]))

        self.add_application_status_button.setText(_translate("Dialog", "Add Status"))
