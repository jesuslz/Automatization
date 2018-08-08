import matplotlib.pyplot as plt 
import numpy as np
def plot_ASAP(fig, ax, x, y, titulo, angle):
    '''
    plt.plot(x, y, marker='o')
    plt.grid()
    plt.xticks([i for i in range(7)], ['%s' % i for i in x], rotation=45)

    plt.autoscale(tight=True)
    plt.show()'''


    #fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, marker = 'o')

    # Set number of ticks for x-axis
    #ax.set_xticks([i for i in range(7)])
    # Set ticks labels for x-axis
    ax.set_xticklabels(x, rotation=angle)
    plt.title(titulo)
    ax.grid()

def show_plot():
    plt.show()


x = ['7/30/2018', '7/31/2018', '8/1/2018',
     '8/2/2018', '8/3/2018', '8/4/2018', '8/5/2018']
y = [1234, 654, 98, 0, 123, 0, 75]
a = [876, 13, 45, 0, 43, 43, 5]
fig, ax = plt.subplots(1, 1)
plot_ASAP(fig, ax, x, y, 'WASS', 25)
plot_ASAP(fig, ax, x, a, '', 25)
show_plot()

