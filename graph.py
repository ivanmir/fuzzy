import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import skfuzzy as fuzz

def build_graph(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(graph_url)

def build_x0(xpts, ypts, labels, colors):
    fig0, ax0 = plt.subplots()
    for label in range(3):
        ax0.plot(xpts[labels == label], ypts[labels == label], '.',
                color=colors[label])
    ax0.set_title('Test data: 200 points x3 clusters.')
    return fig0

def build_x1(xpts, ypts, labels, colors, np):
    fpcs = []
    fig1, axes1 = plt.subplots(3, 3, figsize=(8, 8))
    alldata = np.vstack((xpts, ypts))

    for ncenters, ax in enumerate(axes1.reshape(-1), 2):
        cntr, u, u0, d, jm, p, fpc = fuzz._cluster.cmeans(
            alldata, ncenters, 2, error=0.005, maxiter=1000, init=None)

        # Store fpc values for later
        fpcs.append(fpc)

        # Plot assigned clusters, for each data point in training set
        cluster_membership = np.argmax(u, axis=0)
        for j in range(ncenters):
            ax.plot(xpts[cluster_membership == j],
                    ypts[cluster_membership == j], '.', color=colors[j])

        # Mark the center of each fuzzy cluster
        for pt in cntr:
            ax.plot(pt[0], pt[1], 'rs')

        ax.set_title('Centers = {0}; FPC = {1:.2f}'.format(ncenters, fpc))
        ax.axis('off')
    
    return fig1, fpcs

def build_x2(xpts, ypts, labels, colors, np, fpcs):
    
    fig2, ax2 = plt.subplots()
    ax2.plot(np.r_[2:11], fpcs)
    ax2.set_xlabel("Number of centers")
    ax2.set_ylabel("Fuzzy partition coefficient")

    return fig2

def build_x3(xpts, ypts, labels, colors, np):
    alldata = np.vstack((xpts, ypts))
    # Regenerate fuzzy model with 3 cluster centers - note that center ordering
    # is random in this clustering algorithm, so the centers may change places
    cntr, u_orig, _, _, _, _, _ = fuzz._cluster.cmeans(
        alldata, 3, 2, error=0.005, maxiter=1000)

    # Show 3-cluster model
    fig3, ax2 = plt.subplots()
    ax2.set_title('Trained model')
    for j in range(3):
        ax2.plot(alldata[0, u_orig.argmax(axis=0) == j],
                alldata[1, u_orig.argmax(axis=0) == j], 'o',
                label='series ' + str(j))
    ax2.legend()

    return fig3
