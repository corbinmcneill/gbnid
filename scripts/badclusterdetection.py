from sys import argv

def badclusterdetection(clustername, dataname, goodclusters):
	clusterfile = open(clustername, 'r')
	datafile = open(dataname, 'r')
	goodclusters = int(goodclusters)

	# process data file to determine which entries are normal
	# and which are anamolous 
	data = {}
	line = datafile.readline()
	while line != '':
		cleanlinesplit = line.rstrip().split(' ')
		data[int(cleanlinesplit[0])-2] = cleanlinesplit[1].split(',')[-1]
		line = datafile.readline()

	# read clusters from clusterfile
	totalVertices = 0
	clusters = []
	line = clusterfile.readline()
	while line != '':
		if line != '\n':
			clusters.append(line.rstrip().split(' '))
			totalVertices += len(line.split(' '))
		line = clusterfile.readline()

	# analyze clusters
	tp = 0
	tn = 0
	fp = 0
	fn = 0
	for i,cluster in enumerate(sorted(clusters, key=len, reverse=True)): 
		if i < goodclusters:
			for vertex in cluster:
				if data[int(vertex)] == "normal.":
					tp += 1
				else:
					fp += 1
		else:
			for vertex in cluster:
				if data[int(vertex)] == "normal.":
					fn += 1
				else:
					tn += 1

	#print analysis
	print "Positive Clusters:", str(goodclusters)
	print "Negative Clusters:", str(len(clusters) - goodclusters)
	print "TP:               ", str(tp)
	print "TN:               ", str(tn)
	print "FP:               ", str(fp)
	print "FN:               ", str(fn)
	print "TPR:              ", str(float(tp) / (tp + fp))
	print "TNR:              ", str(float(tn) / (tn + fn))
	print "FPR:              ", str(float(fp) / (tp + fp))
	print "FNR:              ", str(float(fn) / (tn + fn))
	print "ACCURACY:         ", str((tp + tn) / float(tp + tn + fp + fn))
	return (tp + tn) / float(tp + tn + fp + fn)


if __name__ == "__main__":
	filename, clustername, dataname, goodclusters = argv
	badclusterdetection(clustername, dataname, goodclusters)
