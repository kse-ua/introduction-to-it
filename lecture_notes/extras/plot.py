import matplotlib.pyplot as plt

plt.plot([0,1,2],[2,6,7], marker = ">", linestyle = 'dotted')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid()
plt.show()