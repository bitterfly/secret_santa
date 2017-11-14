from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import sys

import santa_design
import show_results
import santa

class SantaDesignClass(QtWidgets.QMainWindow, santa_design.Ui_MainWindow):
    def __init__(self, people, couples, names, parent=None):
        super(SantaDesignClass, self).__init__(parent)

        self.setupUi(self)
        self.afterGeneration = ShowResultsWidget(names)
        self.people = people
        self.couples = couples
        self.names = names

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
    def __init__(self, names, parent=None):
        super(ShowResultsWidget, self).__init__(parent)
        self.setupUi(self)
        self.santas = []
        self.names = names
        self.btnSure.hide()
        self.lblSanta.hide()

        self.wgtParticipants.itemDoubleClicked.connect(self.choose_participant)
        self.btnSure.clicked.connect(self.show_santa)

        self.btnClean.clicked.connect(self.clean_screen)

    def clean_screen(self):
        self.lblSanta.hide()
        self.btnSure.hide()

    def show_santa(self):
        self.lblSanta.setText("%s,\nтрябва да купиш подарък на\n%s" % (self.current_name, self.current_santa))
        self.lblSanta.adjustSize()
        self.lblSanta.show()

    def set_santas(self, santas):
        self.santas = santas
        self.names_in_list_view = list(self.santas.keys())

        for i in self.names_in_list_view:
            item = QListWidgetItem(self.names[i])
            self.wgtParticipants.addItem(item)

    def choose_participant(self, item):
        index = self.wgtParticipants.row(item)
        short_name = self.names_in_list_view[index]
        name = self.names[short_name]
        self.btnSure.setText("Сигурен ли си,\nче си %s?" % name)
        self.btnSure.show()

        self.current_name = name
        self.current_santa = self.names[self.santas[short_name]]

        # print(short_name, self.current_name, self.current_santa)


def main():
    Names = {"a": "Ани", "d": "Додо", "r": "Рали", "g": "Георги", "z":"Звезди", "h": "Христо", "v": "Велин"}
    People = list(Names.keys())
    Couples = ["ad", "hr"]

    app = QtWidgets.QApplication(sys.argv)
    form = SantaDesignClass(People, Couples, Names)
    form.show()
    app.exec_()



if __name__ == "__main__":
    main()

