import scipy.io


def get_data_from_struct(mat_file, struct, field):
	"""
	Получает данные из структуры mat-файла
	:param mat_file:    название файла
	:param struct:      структура
	:param field:       поле структуры
	:return:            значение поля структуры
	"""
	content = scipy.io.loadmat(mat_file)
	return content.get(struct)[field][0][0]


def get_data_from_variable(mat_file, var):
	"""
	Получает данные из переменной mat-файла
	:param mat_file:    название фала
	:param var:         переменная
	:return:            значение переменной
	"""
	content = scipy.io.loadmat(mat_file)
	return content.get(var)
