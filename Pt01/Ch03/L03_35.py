import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.figtext(0.5, 0.01, 'figtext')

plt.suptitle('suptitle')

plt.subplot(121)
plt.title('title 1')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.text(0.2, 0.2, 'text 1')
plt.annotate('annotate', xy=(0.2, 0.4), xytext=(0.6, 0.7), arrowprops=dict(facecolor='black', shrink=0.05))

plt.subplot(122)
plt.title('title 2')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.text(0.5, 0.5, 'text 2')

plt.show()