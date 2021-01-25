"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

class Boid:
    def __init__(self,xs,ys,xvs,yvs):
        #define xs ys xvs yvs
        #define global properties
        
    def _fly_towards_the_middle(self,pos,vel,pos_adj):
        return pos+(pos_adj-pos)*0.01/len(xs) #ToDo: add len(xs) to properties
    
    def _fly_away_from_nearby_boids(self,pos,vel,pos_adj):
        return vel+(pos-pos_adj)
    
    def update_boids(self):
        for i in range(len(xs)):
            for j in range(len(xs)): 
                xvs[i] = _fly_towards_the_middle(xvs[i],xs[i],xs[j])
                yvs[i] = _fly_towards_the_middle(yvs[i],ys[i],ys[j])
                
        for i in range(len(xs)):
            for j in range(len(xs)): 
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100: #toDo: add condition check as a hidden method
                    xvs[i] = _fly_away_from_nearby_boids(xs[i],xvs[i],xs[j])
                    yvs[i] = _fly_away_from_nearby_boids(ys[i],yvs[i],ys[j])
                    
                    
                    
                    
def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            
    for i in range(len(xs)):
        for j in range(len(xs)):
            
    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
