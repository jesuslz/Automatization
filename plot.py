import numpy as np 
import matplotlib.pyplot as plt 

data = 	[[5475, 4522, 746, 0, 207, 0 ],
	     [4801,	3992, 592, 0, 217, 0 ],
	     [6818, 4971, 1638, 0, 209, 0 ], 
	     [4859,	3846, 789,  0, 224, 0 ],
         [7986, 5987, 134, 0, 234, 90 ],
         [8997, 6742, 1987, 0, 123, 0 ],
         [6097, 1233, 4562, 0, 143, 0]]

columns = ['8/20/18', '8/21/18', '8/22/18', '8/23/18', '8/24/18', '8/25/18', '8/26/18']
rows = ['%s ' % x for x in ['total', 'completed', 'failed', 'in_prog', 'timeout', 'trans_fail']]

'''calcular el limite superior del eje 7'''
#y_limit_superior = max(np.array(data)[:,0])
#print(y_limit_superior)
yLimitSuperior = (max(max(data)) + 1000) - (max(max(data)) + 1000) % 1000

values = np.arange(0, yLimitSuperior, 1000)
value_increment = 1000

#colores
colors = ['#F23D2B', '#1588CE', '#FEE734', '#986B45', '#652981', '#169C72']
n_rows = len(data)

y_offset = np.zeros(len(columns))

data_numpy = np.array(data)
for i in range(len(data_numpy[0])):
    plt.plot(columns, data_numpy[:,i], color = colors[i], marker = 'o', markersize = 2)

# Add a table at the bottom of the axes
the_table = plt.table(cellText=data_numpy.transpose(),
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      cellLoc = 'center',
                      fontsize = 2,
                      loc='bottom')

the_table.set_fontsize(8)
plt.subplots_adjust(left=0.2, bottom=0.25)

plt.ylabel("Frecuancia")
plt.yticks(values, ['%d' % val for val in values])
#plt.xticks(np.arange(0, 7), [])
plt.autoscale()
plt.xticks([])
plt.title('WASS')
plt.grid(linestyle = "--")
plt.show()

plt.savefig('was2.png', dpi = 500)
