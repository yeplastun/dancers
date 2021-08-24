import random

import pandas as pd

dancers = pd.read_csv('C:/Users/plast/OneDrive/Desktop/dancers.csv')
if (len(dancers.index) >= 32):
    top32 = dancers.sort_values(by='Рейтинг', ascending=False)  # сортировка по убыванию рейтинга
    print(top32.iloc[0:32])  # топ-32
    pairs = top32.iloc[0:32].index.array
    random.shuffle(pairs)
    print(pairs)
    with open('C:/Users/plast/OneDrive/Desktop/pairs.txt', 'w') as file:
        for i in range(0, len(pairs), 2):
            file.write(dancers.loc[pairs[i], 'Танцор'], 'vs', dancers.loc[pairs[i + 1], 'Танцор'])
    file.close()
    file.readline(2)
elif (len(dancers.index) >= 16):
    top16 = dancers.sort_values(by='Рейтинг', ascending=False)  # сортировка по убыванию рейтинга
    print(top16.iloc[0:16])  # топ-16
    pairs = top16.iloc[0:16].index.array
    random.shuffle(pairs)
    print(pairs)
    for i in range(0, len(pairs), 2):
        print(dancers.loc[pairs[i], 'Танцор'], 'vs', dancers.loc[pairs[i + 1], 'Танцор'])
elif (len(dancers.index) >= 8):
    top8 = dancers.sort_values(by='Рейтинг', ascending=False)  # сортировка по убыванию рейтинга
    print(top8.iloc[0:8])  # топ-8
    pairs = top8.iloc[0:8].index.array
    random.shuffle(pairs)
    print(pairs)
    for i in range(0, len(pairs), 2):
        print(dancers.loc[pairs[i], 'Танцор'], 'vs', dancers.loc[pairs[i + 1], 'Танцор'])
else:
    print("Недостаточно участников для проведения баттла")
