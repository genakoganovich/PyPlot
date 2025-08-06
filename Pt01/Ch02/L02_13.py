import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]

line = plt.plot(x, y, color='red')
plt.setp(line, color='red', linewidth=1)


plt.show()