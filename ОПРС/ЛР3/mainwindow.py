from PyQt5.QtWidgets import *
import form
import pyqtgraph as pg
import Thread


class MainWindow(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.thread_instance1 = Thread.ThreadForMathPend()
        Thread.sender1.data.connect(self.upd1)
        self.thread_instance2 = Thread.ThreadForIdMathPend()
        Thread.sender2.data.connect(self.upd2)
        self.thread_instance3 = Thread.ThreadForIdSpPend()
        Thread.sender3.data.connect(self.upd3)
        self.thread_instance4 = Thread.ThreadForSpPend()
        Thread.sender4.data.connect(self.upd4)

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
        self.plt1.setLabel('left', 'Угол')
        self.plt1.setLabel('bottom', 'Время')
        self.plt1.addLegend()
        self.graph1 = self.plt1.plot([0], [0], pen=pg.mkPen('b', width=3), name='.. Идеальный математический мятник')
        self.widget.layout().addWidget(self.plt1, 0, 0)

        self.plt2 = pg.plot()
        self.plt2.showGrid(x=False, y=False)
        #self.plt2.win.hide()
        self.plt2.setLabel('left', 'Угол')
        self.plt2.setLabel('bottom', 'Время')
        self.plt2.addLegend()
        self.graph2 = self.plt2.plot([0], [0], pen=pg.mkPen('y', width=3), name='.. Реальный математический маятник')
        self.widget.layout().addWidget(self.plt2, 1, 0)

        self.plt3 = pg.plot()
        self.plt3.showGrid(x=False, y=False)
        #self.plt3.win.hide()
        self.plt3.setLabel('left', 'Координата')
        self.plt3.setLabel('bottom', 'Время')
        self.plt3.addLegend()
        self.graph3 = self.plt3.plot([0], [0], pen=pg.mkPen('b', width=3), name='.. Идеальный пружинный маятник')
        self.widget.layout().addWidget(self.plt3, 0, 1)

        self.plt4 = pg.plot()
        self.plt4.showGrid(x=False, y=False)
        #self.plt4.win.hide()
        self.plt4.setLabel('left', 'Координата')
        self.plt4.setLabel('bottom', 'Время')
        self.plt4.addLegend()
        self.graph4 = self.plt4.plot([0], [0], pen=pg.mkPen('y', width=3), name='.. Реальный пружинный маятник')
        self.widget.layout().addWidget(self.plt4, 1, 1)

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
        self.thread_instance1.set_param(float(self.step.text()), float(self.precision.text()),
                                        float(self.t0.text()), float(self.ft.text()))
        self.thread_instance1.start()

        self.thread_instance2.set_param(float(self.step.text()), float(self.precision.text()),
                                        float(self.t0.text()), float(self.ft.text()))
        self.thread_instance2.start()

        self.thread_instance3.set_param(float(self.step.text()), float(self.precision.text()),
                                        float(self.t0.text()), float(self.ft.text()))
        self.thread_instance3.start()

        self.thread_instance4.set_param(float(self.step.text()), float(self.precision.text()),
                                        float(self.t0.text()), float(self.ft.text()))
        self.thread_instance4.start()

    def upd1(self, data):
        self.time.setNum(data[0][len(data[0])-1])
        self.graph2.setData(data[0], data[1])

    def upd2(self, data):
        self.time_2.setNum(data[0][len(data[0])-1])
        self.graph1.setData(data[0], data[1])

    def upd3(self, data):
        self.time_3.setNum(data[0][len(data[0])-1])
        self.graph3.setData(data[0], data[1])

    def upd4(self, data):
        self.time_4.setNum(data[0][len(data[0])-1])
        self.graph4.setData(data[0], data[1])
