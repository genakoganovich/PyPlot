import matplotlib.pyplot as plt

plt.plot([1, 5, 10, 15, 20], [1, 7, 3, 5, 11])
plt.xlabel('Day', fontsize=15, color='blue')
plt.title('Chart price', fontsize=17, loc='center')
plt.text(5, 10, 'type: Steel')
plt.show()