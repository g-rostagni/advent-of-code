

for i in range(1,len(data)):
        for j in range(i,len(data)):
                for k in range(j,len(data)):
                        if data[i]+data[j]+data[k] == 2020:
                                print(data[i],data[j],data[k],data[i]*data[j]*data[k])
