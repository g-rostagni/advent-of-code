def import_data(filename):
        f = open(filename,'r')
        data = f.readline().strip().split(',')
        return data

def sum_(n):
        return int(n*(n+1)/2)

import time

t0 = time.time()

data = [int(i) for i in import_data('7-data')]

for i in range(min(data),max(data)+1):
        fuel = 0
        for p in data:
                fuel += sum_(abs(i - p))
        if  i == min(data) or fuel < min_fuel:
                min_pos = i
                min_fuel = fuel

print('best position:',min_pos,', minimum fuel:',min_fuel)

t1 = time.time()

print((t1-t0)*1000,'ms')
