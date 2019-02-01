import subprocess
import numpy as np
from .Buffers import buffers
import json
import sys
import readline
import matplotlib

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    X = req
    x = json.loads(X)
    polygons = buffers.voronoi_polygons(np.array(x))
    polygons.plot(color='red', markersize=100, figsize=(4, 4))
    import matplotlib.pyplot as plt
    plt.savefig('/dev/stdout',format='png')
