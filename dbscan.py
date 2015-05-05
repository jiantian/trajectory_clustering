
from __future__ import division
from random import choice
import math
import sys

def initializeDict(objects):
	d = {}
	for item in objects:
		d[item] = 'unvisited'
	return d

def neighbor(p, eps, objects):
	neighbors = []
	for point in objects:
		if p != point:
			distance = math.sqrt((p[0]-point[0])**2 \
					+ (p[1]-point[1])**2)
			if distance <= eps:
				neighbors.append(point)
	return neighbors

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Usage: python exer3_DBSCAN.py MinPts Eps"
		sys.exit()

	minpts = int(sys.argv[1])
	eps = float(sys.argv[2])

	objects = [(1,3), (1,2), (2,1), (2,2), (2,3), \
				(3,2), (5,3), (4,3), (4,5), (5,4), \
				(5,5), (6,4), (6,5)]

	# mark all objects as unvisited
	dict_obj = initializeDict(objects)

	clusters = []
	while(1):
		# randomly select an unvisited object p
		list_unvisited = []
		for key in dict_obj:
			if dict_obj[key] == 'unvisited':
				list_unvisited.append(key)
		if len(list_unvisited) == 0:
			break
		p = choice(list_unvisited)
		# mark p as visited
		dict_obj[p] = 'visited'
		N = neighbor(p, eps, objects)
		#print p
		#print N
		if len(N) >= minpts:
			# create a new cluster C and add p to C
			cluster = set()
			cluster.add(p)
			for point in N:
				if dict_obj[point] == 'unvisited':
					dict_obj[point] = 'visited'
					N_prime = neighbor(point, eps, objects)
					if len(N_prime) >= minpts:
						for item in N_prime:
							N.append(item)
				# if point is not yet a member of any cluster, add to C
				exist = 0
				for C in clusters:
					if point in C:
						exist = 1
						break
				if exist == 0:
					cluster.add(point)
			clusters.append(cluster)
		else:
			dict_obj[p] = 'noise'

	print clusters
