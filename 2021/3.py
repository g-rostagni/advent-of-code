def import_data(filename):
        f = open(filename,'r')
        data = []
        for line in f:
                data.append(line.strip())
        return data

def find_rating(dataIN,gas):
        vals = dataIN.copy()
        i = 0
        while len(vals) > 1:
                vals0 = []
                vals1 = []
                for entry in vals:
                        if entry[i] == '1':
                                vals1.append(entry)
                        else:
                                vals0.append(entry)
                if (gas == 'ox' and len(vals1) >= len(vals)/2) or (gas == 'co' and len(vals1) < len(vals)/2):
                        vals = vals1.copy()
                else:
                        vals = vals0.copy()
                i += 1
        return int(vals[0],2) #returns a decimal int

data = import_data('3-data')

ox = find_rating(data,'ox')
co = find_rating(data,'co')

print(ox,co,ox*co)
