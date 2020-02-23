import sys

from Lab2.src.functions import functions_dict
from Lab2.src.research import research


f = open('out.csv', 'w')
sys.stdout = f

if __name__ == '__main__':
    for name, _ in functions_dict.items():
        research(name)
