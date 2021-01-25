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
        self.num_boids = len(xs)
        
    @property
    def LIMIT(self):
        return 100
    @property
    def VEL_LIMIT(self):
        return 0.125
    
    def _fly_towards_the_middle(self,pos,vel,pos_adj):
        return pos+(pos_adj-pos)/self.num_boids/self.LIMIT #ToDo: add len(xs) to properties
    
    def _fly_away_from_nearby_boids(self,pos,vel,pos_adj):
        return vel+(pos-pos_adj)*self.VEL_LIMIT/self.num_boids
    
    def _match_speed(self, vel,vel_adj):
        return vel+(vel_adj-vel)*
    
    def _move(pos,vel):
        return pos+vel
    def _must_fly_away_or_match_speed(self,x1,x2,y1,y2, choice):
        if choice=='fly_away':
            L = self.LIMIT**2
        if choice=='match_speed':
            L = self.LIMIT**2
        else:
            raise ValueError
        return (x1-x2)**2 + (y1-y2)**2 < L
    
    def update_boids(self):
        for i in range(self.num_boids):
            for j in range(self.num_boids): 
                xvs[i] = self._fly_towards_the_middle(xvs[i],xs[i],xs[j])
                yvs[i] = self._fly_towards_the_middle(yvs[i],ys[i],ys[j])
                
        for i in range(self.num_boids):
            for j in range(self.num_boids): 
                if self.must_fly_away_or_match_speed(x[i],x[j],y[i],y[j],'fly_away'): #toDo: add condition check as a hidden method
                    xvs[i] = self._fly_away_from_nearby_boids(xs[i],xvs[i],xs[j])
                    yvs[i] = self._fly_away_from_nearby_boids(ys[i],yvs[i],ys[j])

        for i in range(self.num_boids):
            for j in range(self.num_boids): 
                if self._must_fly_away_or_match_speed('match_speed') :
                    xvs[i] = self._match_speed(xvs[i],xvs[j])
                    yvs[i] = self._match_speed(yvs[i],yvs[j])
                    
        
        for i in range(self.num_boids):
            xs[i] = self._move(xs[i]+xvs[i])
            ys[i] = self._move(ys[i]+yvs[i])
                    
                    
'''                    
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
        ys[i]=ys[i]+yvs[i]'''


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
