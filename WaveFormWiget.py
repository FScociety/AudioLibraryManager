from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import time

class WaveForm(QtWidgets.QWidget):
    _bar_distance = 1
    _clamp = 1

    def __init__(self, *args, **kwargs):
        super(WaveForm, self).__init__(*args, **kwargs)
        self._data = []

    def plot(self, data):
        self._data = data

        max = 0
        for n in self._data:
            if n > max:
                max = n

        self._highest_point = max

        self.update()


    def paintEvent(self, e):
        _time = time.time()

        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setStyle(Qt.SolidPattern)

        # Render WaveForm
        if (len(self._data) != 0):
            barWidth = painter.device().width() / len(self._data)

            brush.setColor(QtGui.QColor("White"))

            steps = len(self._data) / painter.device().width()
            steps *= self._bar_distance
            steps = round(steps)
            i = 0
            i_temp = 0
            smooth_n = 0

            for n in self._data:
                smooth_n += n

                if i_temp >= steps:
                    i_temp = 0
                    smooth_n /= steps

                    fixed_height = smooth_n / self._highest_point * painter.device().height() / 1.8
                    if fixed_height <= self._clamp and fixed_height >= -self._clamp:
                        fixed_height = self._clamp
                    bar = QtCore.QRect(barWidth * i, painter.device().height() / 2 - fixed_height / 2, barWidth + 1, fixed_height)
                    painter.fillRect(bar, brush)
            
                i += 1
                i_temp += 1

            painter.end()

            print("Rendering took", time.time() - _time, "for", i / steps, "elements")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    waveForm = WaveForm()
    waveForm.show()
    app.exec_()