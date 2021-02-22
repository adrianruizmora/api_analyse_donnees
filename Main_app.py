import pandas
import os

# ------- COMMANDES PANDAS ------- #

cc = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', header = 2, names = ['X1', 'X2', 'X3'])
# Pour changer le nom des colonnes
dl = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', header = 2)
# pour supprimer les deux lignes en tête
di = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', skiprows = [0, 1])
# pour supprimer l'index 0 et 1.
fc = pandas.read_csv('https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv', usecols = ['A', 'C', 'G']
# pour lire certaines colonnes

# print(cc)
# print(dl)
# print(di)
# print(fc)



