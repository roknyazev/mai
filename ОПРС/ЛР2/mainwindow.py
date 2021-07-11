from PyQt5.QtWidgets import *
import form
import pyqtgraph as pg
import Thread


class MainWindow(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread_instance = Thread.ThreadForIntegrator()
        Thread.sender.data.connect(self.upd)
        self.pushButton.clicked.connect(self.simulation)
        self.Slider_Precision.valueChanged.connect(self.upd_precision)
        self.Slider_Step.valueChanged.connect(self.upd_step)
        self.Slider_t0.valueChanged.connect(self.upd_t0)
        self.Slider_ft.valueChanged.connect(self.upd_ft)

        self.precision.setNum(1 / 10 ** self.Slider_Precision.value())
        self.step.setNum(self.Slider_Step.value() / 10000)
        self.t0.setNum(self.Slider_t0.value())
        self.ft.setNum(self.Slider_ft.value())

        self.widget = self.label
        self.widget.setLayout(QGridLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.plt1 = pg.plot()
        self.plt1.showGrid(x=False, y=False)
        #self.plt1.win.hide()
        self.plt1.setLabel('left', 'У1')
        self.plt1.setLabel('bottom', 'У2')
        self.plt1.addLegend()

        self.orbit = self.plt1.plot([0], [0], pen=pg.mkPen('w', width=3), name=' Орбита')

        self.widget.layout().addWidget(self.plt1, 0, 0)

        self.x = [[], []]

    def upd_precision(self):
        self.precision.setNum(1 / 10 ** self.Slider_Precision.value())

    def upd_step(self):
        self.step.setNum(self.Slider_Step.value() / 10000)

    def upd_t0(self):
        self.t0.setNum(self.Slider_t0.value())

    def upd_ft(self):
        self.ft.setNum(self.Slider_ft.value())

    def simulation(self):
        self.thread_instance.set_param(float(self.step.text()), float(self.precision.text()),
                                       float(self.t0.text()), float(self.ft.text()))
        self.thread_instance.start()

    def upd(self, data):
        self.time.setNum(data[0][len(data[0])-1])
        self.orbit.setData(data[1], data[2])
