import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]

line = plt.plot(x, y)
plt.setp(line, linestyle='--')

plt.show()