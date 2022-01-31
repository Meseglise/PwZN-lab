import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ad = pd.read_csv('apple-production.csv')
sad = ad.groupby('Entity').agg(Summaried_apple_production = ('Crops - Apples - 515 - Production - 5510 - tonnes', np.sum))
#sadtw = sad/2731467611
# perc_ap = sadtw.sort_values('Summarised_apple_production')
# nap_tot = perc_ap.to_numpy()
# knap_tot = nap_tot[109:129]
#names = ["Turkey", "Italy", "Low Income Food Deficit Countries", "South America", "France", "Western Asia", "USSR", "Souther Asia", "Southern Europe", "United States", "Northern America", "Western Europe", "Americas", "Eastern Europe", "European Union", "China", "Eastern Asia", "Europe", "Asia", "World"]

china_ap = ad.loc[ad['Entity'] == 'China']
usa_ap = ad.loc[ad['Entity'] == 'United States']
france_ap = ad.loc[ad['Entity'] == 'France']
italy_ap = ad.loc[ad['Entity'] == 'Italy']
turkey_ap = ad.loc[ad['Entity'] == 'Turkey']
world_ap = ad.loc[ad['Entity'] == 'World']

ndates = china_ap['Year'].to_numpy()
nchina_ap = china_ap['Crops - Apples - 515 - Production - 5510 - tonnes'].to_numpy()
nusa_ap = usa_ap['Crops - Apples - 515 - Production - 5510 - tonnes'].to_numpy()
nfrance_ap = france_ap['Crops - Apples - 515 - Production - 5510 - tonnes'].to_numpy()
nitaly_ap = italy_ap['Crops - Apples - 515 - Production - 5510 - tonnes'].to_numpy()
nturkey_ap = turkey_ap['Crops - Apples - 515 - Production - 5510 - tonnes'].to_numpy()


plt.plot(ndates, nchina_ap, label = 'Chiny')
plt.plot(ndates, nusa_ap, label = 'USA')
plt.plot(ndates, nfrance_ap, label = 'Francja')
plt.plot(ndates, nitaly_ap, label = 'Wlochy')
plt.plot(ndates, nturkey_ap, label = 'Turcja')

plt.title('Produkcja jablek na przestrzeni lat')
plt.xlabel('Rok')
plt.xlim(1961, 2018)
plt.ylabel('Ton jablek')
plt.ylim(0, 50000000)
plt.legend(loc="upper left")
plt.show()

print(sad)

