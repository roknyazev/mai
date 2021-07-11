import numpy as np


def transform_matrix(state_vector, dt):
    """
    Матрица перехода от state_vector(t) к state_vector(t + dt), где t - произвольный момент времени
    :param state_vector:    Вектор состояния в момент времени t
    :param dt:              Шаг времени
    :return:                Матрица перехода
    """
    elem00 = 1 + (0.1 - 0.05 * state_vector[1] - 0.03 * state_vector[0]) * dt
    #elem01 = 0.05 * dt
    #elem10 = -0.15 * dt
    elem11 = 1 - (0.2 - 0.15 * state_vector[0]) * dt
    return np.array([[elem00, 0], [0, elem11]])


def random_effects_influence(state_vector, dt):
    """
    Матрица влияния случайных воздействий
    В данном случае учитывает мультипликативность ошибок
    :param state_vector:    Вектор состояния в текущий момент времени
    :param dt:              Шаг времени
    :return:                Матрица влияния случайных воздействий
    """
    elem00 = state_vector[0] * 0.13
    elem11 = -state_vector[1] * 0.13
    return np.array([[elem00, 0], [0, elem11]])


def random_effects_cov(args):
    """
    Ковариационная матрица случайных воздействий
    :param args:    Необязательные аргументы
    :return:        Ковариационная матрица случайных воздействий
    """
    if args is None:
        return np.array([[0.0089, 0.0009], [0.0009, 0.001]])
    else:
        pass


def vectors_relationship(args):
    if args is None:
        return np.array([[0, 1]])
    else:
        pass


def random_errors_cov(args):
    """
    Ковариационная матрица случайных ошибок
    В данном случае матрица будет состоять из одной лишь дисперсии: [D_err]
    :param args:    Необязательные аргументы
                    В данном случае: args[0] - ошибка из задания,
                    args[1] - второй элемент скорректированного вектора состояния
                              (элемент, который подвергается измерению)
    :return:        Ковариационная матрица случайных ошибок
    """
    if args is None:
        pass
    else:
        err = (0.01 * args[0] * args[1])**2
        return np.array([err])
