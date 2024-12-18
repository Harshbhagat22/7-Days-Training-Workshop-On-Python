import matplotlib.pyplot as plt
import numpy as np
x = np.array([35,25,20,20])
mycolor = ["Nagpur","Mumbai","Delhi","Kolkata"]
plt.pie(x,labels = mycolor,startangle=90)
plt.show()