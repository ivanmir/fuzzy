from __future__ import division, print_function
from flask import Flask, render_template
import graph as g
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# Define three cluster centers
centers = [[4, 2],
           [1, 7],
           [5, 6]]

# Define three cluster sigmas in x and y, respectively
sigmas = [[0.8, 0.3],
          [0.3, 0.5],
          [1.1, 0.7]]

def generateTestData():
    # Generate test data
    np.random.seed()  # Set seed for reproducibility
    xpts = np.zeros(1)
    ypts = np.zeros(1)
    labels = np.zeros(1)
    for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
        xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))
        ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
        labels = np.hstack((labels, np.ones(200) * i))
    return xpts, ypts, labels

@app.route('/graphs')
def graphs():
    
    #Clears all previously plotted graphs
    plt.close('all')
    
    #Regenerate random numbers
    xpts, ypts, labels = generateTestData()

    graph1_url = g.build_graph(g.build_x0(xpts, ypts, labels, colors))
    g1, fpcs = g.build_x1(xpts, ypts, labels, colors, np)
    graph2_url = g.build_graph(g1)
    graph3_url = g.build_graph(g.build_x2(xpts, ypts, labels, colors, np, fpcs))
    graph4_url = g.build_graph(g.build_x3(xpts, ypts, labels, colors, np))
 
    return render_template('graphs.html',
    graph1=graph1_url,
    graph2=graph2_url,
    graph3=graph3_url,
    graph4=graph4_url,
    )
 
if __name__ == '__main__':
    app.debug = True
    app.run()