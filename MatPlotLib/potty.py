import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
x=[1,2,3,4,5]
y=[5,10,5,10,20]
mpl.title('north')
mpl.plot(x,y,color='blue',marker='o',mfc='k',mec='k',ms=10,ls='--',lw=3)
mpl.xlabel('south')
mpl.ylabel('west')
mpl.plot([2],[8],"g^")
mpl.show()
