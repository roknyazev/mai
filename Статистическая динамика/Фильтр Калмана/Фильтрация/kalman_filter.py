import numpy as np
from numpy import linalg as la
import model as m

test = [0]


def prediction(state_vector, cov_matrix, dt, rand_eff_args):
    """
    Прогнозирует на основе модели
    вектор состояния и ковариационную матрицу вектора состояния в момент измерения
    :param state_vector:   Скорректированный вектор состояния в предыдущий момент времени
    :param cov_matrix:     Скорректированная ковариационная матрица вектора состояния в предыдущий момент времени
    :param dt:             Шаг времени
    :param rand_eff_args:  Необязательные аргументы для рассчета ковариационной матрицы случайных воздействий
    :return:               Прогноз вектора состояния и ковариационной матрицы
    """
    X_ = state_vector
    P_ = cov_matrix

    F = m.transform_matrix(state_vector, dt)
    D = m.random_effects_cov(rand_eff_args)
    L = m.random_effects_influence(state_vector, dt)
    test.append(np.dot(np.dot(L, D), np.transpose(L))[0, 1])

    X_ = np.dot(F, X_)
    P_ = np.dot(np.dot(F, P_), np.transpose(F)) + D#np.dot(np.dot(L, D), np.transpose(L))
    return X_, P_


def correction(predicted_state_vector, predicted_cov_matrix, measured_state_vector, rand_err_args):
    """
    Корректирует прогноз
    :param predicted_state_vector:  Спрогнозированный вектор состояния
    :param predicted_cov_matrix:    Спрогнозированная ковариационная матрица
    :param measured_state_vector:   Измерения  вектора состояния (компоненты, которые не подвергались измерению
                                    должны иметь значение NaN (из numpy))
    :param rand_err_args:           Необязательные аргументы для рассчета ковариационной матрицы
                                    случайных ошибок измерения
    :return:                        Скорректированные вектор состояния и ковариационная матрица
    """
    indexes = []

    X = predicted_state_vector
    P = predicted_cov_matrix
    Y = measured_state_vector
    D = m.random_errors_cov(rand_err_args)
    H = m.vectors_relationship(None)

    for i in range(len(Y)):
        if not np.isnan(Y[i]):
            indexes.append(i)
    if len(indexes) == 1:
        i = indexes[0]

        P_inv = la.inv(P)
        summ = P_inv + np.dot((H.T * (1/D[0])), H)
        P = la.inv(summ)

        tmp1 = np.dot(P, (H.T * (1/D[0])))
        tmp1 = tmp1.reshape(2)
        tmp2 = Y[i] - X[i]
        X = X + tmp1 * tmp2
        #X[i] = X[i] + (P[i, i] / D[0]) * (Y[i] - X[i])
    else:
        pass  # FIXME Не рассмотрен случай с измерением нескольких элементов вектора состояния
    return X, P


def kalman(previous_corrected_state_vector, previous_corrected_cov_matrix, current_measured_state_vector, dt,
           rand_eff_args=None, rand_err_args=None):
    """
    Осуществляет прогноз вектора состояния и ковариационной матрицы и последующую их коррекцию (алгоритм Калмана)
    :param previous_corrected_state_vector: Скорректированный вектор состояния в предыдущий момент времени
    :param previous_corrected_cov_matrix:   Скорректированная ковариационная матрица вектора состояния
                                            в предыдущий момент времени
    :param current_measured_state_vector:   Вектор измерений в текущий момент времени
    :param dt:                              Шаг времени
    :param rand_eff_args:                   Необязательные аргументы для рассчета ков. матрицы случайных воздействий
    :param rand_err_args:                   Необязательные аргументы для рассчета ков. матрицы
                                            случайных ошибок измерения
    :return: Скорректированные вектор состояния и ковариационная матрица вектора состояния
    """
    X_ = np.array(previous_corrected_state_vector)
    P_ = np.array(previous_corrected_cov_matrix)
    Y = np.array(current_measured_state_vector)

    X, P = prediction(X_, P_, dt, rand_eff_args)
    result_vector, result_cov = correction(X, P, Y, rand_err_args)

    return result_vector, result_cov
