
import math;
import tkinter;
import sys
import matplotlib.animation as ani
from matplotlib.patches import Circle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
states=[]

steps=0
class View :
    def animation():
        root = tkinter.Tk()
        

        label = tkinter.Label(root,text="Two Body Animation").grid(column=0, row=0)

        r = 2
        def circle(phi, phi_off,offset_x, offset_y):
            return np.array([r*np.cos(phi+phi_off), r*np.sin(phi+phi_off)]) + np.array([offset_x, offset_y])

        plt.rcParams["figure.figsize"] = 8,6
        
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0,row=1)
        
        def Pause():

            return ani.event_source.stop()

#unpause
        def Play():
            return ani.event_source.start()
        

        a=tkinter.Button( root,text="Play", command=Play).grid(column=0,row=2)
        b=tkinter.Button( root,text="Pause", command=Pause).grid(column=0,row=3)
        def endProgam():
            raise SystemExit
            sys.exit()
        


        B = tkinter.Button(root, text = "Exit", command = endProgam).grid(column=1,row=3)
        ax.axis([-30,30,-30,30])
        ax.set_aspect("equal")
        
# create initial conditions
        phi_offs = [ np.pi/2, np.pi] 
        offset_xs = [states[0][0],states[0][1]]
        offset_ys = [states[0][2],states[0][3]]
# amount of points
        N = len(phi_offs)

# create a point in the axes
        points = []
        for i in range(N):
            x,y = circle(0, phi_offs[i], offset_xs[i], offset_ys[i])
            points.append(ax.plot(x, y, marker="o")[0])

        
        
        def update(phi, phi_off, offset_x,offset_y):
          
                
        # set point coordinates
            
            for i in range(N):
                x, y = circle(phi,phi_off[i], offset_x[i], offset_y[i])
                
                points[i].set_data([states[0][i]],[states[0][i+2]])
                
              
            del states[0]
            
        
          #points[i].set_data(states1[0][0],states1[0][1],[state["positions"][i]["y"] ])
            return points
        ani = animation.FuncAnimation(fig,update,
        fargs=(phi_offs, offset_xs, offset_ys), 
        interval = 2, 
        frames=np.linspace(0,2*np.pi,360, endpoint=False),
        blit=True)





        tkinter.mainloop()
        
        


class App:
    def ReadValues():
        f = open("test.txt", "r")
        lines = f.readlines()
        for line in lines:
            coords= line.split(",")
            coords[3]=coords[3].rstrip("\n")
            states.append([float(coords[0]),float(coords[2]),float(coords[1]),float(coords[3])])
            
            
        f.close()
        open('test.txt', 'w').close()


App.ReadValues()

View.animation()