def import_data(filename):
        f = open(filename,'r')
        dataF = f.readline().strip().split(',')
        dataS = [0 for i in range(9)]
        for n in dataF:
                dataS[int(n)] += 1
        return dataS

def update(dataF):
        dataF_new = [0 for i in range(9)]
        for i in range(9):
                if i == 0:
                        dataF_new[6] += dataF[0]
                dataF_new[i-1] += dataF[i]
        return dataF_new

import time
t0 = time.time()

data = import_data('6-data')
days = 256

for i in range(days):
        data = update(data)

tot = 0
for n in data:
        tot += n
print('number of fish after',days,'days:',tot)

t1 = time.time()

print('time:',(t1-t0)*1000,'ms')

