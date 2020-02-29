import sys

from Lab3.src.functions import functions_arr
from Lab3.src.research import research


f = open('out.csv', 'w')
std = sys.stdout
sys.stdout = f

if __name__ == '__main__':
    for name in functions_arr:
        research(name)

f.close()
sys.stdout = std
