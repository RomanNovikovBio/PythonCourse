import numpy as np
import matplotlib.pyplot as plt 

import pandas as pd  
import seaborn as sns 

# загружаем датасет
boston = datasets.load_boston()
boston_df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
#добавляем столбец со стоимостью
boston_df['PRICE'] = boston.target
# смотрим, какие данные у нас есть
print ("Columns: " + " ".join (boston_df.columns))

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston_df['RM'], bins=30)
plt.title('RM distribution')
plt.show()


plt.scatter (boston_df["RM"], boston_df["PRICE"])
plt.title ("average number of rooms per dwelling")
plt.xlabel ("RM")
plt.ylabel ("PRICE")
plt.plot(np.unique(boston_df["RM"]), np.poly1d(np.polyfit(boston_df["RM"],boston_df["PRICE"],1))(np.unique(boston_df["RM"])))
plt.show()


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(boston_df['LSTAT'], bins=30)
plt.title('LSTAT distribution')
plt.show()

plt.scatter (boston_df["LSTAT"], boston_df["PRICE"])
plt.title (" % lower status of the population")
plt.xlabel ("LSTAT")
plt.ylabel ("PRICE")
plt.plot(np.unique(boston_df["LSTAT"]), np.poly1d(np.polyfit(boston_df["LSTAT"],boston_df["PRICE"],1))(np.unique(boston_df["LSTAT"])))
plt.show()
