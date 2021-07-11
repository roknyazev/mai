from collections import namedtuple
import sys


class AbstractModel:
    def __init__(self):
        self.InitialValues = []
        self.RightParts = []


class AbstractIntegrator:

    def __init__(self, model: AbstractModel, step, precision, initial_time, final_time):

        constants = namedtuple('constants',
                               ['model', 'precision', 'ft', 'equations_number',
                                'sampling_increment', 'initial_time', 'rounding_error'])
        self.const = constants(model, precision, final_time, len(model.RightParts),
                               step, initial_time, 2 * sys.float_info.epsilon / precision)

        self.new_step = step
        self.t = initial_time
        self.t_out = initial_time
