#from eve import Eve
#from flask import jsonify, Flask
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import timeit
start = timeit.default_timer()
data = pd.read_csv('/volume1/sample.csv')
data.head()
f1 = data['V1'].values
f2 = data['V2'].values
X=np.matrix(list(zip(f1,f2)))
kmeans = KMeans(n_clusters=20)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
print (centroids)
stop = timeit.default_timer()
print ('Total runtime is ', stop - start)

#app = Eve()
#@app.route('/result')
#def processor():
    #centdata = [kmeans.cluster_centers_]
    #kmeans = KMeans(n_clusters=100)
    #kmeans = kmeans.fit(X)
    #labels = kmeans.predict(X)
    #centroids = kmeans.cluster_centers_
    #return (kmeans.cluster_centers_)

#if __name__ == '__main__':
#    app.run()
