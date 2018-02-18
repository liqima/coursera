# llinear regression with moltiple variables
import matplotlib.pyplot as plt

def linear_regression(x, y):
	features_num = len(x[1])
	t = [0] * (features_num + 1) # init the t
	# print(t)
	m = len(y)
	iterator = 100
	y_predict = [0] * m # init the predicted y value
	# print(y_predict)
	learning_rate = 0.1
	cost = []
	times = []
	for time in range(iterator):
		square_error = 0
		times.append(time)
		for i in range(m):
			y_pre = 0
			for feature in range(features_num):
				y_pre += t[feature + 1] * x[i][feature]
			y_pre += t[0]
			y_predict[i] = y_pre
			square_error += (y_pre - y[i]) ** 2 
		square_error = square_error / (2 * m)
		cost.append(square_error)
		# print(square_error)
		# print(t)
		t = update(x, y, t, learning_rate, y_predict) 
	plt.plot(times, cost)
	plt.show()

def update(x, y, t, learning_rate, y_predict):
	m = len(y)
	new_t = [0] * (len(t))
	for i in range(m):
		for position in range(m):
			new_t[0] += (y_predict[position] - y[position])
	new_t[0] = new_t[0] * learning_rate / m
	for j in range(1, len(t)):
		for position in range(m):
			new_t[j] += (y_predict[position] - y[position]) * x[position][j-1]
		new_t[j] = new_t[j] * learning_rate / m
	for i in range(len(new_t)):
		new_t[i] = t[i] - new_t[i]
	return new_t
x = [[1, 2, 1], [3, 4, 1], [2, 3, 3]]
y = [5, 11, 8]
linear_regression(x, y)