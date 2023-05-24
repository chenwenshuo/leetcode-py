import matplotlib.pyplot as plt

sq = [1, 3, 4, 5, 8, 2]

sq1 = [1, 7, 4, 5, 9, 2]

plt.plot(sq, linewidth=5)
plt.plot(sq1)
plt.scatter([3,5,6,7,8,9], [4,5,6,7,8,2], s=20)
plt.title("test title")
plt.xlabel("V", fontsize=14)
plt.ylabel("Y", fontsize=20)
plt.tick_params(axis='both', labelsize=14)
plt.show()
