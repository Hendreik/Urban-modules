# module_11_1.py
"""
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
"""
import matplotlib as mt
import numpy as np
import pandas as pd

print(mt.__version__)

serie1 = pd.Series([np.__version__, 11, 12, 13, 14, 15,'nums'])

print(serie1)

dates = pd.date_range("20241101", periods=8)

pd.DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
	'2024-01-05', '2024-01-06'],
    dtype='datetime64[ns]', freq='D')

# DataFrame
df = pd.DataFrame(np.random.randn(8, 3), index=dates, columns=list("XYZ"))

print(df)

df2 = pd.DataFrame(
    {
        "X4": np.array([0] * 5, dtype="int32"),
        "X5": pd.Categorical(["s1", "s2", "s3", "s4","s5"]),
        "X2": pd.Timestamp("20240102"),
        "X3": pd.Series(333, index=list(range(5)), dtype="float32"),
        "X1": 100,
        "X6": "finish",
    })

print(df2)
##################
import matplotlib.pyplot as plt

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 4, 2], [2, 4, 2, 1])  # Plot some data on the Axes.
plt.show()                           # Show the figure.
#############
ar1 = np.array([101, 102, 103, 104])
ar2 = np.array(['a', 'b', 'c', 'd'])
ar3=np.concatenate((ar1, ar2))
print(np.sort(ar3))


