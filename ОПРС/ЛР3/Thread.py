from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import dpintegrator
import Otvibration


class ThreadForMathPend(QThread, QObject):
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
        model = Otvibration.MathPendulum(10, 10, 1)
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
        sender1.data.emit(results)


class Sender1(QObject):
    data = pyqtSignal(list)


sender1 = Sender1()


class ThreadForIdMathPend(QThread, QObject):
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
        model = Otvibration.IdealMathPendulum(10, 10)
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
        sender2.data.emit(results)


class Sender2(QObject):
    data = pyqtSignal(list)


sender2 = Sender2()


class ThreadForIdSpPend(QThread, QObject):
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
        model = Otvibration.IdealSpringPendulum(10, 10)
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
        sender3.data.emit(results)


class Sender3(QObject):
    data = pyqtSignal(list)


sender3 = Sender3()


class ThreadForSpPend(QThread, QObject):
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
        model = Otvibration.SpringPendulum(10, 10, 10, 0)
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

        sender4.data.emit(results)


class Sender4(QObject):

    data = pyqtSignal(list)


sender4 = Sender4()
