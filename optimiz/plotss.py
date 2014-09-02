import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

delay=np.loadtxt('delay.txt')
vms=np.loadtxt('vms.txt')
que=np.loadtxt('queue.txt')
t1=np.linspace(0,500,num=500)
t2=np.linspace(0,500,num=50)

if 1:

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    offset = 60
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    host.set_xlim(0, 500)
    host.set_ylim(0, np.max(que)+1)

    host.set_xlabel("Time")
    host.set_ylabel("Queue")
    par1.set_ylabel("VMs")
    par2.set_ylabel("Delay")

    p1, = host.plot(t1,que, label="Queue")
    p2, = par1.plot(t1,vms, label="VMs")
    p3, = par2.plot(t2,delay, label="Delay")

    par1.set_ylim(0, np.max(vms)+1)
    par2.set_ylim(0, np.max(delay)+1)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    plt.grid(True)
    plt.draw()
    plt.show()