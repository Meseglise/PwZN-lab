import asyncio
import numpy as np
import matplotlib.pyplot as plt
import random

async def random_list():
    await asyncio.sleep(10)
    randomlist = []
    for i in range(0, 10000):
        n = random.randint(1, 10000) / 10000
        randomlist.append(n)
    print("Wytworzono tablice")
    return randomlist

async def random_mean(randomlist):
    rand_mean = np.mean(randomlist)
    print("Obliczono srednia")
    return rand_mean

async def random_std(randomlist):
    await asyncio.sleep(1)
    rand_std = np.std(randomlist)
    print("Obliczono odchylenie")
    return rand_std

async def write_data(randomlist, rand_mean, rand_std):
    file1 = open("Dane.txt", "w")
    file1.write(
        f"Wygenerowano liste przypadkowych liczb:\n{randomlist}\nSrednia wartosc:\n{rand_mean}\nOdchylenie standardowe:\n{rand_std}")
    file1.close()

async def make_x():
    x_list = list(range(0, 10000))
    return x_list

# async def polyfit(randomlist, x_list):
#     z = np.polyfit(x_list, randomlist, 3)
#     poly = np.poly1d(z)
#     return poly

# async def plot_data(randomlist, x_list):
#     plt.plot(np.array(randomlist))
#     # plt.plot(x_list, poly, label='Dopasowana')
#
#     plt.title('Produkcja jablek na przestrzeni lat')
#     plt.xlabel('Rok')
#     plt.ylabel('Ton jablek')
#     plt.show()

async def main():
    randomlist = await asyncio.gather(*[random_list()])
    rand_mean = await asyncio.gather(*[random_mean(randomlist)])
    rand_std = await asyncio.gather(*[random_std(randomlist)])
    await asyncio.gather(*[write_data(randomlist, rand_mean, rand_std)])
    x_list = await asyncio.gather(*[make_x()])
    # poly = await asyncio.gather(*[polyfit(randomlist, x_list)])
    # await asyncio.gather(*[plot_data(randomlist, x_list)])



asyncio.run(main())

