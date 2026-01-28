import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.plot(x, y)
plt.title("Simple Test Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("test_graph.png")
plt.close()