import numpy as np
from matplotlib import pyplot as plt




def function_plot(equation, min, max):

   plt.close('all')

   plt.rcParams["figure.figsize"] = [7.50, 3.50]
   plt.rcParams["figure.autolayout"] = True

   plt.title("f(x) = " + equation)
   plt.xlabel("x")
   plt.ylabel("f(x)")

   x = np.linspace(min, max, 100)

   eq = eval(equation)

   plt.plot(x, eq , color='red')

   plt.show()