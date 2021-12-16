# this code is really really ugly
# if for some reason you are looking at this to fix yours, don't
# why would you even be looking at my code in the first place? go look at graeme's, he can actually code, and it's readable

def import_data(filename):
        f = open(filename,'r')
        data = f.readline().strip()
        return data
        
def hex2bin(n):
	nbin = ''
	for char in n:
		nbin += format(int(char,16), '04b')
	return nbin
	
def operator(packet):
	subpackets = []
	packet.get_op_type()
	if packet.op_type == 0:
		i = 0
		lensp = get_len_subpacket(packet.trail)
		while i+lensp <= packet.lensp:
			subpackets.append(packet.trail[i:i+lensp])
			i += lensp
			if len(packet.trail[i:]) < 11:
				break
			lensp = get_len_subpacket(packet.trail[i:])
		spend = packet.trail[i:packet.lensp]
		if subpackets:
			subpackets[-1] += spend
		else:
			subpackets.append(spend)
	else:
		x = 0
		for i in range(packet.nsp):
			lensp = get_len_subpacket(packet.trail[x:])
			subpackets.append(packet.trail[x:x+lensp])
			x += lensp
	vals = []
	for subpacket in subpackets:
		vals.append(read_type(subpacket))
	valtot = 0
	match packet.ID:
		case 0:
			for val in vals:
				valtot += val
		case 1:
			valtot = 1
			for val in vals:
				valtot *= val
		case 2:
			valtot = 1e20
			for val in vals:
				valtot = min(valtot,val)
		case 3:
			for val in vals:
				valtot = max(valtot,val)
		case 5:
			valtot = int(vals[0] > vals[1])
		case 6:
			valtot = int(vals[0] < vals[1])
		case 7:
			valtot = int(vals[0] == vals[1])
	return valtot
	
def get_len_subpacket(sp):
	subpacket = Packet(sp)
	if subpacket.typ == 'litval':
		subpacket.get_litval()
		return 6 + subpacket.lensp
	else:
		subpacket.get_op_type()
		if subpacket.op_type == 0:
			return 22 + subpacket.lensp
		else:
			x = 0
			lensp = 0
			for i in range(subpacket.nsp):
				x += get_len_subpacket(subpacket.trail[x:])
			return 18 + x
	
def read_type(p):
	packet = Packet(p)
	if packet.typ == 'litval':
		val = packet.get_litval()
	else:
		val = operator(packet)
	return val
	
class Packet:
	def __init__(self, packet):
		self.ver = int(packet[:3],2)
		self.ID = int(packet[3:6],2)
		self.typ = 'litval' if self.ID == 4 else 'operator'
		self.trail = packet[6:]
	
	def get_litval(self):
		if self.typ != 'litval':
			return 'Error'
		n = ''
		for i in range(0, len(self.trail), 5):
			n += self.trail[i+1:i+5]
			if self.trail[i] == '0':
				break
		self.litval = int(n,2)
		self.lensp = i+5
		return self.litval
	
	def get_op_type(self):
		if self.typ != 'operator':
			return 'Error'
		self.op_type = int(self.trail[0])
		if self.op_type:
			self.nsp = int(self.trail[1:12],2)
			self.trail = self.trail[12:]
		else:
			self.lensp = int(self.trail[1:16],2)
			self.trail = self.trail[16:]
        
data = import_data('16-data')

databin = hex2bin(data)

val = read_type(databin)
print(val)
