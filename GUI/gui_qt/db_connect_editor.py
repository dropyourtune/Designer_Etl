# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_connect_editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(877, 432)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(210, 20, 371, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 351, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_dbtype = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.lineEdit_dbtype.setObjectName("lineEdit_dbtype")
        self.horizontalLayout_6.addWidget(self.lineEdit_dbtype)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_dbtype = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbtype.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbtype.setObjectName("label_dbtype")
        self.horizontalLayout_17.addWidget(self.label_dbtype)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_dbhost = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbhost.setReadOnly(False)
        self.lineEdit_dbhost.setObjectName("lineEdit_dbhost")
        self.horizontalLayout_7.addWidget(self.lineEdit_dbhost)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_dbHost = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbHost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbHost.setObjectName("label_dbHost")
        self.horizontalLayout_18.addWidget(self.label_dbHost)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_18)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_dbuser = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbuser.setReadOnly(False)
        self.lineEdit_dbuser.setObjectName("lineEdit_dbuser")
        self.horizontalLayout_8.addWidget(self.lineEdit_dbuser)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_dbUser = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbUser.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbUser.setObjectName("label_dbUser")
        self.horizontalLayout_19.addWidget(self.label_dbUser)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_dbpass = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbpass.setReadOnly(False)
        self.lineEdit_dbpass.setObjectName("lineEdit_dbpass")
        self.horizontalLayout_9.addWidget(self.lineEdit_dbpass)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_dbPass = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbPass.setObjectName("label_dbPass")
        self.horizontalLayout_20.addWidget(self.label_dbPass)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_dbbase = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbbase.setReadOnly(False)
        self.lineEdit_dbbase.setObjectName("lineEdit_dbbase")
        self.horizontalLayout_10.addWidget(self.lineEdit_dbbase)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_dbBase = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbBase.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbBase.setObjectName("label_dbBase")
        self.horizontalLayout_21.addWidget(self.label_dbBase)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.dbSchema = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.dbSchema.setObjectName("dbSchema")
        self.horizontalLayout_16.addWidget(self.dbSchema)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.dbSchema_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.dbSchema_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dbSchema_2.setObjectName("dbSchema_2")
        self.horizontalLayout_22.addWidget(self.dbSchema_2)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_22)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_dbport = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_dbport.setReadOnly(False)
        self.lineEdit_dbport.setObjectName("lineEdit_dbport")
        self.horizontalLayout_11.addWidget(self.lineEdit_dbport)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_dbPort = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_dbPort.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_dbPort.setObjectName("label_dbPort")
        self.horizontalLayout_23.addWidget(self.label_dbPort)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_23)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_chose_loadMode = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_chose_loadMode.setObjectName("comboBox_chose_loadMode")
        self.horizontalLayout_2.addWidget(self.comboBox_chose_loadMode)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_loadMode = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_loadMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_loadMode.setObjectName("label_loadMode")
        self.horizontalLayout_24.addWidget(self.label_loadMode)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_target_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_target_name.setObjectName("lineEdit_target_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_target_name)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_receiver = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_receiver.setObjectName("label_receiver")
        self.horizontalLayout_14.addWidget(self.label_receiver)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.pushButton_Open = QtWidgets.QPushButton(Form)
        self.pushButton_Open.setGeometry(QtCore.QRect(640, 20, 112, 32))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton_Save = QtWidgets.QPushButton(Form)
        self.pushButton_Save.setGeometry(QtCore.QRect(640, 60, 112, 32))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_SaveAs = QtWidgets.QPushButton(Form)
        self.pushButton_SaveAs.setGeometry(QtCore.QRect(640, 100, 112, 32))
        self.pushButton_SaveAs.setObjectName("pushButton_SaveAs")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_dbtype.setText(_translate("Form", "dbtype"))
        self.label_dbHost.setText(_translate("Form", "dbHost"))
        self.label_dbUser.setText(_translate("Form", "dbUser"))
        self.label_dbPass.setText(_translate("Form", "dbPass"))
        self.label_dbBase.setText(_translate("Form", "dbBase"))
        self.dbSchema_2.setText(_translate("Form", "dbScheme"))
        self.label_dbPort.setText(_translate("Form", "dbPort"))
        self.label_loadMode.setText(_translate("Form", "Load Mode"))
        self.label_receiver.setText(_translate("Form", "Target table name"))
        self.pushButton_Open.setText(_translate("Form", "Open"))
        self.pushButton_Save.setText(_translate("Form", "Save"))
        self.pushButton_SaveAs.setText(_translate("Form", "Save As..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
