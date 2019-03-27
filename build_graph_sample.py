import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('graph_data.csv')
plt.style.use("ggplot")
print(data)
fig, ax = plt.subplots()

ax.plot(data.exp, data.result, marker='o')
ax.set_title('Зависимость точности работы алгоритма от размерности пространства поиска')
plt.show()