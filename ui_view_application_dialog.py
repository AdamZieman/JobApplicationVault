from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewApplication_Dialog(object):
    def setupUi(self, Dialog):
        # dialog window
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 800)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 800))
        self.dialogWindowLayout = QtWidgets.QVBoxLayout(Dialog)
        self.dialogWindowLayout.setContentsMargins(0, 0, 0, 0)
        self.dialogWindowLayout.setSpacing(0)
        self.dialogWindowLayout.setObjectName("dialogWindowLayout")

        # scroll area
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 1533))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")





        # title frame
        self.title_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.title_frame.setStyleSheet(
            "QFrame {\n"
                "color: white;\n"
                "background-color: rgb(33, 150, 243);\n"
            "}"
        )
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.title_frame)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # title label
        self.title_label = QtWidgets.QLabel(self.title_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.scrollAreaLayout.addWidget(self.title_frame)





        # body frame
        self.body_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
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
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.bodyFrameLayout = QtWidgets.QVBoxLayout(self.body_frame)
        self.bodyFrameLayout.setContentsMargins(24, 24, 24, 24)
        self.bodyFrameLayout.setSpacing(24)
        self.bodyFrameLayout.setObjectName("bodyFrameLayout")





        # company details group box
        self.company_details_group_box = QtWidgets.QGroupBox(self.body_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.company_details_group_box.setFont(font)
        self.company_details_group_box.setFlat(True)
        self.company_details_group_box.setObjectName("company_details_group_box")
        self.companyDetailsGroupBoxLayout = QtWidgets.QVBoxLayout(self.company_details_group_box)
        self.companyDetailsGroupBoxLayout.setObjectName("companyDetailsGroupBoxLayout")

        # company frame
        self.company_frame = QtWidgets.QFrame(self.company_details_group_box)
        self.company_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.company_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.company_frame.setObjectName("company_frame")
        self.companyFrameLayout = QtWidgets.QVBoxLayout(self.company_frame)
        self.companyFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.companyFrameLayout.setObjectName("companyFrameLayout")

        # company label
        self.company_label = QtWidgets.QLabel(self.company_frame)
        self.company_label.setObjectName("company_label")
        self.companyFrameLayout.addWidget(self.company_label)

        # company line edit
        self.company_line_edit = QtWidgets.QLineEdit(self.company_frame)
        self.company_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.company_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.company_line_edit.setReadOnly(True)
        self.company_line_edit.setObjectName("company_line_edit")
        self.companyFrameLayout.addWidget(self.company_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.company_frame)

        # city frame
        self.city_frame = QtWidgets.QFrame(self.company_details_group_box)
        self.city_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.city_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.city_frame.setObjectName("city_frame")
        self.cityFrameLayout = QtWidgets.QVBoxLayout(self.city_frame)
        self.cityFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.cityFrameLayout.setObjectName("cityFrameLayout")

        # city label
        self.city_label = QtWidgets.QLabel(self.city_frame)
        self.city_label.setObjectName("city_label")
        self.cityFrameLayout.addWidget(self.city_label)

        # city line edit
        self.city_line_edit = QtWidgets.QLineEdit(self.city_frame)
        self.city_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.city_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.city_line_edit.setReadOnly(True)
        self.city_line_edit.setObjectName("city_line_edit")
        self.cityFrameLayout.addWidget(self.city_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.city_frame)

        # state frame
        self.state_frame = QtWidgets.QFrame(self.company_details_group_box)
        self.state_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_frame.setObjectName("state_frame")
        self.stateFrameLayout = QtWidgets.QVBoxLayout(self.state_frame)
        self.stateFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.stateFrameLayout.setObjectName("stateFrameLayout")

        # state label
        self.state_label = QtWidgets.QLabel(self.state_frame)
        self.state_label.setObjectName("state_label")
        self.stateFrameLayout.addWidget(self.state_label)

        # state line edit
        self.state_line_edit = QtWidgets.QLineEdit(self.state_frame)
        self.state_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.state_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.state_line_edit.setReadOnly(True)
        self.state_line_edit.setObjectName("state_line_edit")
        self.stateFrameLayout.addWidget(self.state_line_edit)
        self.companyDetailsGroupBoxLayout.addWidget(self.state_frame)
        self.bodyFrameLayout.addWidget(self.company_details_group_box)





        # position details group box
        self.position_details_group_box = QtWidgets.QGroupBox(self.body_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.position_details_group_box.setFont(font)
        self.position_details_group_box.setFlat(True)
        self.position_details_group_box.setObjectName("position_details_group_box")
        self.positionDetailsGroupBoxLayout = QtWidgets.QVBoxLayout(self.position_details_group_box)
        self.positionDetailsGroupBoxLayout.setObjectName("positionDetailsGroupBoxLayout")

        # position frame
        self.position_frame = QtWidgets.QFrame(self.position_details_group_box)
        self.position_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.position_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.position_frame.setObjectName("position_frame")
        self.positionFrameLayout = QtWidgets.QVBoxLayout(self.position_frame)
        self.positionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.positionFrameLayout.setObjectName("positionFrameLayout")

        # position label
        self.position_label = QtWidgets.QLabel(self.position_frame)
        self.position_label.setObjectName("position_label")
        self.positionFrameLayout.addWidget(self.position_label)

        # position line edit
        self.position_line_edit = QtWidgets.QLineEdit(self.position_frame)
        self.position_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.position_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.position_line_edit.setReadOnly(True)
        self.position_line_edit.setObjectName("position_line_edit")
        self.positionFrameLayout.addWidget(self.position_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.position_frame)

        # work style frame
        self.work_style_frame = QtWidgets.QFrame(self.position_details_group_box)
        self.work_style_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.work_style_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.work_style_frame.setObjectName("work_style_frame")
        self.workStyleFrameLayout = QtWidgets.QVBoxLayout(self.work_style_frame)
        self.workStyleFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.workStyleFrameLayout.setObjectName("workStyleFrameLayout")

        # work style label
        self.work_style_label = QtWidgets.QLabel(self.work_style_frame)
        self.work_style_label.setObjectName("work_style_label")
        self.workStyleFrameLayout.addWidget(self.work_style_label)

        # work style line edit
        self.work_style_line_edit = QtWidgets.QLineEdit(self.work_style_frame)
        self.work_style_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.work_style_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.work_style_line_edit.setReadOnly(True)
        self.work_style_line_edit.setObjectName("work_style_line_edit")
        self.workStyleFrameLayout.addWidget(self.work_style_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.work_style_frame)

        # employment status frame
        self.employment_status_frame = QtWidgets.QFrame(self.position_details_group_box)
        self.employment_status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.employment_status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.employment_status_frame.setObjectName("employment_status_frame")
        self.employmentStatusLayout = QtWidgets.QVBoxLayout(self.employment_status_frame)
        self.employmentStatusLayout.setContentsMargins(0, 0, 0, 0)
        self.employmentStatusLayout.setObjectName("employmentStatusLayout")

        # employment status label
        self.employment_status_label = QtWidgets.QLabel(self.employment_status_frame)
        self.employment_status_label.setObjectName("employment_status_label")
        self.employmentStatusLayout.addWidget(self.employment_status_label)

        # employment status line edit
        self.employment_status_line_edit = QtWidgets.QLineEdit(self.employment_status_frame)
        self.employment_status_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.employment_status_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employment_status_line_edit.setReadOnly(True)
        self.employment_status_line_edit.setObjectName("employment_status_line_edit")
        self.employmentStatusLayout.addWidget(self.employment_status_line_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.employment_status_frame)

        # job description frame
        self.job_description_frame = QtWidgets.QFrame(self.position_details_group_box)
        self.job_description_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.job_description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.job_description_frame.setObjectName("job_description_frame")
        self.jobDescriptionFrameLayout = QtWidgets.QVBoxLayout(self.job_description_frame)
        self.jobDescriptionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.jobDescriptionFrameLayout.setObjectName("jobDescriptionFrameLayout")

        # job description label
        self.job_description_label = QtWidgets.QLabel(self.job_description_frame)
        self.job_description_label.setObjectName("job_description_label")
        self.jobDescriptionFrameLayout.addWidget(self.job_description_label)

        # job description plain text edit
        self.job_description_plain_text_edit = QtWidgets.QPlainTextEdit(self.job_description_frame)
        self.job_description_plain_text_edit.setMinimumSize(QtCore.QSize(0, 250))
        self.job_description_plain_text_edit.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.job_description_plain_text_edit.setFont(font)
        self.job_description_plain_text_edit.setObjectName("job_description_plain_text_edit")
        self.jobDescriptionFrameLayout.addWidget(self.job_description_plain_text_edit)
        self.positionDetailsGroupBoxLayout.addWidget(self.job_description_frame)
        self.bodyFrameLayout.addWidget(self.position_details_group_box)





        # contact information group box
        self.contact_information_group_box = QtWidgets.QGroupBox(self.body_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.contact_information_group_box.setFont(font)
        self.contact_information_group_box.setFlat(True)
        self.contact_information_group_box.setObjectName("contact_information_group_box")
        self.contactionInformationGroupBoxLayout = QtWidgets.QVBoxLayout(self.contact_information_group_box)
        self.contactionInformationGroupBoxLayout.setObjectName("contactionInformationGroupBoxLayout")

        # contact table widget
        self.contact_table_widget = QtWidgets.QTableWidget(self.contact_information_group_box)
        self.contact_table_widget.setMinimumSize(QtCore.QSize(0, 150))
        self.contact_table_widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.contact_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.contact_table_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.contact_table_widget.setShowGrid(False)
        self.contact_table_widget.setObjectName("contact_table_widget")
        self.contact_table_widget.setColumnCount(5)
        self.contact_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.contact_table_widget.setHorizontalHeaderItem(4, item)
        self.contact_table_widget.verticalHeader().setVisible(False)
        self.contactionInformationGroupBoxLayout.addWidget(self.contact_table_widget)

        # add contact frame
        self.add_contact_frame = QtWidgets.QFrame(self.contact_information_group_box)
        self.add_contact_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_contact_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_contact_frame.setObjectName("add_contact_frame")
        self.addContactFrameLayout = QtWidgets.QVBoxLayout(self.add_contact_frame)
        self.addContactFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.addContactFrameLayout.setSpacing(0)
        self.addContactFrameLayout.setObjectName("addContactFrameLayout")

        # position outter frame
        self.position_outter_frame = QtWidgets.QFrame(self.add_contact_frame)
        self.position_outter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.position_outter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.position_outter_frame.setObjectName("position_outter_frame")
        self.positionOutterFrameLayout = QtWidgets.QHBoxLayout(self.position_outter_frame)
        self.positionOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.positionOutterFrameLayout.setSpacing(0)
        self.positionOutterFrameLayout.setObjectName("positionOutterFrameLayout")

        # contact position frame
        self.contact_position_frame = QtWidgets.QFrame(self.position_outter_frame)
        self.contact_position_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_position_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_position_frame.setObjectName("contact_position_frame")
        self.contactionPositionFrameLayout = QtWidgets.QVBoxLayout(self.contact_position_frame)
        self.contactionPositionFrameLayout.setContentsMargins(0, 0, 9, 0)
        self.contactionPositionFrameLayout.setSpacing(6)
        self.contactionPositionFrameLayout.setObjectName("contactionPositionFrameLayout")

        # contact position label
        self.contact_position_label = QtWidgets.QLabel(self.contact_position_frame)
        self.contact_position_label.setObjectName("contact_position_label")
        self.contactionPositionFrameLayout.addWidget(self.contact_position_label)

        # contact position line edit
        self.contact_position_line_edit = QtWidgets.QLineEdit(self.contact_position_frame)
        self.contact_position_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.contact_position_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_position_line_edit.setObjectName("contact_position_line_edit")
        self.contactionPositionFrameLayout.addWidget(self.contact_position_line_edit)
        self.positionOutterFrameLayout.addWidget(self.contact_position_frame)

        # spacer item
        spacerItem = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.positionOutterFrameLayout.addItem(spacerItem)
        self.addContactFrameLayout.addWidget(self.position_outter_frame)

        # contact name outter frame
        self.contact_name_outter_frame = QtWidgets.QFrame(self.add_contact_frame)
        self.contact_name_outter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_name_outter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_name_outter_frame.setObjectName("contact_name_outter_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contact_name_outter_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # contact first name frame
        self.contact_first_name_frame = QtWidgets.QFrame(self.contact_name_outter_frame)
        self.contact_first_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_first_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_first_name_frame.setObjectName("contact_first_name_frame")
        self.contactFirstNameLayout = QtWidgets.QVBoxLayout(self.contact_first_name_frame)
        self.contactFirstNameLayout.setContentsMargins(0, 0, -1, 0)
        self.contactFirstNameLayout.setObjectName("contactFirstNameLayout")

        # contact first name label
        self.contact_first_name_label = QtWidgets.QLabel(self.contact_first_name_frame)
        self.contact_first_name_label.setObjectName("contact_first_name_label")
        self.contactFirstNameLayout.addWidget(self.contact_first_name_label)

        # contact first name line edit
        self.contact_first_name_line_edit = QtWidgets.QLineEdit(self.contact_first_name_frame)
        self.contact_first_name_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.contact_first_name_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_first_name_line_edit.setObjectName("contact_first_name_line_edit")
        self.contactFirstNameLayout.addWidget(self.contact_first_name_line_edit)
        self.horizontalLayout.addWidget(self.contact_first_name_frame)

        # contact last name frame
        self.contact_last_name_frame = QtWidgets.QFrame(self.contact_name_outter_frame)
        self.contact_last_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_last_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_last_name_frame.setObjectName("contact_last_name_frame")
        self.contactLastNameLayout = QtWidgets.QVBoxLayout(self.contact_last_name_frame)
        self.contactLastNameLayout.setContentsMargins(9, 0, 0, 0)
        self.contactLastNameLayout.setObjectName("contactLastNameLayout")

        # contact last name label
        self.contact_last_name_label = QtWidgets.QLabel(self.contact_last_name_frame)
        self.contact_last_name_label.setObjectName("contact_last_name_label")
        self.contactLastNameLayout.addWidget(self.contact_last_name_label)

        # contact last name line edit
        self.contact_last_name_line_edit = QtWidgets.QLineEdit(self.contact_last_name_frame)
        self.contact_last_name_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.contact_last_name_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_last_name_line_edit.setObjectName("contact_last_name_line_edit")
        self.contactLastNameLayout.addWidget(self.contact_last_name_line_edit)
        self.horizontalLayout.addWidget(self.contact_last_name_frame)
        self.addContactFrameLayout.addWidget(self.contact_name_outter_frame)

        # contact reachback outter frame
        self.contact_reachback_outter_frame = QtWidgets.QFrame(self.add_contact_frame)
        self.contact_reachback_outter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_reachback_outter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_reachback_outter_frame.setObjectName("contact_reachback_outter_frame")
        self.contactReachbackOutterFrameLayout = QtWidgets.QHBoxLayout(self.contact_reachback_outter_frame)
        self.contactReachbackOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactReachbackOutterFrameLayout.setSpacing(0)
        self.contactReachbackOutterFrameLayout.setObjectName("contactReachbackOutterFrameLayout")

        # contact phone frame
        self.contact_phone_frame = QtWidgets.QFrame(self.contact_reachback_outter_frame)
        self.contact_phone_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_phone_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_phone_frame.setObjectName("contact_phone_frame")
        self.contactPhoneFrameLayout = QtWidgets.QVBoxLayout(self.contact_phone_frame)
        self.contactPhoneFrameLayout.setContentsMargins(0, 0, -1, 0)
        self.contactPhoneFrameLayout.setObjectName("contactPhoneFrameLayout")

        # contact phone label
        self.contact_phone_label = QtWidgets.QLabel(self.contact_phone_frame)
        self.contact_phone_label.setObjectName("contact_phone_label")
        self.contactPhoneFrameLayout.addWidget(self.contact_phone_label)

        # contact phone line edit
        self.contact_phone_line_edit = QtWidgets.QLineEdit(self.contact_phone_frame)
        self.contact_phone_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.contact_phone_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_phone_line_edit.setObjectName("contact_phone_line_edit")
        self.contactPhoneFrameLayout.addWidget(self.contact_phone_line_edit)
        self.contactReachbackOutterFrameLayout.addWidget(self.contact_phone_frame)

        # contact email frame
        self.contact_email_frame = QtWidgets.QFrame(self.contact_reachback_outter_frame)
        self.contact_email_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_email_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_email_frame.setObjectName("contact_email_frame")
        self.contactEmailLayout = QtWidgets.QVBoxLayout(self.contact_email_frame)
        self.contactEmailLayout.setContentsMargins(-1, 0, 0, 0)
        self.contactEmailLayout.setObjectName("contactEmailLayout")

        # contact email label
        self.contact_email_label = QtWidgets.QLabel(self.contact_email_frame)
        self.contact_email_label.setObjectName("contact_email_label")
        self.contactEmailLayout.addWidget(self.contact_email_label)

        # contact email line edit
        self.contact_email_line_edit = QtWidgets.QLineEdit(self.contact_email_frame)
        self.contact_email_line_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.contact_email_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_email_line_edit.setObjectName("contact_email_line_edit")
        self.contactEmailLayout.addWidget(self.contact_email_line_edit)
        self.contactReachbackOutterFrameLayout.addWidget(self.contact_email_frame)
        self.addContactFrameLayout.addWidget(self.contact_reachback_outter_frame)

        # contact error frame
        self.contact_error_frame = QtWidgets.QFrame(self.add_contact_frame)
        self.contact_error_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.contact_error_frame.setStyleSheet(
            "QFrame {\n"
                "color: red;\n"
            "}"
        )
        self.contact_error_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_error_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_error_frame.setObjectName("contact_error_frame")
        self.contactErrorFrameLayout = QtWidgets.QVBoxLayout(self.contact_error_frame)
        self.contactErrorFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactErrorFrameLayout.setSpacing(0)
        self.contactErrorFrameLayout.setObjectName("contactErrorFrameLayout")

        # contact error label
        self.contact_error_label = QtWidgets.QLabel(self.contact_error_frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.contact_error_label.setFont(font)
        self.contact_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_error_label.setObjectName("contact_error_label")
        self.contactErrorFrameLayout.addWidget(self.contact_error_label)
        self.addContactFrameLayout.addWidget(self.contact_error_frame)

        # contact action frame
        self.contact_action_frame = QtWidgets.QFrame(self.add_contact_frame)
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
        self.contact_action_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contact_action_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contact_action_frame.setObjectName("contact_action_frame")
        self.contactActionFrameLayout = QtWidgets.QHBoxLayout(self.contact_action_frame)
        self.contactActionFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.contactActionFrameLayout.setSpacing(0)
        self.contactActionFrameLayout.setObjectName("contactActionFrameLayout")

        # spacer item
        spacerItem1 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.contactActionFrameLayout.addItem(spacerItem1)

        # add contact button
        self.add_contact_button = QtWidgets.QPushButton(self.contact_action_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_contact_button.setFont(font)
        self.add_contact_button.setObjectName("add_contact_button")
        self.contactActionFrameLayout.addWidget(self.add_contact_button)

        # spacer item
        spacerItem2 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.contactActionFrameLayout.addItem(spacerItem2)
        self.addContactFrameLayout.addWidget(self.contact_action_frame)
        self.contactionInformationGroupBoxLayout.addWidget(self.add_contact_frame)
        self.bodyFrameLayout.addWidget(self.contact_information_group_box)





        # application status history group box
        self.application_status_history_group_box = QtWidgets.QGroupBox(self.body_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.application_status_history_group_box.setFont(font)
        self.application_status_history_group_box.setFlat(True)
        self.application_status_history_group_box.setObjectName("application_status_history_group_box")
        self.applicationStatusHistoryGroupBoxLayout = QtWidgets.QVBoxLayout(self.application_status_history_group_box)
        self.applicationStatusHistoryGroupBoxLayout.setObjectName("applicationStatusHistoryGroupBoxLayout")

        # application status history table widget
        self.application_status_history_table_widget = QtWidgets.QTableWidget(self.application_status_history_group_box)
        self.application_status_history_table_widget.setMinimumSize(QtCore.QSize(0, 150))
        self.application_status_history_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.application_status_history_table_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.application_status_history_table_widget.setShowGrid(False)
        self.application_status_history_table_widget.setWordWrap(True)
        self.application_status_history_table_widget.setObjectName("application_status_history_table_widget")
        self.application_status_history_table_widget.setColumnCount(2)
        self.application_status_history_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.application_status_history_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.application_status_history_table_widget.setHorizontalHeaderItem(1, item)
        self.application_status_history_table_widget.verticalHeader().setVisible(False)
        self.applicationStatusHistoryGroupBoxLayout.addWidget(self.application_status_history_table_widget)

        # application status history actions frame
        self.application_status_history_actions_frame = QtWidgets.QFrame(self.application_status_history_group_box)
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
        self.application_status_history_actions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.application_status_history_actions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.application_status_history_actions_frame.setObjectName("application_status_history_actions_frame")
        self.applicationStatusHistoryActionsFrameLayout = QtWidgets.QHBoxLayout(self.application_status_history_actions_frame)
        self.applicationStatusHistoryActionsFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.applicationStatusHistoryActionsFrameLayout.setObjectName("applicationStatusHistoryActionsFrameLayout")

        # application status combo box
        self.application_status_combo_box = QtWidgets.QComboBox(self.application_status_history_actions_frame)
        self.application_status_combo_box.setMinimumSize(QtCore.QSize(0, 25))
        self.application_status_combo_box.setMaximumSize(QtCore.QSize(16777215, 25))
        self.application_status_combo_box.setObjectName("application_status_combo_box")

        for _ in range(5):
            self.application_status_combo_box.addItem("")

        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.application_status_combo_box)

        # application status date edit
        self.application_status_date_edit = QtWidgets.QDateEdit(self.application_status_history_actions_frame)
        self.application_status_date_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.application_status_date_edit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.application_status_date_edit.setMaximumDate(QtCore.QDate(2124, 12, 31))
        self.application_status_date_edit.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.application_status_date_edit.setCalendarPopup(True)
        self.application_status_date_edit.setObjectName("application_status_date_edit")
        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.application_status_date_edit)

        # add application status button
        self.add_application_status_button = QtWidgets.QPushButton(self.application_status_history_actions_frame)
        self.add_application_status_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_application_status_button.setFont(font)
        self.add_application_status_button.setObjectName("add_application_status_button")
        self.applicationStatusHistoryActionsFrameLayout.addWidget(self.add_application_status_button)
        self.applicationStatusHistoryGroupBoxLayout.addWidget(self.application_status_history_actions_frame)
        self.bodyFrameLayout.addWidget(self.application_status_history_group_box)





        # actions outter frame
        self.actions_outter_frame = QtWidgets.QFrame(self.body_frame)
        self.actions_outter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.actions_outter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actions_outter_frame.setObjectName("actions_outter_frame")
        self.actionsOutterFrameLayout = QtWidgets.QVBoxLayout(self.actions_outter_frame)
        self.actionsOutterFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.actionsOutterFrameLayout.setSpacing(0)
        self.actionsOutterFrameLayout.setObjectName("actionsOutterFrameLayout")

        # error frame
        self.error_frame = QtWidgets.QFrame(self.actions_outter_frame)
        self.error_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.error_frame.setFont(font)
        self.error_frame.setStyleSheet(
            "QFrame {\n"
                "color: red;\n"
            "}"
        )
        self.error_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_frame.setObjectName("error_frame")
        self.errorFrame_layout = QtWidgets.QVBoxLayout(self.error_frame)
        self.errorFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.errorFrame_layout.setSpacing(0)
        self.errorFrame_layout.setObjectName("errorFrame_layout")

        # error label
        self.error_label = QtWidgets.QLabel(self.error_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.errorFrame_layout.addWidget(self.error_label)
        self.actionsOutterFrameLayout.addWidget(self.error_frame)

        # actions frame
        self.actions_frame = QtWidgets.QFrame(self.actions_outter_frame)
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
        self.actions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.actions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.actionsFrame_layout = QtWidgets.QHBoxLayout(self.actions_frame)
        self.actionsFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.actionsFrame_layout.setSpacing(0)
        self.actionsFrame_layout.setObjectName("actionsFrame_layout")

        # spacer item
        spacerItem3 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actionsFrame_layout.addItem(spacerItem3)

        # save button
        self.save_button = QtWidgets.QPushButton(self.actions_frame)
        self.save_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.actionsFrame_layout.addWidget(self.save_button)

        # spacer item
        spacerItem4 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actionsFrame_layout.addItem(spacerItem4)
        self.actionsOutterFrameLayout.addWidget(self.actions_frame)
        self.bodyFrameLayout.addWidget(self.actions_outter_frame)
        self.scrollAreaLayout.addWidget(self.body_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.dialogWindowLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
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
        self.contact_information_group_box.setTitle(_translate("Dialog", "Contact Information"))
        item = self.contact_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Position"))
        item = self.contact_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First Name"))
        item = self.contact_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Last Name"))
        item = self.contact_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        item = self.contact_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Phone"))
        self.contact_position_label.setText(_translate("Dialog", "Position:"))
        self.contact_first_name_label.setText(_translate("Dialog", "*First Name:"))
        self.contact_last_name_label.setText(_translate("Dialog", "*Last Name:"))
        self.contact_phone_label.setText(_translate("Dialog", "Phone Number:"))
        self.contact_email_label.setText(_translate("Dialog", "Email Address:"))
        self.contact_error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))
        self.add_contact_button.setText(_translate("Dialog", "Add Contact"))
        self.application_status_history_group_box.setTitle(_translate("Dialog", "Application Status History"))
        item = self.application_status_history_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Status"))
        item = self.application_status_history_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date"))

        application_statuses = ["-", "Screening Interview", "Technical Interview", "Job Offer", "Application Rejected" ]
        for index in range(5):
             self.application_status_combo_box.setItemText(index, _translate("Dialog", application_statuses[index]))

        self.add_application_status_button.setText(_translate("Dialog", "Add Status"))
        self.error_label.setText(_translate("Dialog", "SAMPLE ERROR MESSAGE"))
        self.save_button.setText(_translate("Dialog", "Save"))
