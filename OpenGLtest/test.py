from pyqtgraph.Qt import QtGui, QtCore                                              
import pyqtgraph as pg                                                              

app = QtGui.QApplication([])                                                        
view = pg.GraphicsView()                                                            
l = pg.GraphicsLayout()                                                             
view.setCentralItem(l)                                                              
view.show()                                                                         
view.resize(800,600)                                                                

p0 = l.addPlot(0, 0)                                                                
p0.showGrid(x = True, y = True, alpha = 0.3)                                        
#p0.hideAxis('bottom')                                                              
p1 = l.addPlot(1, 0)                                                                
p1.showGrid(x = True, y = True, alpha = 0.3)                                        

p1.setXLink(p0)                                                                     

l.layout.setSpacing(0.)                                                             
l.setContentsMargins(0., 0., 0., 0.)                                                

if __name__ == '__main__':                                                          
    import sys                                                                      
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):         
        QtGui.QApplication.instance().exec_()  