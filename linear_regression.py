# linear regression with one variable using gradient decent
import matplotlib.pyplot as plt

def linear_regression_one_variable(x, y):
	m = len(x)
	t0 = t1 = 0
	iterator = 400
	learning_rate = 0.05
	times = []
	cost = []
	for time in range(iterator):
		square_error = 0
		for i in range(m):
			square_error = square_error + (t0 + t1 * x[i] - y[i]) ** 2
		times.append(time + 1)
		square_error = square_error / (2 * m)
		cost.append(square_error)
		t0, t1 = update(x, y, t0, t1, learning_rate)
		
	# plot
	print(t0, t1, square_error)
	plt.scatter(x, y)
	plt.plot([0, max(x)], [t0, t0 + t1 * max(x)])
	# plt.scatter(times, cost)
	plt.show()

def update(x, y, t0, t1, learning_rate):
	m = len(x)
	new_t0 = 0
	for i in range(m):
		new_t0 = new_t0 + (t0 + t1 * x[i] - y[i])
	new_t0 = new_t0 / m
	new_t0 = t0 - learning_rate * new_t0
	new_t1 = 0
	for i in range(m):
		new_t1 = new_t1 + (t0 + t1 * x[i] - y[i]) * x[i]
	new_t1 = new_t1 / m
	new_t1 = t1 - learning_rate * new_t1
	return new_t0, new_t1

x = [1, 2, 3]
y = [2, 4, 6]
linear_regression_one_variable(x, y)