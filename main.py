from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys

from library import Library
import config
from ui import Ui

music_libary = None
window = None

search_results = []

def init_library():
    global music_libary
    music_libary = Library(config.music_libaries[0])

def init_ui():
    app = QApplication(sys.argv)
    global window
    window = Ui()
    window.lineEdit.textChanged.connect(search)
    window.fileView.itemSelectionChanged.connect(itemSelectionChanged)
    window.show()
    sys.exit(app.exec_())

def itemSelectionChanged():
    row = window.fileView.currentRow()
    global music_libary
    
    if (row >= 0 and row < len(search_results)):
        select = search_results[row]
        select.printNames()

        # window.canvas.loadAudio(select)
        window.ploting(select)


def search(name):
    global search_results
    search_results = music_libary.search(name)
    length = len(search_results)
    window.fileView.setRowCount(length)

    for i in range(length):
        window.fileView.setItem(i, 0, QTableWidgetItem(search_results[i].file_name))
        window.fileView.setItem(i, 1, QTableWidgetItem(str(search_results[i].file_length)))
        window.fileView.setItem(i, 2, QTableWidgetItem(search_results[i].file_extension))
        window.fileView.setItem(i, 3, QTableWidgetItem(search_results[i].file_path))


if __name__ == '__main__':
    init_library()
    init_ui()