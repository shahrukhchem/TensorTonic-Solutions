from collections import defaultdict
import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points=np.array(points)
    assignments=np.array(assignments)
    clusterdict = defaultdict(list)
    for p,a in zip(points,assignments):
        clusterdict[a].append(p)
    res=[]
    for i in range(k):
        clusterpoints=np.array(clusterdict[i])
        nopincluster=len(clusterpoints)
        if len(clusterpoints) == 0:
            res.append([0] * points.shape[1])  
        else:
            currres=clusterpoints.sum(axis=0)
            currres=currres/nopincluster
            res.append(currres.tolist())
    return list(res)
        
        