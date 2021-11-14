from ascii_graph import Pyasciigraph
import argparse

parser = argparse.ArgumentParser(description = "Arguments description")
parser.add_argument('-file', help = 'name of file', default = 'Quo_Vadis.txt')
parser.add_argument('-n1', '--number1', help = 'number of words', type = int, default = 10)
parser.add_argument('-n2', '--number2', help = 'minimal word lenght', type = int, default = 0)
args = parser.parse_args()

with open(args.file) as f:
    data = f.read().strip().split()
    col = []
    hist = {}
    for word in data:
        if len(word)>args.number2:
            col.append(word)
        else:
            continue
    for word in col:
        hist[word] = hist.get(word, 0)+1

graph = Pyasciigraph()

info = [(f'{k}', v) for k, v in hist.items()]
info.sort(key = lambda e: e[1], reverse = True)

a = 0
for line in graph.graph('Histogram', info):
    print(line)
    if a-1<args.number1:
        a+=1
        continue
    else:
        print("Finished")
        break