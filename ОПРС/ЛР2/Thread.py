from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import dpintegrator
import arenstorfmodel


class ThreadForIntegrator(QThread, QObject):
    def __init__(self):
        super().__init__()
        self.step = None
        self.precision = None
        self.t0 = None
        self.ft = None

    def set_param(self, step, precision, t0, ft):
        self.step = step
        self.precision = precision
        self.t0 = t0
        self.ft = ft

    def run(self):
        model = arenstorfmodel.ArenstorfModel()
        integrator = dpintegrator.DormandPrinceIntegrator(model, self.step, self.precision, self.t0, self.ft)
        x = [[], [], []]
        for data in integrator:
            if data == 0:
                continue
            elif data is None:
                break
            else:
                for results in data:
                    x[0].append(results[0])
                    for i in (1, 2):
                        x[i].append(results[1][i-1])
                    self.slot(x)

    @pyqtSlot(name='call_function')
    def slot(self, results):
        sender.data.emit(results)


class Sender(QObject):
    data = pyqtSignal(list)


sender = Sender()
