from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import santa_design
import show_results
import santa
import secret

class SantaDesignClass(QtWidgets.QMainWindow, santa_design.Ui_MainWindow):
    def __init__(self, people, couples, names, emails, parent=None):
        super(SantaDesignClass, self).__init__(parent)

        self.setupUi(self)
        self.afterGeneration = ShowResultsWidget(people, names, emails)
        self.people = people
        self.couples = couples
        self.names = names
        self.emails = emails

        self.setCentralWidget(self.buttonWidget)

        self.btnChooseSanta.clicked.connect(self.generate_santas)

        movie_dahser = QtGui.QMovie("dasher.gif")
        self.lblDasher.setMovie(movie_dahser)
        movie_dahser.setScaledSize(self.lblDasher.size())
        movie_dahser.start()

        movie_vixen = QtGui.QMovie("vixen.gif")
        self.lblVixen.setMovie(movie_vixen)
        movie_vixen.setScaledSize(self.lblVixen.size())
        movie_vixen.start()



    def generate_santas(self):
        santas = santa.get_santas(self.people, self.couples)
        # print(santas)
        self.afterGeneration.set_santas(santas)
        self.setCentralWidget(self.afterGeneration)

        return santas

class ShowResultsWidget(QtWidgets.QWidget, show_results.Ui_Form):
    def __init__(self, people, names, emails, parent=None):
        super(ShowResultsWidget, self).__init__(parent)
        self.setupUi(self)
        self.santas = []
        self.names = names
        self.people = people
        self.emails = emails
        self.lblSanta.hide()

        self.wgtParticipants.itemDoubleClicked.connect(self.choose_participant)

        self.btnShow.clicked.connect(self.show_santa)
        self.btnShow.hide()

        self.btnSend.clicked.connect(self.send_email)
        self.btnSend.hide()

        self.btnClean.clicked.connect(self.clean_screen)
        self.btnClean.hide()

    def clean_screen(self):
        self.lblSanta.hide()
        self.btnShow.hide()
        self.btnSend.hide()
        self.btnClean.hide()

    def set_mailing(self):
        receiver = self.emails[self.current_short_name]
        msg = self.make_email_message(receiver)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(secret.sender, secret.sender_password)

        server.sendmail(secret.sender, receiver, msg)

    def make_message(self):
        return "\n%s,\nтрябва да купиш подарък на %s\nЛимит за финанси: 25лв." % (self.current_name, self.current_santa)

    def make_email_message(self, receiver):
        msg = MIMEMultipart("alternative")
        msg["Sender"] = secret.sender
        msg["Receiver"] = receiver
        msg["Subject"] = 'Таен дядо'
        body = MIMEText(self.make_message(),
                 "plain", "utf-8")
        msg.attach(body)

        return msg.as_string().encode('ascii')


    def send_email(self):
        self.btnClean.show()
        self.set_mailing()
        self.lblSanta.setText("Email sent.")

    def show_santa(self):
        self.lblSanta.setText(self.make_message())
        self.lblSanta.adjustSize()
        self.lblSanta.show()
        self.btnClean.show()

    def set_santas(self, santas):
        self.santas = santas
        self.names_in_list_view = list(self.people)

        for i in self.names_in_list_view:
            item = QListWidgetItem(self.names[i])
            self.wgtParticipants.addItem(item)

    def choose_participant(self, item):
        index = self.wgtParticipants.row(item)
        short_name = self.names_in_list_view[index]
        name = self.names[short_name]

        self.lblSanta.setText("")
        self.btnShow.show()
        self.btnSend.show()
        self.lblSanta.show()



        self.current_name = name
        self.current_short_name = short_name
        self.current_santa = self.names[self.santas[short_name]]

        # print(short_name, self.current_name, self.current_santa)


def main():
    People = list(secret.Names.keys())

    app = QtWidgets.QApplication(sys.argv)
    form = SantaDesignClass(People, secret.Couples, secret.Names, secret.Emails)
    form.show()
    app.exec_()



if __name__ == "__main__":
    main()

