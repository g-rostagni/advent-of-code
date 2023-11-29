flows = {}
tunnels = {}
with open("16-test","r") as f:
	for line in f.readlines():
		l = line.strip().split(" ")
		flows[l[1]] = int(l[4].split("=")[1][:-1])
		tunnels[l[1]] = []
		for valve in l[9:]:
			tunnels[l[1]].append(valve.replace(",","")) 

#totflows = {f: [-1,0,set(),""] for f in flows}

#totflows["AA"] = [0,0,set(),"AA"]
#queue = ["AA"]
#time_tot = 30
#for minute in range(1,time_tot + 1):
#	queuenext = []
#	TFnext = {}
#	for f in totflows:
#		TFnext[f] = [a for a in totflows[f]]
#	for v in queue:							# loop over all points in the queue
#		for dest in tunnels[v]:					# loop over all possible destinations from that point
#			if totflows[v][0] > TFnext[dest][0]:
#				TFnext[dest][0] = totflows[v][0]	# update flow
#				TFnext[dest][1] = minute		# update time to get there
#				TFnext[dest][2] = {a for a in totflows[v][2]}	# update path
#				TFnext[dest][3] = "Moved from " + v + " to " + dest
#				queuenext.append(dest)
#	for v in queue:
#		# if the valve has a flow
#		# if it hasn't been activated
#		# if activating it would give more flow
#		flow_act = totflows[v][0] + flows[v] * (time_tot - minute)
#		if flows[v] and not v in totflows[v][2] and flow_act > TFnext[v][0]:				# if we haven't yet activated that valve
#			TFnext[v][0] = flow_act
#			TFnext[v][1] = minute
#			TFnext[v][2] = {a for a in totflows[v][2]}
#			TFnext[v][2].add(v)
#			TFnext[v][3] = "Opened valve " + v
#			queuenext.append(v)
#	queue = [q for q in queuenext]
#	for f in TFnext:
#		totflows[f] = [a for a in TFnext[f]]
#	print(minute)
#	for t in totflows:
#		if totflows[t][1] == minute:
#			print(t,totflows[t])
# 
#maxflow = 0
#for t in totflows:
#	if totflows[t][0] > maxflow:
#		maxflow = totflows[t][0]
#print(maxflow)









# start from AA
# look at all cells accessible from AA (including activating AA)
# for each get:
#	the time to get there (the path will stop at t=30)
#	the path to get there (list or string containing all visited paths up to this, to avoid activating valves twice)
#	the total flow we get for that path
# update a new dict with these three values
# for the next step look at all point we can get from there, including staying there and activating a valve
# if the flow we can get is greater than what we had: update the point and add it to the queue for the next step
# keep going until there is nothing to update anymore: then we should have found a path of maximal flow


