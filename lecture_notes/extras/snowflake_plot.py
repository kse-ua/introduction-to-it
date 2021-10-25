from snowflake import koch_snowflake
import matplotlib.pyplot as plt

x, y = koch_snowflake(order=10)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()