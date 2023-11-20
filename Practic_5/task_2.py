import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import requests

url="https://scipy-lectures.org/_downloads/populations.txt"
responce=requests.get(url)
c = StringIO(responce.text)
data=np.loadtxt(c)
year, hares,lynxes, carrots = data.T
populations= data[:,1:]

print("Mean:",populations.mean(axis=0))     # Среднее значение численности
print("Std:", populations.std(axis=0))      # Стандартная девиация

max_years=np.argmax(populations,axis=0)
print("Максимальный год",year[max_years])   # Год наибольшей популяции

max_species=np.argmax(populations,axis=1)
species=np.array(['hare','lynx','carrot'])
print("Макс.видов")
print(year)
print(species[max_species])

above=np.any(populations>50000,axis=1)
print("Популяция превышает 50000",year[above])

top=np.argsort(populations,axis=0)[:2]
print(year[top])

haregrade=np.gradient(hares,1.0)
lynxesgrade=np.gradient(lynxes,1.0)
print("Разница",np.corrcoef(haregrade,lynxesgrade)[0,1])

plt.plot(year,haregrade,year,lynxesgrade)
plt.savefig("plot.png")




