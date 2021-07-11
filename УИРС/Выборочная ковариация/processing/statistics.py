import numpy


def sample_cov(sample1, sample2, length):
	i = 0
	s = 0
	while i < length:
		s += sample1[i]*sample2[i]
		i += 1
	return s/length


def cov_fnc(fnc1, fnc2, length, step):
	f = []
	i = 1
	while i <= length:
		sample1 = fnc1[0:i]
		sample2 = fnc2[0:i]
		print('\r', i, end='')
		cov = sample_cov(sample1, sample2, i)
		f.append(cov)
		i += step
	return f


def sample_mean(data, length):
	"""
	:param data:    Выборка
	:param length:  Длина выборки
	:return:        Выборочное среднее
	"""
	m = 0
	i = 0
	while i < length:
		m += data[i]
		i += 1
	return m/length


def fnc_sm(matrix):
	n = len(matrix)
	m = len(matrix[0])
	fnc = numpy.empty(m)
	i = 0
	while i < m:
		fnc[i] = sample_mean(matrix[:, i], n)
		i += 1
	return fnc
