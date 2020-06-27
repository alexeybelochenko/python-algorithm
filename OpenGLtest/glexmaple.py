import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys
from opensimplex import OpenSimplex

class Terrain(object):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.show()
        self.w.setWindowTitle('Example')
        self.w.setCameraPosition(distance=30, elevation=8)

        grid = gl.GLGridItem()
        grid.scale(2,2,2)
        self.w.addItem(grid)

        self.nstep = 1
        self.ypoints = range(-20, 22, self.nstep)
        self.xpoints = range(-20, 22, self.nstep)
        self.nfaces = len(self.ypoints)

        verts = np.array([
            [
                x,y,0
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)

        ], dtype=np.float32)

        faces = []

        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append()


    
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    t = Terrain()
    t.start()