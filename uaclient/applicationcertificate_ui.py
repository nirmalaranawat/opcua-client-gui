# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uaclient\applicationcertificate_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApplicationCertificateDialog(object):
    def setupUi(self, ApplicationCertificateDialog):
        ApplicationCertificateDialog.setObjectName("ApplicationCertificateDialog")
        ApplicationCertificateDialog.resize(504, 164)
        self.gridLayout = QtWidgets.QGridLayout(ApplicationCertificateDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 3)
        self.privateKeyLabel = QtWidgets.QLabel(ApplicationCertificateDialog)
        self.privateKeyLabel.setObjectName("privateKeyLabel")
        self.gridLayout.addWidget(self.privateKeyLabel, 2, 0, 1, 2)
        self.privateKeyButton = QtWidgets.QPushButton(ApplicationCertificateDialog)
        self.privateKeyButton.setObjectName("privateKeyButton")
        self.gridLayout.addWidget(self.privateKeyButton, 2, 2, 1, 1)
        self.certificateLabel = QtWidgets.QLabel(ApplicationCertificateDialog)
        self.certificateLabel.setObjectName("certificateLabel")
        self.gridLayout.addWidget(self.certificateLabel, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(ApplicationCertificateDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.certificateButton = QtWidgets.QPushButton(ApplicationCertificateDialog)
        self.certificateButton.setObjectName("certificateButton")
        self.gridLayout.addWidget(self.certificateButton, 1, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ApplicationCertificateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(ApplicationCertificateDialog)
        self.buttonBox.accepted.connect(ApplicationCertificateDialog.accept)
        self.buttonBox.rejected.connect(ApplicationCertificateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ApplicationCertificateDialog)

    def retranslateUi(self, ApplicationCertificateDialog):
        _translate = QtCore.QCoreApplication.translate
        ApplicationCertificateDialog.setWindowTitle(_translate("ApplicationCertificateDialog", "ApplicationCertificateDialog"))
        self.privateKeyLabel.setText(_translate("ApplicationCertificateDialog", "None"))
        self.privateKeyButton.setText(_translate("ApplicationCertificateDialog", "Select private key"))
        self.certificateLabel.setText(_translate("ApplicationCertificateDialog", "None"))
        self.label_3.setText(_translate("ApplicationCertificateDialog", "Application Authentication Settings:"))
        self.certificateButton.setText(_translate("ApplicationCertificateDialog", "Select certificate"))
