import statistics
import sim_results

G_STEP = 1


def process_results(params):
	print('\n')
	count_of_values = len(params[0][0])
	count_of_parameters = len(params)
	matrix = []
	for i in range(count_of_parameters):
		matrix.append([])
		for j in range(count_of_parameters):
			matrix[i].append([])
			matrix[i][j].append(sim_results.np.empty([count_of_values]))
	i = 0
	while i < count_of_parameters:
		j = 0
		while j <= i:
			tmp = sim_results.np.empty([len(params[0]), int(count_of_values/G_STEP)])  # FIXME int(count_of_values/G_STEP)
			for k in range(len(params[0])):
				a = statistics.cov_fnc(params[i][k], params[j][k], count_of_values, G_STEP)
				tmp[k] = a
			fnc = statistics.fnc_sm(tmp)
			matrix[i][j] = fnc
			print('\nПосчитана ковариация:', i, ' ', j)

			j += 1
		i += 1
	return matrix
