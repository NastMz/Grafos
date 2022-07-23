# Form implementation generated from reading ui file '.\Qt\MainWindowView.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindowView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 570)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(56, 58, 89);\n"
"    width: 10px;\n"
"    margin: 10px 0 10px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(254, 121, 199);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(98, 114, 164);\n"
"    height: 10px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(98, 114, 164);\n"
"    height: 10px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,  QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,  QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"/* Horizontal */\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color:  rgb(56, 58, 89);\n"
"    height: 10px;\n"
"    margin: 0 10px 0 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(254, 121, 199);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(98, 114, 164);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(98, 114, 164);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,  QScrollBar::down-arrow:horizontal{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,  QScrollBar::sub-page:horizontal{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 11, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}    ")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_header = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_header.setStyleSheet("QFrame{\n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(56, 58, 89);\n"
"    border-radius: 20px;\n"
"    color: rgb(98, 114, 164);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(254, 121, 199);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout_3.setContentsMargins(25, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_header)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(581, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_btns = QtWidgets.QFrame(self.frame_header)
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.minimize_btn = QtWidgets.QPushButton(self.frame_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.minimize_btn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_btn.setFont(font)
        self.minimize_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minimize_btn.setAutoDefault(True)
        self.minimize_btn.setObjectName("minimize_btn")
        self.horizontalLayout_8.addWidget(self.minimize_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame_btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.close_btn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_8.addWidget(self.close_btn)
        self.horizontalLayout_3.addWidget(self.frame_btns)
        self.verticalLayout_2.addWidget(self.frame_header)
        self.frame_body = QtWidgets.QFrame(self.dropShadowFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_body.sizePolicy().hasHeightForWidth())
        self.frame_body.setSizePolicy(sizePolicy)
        self.frame_body.setMaximumSize(QtCore.QSize(780, 460))
        self.frame_body.setStyleSheet("background-color: rgb(67, 69, 106)")
        self.frame_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_body.setObjectName("frame_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_sidebar = QtWidgets.QFrame(self.frame_body)
        self.frame_sidebar.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_sidebar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_sidebar.setStyleSheet("QFrame {\n"
"    background-color: rgb(56, 58, 89);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(98, 114, 164);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(254, 121, 199);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_sidebar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_sidebar.setObjectName("frame_sidebar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_sidebar)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.matrix_btn = QtWidgets.QPushButton(self.frame_sidebar)
        self.matrix_btn.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.matrix_btn.setFont(font)
        self.matrix_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.matrix_btn.setFlat(False)
        self.matrix_btn.setObjectName("matrix_btn")
        self.verticalLayout_3.addWidget(self.matrix_btn)
        self.list_btn = QtWidgets.QPushButton(self.frame_sidebar)
        self.list_btn.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_btn.setFont(font)
        self.list_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.list_btn.setObjectName("list_btn")
        self.verticalLayout_3.addWidget(self.list_btn)
        self.graph_btn = QtWidgets.QPushButton(self.frame_sidebar)
        self.graph_btn.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graph_btn.setFont(font)
        self.graph_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.graph_btn.setObjectName("graph_btn")
        self.verticalLayout_3.addWidget(self.graph_btn)
        self.route_btn = QtWidgets.QPushButton(self.frame_sidebar)
        self.route_btn.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.route_btn.setFont(font)
        self.route_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.route_btn.setObjectName("route_btn")
        self.verticalLayout_3.addWidget(self.route_btn)
        self.horizontalLayout.addWidget(self.frame_sidebar)
        self.frame_content = QtWidgets.QFrame(self.frame_body)
        self.frame_content.setStyleSheet("QStackedWidget{\n"
"    background-color: rgb(67, 69, 106)\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(67, 69, 106);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(254, 121, 199);\n"
"    padding: 20px;\n"
"}")
        self.frame_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        font = QtGui.QFont()
        font.setKerning(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.matrix_page = QtWidgets.QWidget()
        self.matrix_page.setObjectName("matrix_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.matrix_page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.matrix_page)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.matrix_page)
        self.frame_2.setMaximumSize(QtCore.QSize(630, 410))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_widget = QtWidgets.QTableWidget(self.frame_2)
        self.table_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.table_widget.setFont(font)
        self.table_widget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.table_widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.table_widget.setAutoFillBackground(False)
        self.table_widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(98, 114, 164);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(56, 58, 89);\n"
"    padding: 4px;\n"
"    border: 1px solid rgb(67, 69, 106);\n"
"    font-size: 14pt;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: rgb(67, 69, 106);\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(56, 58, 89);\n"
"    border: 1px solidrgb(67, 69, 106);\n"
"}\n"
"")
        self.table_widget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.table_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.table_widget.setLineWidth(0)
        self.table_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_widget.setProperty("showDropIndicator", False)
        self.table_widget.setDragDropOverwriteMode(False)
        self.table_widget.setAlternatingRowColors(False)
        self.table_widget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_widget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.table_widget.setShowGrid(True)
        self.table_widget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.table_widget.setWordWrap(True)
        self.table_widget.setCornerButtonEnabled(False)
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(5)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.horizontalHeader().setVisible(True)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget.horizontalHeader().setDefaultSectionSize(30)
        self.table_widget.horizontalHeader().setMinimumSectionSize(0)
        self.table_widget.verticalHeader().setVisible(True)
        self.table_widget.verticalHeader().setCascadingSectionResizes(False)
        self.table_widget.verticalHeader().setDefaultSectionSize(30)
        self.table_widget.verticalHeader().setHighlightSections(True)
        self.table_widget.verticalHeader().setMinimumSectionSize(0)
        self.horizontalLayout_4.addWidget(self.table_widget)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.stackedWidget.addWidget(self.matrix_page)
        self.list_page = QtWidgets.QWidget()
        self.list_page.setObjectName("list_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.list_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.list_page)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.list_page)
        self.frame_3.setMaximumSize(QtCore.QSize(630, 410))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(40, 15, 40, 15)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("color: rgb(98, 114, 164);\n"
"background-color: rgb(56, 58, 89);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.listWidget.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 9)
        self.stackedWidget.addWidget(self.list_page)
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.graph_page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.graph_page)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.graph_img = QtWidgets.QVBoxLayout()
        self.graph_img.setContentsMargins(30, 15, 30, 30)
        self.graph_img.setSpacing(0)
        self.graph_img.setObjectName("graph_img")
        self.verticalLayout_6.addLayout(self.graph_img)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 9)
        self.stackedWidget.addWidget(self.graph_page)
        self.route_page = QtWidgets.QWidget()
        self.route_page.setObjectName("route_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.route_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.route_frame = QtWidgets.QFrame(self.route_page)
        self.route_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.route_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.route_frame.setObjectName("route_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.route_frame)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.route_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.route_container = QtWidgets.QFrame(self.route_frame)
        self.route_container.setStyleSheet("QLineEdit{\n"
"    border:0;\n"
"    font-size: 14px;\n"
"    background-color: rgb(56, 58, 89);\n"
"    font-family: Roboto;\n"
"    color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"    border:0;\n"
"    font-size: 14px;\n"
"    background-color: rgb(56, 58, 89);\n"
"    font-family: Roboto;\n"
"    color: rgb(254, 121, 199);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(254, 121, 199);\n"
"    color:#fff;\n"
"    border: none;\n"
"     border-radius: 15px;\n"
"    font-weight: Bold;\n"
"    font-family: Roboto Black;\n"
"    min-width: 100px;\n"
"    min-height: 30px;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(214,101,169);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font-weight: Bold\n"
"}")
        self.route_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.route_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.route_container.setObjectName("route_container")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.route_container)
        self.verticalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.form_container_frame = QtWidgets.QFrame(self.route_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_container_frame.sizePolicy().hasHeightForWidth())
        self.form_container_frame.setSizePolicy(sizePolicy)
        self.form_container_frame.setStyleSheet("")
        self.form_container_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.form_container_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.form_container_frame.setObjectName("form_container_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.form_container_frame)
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.form_frame = QtWidgets.QFrame(self.form_container_frame)
        self.form_frame.setStyleSheet("QLabel {\n"
"    padding: 2px;\n"
"}")
        self.form_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.form_frame.setObjectName("form_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.form_frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.from_frame = QtWidgets.QFrame(self.form_frame)
        self.from_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.from_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.from_frame.setObjectName("from_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.from_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_frame = QtWidgets.QFrame(self.from_frame)
        self.label_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.label_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.label_frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.from_option = QtWidgets.QComboBox(self.label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_option.sizePolicy().hasHeightForWidth())
        self.from_option.setSizePolicy(sizePolicy)
        self.from_option.setMinimumSize(QtCore.QSize(60, 0))
        self.from_option.setObjectName("from_option")
        self.horizontalLayout_6.addWidget(self.from_option)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_8.addWidget(self.label_frame)
        self.horizontalLayout_9.addWidget(self.from_frame)
        self.to_frame = QtWidgets.QFrame(self.form_frame)
        self.to_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.to_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.to_frame.setObjectName("to_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.to_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_frame_2 = QtWidgets.QFrame(self.to_frame)
        self.label_frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_frame_2.setObjectName("label_frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.label_frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.label_frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.to_option = QtWidgets.QComboBox(self.label_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_option.sizePolicy().hasHeightForWidth())
        self.to_option.setSizePolicy(sizePolicy)
        self.to_option.setMinimumSize(QtCore.QSize(60, 0))
        self.to_option.setObjectName("to_option")
        self.horizontalLayout_7.addWidget(self.to_option)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_9.addWidget(self.label_frame_2)
        self.horizontalLayout_9.addWidget(self.to_frame)
        self.frame = QtWidgets.QFrame(self.form_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_calculate = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_calculate.setObjectName("btn_calculate")
        self.verticalLayout_10.addWidget(self.btn_calculate)
        self.horizontalLayout_9.addWidget(self.frame)
        spacerItem4 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.form_frame)
        self.verticalLayout_12.addWidget(self.form_container_frame)
        self.img_container = QtWidgets.QFrame(self.route_container)
        self.img_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.img_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.img_container.setObjectName("img_container")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.img_container)
        self.verticalLayout_13.setContentsMargins(90, 0, 90, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.route_img = QtWidgets.QVBoxLayout()
        self.route_img.setContentsMargins(0, 0, 0, 0)
        self.route_img.setSpacing(0)
        self.route_img.setObjectName("route_img")
        self.verticalLayout_13.addLayout(self.route_img)
        self.verticalLayout_12.addWidget(self.img_container)
        self.route_info = QtWidgets.QFrame(self.route_container)
        self.route_info.setStyleSheet("QLabel {\n"
"    color: rgb(98, 114, 164);\n"
"    font-size: 14px;\n"
"    padding: 2px;\n"
"    font-weight: bold;\n"
"}")
        self.route_info.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.route_info.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.route_info.setObjectName("route_info")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.route_info)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_4 = QtWidgets.QFrame(self.route_info)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.route_label = QtWidgets.QLabel(self.frame_4)
        self.route_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.route_label.setObjectName("route_label")
        self.horizontalLayout_10.addWidget(self.route_label)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.route_text = QtWidgets.QLineEdit(self.frame_4)
        self.route_text.setEnabled(False)
        self.route_text.setAcceptDrops(False)
        self.route_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.route_text.setReadOnly(True)
        self.route_text.setObjectName("route_text")
        self.horizontalLayout_10.addWidget(self.route_text)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_14.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.route_info)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.weight_label = QtWidgets.QLabel(self.frame_5)
        self.weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weight_label.setObjectName("weight_label")
        self.horizontalLayout_11.addWidget(self.weight_label)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.weight_text = QtWidgets.QLineEdit(self.frame_5)
        self.weight_text.setEnabled(False)
        self.weight_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weight_text.setReadOnly(True)
        self.weight_text.setObjectName("weight_text")
        self.horizontalLayout_11.addWidget(self.weight_text)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_14.addWidget(self.frame_5)
        self.verticalLayout_12.addWidget(self.route_info)
        self.verticalLayout_12.setStretch(1, 10)
        self.verticalLayout_11.addWidget(self.route_container)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 9)
        self.verticalLayout_7.addWidget(self.route_frame)
        self.stackedWidget.addWidget(self.route_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_content)
        self.verticalLayout_2.addWidget(self.frame_body)
        self.horizontalLayout_2.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">GRAFOS</span> APP</p></body></html>"))
        self.minimize_btn.setText(_translate("MainWindow", "-"))
        self.close_btn.setText(_translate("MainWindow", "X"))
        self.matrix_btn.setText(_translate("MainWindow", "Matriz"))
        self.list_btn.setText(_translate("MainWindow", "Lista"))
        self.graph_btn.setText(_translate("MainWindow", "Grafo"))
        self.route_btn.setText(_translate("MainWindow", "Ruta mas corta"))
        self.label.setText(_translate("MainWindow", "Matriz de Adyacencia"))
        self.table_widget.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Lista de Adyacencia"))
        self.label_3.setText(_translate("MainWindow", "Grafo"))
        self.label_4.setText(_translate("MainWindow", "Ruta mas corta"))
        self.label_6.setText(_translate("MainWindow", "Desde:"))
        self.label_7.setText(_translate("MainWindow", "Hasta:"))
        self.btn_calculate.setText(_translate("MainWindow", "Calcular"))
        self.route_label.setText(_translate("MainWindow", "Ruta:"))
        self.weight_label.setText(_translate("MainWindow", "Peso:"))
