import ml_getdata
import numpy as np

G_PATH = ''


def get_sim_results(count_of_results, count_of_parameters):
	"""
	Получение результатов моделирования
	:param count_of_results:    Количество моделирований (файлов с результатами)
	:param count_of_parameters: Количество параметров модели (время + компоненты фазового вектора)
	:return:                    Список параметров;
								в каждом параметре массив результатов;
								в каждом результате массив соотв. значений
	"""
	filename = ['result', '.mat']
	count_of_values = len(ml_getdata.get_data_from_variable(G_PATH + str(1).join(filename), 'res')[0])

	AllData = []
	for i in range(count_of_parameters-1):
		AllData.append(np.empty([count_of_results, count_of_values]))

	number_of_res = 1
	while number_of_res <= count_of_results:
		print('\rПолучено результатов:', number_of_res, end='')
		tmp1 = ml_getdata.get_data_from_variable(G_PATH + str(number_of_res).join(filename), 'res')

		number_of_par = 0
		while number_of_par < count_of_parameters-1:
			AllData[number_of_par][number_of_res-1] = tmp1[number_of_par+1].copy()
			number_of_par += 1

		number_of_res += 1
	return AllData
