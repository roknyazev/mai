import form
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QGridLayout

import ml_getdata

import sim_results
import process


class MainWindow(QMainWindow, form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.widget = self.label
		self.set_layout()

		self.plt1 = pg.plot()
		self.plt2 = pg.plot()
		self.plt3 = pg.plot()
		self.plt4 = pg.plot()
		self.plt5 = pg.plot()
		self.plt6 = pg.plot()
		self.plt7 = pg.plot()
		self.plt8 = pg.plot()
		self.plt9 = pg.plot()
		self.plt10 = pg.plot()

		self.place_plots()
		self.set_plt_settings()

		process.G_STEP = 50
		sim_results.G_PATH = 'nonlin_results/'

		self.time = ml_getdata.get_data_from_variable('nonlin_results/result1.mat', 'res')
		self.data = sim_results.get_sim_results(100, 5)
		self.cov_matrix = process.process_results(self.data)

		self.standard1 = ml_getdata.get_data_from_variable('stand1.mat', 'standard')
		self.standard2 = ml_getdata.get_data_from_variable('stand2.mat', 'standard')

		self.draw_standard_cov1()
		self.draw_standard_cov2()
		self.draw_sample_cov()

	def set_layout(self):
		self.widget.setLayout(QGridLayout())
		self.widget.layout().setContentsMargins(0, 0, 0, 0)
		self.widget.layout().setSpacing(0)

	def place_plots(self):
		self.widget.layout().addWidget(self.plt1, 0, 0)
		self.widget.layout().addWidget(self.plt2, 1, 0)
		self.widget.layout().addWidget(self.plt3, 1, 1)
		self.widget.layout().addWidget(self.plt4, 2, 0)
		self.widget.layout().addWidget(self.plt5, 2, 1)

		self.widget.layout().addWidget(self.plt6, 2, 2)
		self.widget.layout().addWidget(self.plt7, 3, 0)
		self.widget.layout().addWidget(self.plt8, 3, 1)
		self.widget.layout().addWidget(self.plt9, 3, 2)
		self.widget.layout().addWidget(self.plt10, 3, 3)

	def set_plt_settings(self):
		self.plt1.win.hide()
		self.plt2.win.hide()
		self.plt3.win.hide()
		self.plt4.win.hide()
		self.plt5.win.hide()
		self.plt6.win.hide()
		self.plt7.win.hide()
		self.plt8.win.hide()
		self.plt9.win.hide()
		self.plt10.win.hide()

		self.plt1.addLegend(offset=(250, 30))
		self.plt2.addLegend(offset=(250, 30))
		self.plt3.addLegend(offset=(250, 30))
		self.plt4.addLegend(offset=(250, 30))
		self.plt5.addLegend(offset=(250, 30))
		self.plt6.addLegend(offset=(250, 30))
		self.plt7.addLegend(offset=(250, 30))
		self.plt8.addLegend(offset=(250, 30))
		self.plt9.addLegend(offset=(250, 30))
		self.plt10.addLegend(offset=(250, 30))

	def draw_sample_cov(self):
		self.plt1.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[0][0], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Дисперсия 0 0 (нелин.)')
		self.plt2.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[1][0], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 1 0 (нелин.)')
		self.plt3.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[1][1], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Дисперсия 1 1 (нелин.)')
		self.plt4.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[2][0], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 2 0 (нелин.)')
		self.plt5.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[2][1], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 2 1 (нелин.)')
		self.plt6.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[2][2], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Дисперсия 2 2 (нелин.)')
		self.plt7.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[3][0], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 3 0 (нелин.)')
		self.plt8.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[3][1], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 3 1 (нелин.)')
		self.plt9.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[3][2], pen=pg.mkPen((222, 122, 9), width=2),
		               name='Ковариация 3 2 (нелин.)')
		self.plt10.plot(self.time[0][1:-1:process.G_STEP], self.cov_matrix[3][3], pen=pg.mkPen((222, 122, 9), width=2),
		                name='Дисперсия 3 3 (нелин.)')

	def draw_standard_cov1(self):
		self.plt1.plot(self.time[0][1:-1:process.G_STEP], self.standard1[0][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Дисперсия 0 0 (1 способ)')
		self.plt2.plot(self.time[0][1:-1:process.G_STEP], self.standard1[1][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 1 0 (1 способ)')
		self.plt3.plot(self.time[0][1:-1:process.G_STEP], self.standard1[2][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Дисперсия 1 1 (1 способ)')
		self.plt4.plot(self.time[0][1:-1:process.G_STEP], self.standard1[3][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 2 0 (1 способ)')
		self.plt5.plot(self.time[0][1:-1:process.G_STEP], self.standard1[4][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 2 1 (1 способ)')
		self.plt6.plot(self.time[0][1:-1:process.G_STEP], self.standard1[5][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Дисперсия 2 2 (1 способ)')
		self.plt7.plot(self.time[0][1:-1:process.G_STEP], self.standard1[6][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 3 0 (1 способ)')
		self.plt8.plot(self.time[0][1:-1:process.G_STEP], self.standard1[7][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 3 1 (1 способ)')
		self.plt9.plot(self.time[0][1:-1:process.G_STEP], self.standard1[8][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 194), width=1), name='Ковариация 3 2 (1 способ)')
		self.plt10.plot(self.time[0][1:-1:process.G_STEP], self.standard1[9][1:-1:process.G_STEP],
		                pen=pg.mkPen((105, 185, 194), width=1), name='Дисперсия 3 3 (1 способ)')

	def draw_standard_cov2(self):
		self.plt1.plot(self.time[0][1:-1:process.G_STEP], self.standard2[0][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Дисперсия 0 0 (2 способ)')
		self.plt2.plot(self.time[0][1:-1:process.G_STEP], self.standard2[1][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 1 0 (2 способ)')
		self.plt3.plot(self.time[0][1:-1:process.G_STEP], self.standard2[2][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Дисперсия 1 1 (2 способ)')
		self.plt4.plot(self.time[0][1:-1:process.G_STEP], self.standard2[3][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 2 0 (2 способ)')
		self.plt5.plot(self.time[0][1:-1:process.G_STEP], self.standard2[4][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 2 1 (2 способ)')
		self.plt6.plot(self.time[0][1:-1:process.G_STEP], self.standard2[5][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Дисперсия 2 2 (2 способ)')
		self.plt7.plot(self.time[0][1:-1:process.G_STEP], self.standard2[6][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 3 0 (2 способ)')
		self.plt8.plot(self.time[0][1:-1:process.G_STEP], self.standard2[7][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 3 1 (2 способ)')
		self.plt9.plot(self.time[0][1:-1:process.G_STEP], self.standard2[8][1:-1:process.G_STEP],
		               pen=pg.mkPen((105, 185, 100), width=1), name='Ковариация 3 2 (2 способ)')
		self.plt10.plot(self.time[0][1:-1:process.G_STEP], self.standard2[9][1:-1:process.G_STEP],
		                pen=pg.mkPen((105, 185, 100), width=1), name='Дисперсия 3 3 (2 способ)')