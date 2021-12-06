import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from rich.console import Console
import rich.traceback
from rich.progress import track
import argparse

parser = argparse.ArgumentParser(description="Arguments description")
parser.add_argument('-s1', '--size', help='size of the net', type=int, default=60)
parser.add_argument('-v1', '--valuej', help='value of J', type=float, default=0.4)
parser.add_argument('-v2', '--valueh', help='value of field H', type=float, default=0.5)
parser.add_argument('-b1', '--parabeta', help='beta parameter', type=float, default=0.7)
parser.add_argument('-n1', '--nstep', help='number of steps of simulation', type=int, default=300)
parser.add_argument('-p1', '--path', help='path to saving file', default='Grids/')
parser.add_argument('-f1', '--file', help='file name', default='gridn')
parser.add_argument('-e1', '--ext', help='file extension', default='.png')
args = parser.parse_args()

console = Console()
console.clear()
console.rule("Ising model simulation")
console.print("[bold red]Simulation is running[/bold red]")

class Isingmodel():
    def algorithm(self, draw, N, beta):
        for i in range(N):
            for j in range(N):
                beta = args.parabeta
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s = draw[a, b]
                nb = draw[(a + 1) % N, b] + draw[a, (b + 1) % N] + draw[(a - 1) % N, b] + draw[a, (b - 1) % N]
                cost = 2 * s * nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost * beta):
                    s *= -1
                draw[a, b] = s
        return draw

    def plot(self, f, draw, i, N):
        X, Y = np.meshgrid(range(N), range(N))
        plt.pcolormesh(X, Y, draw, shading= 'auto', cmap = 'rainbow')
        plt.axis('off')
        
    def simulate(self):
        N = args.size
        temp = args.valuej
        draw = 2 * np.random.randint(2, size=(N, N)) - 1
        fig = plt.figure(figsize=(30, 30), dpi=80)
        self.plot(fig, draw, 0, N)
        for i in track(range(args.nstep)):
            self.algorithm(draw, N, 1.0 / temp)
            plt.clf()
            self.plot(fig, draw, i, N)
            plt.savefig(f'{args.path}{args.file}{i}{args.ext}', bbox_inches = 'tight', pad_inches = 0)

runsim = Isingmodel()
runsim.simulate()



