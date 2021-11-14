import rich
import argparse
import PIL

parser = argparse.ArgumentParser(description = "Arguments description")
parser.add_argument('-s1', '--size', help = 'size of the net',type = int, default = 10)
parser.add_argument('-v1', '--valuej', help = 'value of J', type = float, default = 0.5)
parser.add_argument('-v2', '--valueh', help = 'value of field H', type = float, default = 0.5)
parser.add_argument('-p1', '--parabeta', help = 'beta parameter', type = float, default = 0.5)
parser.add_argument('-n1', '--nstep', help = 'number of steps of simulation', type = int, default = 5)
#parser.add_argument('-d1', '--sdensisty', help = 'start spin density', type = int, default = 5)
#parser.add_argument('-d1', '-file', help = 'name of file', default = 'Quo_Vadis.txt')

args = parser.parse_args()

