#!/usr/bin/python
# -*-coding:Utf-8 -*

import sys
import os
from PyQt4 import QtGui, QtCore
import random
import re
import requests

from functions import simpleChar


class Signing(QtGui.QDialog):

    def __init__(self, parent):

        super(Signing, self).__init__(parent)

        self.parent = parent

        self.initUI()
        self.defineSlots()


    def askQuestion(self):

        questions = [
                     ('What animal has a trunk ?', 'elephant'),
                     ('How many continents are there ?', '6'),
                     ('Where is Big Ben ?', 'london')
                    ]
        question = questions[random.randint(0, len(questions) - 1)]
        self.answer = question[1]

        return question[0]


    def defineSlots(self):

        """Establish the slots"""

        self.ok_button.clicked.connect(self.validateForm)


    def validateForm(self):

        # http://sametmax.com/valider-une-adresse-email-avec-une-regex-en-python/

        validate = True

        email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)

        # if email_re.search(self.line_email.text()) is None:
            # self.line_email.setStyleSheet('QLineEdit {background-color: #FFA07A}')
            # validate = False
        # else:
            # self.line_email.setStyleSheet(None)

        # user_answer = simpleChar(self.line_question.text())

        # if self.combo_status.currentIndex() == 0:
            # self.combo_status.setStyleSheet('QComboBox {background-color: #FFA07A}')
            # validate = False
        # else:
            # self.combo_status.setStyleSheet(None)

        # if user_answer != self.answer:
            # self.line_question.setStyleSheet('QLineEdit {background-color: #FFA07A}')
            # validate = False
            # self.form_sign.labelForField(self.line_question).setText(self.askQuestion())
        # else:
            # self.line_question.setStyleSheet(None)


        if validate:
            # payload = {
                       # 'status': self.combo_status.currentText(),
                       # 'email': self.line_email.text(),
                       # 'user_id': None
                      # }
            payload = {
                       'status': 'student',
                       'email': 'jp@um2.fr',
                       'user_id': None
                      }
            # r = requests.post("http://chembrows.com/cgi-bin/test.py", params=payload)
            r = requests.post("http://127.0.0.1:8000/cgi-bin/test.py", data=payload)


            print(r.text)

            self.parent.fen_signing.close()
            del self.parent.fen_signing


    def initUI(self):

        """Handles the display"""

        self.parent.fen_signing = QtGui.QWidget()
        self.parent.fen_signing.setWindowTitle('Signing up')

        self.combo_status = QtGui.QComboBox()
        self.combo_status.addItem(None)
        self.combo_status.addItem("Student")
        self.combo_status.addItem("PhD student")
        self.combo_status.addItem("Post doc")
        self.combo_status.addItem("Researcher")
        self.combo_status.addItem("Professor")
        self.combo_status.addItem("Obi Wan Kenobi")

        self.form_sign = QtGui.QFormLayout()

        self.form_sign.addRow("What are you? :", self.combo_status)

        self.line_email = QtGui.QLineEdit(self)


        self.form_sign.addRow("Email :", self.line_email)

        self.line_question = QtGui.QLineEdit()
        self.line_question.setPlaceholderText("Prove you are human !")
        self.form_sign.addRow(self.askQuestion(), self.line_question)

        self.ok_button = QtGui.QPushButton("OK", self)
        self.cancel_button = QtGui.QPushButton("Cancel", self)

        self.hbox_buttons = QtGui.QHBoxLayout()
        self.vbox_global = QtGui.QVBoxLayout()

        self.hbox_buttons.addWidget(self.cancel_button)
        self.hbox_buttons.addWidget(self.ok_button)

        self.vbox_global.addLayout(self.form_sign)
        self.vbox_global.addLayout(self.hbox_buttons)

        self.parent.fen_signing.setLayout(self.vbox_global)
        self.parent.fen_signing.show()



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    parent = QtGui.QWidget()
    obj = Signing(parent)
    sys.exit(app.exec_())