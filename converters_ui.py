# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converters.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_converters(object):
    def setupUi(self, converters):
        converters.setObjectName(_fromUtf8("converters"))
        converters.resize(1029, 530)
        self.verticalLayout = QtGui.QVBoxLayout(converters)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(converters)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.tw_converters = QtGui.QTableWidget(converters)
        self.tw_converters.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tw_converters.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tw_converters.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tw_converters.setObjectName(_fromUtf8("tw_converters"))
        self.tw_converters.setColumnCount(3)
        self.tw_converters.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tw_converters.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tw_converters.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tw_converters.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tw_converters)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_add_converter = QtGui.QPushButton(converters)
        self.pb_add_converter.setObjectName(_fromUtf8("pb_add_converter"))
        self.horizontalLayout.addWidget(self.pb_add_converter)
        self.pb_modify_converter = QtGui.QPushButton(converters)
        self.pb_modify_converter.setObjectName(_fromUtf8("pb_modify_converter"))
        self.horizontalLayout.addWidget(self.pb_modify_converter)
        self.pb_delete_converter = QtGui.QPushButton(converters)
        self.pb_delete_converter.setObjectName(_fromUtf8("pb_delete_converter"))
        self.horizontalLayout.addWidget(self.pb_delete_converter)
        self.pb_load_from_file = QtGui.QPushButton(converters)
        self.pb_load_from_file.setObjectName(_fromUtf8("pb_load_from_file"))
        self.horizontalLayout.addWidget(self.pb_load_from_file)
        self.pb_load_from_repo = QtGui.QPushButton(converters)
        self.pb_load_from_repo.setObjectName(_fromUtf8("pb_load_from_repo"))
        self.horizontalLayout.addWidget(self.pb_load_from_repo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(converters)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_converter_name = QtGui.QLineEdit(converters)
        self.le_converter_name.setObjectName(_fromUtf8("le_converter_name"))
        self.horizontalLayout_3.addWidget(self.le_converter_name)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(converters)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.le_converter_description = QtGui.QLineEdit(converters)
        self.le_converter_description.setObjectName(_fromUtf8("le_converter_description"))
        self.horizontalLayout_5.addWidget(self.le_converter_description)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(converters)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.pb_code_help = QtGui.QPushButton(converters)
        self.pb_code_help.setObjectName(_fromUtf8("pb_code_help"))
        self.verticalLayout_3.addWidget(self.pb_code_help)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.pteCode = QtGui.QPlainTextEdit(converters)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.pteCode.setFont(font)
        self.pteCode.setObjectName(_fromUtf8("pteCode"))
        self.horizontalLayout_2.addWidget(self.pteCode)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pb_save_converter = QtGui.QPushButton(converters)
        self.pb_save_converter.setObjectName(_fromUtf8("pb_save_converter"))
        self.verticalLayout_2.addWidget(self.pb_save_converter)
        self.pb_cancel_converter = QtGui.QPushButton(converters)
        self.pb_cancel_converter.setObjectName(_fromUtf8("pb_cancel_converter"))
        self.verticalLayout_2.addWidget(self.pb_cancel_converter)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pb_cancel_widget = QtGui.QPushButton(converters)
        self.pb_cancel_widget.setObjectName(_fromUtf8("pb_cancel_widget"))
        self.horizontalLayout_4.addWidget(self.pb_cancel_widget)
        self.pbOK = QtGui.QPushButton(converters)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout_4.addWidget(self.pbOK)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(converters)
        QtCore.QMetaObject.connectSlotsByName(converters)

    def retranslateUi(self, converters):
        converters.setWindowTitle(_translate("converters", "Time converters", None))
        self.label_4.setText(_translate("converters", "Converters", None))
        self.tw_converters.setSortingEnabled(True)
        item = self.tw_converters.horizontalHeaderItem(0)
        item.setText(_translate("converters", "Name", None))
        item = self.tw_converters.horizontalHeaderItem(1)
        item.setText(_translate("converters", "Description", None))
        item = self.tw_converters.horizontalHeaderItem(2)
        item.setText(_translate("converters", "Code", None))
        self.pb_add_converter.setText(_translate("converters", "Add new converter", None))
        self.pb_modify_converter.setText(_translate("converters", "Modify converter", None))
        self.pb_delete_converter.setText(_translate("converters", "Delete converter", None))
        self.pb_load_from_file.setText(_translate("converters", "Load converters from file", None))
        self.pb_load_from_repo.setText(_translate("converters", "Load converters from BORIS repository", None))
        self.label_2.setText(_translate("converters", "Name", None))
        self.label_3.setText(_translate("converters", "Description", None))
        self.label.setText(_translate("converters", "Python code", None))
        self.pb_code_help.setText(_translate("converters", "Help", None))
        self.pb_save_converter.setText(_translate("converters", "Save converter", None))
        self.pb_cancel_converter.setText(_translate("converters", "Cancel", None))
        self.pb_cancel_widget.setText(_translate("converters", "Cancel", None))
        self.pbOK.setText(_translate("converters", "OK", None))

