import sqlite3

from PyQt5.QtCore import QSize, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import (
    QDialog, QWidget, QStackedWidget, QTableWidget, QTableWidgetItem,
    QFrame, QGroupBox,
    QLabel, QSpacerItem,
    QPushButton, QLineEdit, QComboBox, QCheckBox,
    QHBoxLayout, QVBoxLayout, QSizePolicy,
    QAbstractScrollArea, QAbstractItemView
    )

from ui_new_application_dialog import *
from ui_view_application_dialog import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 878)
        MainWindow.setAnimated(False)

        # central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralWidget_layout = QHBoxLayout(self.centralwidget)
        self.centralWidget_layout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget_layout.setSpacing(0)
        self.centralWidget_layout.setObjectName("centralWidget_layout")





        # side frame
        self.side_frame = QFrame(self.centralwidget)
        self.side_frame.setMinimumSize(QSize(200, 0))
        self.side_frame.setMaximumSize(QSize(0, 16777215))
        self.side_frame.setStyleSheet("")
        self.side_frame.setFrameShape(QFrame.NoFrame)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.side_frame.setObjectName("side_frame")
        self.sideFrame_layout = QVBoxLayout(self.side_frame)
        self.sideFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.sideFrame_layout.setSpacing(0)
        self.sideFrame_layout.setObjectName("sideFrame_layout")

        # application title frame
        self.application_title_frame = QFrame(self.side_frame)
        self.application_title_frame.setMinimumSize(QSize(0, 80))
        self.application_title_frame.setMaximumSize(QSize(16777215, 80))
        self.application_title_frame.setStyleSheet(
            "background-color: rgb(25, 105, 170);\n"
            "color: rgb(220, 220, 220);"
        )
        self.application_title_frame.setFrameShape(QFrame.NoFrame)
        self.application_title_frame.setFrameShadow(QFrame.Raised)
        self.application_title_frame.setObjectName("application_title_frame")
        self.applicationTitleFrame_layout = QVBoxLayout(self.application_title_frame)
        self.applicationTitleFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationTitleFrame_layout.setSpacing(0)
        self.applicationTitleFrame_layout.setObjectName("applicationTitleFrame_layout")

        # application title label
        self.application_title = QLabel(self.application_title_frame)
        font = QFont()
        font.setPointSize(12)
        self.application_title.setFont(font)
        self.application_title.setAlignment(Qt.AlignCenter)
        self.application_title.setObjectName("application_title")
        self.applicationTitleFrame_layout.addWidget(self.application_title)
        self.sideFrame_layout.addWidget(self.application_title_frame)

        # navagation frame
        self.navagation_frame = QFrame(self.side_frame)
        self.navagation_frame.setStyleSheet(
            "QFrame{\n"
                "background-color: rgb(50, 50, 75);\n"
                "color: white;\n"
            "}\n"
            "QPushButton {\n"
                "border: none;\n"
                "background-color: rgb(50, 50, 75);\n"
                "color: white;\n"
            "}\n"
            "QPushButton:Hover {\n"
                "background-color: rgb(59, 61, 90);\n"
            "}"
        )
        self.navagation_frame.setFrameShape(QFrame.NoFrame)
        self.navagation_frame.setFrameShadow(QFrame.Raised)
        self.navagation_frame.setObjectName("navagation_frame")
        self.navagationFrame_layout = QVBoxLayout(self.navagation_frame)
        self.navagationFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.navagationFrame_layout.setSpacing(0)
        self.navagationFrame_layout.setObjectName("navagationFrame_layout")

        # applications page button
        self.applications_page_button = QPushButton(self.navagation_frame)
        self.applications_page_button.setMinimumSize(QSize(0, 60))
        self.applications_page_button.setMaximumSize(QSize(16777215, 100000))
        self.applications_page_button.setStyleSheet(
            "background-color: rgb(33, 150, 243)"
        )
        font = QFont()
        font.setPointSize(10)
        self.applications_page_button.setFont(font)
        self.applications_page_button.setObjectName("applications_page_button")
        self.navagationFrame_layout.addWidget(self.applications_page_button)
        self.applications_page_button.clicked.connect(self.show_applications_page)

        # contacts page button
        self.contacts_page_button = QPushButton(self.navagation_frame)
        self.contacts_page_button.setMinimumSize(QSize(0, 60))
        self.contacts_page_button.setMaximumSize(QSize(16777215, 100000))
        font = QFont()
        font.setPointSize(10)
        self.contacts_page_button.setFont(font)
        self.contacts_page_button.setObjectName("contacts_page_button")
        self.navagationFrame_layout.addWidget(self.contacts_page_button)
        self.contacts_page_button.clicked.connect(self.show_contacts_page)

        # questions page button
        self.questions_page_button = QPushButton(self.navagation_frame)
        self.questions_page_button.setMinimumSize(QSize(0, 60))
        self.questions_page_button.setMaximumSize(QSize(16777215, 100000))
        font = QFont()
        font.setPointSize(10)
        self.questions_page_button.setFont(font)
        self.questions_page_button.setObjectName("questions_page_button")
        self.navagationFrame_layout.addWidget(self.questions_page_button)
        self.questions_page_button.clicked.connect(self.show_questions_page)

        # statistics page button
        self.statistics_page_button = QPushButton(self.navagation_frame)
        self.statistics_page_button.setMinimumSize(QSize(0, 60))
        self.statistics_page_button.setMaximumSize(QSize(16777215, 100000))
        font = QFont()
        font.setPointSize(10)
        self.statistics_page_button.setFont(font)
        self.statistics_page_button.setObjectName("statistics_page_button")
        self.navagationFrame_layout.addWidget(self.statistics_page_button)
        self.statistics_page_button.clicked.connect(self.show_statistics_page)

        # navagation frame bottom spacer
        spacerItem = QSpacerItem(20, 551, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.navagationFrame_layout.addItem(spacerItem)
        self.sideFrame_layout.addWidget(self.navagation_frame)
        self.centralWidget_layout.addWidget(self.side_frame)





        # main frame
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.mainFrame_layout = QVBoxLayout(self.main_frame)
        self.mainFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame_layout.setSpacing(0)
        self.mainFrame_layout.setObjectName("mainFrame_layout")

        # stacked widget
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setStyleSheet(
            "background-color: rgb(240, 240, 240);"
        )
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")





        # applications page
        self.applications_page = QWidget()
        self.applications_page.setStyleSheet(
            "QPushButton {\n"
                "padding: 15px 35px;\n"
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
        self.applications_page.setObjectName("applications_page")
        self.applicationsPage_layout = QVBoxLayout(self.applications_page)
        self.applicationsPage_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationsPage_layout.setSpacing(0)
        self.applicationsPage_layout.setObjectName("applicationsPage_layout")

        # applications page header frame
        self.applications_header_frame = QFrame(self.applications_page)
        self.applications_header_frame.setMinimumSize(QSize(0, 80))
        self.applications_header_frame.setMaximumSize(QSize(16777215, 80))
        self.applications_header_frame.setStyleSheet(
            "background-color: rgb(33, 150, 243);\n"
            "color: white;"
        )
        self.applications_header_frame.setFrameShape(QFrame.StyledPanel)
        self.applications_header_frame.setFrameShadow(QFrame.Raised)
        self.applications_header_frame.setObjectName("applications_header_frame")
        self.applicationsHeaderFrame_layout = QVBoxLayout(self.applications_header_frame)
        self.applicationsHeaderFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationsHeaderFrame_layout.setSpacing(0)
        self.applicationsHeaderFrame_layout.setObjectName("applicationsHeaderFrame_layout")

        # applications page title label
        self.applications_title = QLabel(self.applications_header_frame)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.applications_title.setFont(font)
        self.applications_title.setAlignment(Qt.AlignCenter)
        self.applications_title.setObjectName("applications_title")
        self.applicationsHeaderFrame_layout.addWidget(self.applications_title)
        self.applicationsPage_layout.addWidget(self.applications_header_frame)

        # applications body frame
        self.applications_body_frame = QFrame(self.applications_page)
        self.applications_body_frame.setFrameShape(QFrame.StyledPanel)
        self.applications_body_frame.setFrameShadow(QFrame.Raised)
        self.applications_body_frame.setObjectName("applications_body_frame")
        self.applicationsBodyFrame_layout = QHBoxLayout(self.applications_body_frame)
        self.applicationsBodyFrame_layout.setContentsMargins(24, 24, 24, 24)
        self.applicationsBodyFrame_layout.setSpacing(24)
        self.applicationsBodyFrame_layout.setObjectName("applicationsBodyFrame_layout")

        # application filter outter frame
        self.application_filter_outter_frame = QFrame(self.applications_body_frame)
        self.application_filter_outter_frame.setMinimumSize(QSize(200, 0))
        self.application_filter_outter_frame.setMaximumSize(QSize(200, 16777215))
        self.application_filter_outter_frame.setFrameShape(QFrame.NoFrame)
        self.application_filter_outter_frame.setFrameShadow(QFrame.Raised)
        self.application_filter_outter_frame.setObjectName("application_filter_outter_frame")
        self.applicationFilterOutterFrame_layout = QVBoxLayout(self.application_filter_outter_frame)
        self.applicationFilterOutterFrame_layout.setContentsMargins(0, 24, 0, 0)
        self.applicationFilterOutterFrame_layout.setSpacing(15)
        self.applicationFilterOutterFrame_layout.setObjectName("applicationFilterOutterFrame_layout")

        # application filter content group box
        self.application_filter_content_groupbox = QGroupBox(self.application_filter_outter_frame)
        self.application_filter_content_groupbox.setMinimumSize(QSize(200, 0))
        self.application_filter_content_groupbox.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.application_filter_content_groupbox.setFont(font)
        self.application_filter_content_groupbox.setFocusPolicy(Qt.NoFocus)
        self.application_filter_content_groupbox.setStyleSheet(
            "QGroupBox {\n"
                "color: rgb(33, 150, 243);\n"
                "padding-top: 15px;\n"
            "}\n"
            "QLineEdit {\n"
                "border: 0px;\n"
                "background-color: white;\n"
            "}\n"
            "QComboBox {\n"
                "border: 0px;\n"
                "background-color: white;\n"
            "}\n"
            "QListView {\n"
                "background-color: white;\n"
            "}\n"
            "QGroupBox {\n"
                "border: 1px solid rgb(220, 220, 220);\n"
                "border-radius: 20px;\n"
            "}"
        )
        self.application_filter_content_groupbox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.application_filter_content_groupbox.setFlat(True)
        self.application_filter_content_groupbox.setCheckable(False)
        self.application_filter_content_groupbox.setObjectName("application_filter_content_groupbox")
        self.applicationFilterContentGroupbox_layout = QVBoxLayout(self.application_filter_content_groupbox)
        self.applicationFilterContentGroupbox_layout.setContentsMargins(-1, 10, 9, 9)
        self.applicationFilterContentGroupbox_layout.setSpacing(12)
        self.applicationFilterContentGroupbox_layout.setObjectName("applicationFilterContentGroupbox_layout")

        # application company filter frame
        self.application_company_filter_frame = QFrame(self.application_filter_content_groupbox)
        self.application_company_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.application_company_filter_frame.setFrameShadow(QFrame.Raised)
        self.application_company_filter_frame.setObjectName("application_company_filter_frame")
        self.applicationCompanyFilterFrame_layout = QVBoxLayout(self.application_company_filter_frame)
        self.applicationCompanyFilterFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationCompanyFilterFrame_layout.setObjectName("applicationCompanyFilterFrame_layout")

        # application company filter label
        self.application_company_filter_label = QLabel(self.application_company_filter_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.application_company_filter_label.setFont(font)
        self.application_company_filter_label.setObjectName("application_company_filter_label")
        self.applicationCompanyFilterFrame_layout.addWidget(self.application_company_filter_label)

        # application company filter line edit
        self.application_company_filter_line_edit = QLineEdit(self.application_company_filter_frame)
        self.application_company_filter_line_edit.setMinimumSize(QSize(0, 25))
        self.application_company_filter_line_edit.setMaximumSize(QSize(16777215, 25))
        self.application_company_filter_line_edit.setObjectName("application_company_filter_line_edit")
        self.applicationCompanyFilterFrame_layout.addWidget(self.application_company_filter_line_edit)
        self.applicationFilterContentGroupbox_layout.addWidget(self.application_company_filter_frame)

        # application position filter frame
        self.application_position_filter_frame = QFrame(self.application_filter_content_groupbox)
        self.application_position_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.application_position_filter_frame.setFrameShadow(QFrame.Raised)
        self.application_position_filter_frame.setObjectName("application_position_filter_frame")
        self.applicationPositionFilterFrame_layout = QVBoxLayout(self.application_position_filter_frame)
        self.applicationPositionFilterFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationPositionFilterFrame_layout.setObjectName("applicationPositionFilterFrame_layout")

        # application position filter label
        self.application_position_filter_label = QLabel(self.application_position_filter_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.application_position_filter_label.setFont(font)
        self.application_position_filter_label.setObjectName("application_position_filter_label")
        self.applicationPositionFilterFrame_layout.addWidget(self.application_position_filter_label)

        # application position filter line edit
        self.application_position_filter_line_edit = QLineEdit(self.application_position_filter_frame)
        self.application_position_filter_line_edit.setMinimumSize(QSize(0, 25))
        self.application_position_filter_line_edit.setMaximumSize(QSize(16777215, 25))
        self.application_position_filter_line_edit.setObjectName("application_position_filter_line_edit")
        self.applicationPositionFilterFrame_layout.addWidget(self.application_position_filter_line_edit)
        self.applicationFilterContentGroupbox_layout.addWidget(self.application_position_filter_frame)

        # application city filter frame
        self.application_city_filter_frame = QFrame(self.application_filter_content_groupbox)
        self.application_city_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.application_city_filter_frame.setFrameShadow(QFrame.Raised)
        self.application_city_filter_frame.setObjectName("application_city_filter_frame")
        self.applicationCityFilterFrame_layout = QVBoxLayout(self.application_city_filter_frame)
        self.applicationCityFilterFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationCityFilterFrame_layout.setObjectName("applicationCityFilterFrame_layout")

        # application city filter label
        self.application_city_filter_label = QLabel(self.application_city_filter_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.application_city_filter_label.setFont(font)
        self.application_city_filter_label.setObjectName("application_city_filter_label")
        self.applicationCityFilterFrame_layout.addWidget(self.application_city_filter_label)

        # application city filter line edit
        self.application_city_filter_line_edit = QLineEdit(self.application_city_filter_frame)
        self.application_city_filter_line_edit.setMinimumSize(QSize(0, 25))
        self.application_city_filter_line_edit.setMaximumSize(QSize(16777215, 25))
        self.application_city_filter_line_edit.setObjectName("application_city_filter_line_edit")
        self.applicationCityFilterFrame_layout.addWidget(self.application_city_filter_line_edit)
        self.applicationFilterContentGroupbox_layout.addWidget(self.application_city_filter_frame)

        # application state filter frame
        self.application_state_filter_frame = QFrame(self.application_filter_content_groupbox)
        self.application_state_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.application_state_filter_frame.setFrameShadow(QFrame.Raised)
        self.application_state_filter_frame.setObjectName("application_state_filter_frame")
        self.applicationStateFilterFrame_layout = QVBoxLayout(self.application_state_filter_frame)
        self.applicationStateFilterFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationStateFilterFrame_layout.setObjectName("applicationStateFilterFrame_layout")

        # application state filter label
        self.application_state_filter_label = QLabel(self.application_state_filter_frame)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.application_state_filter_label.setFont(font)
        self.application_state_filter_label.setObjectName("application_state_filter_label")
        self.applicationStateFilterFrame_layout.addWidget(self.application_state_filter_label)

        # application state filter combo box
        self.application_state_filter_combo_box = QComboBox(self.application_state_filter_frame)
        self.application_state_filter_combo_box.setMinimumSize(QSize(0, 25))
        self.application_state_filter_combo_box.setMaximumSize(QSize(16777215, 25))
        self.application_state_filter_combo_box.setStyleSheet("")
        self.application_state_filter_combo_box.setObjectName("application_state_filter_combo_box")
        for i in range(51):
            self.application_state_filter_combo_box.addItem("")
        self.applicationStateFilterFrame_layout.addWidget(self.application_state_filter_combo_box)
        self.applicationFilterContentGroupbox_layout.addWidget(self.application_state_filter_frame)

        # application status filter group box
        self.application_status_filter_groupbox = QGroupBox(self.application_filter_content_groupbox)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.application_status_filter_groupbox.setFont(font)
        self.application_status_filter_groupbox.setStyleSheet(
            "QGroupBox {\n"
                "padding-top: 0px;\n"
                "color: black;\n"
                "border-radius: 10px;\n"
            "}\n"
            "QCheckBox:Indicator:Unchecked {\n"
                "border: 1px solid rgb(220, 220, 220);\n"
                "border-radius: 2px;\n"
                "background-color: white;\n"
            "}"
        )
        self.application_status_filter_groupbox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.application_status_filter_groupbox.setFlat(True)
        self.application_status_filter_groupbox.setObjectName("application_status_filter_groupbox")
        self.applicationStatusFilterGroupBox_layout = QVBoxLayout(self.application_status_filter_groupbox)
        self.applicationStatusFilterGroupBox_layout.setContentsMargins(-1, 20, -1, -1)
        self.applicationStatusFilterGroupBox_layout.setObjectName("applicationStatusFilterGroupBox_layout")

        # application submitted check box
        self.application_submitted_checkbox = QCheckBox(self.application_status_filter_groupbox)
        self.application_submitted_checkbox.setAutoFillBackground(False)
        self.application_submitted_checkbox.setObjectName("application_submitted_checkbox")
        self.applicationStatusFilterGroupBox_layout.addWidget(self.application_submitted_checkbox)

        # screening interview check box
        self.screening_interview_checkbox = QCheckBox(self.application_status_filter_groupbox)
        self.screening_interview_checkbox.setObjectName("screening_interview_checkbox")
        self.applicationStatusFilterGroupBox_layout.addWidget(self.screening_interview_checkbox)

        # technical interview check box
        self.technical_interview_checkbox = QCheckBox(self.application_status_filter_groupbox)
        self.technical_interview_checkbox.setObjectName("technical_interview_checkbox")
        self.applicationStatusFilterGroupBox_layout.addWidget(self.technical_interview_checkbox)

        # job offer check box
        self.job_offer_check_box = QCheckBox(self.application_status_filter_groupbox)
        self.job_offer_check_box.setObjectName("job_offer_check_box")
        self.applicationStatusFilterGroupBox_layout.addWidget(self.job_offer_check_box)

        # application rejected check box
        self.application_rejected_checkbox = QCheckBox(self.application_status_filter_groupbox)
        self.application_rejected_checkbox.setObjectName("application_rejected_checkbox")
        self.applicationStatusFilterGroupBox_layout.addWidget(self.application_rejected_checkbox)
        self.applicationFilterContentGroupbox_layout.addWidget(self.application_status_filter_groupbox)
        self.applicationFilterOutterFrame_layout.addWidget(self.application_filter_content_groupbox)

        # application filter actions frame
        self.application_filter_actions_frame = QFrame(self.application_filter_outter_frame)
        self.application_filter_actions_frame.setMaximumSize(QSize(16777215, 50))
        self.application_filter_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.application_filter_actions_frame.setFrameShadow(QFrame.Raised)
        self.application_filter_actions_frame.setObjectName("application_filter_actions_frame")
        self.applicationFilterActionsFrame_layout = QHBoxLayout(self.application_filter_actions_frame)
        self.applicationFilterActionsFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationFilterActionsFrame_layout.setSpacing(0)
        self.applicationFilterActionsFrame_layout.setObjectName("applicationFilterActionsFrame_layout")

        # application filter actions frame left spacer
        application_filter_actions_frame_left_spacer = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.applicationFilterActionsFrame_layout.addItem(application_filter_actions_frame_left_spacer)

        # apply application filters button
        self.apply_application_filters_button = QPushButton(self.application_filter_actions_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.apply_application_filters_button.setFont(font)
        self.apply_application_filters_button.setObjectName("apply_application_filters_button")
        self.applicationFilterActionsFrame_layout.addWidget(self.apply_application_filters_button)

        # application filter actions frame right spacer
        application_filter_actions_frame_right_spacer = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.applicationFilterActionsFrame_layout.addItem(application_filter_actions_frame_right_spacer)
        self.applicationFilterOutterFrame_layout.addWidget(self.application_filter_actions_frame)

        # application filter outter frame spacer
        application_filter_outter_frame_spacer = QSpacerItem(183, 234, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.applicationFilterOutterFrame_layout.addItem(application_filter_outter_frame_spacer)
        self.applicationsBodyFrame_layout.addWidget(self.application_filter_outter_frame)

        # application content frame
        self.application_content_frame = QFrame(self.applications_body_frame)
        self.application_content_frame.setFrameShape(QFrame.StyledPanel)
        self.application_content_frame.setFrameShadow(QFrame.Raised)
        self.application_content_frame.setObjectName("application_content_frame")
        self.applicationContentFrame_layout = QVBoxLayout(self.application_content_frame)
        self.applicationContentFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationContentFrame_layout.setSpacing(24)
        self.applicationContentFrame_layout.setObjectName("applicationContentFrame_layout")

        # application table widget
        self.appications_table_widget = QTableWidget(self.application_content_frame)
        self.appications_table_widget.setMaximumSize(QSize(16777215, 16777215))
        self.appications_table_widget.setFocusPolicy(Qt.ClickFocus)
        self.appications_table_widget.setStyleSheet(
            "QTableWidget {\n"
                "border: 1px solid rgb(220, 220, 220);\n"
                "background-color: white;\n"
            "}\n"
            "QHeaderView:Section {\n"
                "height: 30px;\n"
                "border: none;\n"
                "background-color: rgb(33, 150, 243);\n"
                "color: white;\n"
            "}\n"
            "QTableWidget:Item {\n"
                "padding-left: 3px;\n"
            "}\n"
            "QTableView::Item {\n"
                "background-color: rgb(213, 230, 243);\n"
            "}\n"
            "QTableView::Item:Alternate {\n"
                "background-color: rgb(236, 240, 243);\n"
            "}\n"
            "QTableView::Item:Selected {\n"
                "background-color: rgb(25, 105, 170);\n"
            "}"
        )
        self.appications_table_widget.setLineWidth(1)
        self.appications_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.appications_table_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.appications_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.appications_table_widget.setAlternatingRowColors(True)
        self.appications_table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.appications_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.appications_table_widget.setTextElideMode(Qt.ElideRight)
        self.appications_table_widget.setShowGrid(False)
        self.appications_table_widget.setGridStyle(Qt.SolidLine)
        self.appications_table_widget.setWordWrap(True)
        self.appications_table_widget.setCornerButtonEnabled(False)
        self.appications_table_widget.setRowCount(0)
        self.appications_table_widget.verticalHeader().setVisible(False)
        self.appications_table_widget.setObjectName("appications_table_widget")
        self.appications_table_widget.setColumnCount(5)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QColor(255, 255, 255))
        # column 0 (company)
        self.appications_table_widget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.appications_table_widget.setColumnWidth(0, 200)
        # column 1 (position)
        self.appications_table_widget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.appications_table_widget.setColumnWidth(1, 300)
        # column 2 (location)
        self.appications_table_widget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.appications_table_widget.setColumnWidth(2, 300)
        # column 3 (status)
        self.appications_table_widget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.appications_table_widget.setColumnWidth(3, 300)
        # column 4 (date)
        self.appications_table_widget.setHorizontalHeaderItem(4, item)
        self.appications_table_widget.horizontalHeader().setVisible(True)
        self.appications_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.appications_table_widget.horizontalHeader().setStretchLastSection(True)
        self.appications_table_widget.verticalHeader().setStretchLastSection(False)
        self.applicationContentFrame_layout.addWidget(self.appications_table_widget)

        # populate the applications table widget
        self.populate_applications_table()

        # application content actions frame
        self.application_content_actions_frame = QFrame(self.application_content_frame)
        self.application_content_actions_frame.setFrameShape(QFrame.StyledPanel)
        self.application_content_actions_frame.setFrameShadow(QFrame.Raised)
        self.application_content_actions_frame.setObjectName("application_content_actions_frame")
        self.applicationContentActionsFrame_layout = QHBoxLayout(self.application_content_actions_frame)
        self.applicationContentActionsFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.applicationContentActionsFrame_layout.setSpacing(24)
        self.applicationContentActionsFrame_layout.setObjectName("applicationContentActionsFrame_layout")

        # application content actions frame left spacer
        application_content_actions_frame_left_spacer = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.applicationContentActionsFrame_layout.addItem(application_content_actions_frame_left_spacer)

        # new application button
        self.new_application_button = QPushButton(self.application_content_actions_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.new_application_button.setFont(font)
        self.new_application_button.clicked.connect(self.openNewApplication)
        self.new_application_button.setObjectName("new_application_button")
        self.applicationContentActionsFrame_layout.addWidget(self.new_application_button)

        # view application button
        self.view_application_button = QPushButton(self.application_content_actions_frame)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.view_application_button.setFont(font)
        self.view_application_button.clicked.connect(self.openViewApplication)
        self.view_application_button.setObjectName("view_application_button")
        self.applicationContentActionsFrame_layout.addWidget(self.view_application_button)

        # application content actions frame right spacer
        application_content_actions_frame_right_spacer = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.applicationContentActionsFrame_layout.addItem(application_content_actions_frame_right_spacer)

        # 
        self.applicationContentFrame_layout.addWidget(self.application_content_actions_frame)
        self.applicationsBodyFrame_layout.addWidget(self.application_content_frame)
        self.applicationsPage_layout.addWidget(self.applications_body_frame)
        self.stackedWidget.addWidget(self.applications_page)





        # Contacts Page
        self.contacts_page = QWidget()
        self.contacts_page.setObjectName("contacts_page")
        self.contactsPage_layout = QVBoxLayout(self.contacts_page)
        self.contactsPage_layout.setContentsMargins(0, 0, 0, 0)
        self.contactsPage_layout.setSpacing(0)
        self.contactsPage_layout.setObjectName("contactsPage_layout")

        # contacts header frame
        self.contacts_header_frame = QFrame(self.contacts_page)
        self.contacts_header_frame.setMinimumSize(QSize(0, 80))
        self.contacts_header_frame.setMaximumSize(QSize(16777215, 80))
        self.contacts_header_frame.setStyleSheet(
            "background-color: rgb(196, 46, 68);\n"
            "color:white;"
        )
        self.contacts_header_frame.setFrameShape(QFrame.StyledPanel)
        self.contacts_header_frame.setFrameShadow(QFrame.Raised)
        self.contacts_header_frame.setObjectName("contacts_header_frame")
        self.contactsHeaderFrame_layout = QVBoxLayout(self.contacts_header_frame)
        self.contactsHeaderFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.contactsHeaderFrame_layout.setSpacing(0)
        self.contactsHeaderFrame_layout.setObjectName("contactsHeaderFrame_layout")

        # contacts page title label
        self.contacts_title = QLabel(self.contacts_header_frame)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.contacts_title.setFont(font)
        self.contacts_title.setAlignment(Qt.AlignCenter)
        self.contacts_title.setObjectName("contacts_title")
        self.contactsHeaderFrame_layout.addWidget(self.contacts_title)
        self.contactsPage_layout.addWidget(self.contacts_header_frame)

        # contacts page body frame
        self.contacts_body_frame = QFrame(self.contacts_page)
        self.contacts_body_frame.setFrameShape(QFrame.StyledPanel)
        self.contacts_body_frame.setFrameShadow(QFrame.Raised)
        self.contacts_body_frame.setObjectName("contacts_body_frame")
        self.contactsPage_layout.addWidget(self.contacts_body_frame)
        self.stackedWidget.addWidget(self.contacts_page)





        # question page
        self.questions_page = QWidget()
        self.questions_page.setObjectName("questions_page")
        self.questionsPage_layout = QVBoxLayout(self.questions_page)
        self.questionsPage_layout.setContentsMargins(0, 0, 0, 0)
        self.questionsPage_layout.setSpacing(0)
        self.questionsPage_layout.setObjectName("questionsPage_layout")

        # questions page header frame
        self.questions_header_frame = QFrame(self.questions_page)
        self.questions_header_frame.setMinimumSize(QSize(0, 80))
        self.questions_header_frame.setMaximumSize(QSize(16777215, 80))
        self.questions_header_frame.setStyleSheet(
            "background-color: rgb(59, 84, 188);\n"
            "color: white;"
        )
        self.questions_header_frame.setFrameShape(QFrame.StyledPanel)
        self.questions_header_frame.setFrameShadow(QFrame.Raised)
        self.questions_header_frame.setObjectName("questions_header_frame")
        self.questionsHeaderFrame_layout = QVBoxLayout(self.questions_header_frame)
        self.questionsHeaderFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.questionsHeaderFrame_layout.setSpacing(0)
        self.questionsHeaderFrame_layout.setObjectName("questionsHeaderFrame_layout")

        # questions page title label
        self.questions_title = QLabel(self.questions_header_frame)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.questions_title.setFont(font)
        self.questions_title.setAlignment(Qt.AlignCenter)
        self.questions_title.setObjectName("questions_title")
        self.questionsHeaderFrame_layout.addWidget(self.questions_title)
        self.questionsPage_layout.addWidget(self.questions_header_frame)

        # questions page body frame
        self.questions_body_frame = QFrame(self.questions_page)
        self.questions_body_frame.setFrameShape(QFrame.StyledPanel)
        self.questions_body_frame.setFrameShadow(QFrame.Raised)
        self.questions_body_frame.setObjectName("questions_body_frame")
        self.questionsPage_layout.addWidget(self.questions_body_frame)
        self.stackedWidget.addWidget(self.questions_page)





        # statistics page
        self.statistics_page = QWidget()
        self.statistics_page.setObjectName("statistics_page")
        self.statisticsPage_layout = QVBoxLayout(self.statistics_page)
        self.statisticsPage_layout.setContentsMargins(0, 0, 0, 0)
        self.statisticsPage_layout.setSpacing(0)
        self.statisticsPage_layout.setObjectName("statisticsPage_layout")

        # statistics page header frame
        self.statistics_header_frame = QFrame(self.statistics_page)
        self.statistics_header_frame.setMinimumSize(QSize(0, 80))
        self.statistics_header_frame.setMaximumSize(QSize(16777215, 80))
        self.statistics_header_frame.setStyleSheet(
            "background-color: rgb(247, 84, 48);\n"
            "color: white;"
        )
        self.statistics_header_frame.setFrameShape(QFrame.NoFrame)
        self.statistics_header_frame.setFrameShadow(QFrame.Raised)
        self.statistics_header_frame.setObjectName("statistics_header_frame")
        self.statisticsHeaderFrame_layout = QVBoxLayout(self.statistics_header_frame)
        self.statisticsHeaderFrame_layout.setContentsMargins(0, 0, 0, 0)
        self.statisticsHeaderFrame_layout.setSpacing(0)
        self.statisticsHeaderFrame_layout.setObjectName("statisticsHeaderFrame_layout")

        # statistics page title label
        self.statistics_title = QLabel(self.statistics_header_frame)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statistics_title.setFont(font)
        self.statistics_title.setAlignment(Qt.AlignCenter)
        self.statistics_title.setObjectName("statistics_title")
        self.statisticsHeaderFrame_layout.addWidget(self.statistics_title)
        self.statisticsPage_layout.addWidget(self.statistics_header_frame)

        # statistics page body frame
        self.statistics_body_frame = QFrame(self.statistics_page)
        self.statistics_body_frame.setFrameShape(QFrame.StyledPanel)
        self.statistics_body_frame.setFrameShadow(QFrame.Raised)
        self.statistics_body_frame.setObjectName("statistics_body_frame")
        self.statisticsPage_layout.addWidget(self.statistics_body_frame)
        self.stackedWidget.addWidget(self.statistics_page)





        # 
        self.mainFrame_layout.addWidget(self.stackedWidget)
        self.centralWidget_layout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        #
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.application_title.setText(_translate("MainWindow", "Job Application Vault"))
        self.applications_page_button.setText(_translate("MainWindow", "Applications"))
        self.contacts_page_button.setText(_translate("MainWindow", "Contacts"))
        self.questions_page_button.setText(_translate("MainWindow", "Questions"))
        self.statistics_page_button.setText(_translate("MainWindow", "Statistics"))
        self.applications_title.setText(_translate("MainWindow", "APPLICATIONS"))
        self.application_filter_content_groupbox.setTitle(_translate("MainWindow", "Filters"))
        self.application_company_filter_label.setText(_translate("MainWindow", "Company:"))
        self.application_position_filter_label.setText(_translate("MainWindow", "Position:"))
        self.application_city_filter_label.setText(_translate("MainWindow", "City:"))
        self.application_state_filter_label.setText(_translate("MainWindow", "State:"))

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
            self.application_state_filter_combo_box.setItemText(index, _translate("MainWindow", us_states[index]))

        self.application_status_filter_groupbox.setTitle(_translate("MainWindow", "Status:"))
        self.application_submitted_checkbox.setText(_translate("MainWindow", "Application Submitted"))
        self.screening_interview_checkbox.setText(_translate("MainWindow", "Screening Interview"))
        self.technical_interview_checkbox.setText(_translate("MainWindow", "Technical Interview"))
        self.job_offer_check_box.setText(_translate("MainWindow", "Job Offer"))
        self.application_rejected_checkbox.setText(_translate("MainWindow", "Application Rejected"))
        self.apply_application_filters_button.setText(_translate("MainWindow", "Apply"))
        self.appications_table_widget.setSortingEnabled(True)
        item = self.appications_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Company"))
        item = self.appications_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Position"))
        item = self.appications_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        item = self.appications_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        item = self.appications_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.new_application_button.setText(_translate("MainWindow", "New Application"))
        self.view_application_button.setText(_translate("MainWindow", "View Application"))
        self.contacts_title.setText(_translate("MainWindow", "CONTACTS"))
        self.questions_title.setText(_translate("MainWindow", "QUESTIONS"))
        self.statistics_title.setText(_translate("MainWindow", "STATISTICS"))





    def show_applications_page(self):
         # Change page
        self.stackedWidget.setCurrentIndex(0)

        # Change application title frame's color
        self.application_title_frame.setStyleSheet(
            "background-color: rgb(25, 105, 170);\n"
            "color: rgb(220, 220, 220);"
        )

        # Change navagation's application button color
        self.applications_page_button.setStyleSheet(
            "background-color: rgb(33, 150, 243)"
        )

        # Revert unselected navagations' button colors
        self.contacts_page_button.setStyleSheet(
            ""
        )
        self.questions_page_button.setStyleSheet(
            ""
        )
        self.statistics_page_button.setStyleSheet(
            ""
        )

    def show_contacts_page(self):
        # Change page
        self.stackedWidget.setCurrentIndex(1)

        # Change application title frame's color
        self.application_title_frame.setStyleSheet(
            "background-color: rgb(137, 28, 48);\n"
            "color: rgb(220, 220, 220);"
        )

        # Change navagation's contact button color
        self.contacts_page_button.setStyleSheet(
            "background-color: rgb(196, 46, 68)"
        )

        # Revert unselected navagations' button colors
        self.applications_page_button.setStyleSheet(
            ""
        )
        self.questions_page_button.setStyleSheet(
            ""
        )
        self.statistics_page_button.setStyleSheet(
            ""
        )

    def show_questions_page(self):
        # Change page
        self.stackedWidget.setCurrentIndex(2)

        # Change application title frame's color
        self.application_title_frame.setStyleSheet(
            "background-color: rgb(44, 58, 130);\n"
            "color: rgb(220, 220, 220);"
        )

        # Change navagation's question button color
        self.questions_page_button.setStyleSheet(
            "background-color: rgb(59, 84, 188)"
        )

        # Revert unselected navagations' button colors
        self.applications_page_button.setStyleSheet(
            ""
        )
        self.contacts_page_button.setStyleSheet(
            ""
        )
        self.statistics_page_button.setStyleSheet(
            ""
        )

    def show_statistics_page(self):
        # Change page
        self.stackedWidget.setCurrentIndex(3)

        # Change application title frame's color
        self.application_title_frame.setStyleSheet(
            "background-color: rgb(172, 58, 32);\n"
            "color: rgb(220, 220, 220);"
        )

        # Change navagation's question button color
        self.statistics_page_button.setStyleSheet(
            "background-color: rgb(247, 84, 48)"
        )

        # Revert unselected navagations' button colors
        self.applications_page_button.setStyleSheet(
            ""
        )
        self.contacts_page_button.setStyleSheet(
            ""
        )
        self.questions_page_button.setStyleSheet(
            ""
        )

    def populate_applications_table(self):
        connection = sqlite3.connect("data/JobApplicationVault_database.db")
        cur = connection.cursor()

        # Set the table widget's row count to the amount of records in the job_applications table
        cur.execute("SELECT COUNT(*) FROM job_applications")
        row_count = cur.fetchone()[0]
        self.appications_table_widget.setRowCount(row_count)
        
        tablerow = 0
        sqlquery = """
            SELECT
                ja.company,
                ja.position,
                ja.city,
                ja.state,
                as1.status,
                date(as1.julian_date)
            FROM
                job_applications ja
            JOIN
                application_statuses as1 ON ja.job_application_id = as1.job_application_id
            WHERE
                as1.julian_date = (
                    SELECT
                        MAX(as2.julian_date)
                    FROM
                        application_statuses as2
                    WHERE
                        as2.job_application_id = ja.job_application_id
            );
        """
        
        for row in cur.execute(sqlquery):
            company, position, city, state, status, date = row
            location = f"{city}, {state}"
        #   self.appications_table_widget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.appications_table_widget.setItem(tablerow, 0, QTableWidgetItem(company))
            self.appications_table_widget.setItem(tablerow, 1, QTableWidgetItem(position))
            self.appications_table_widget.setItem(tablerow, 2, QTableWidgetItem(location))
            self.appications_table_widget.setItem(tablerow, 3, QTableWidgetItem(status))
            self.appications_table_widget.setItem(tablerow, 4, QTableWidgetItem(date))
            tablerow += 1

        # Close the database connection
        connection.close()
    
    def openNewApplication(self):
        self.dialog = QDialog()
        self.dialog.setWindowFlags(self.dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.ui_app_dialog = Ui_NewApplication_Dialog()
        self.ui_app_dialog.setupUi(self.dialog)
        self.ui_app_dialog.create_button.clicked.connect(self.on_create_button_clicked)
        self.dialog.show()

    def on_create_button_clicked(self):
        company = self.ui_app_dialog.company_line_edit.text()
        city = self.ui_app_dialog.city_line_edit.text()
        state = self.ui_app_dialog.state_combo_box.currentText()
        position = self.ui_app_dialog.position_line_edit.text()
        work_style = self.ui_app_dialog.work_style_combo_box.currentText()
        employment_status = self.ui_app_dialog.employment_status_combo_box.currentText()
        job_description = self.ui_app_dialog.job_description_plain_text_edit.toPlainText()
        application_date = self.ui_app_dialog.application_status_date_edit.date()

        # validate required inputs
        if len(company) == 0:
            self.ui_app_dialog.error_label.setText("Missing a company!")
        elif len(city) == 0:
            self.ui_app_dialog.error_label.setText("Missing a city!")
        elif state == "-":
            self.ui_app_dialog.error_label.setText("Missing a state!")
        elif len(position) == 0:
            self.ui_app_dialog.error_label.setText("Missing a position!")
        elif work_style == "-":
            self.ui_app_dialog.error_label.setText("Missing a work-style!")
        elif employment_status == "-":
            self.ui_app_dialog.error_label.setText("Missing an employment status!")
        elif application_date.toString('yyyy-MM-dd') == "2024-01-01":
            self.ui_app_dialog.error_label.setText("Missing a date!")
        else:
            # Connect to SQLite database
            conn = sqlite3.connect('data/JobApplicationVault_database.db')
            cursor = conn.cursor()

            # Insert data into job_applications table
            cursor.execute('''INSERT INTO job_applications (company, position, work_style, employment_status, city, state, job_description)
                            VALUES (?, ?, ?, ?, ?, ?, ?)''', (company, position, work_style, employment_status, city, state, job_description))

            # Get the last inserted row id (job_application_id) for referencing in application_statuses table
            job_application_id = cursor.lastrowid

            # Insert data into application_statuses table
            cursor.execute('''INSERT INTO application_statuses (job_application_id, status, julian_date)
                            VALUES (?, ?, ?)''', (job_application_id, 'Application Submitted', application_date.toJulianDay()))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            # Update the Application's table
            self.populate_applications_table()

            # Close the dialog window
            self.dialog.accept()

    def openViewApplication(self):
        # Get the index of the currently selected row
        selected_row = self.appications_table_widget.currentRow()
        # Check if a valid row is selected
        if selected_row >= 0:
            # Show the dialog
            self.dialog = QDialog()
            self.dialog.setWindowFlags(self.dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            self.ui_app_dialog = Ui_ViewApplication_Dialog()
            self.ui_app_dialog.setupUi(self.dialog)
            self.ui_app_dialog.add_skill_button.clicked.connect(lambda: self.onAddSkillsButtonClicked(job_application_id))
            self.ui_app_dialog.add_contact_button.clicked.connect(lambda: self.addContact(job_application_id))
            self.dialog.show()

            # Retrieve data from the selected row
            company, position, location, application_status, application_date = [self.appications_table_widget.item(selected_row, col).text() for col in range(self.appications_table_widget.columnCount())]
            city, state = location.split(", ")

            # Connect to SQLite database
            conn = sqlite3.connect('data/JobApplicationVault_database.db')
            cursor = conn.cursor()

            # Select the primary key
            job_application_id_query = cursor.execute('''
                    SELECT job_application_id
                    FROM job_applications
                    WHERE company = ? AND position = ? AND city = ? AND state = ?;
                ''', (company, position, city, state)
            )

            # Fetch the result
            job_application_id_result = job_application_id_query.fetchone()

            if job_application_id_result:
                job_application_id = job_application_id_result[0]

                # Connect to SQLite database
                conn = sqlite3.connect('data/JobApplicationVault_database.db')
                cursor = conn.cursor()

                # Retrieve job application details
                job_application_query = cursor.execute('''
                    SELECT * FROM job_applications WHERE job_application_id = ?;
                ''', (job_application_id,))

                job_application_data = job_application_query.fetchone()

                # Retrieve technical skills
                technical_skills_query = cursor.execute('''
                    SELECT skill_name FROM technical_skills
                    INNER JOIN job_application_technical_skills ON
                    technical_skills.technical_skill_id = job_application_technical_skills.technical_skill_id
                    WHERE job_application_technical_skills.job_application_id = ?;
                ''', (job_application_id,))

                technical_skills = [row[0] for row in technical_skills_query.fetchall()]

                # Retrieve contacts
                contacts_query = cursor.execute('''
                    SELECT position, first_name, last_name, email, phone FROM contacts
                    WHERE job_application_id = ?;
                ''', (job_application_id,))

                contacts_data = contacts_query.fetchall()

                # Retrieve application status history
                status_history_query = cursor.execute('''
                    SELECT status, date(julian_date) FROM application_statuses
                    WHERE job_application_id = ? ORDER BY julian_date DESC;
                ''', (job_application_id,))

                status_history_data = status_history_query.fetchall()

                # Commit the changes and close the connection
                conn.commit()
                conn.close()

                # Populate PyQt5 containers
                self.ui_app_dialog.company_line_edit.setText(job_application_data[1])
                self.ui_app_dialog.city_line_edit.setText(job_application_data[5])
                self.ui_app_dialog.state_line_edit.setText(job_application_data[6])
                self.ui_app_dialog.position_line_edit.setText(job_application_data[2])
                self.ui_app_dialog.work_style_line_edit.setText(job_application_data[3])
                self.ui_app_dialog.employment_status_line_edit.setText(job_application_data[4])
                self.ui_app_dialog.job_description_plain_text_edit.setPlainText(job_application_data[7])

                # Populate skills_table
                self.ui_app_dialog.skills_table.setRowCount(len(technical_skills))
                for row, skill in enumerate(technical_skills):
                    self.ui_app_dialog.skills_table.setItem(row, 0, QTableWidgetItem(skill))

                # Populate contact_table_widget
                self.ui_app_dialog.contact_table_widget.setRowCount(len(contacts_data))
                for row, contact in enumerate(contacts_data):
                    for col, value in enumerate(contact):
                        self.ui_app_dialog.contact_table_widget.setItem(row, col, QTableWidgetItem(str(value)))

                # Populate application_status_history_table_widget
                self.ui_app_dialog.application_status_history_table_widget.setRowCount(len(status_history_data))
                for row, status_data in enumerate(status_history_data):
                    for col, value in enumerate(status_data):
                        self.ui_app_dialog.application_status_history_table_widget.setItem(row, col, QTableWidgetItem(str(value)))

    def onAddSkillsButtonClicked(self, job_application_id):
        skill_value = self.ui_app_dialog.add_skill_line_edit.text()
        if len(skill_value) == 0:
            # User inputted a value
            self.ui_app_dialog.skill_error_label.setText("Missing a skill!")
        else:
            # Connect to SQLite database
            conn = sqlite3.connect('data/JobApplicationVault_database.db')
            cursor = conn.cursor()

            try:
                # Check if the skill already exists in the technical_skills table
                existing_skill_query = cursor.execute('''
                    SELECT technical_skill_id FROM technical_skills WHERE skill_name = ?;
                ''', (skill_value,))
                
                existing_skill_result = existing_skill_query.fetchone()

                if existing_skill_result:
                    # Skill already exists, get the skill_id
                    skill_id = existing_skill_result[0]
                else:
                    # Skill doesn't exist, insert into technical_skills table
                    cursor.execute('''
                        INSERT INTO technical_skills (skill_name, occurrences) VALUES (?, 1);
                    ''', (skill_value,))
                    skill_id = cursor.lastrowid

                # Link the skill to the current job application
                cursor.execute('''
                    INSERT INTO job_application_technical_skills (job_application_id, technical_skill_id)
                    VALUES (?, ?);
                ''', (job_application_id, skill_id))

                # Commit the changes
                conn.commit()
                conn.close()

                # Clear the error label
                self.ui_app_dialog.skill_error_label.clear()

                # Update skills_table
                self.updateSkillsTable(job_application_id)

            except Exception:
                self.ui_app_dialog.skill_error_label.setText(f"{skill_value} skill already exists!")
                conn.rollback()
                conn.close()
                
    def updateSkillsTable(self, job_application_id):
        # Update the skills_table with the latest data from the database
        conn = sqlite3.connect('data/JobApplicationVault_database.db')
        cursor = conn.cursor()

        # Retrieve technical skills
        technical_skills_query = cursor.execute('''
            SELECT skill_name FROM technical_skills
            INNER JOIN job_application_technical_skills ON
            technical_skills.technical_skill_id = job_application_technical_skills.technical_skill_id
            WHERE job_application_technical_skills.job_application_id = ?;
        ''', (job_application_id,))

        technical_skills = [row[0] for row in technical_skills_query.fetchall()]

        # Close the connection
        conn.close()

        # Update PyQt5 container
        self.ui_app_dialog.skills_table.setRowCount(len(technical_skills))
        for row, skill in enumerate(technical_skills):
            self.ui_app_dialog.skills_table.setItem(row, 0, QTableWidgetItem(skill))
        
    def addContact(self, job_application_id):
        # Get the values from the input fields
        position = self.ui_app_dialog.contact_position_line_edit.text()
        first_name = self.ui_app_dialog.contact_first_name_line_edit.text()
        last_name = self.ui_app_dialog.contact_last_name_line_edit.text()
        phone = self.ui_app_dialog.contact_phone_line_edit.text()
        email = self.ui_app_dialog.contact_email_line_edit.text()

        # Check if either first name or last name is empty
        if not first_name:
            self.ui_app_dialog.contact_error_label.setText("Enter a first name!")
            return
        elif not last_name:
            self.ui_app_dialog.contact_error_label.setText("Enter a last name!")
            return
        else:
            # Connect to SQLite database
            conn = sqlite3.connect('data/JobApplicationVault_database.db')
            cursor = conn.cursor()

            try:
                # Check if the contact with the same first name and last name already exists for this job application
                existing_contact_query = cursor.execute('''
                    SELECT contact_id FROM contacts
                    WHERE job_application_id = ? AND first_name = ? AND last_name = ?;
                ''', (job_application_id, first_name, last_name))

                existing_contact_id = existing_contact_query.fetchone()

                if existing_contact_id:
                    raise ValueError("Contact with the same first name and last name already exists for this job application.")

                # Insert contact into the database
                cursor.execute('''
                    INSERT INTO contacts (position, first_name, last_name, phone, email, job_application_id)
                    VALUES (?, ?, ?, ?, ?, ?);
                ''', (position, first_name, last_name, phone, email, job_application_id))

                # Commit the changes
                conn.commit()
                conn.close()

                # Update the contact_table_widget
                self.updateContactTableWidget(job_application_id)

                # Clear the input fields
                self.ui_app_dialog.contact_position_line_edit.clear()
                self.ui_app_dialog.contact_first_name_line_edit.clear()
                self.ui_app_dialog.contact_last_name_line_edit.clear()
                self.ui_app_dialog.contact_phone_line_edit.clear()
                self.ui_app_dialog.contact_email_line_edit.clear()
                self.ui_app_dialog.contact_error_label.clear()
            except Exception:
                self.ui_app_dialog.contact_error_label.setText(f"{first_name} {last_name} is already a contact!")
                conn.rollback()
                conn.close()

    def updateContactTableWidget(self, job_application_id):
        conn = sqlite3.connect('data/JobApplicationVault_database.db')
        cursor = conn.cursor()

        contacts_query = cursor.execute('''
            SELECT position, first_name, last_name, email, phone FROM contacts
            WHERE job_application_id = ?;
        ''', (job_application_id,))

        contacts_data = contacts_query.fetchall()

        # Close the connection
        conn.close()

        # Update contact_table_widget
        self.ui_app_dialog.contact_table_widget.setRowCount(len(contacts_data))
        for row, contact in enumerate(contacts_data):
            for col, value in enumerate(contact):
                self.ui_app_dialog.contact_table_widget.setItem(row, col, QTableWidgetItem(str(value)))
