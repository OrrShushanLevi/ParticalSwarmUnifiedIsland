import numpy as np 
class Particle(object) :
    def __init__(self,x0,seed=None):
        self.local_state = np.random.RandomState(seed)
        self.n = len(x0)
        self.current_position = np.copy(x0)          
        self.velocity = self.local_state.uniform(size=self.n)*2 - 1          
        self.position_pbest = np.empty([self.n])          
        self.fitness_pbest = np.inf          
        self.fitness = np.inf
        self.is_gbest = False
        self.is_bounded = False
        
    def evaluate(self,objFunc):
        self.fitness = objFunc(self.current_position)
        if self.fitness < self.fitness_pbest:
            self.position_pbest = np.copy(self.current_position)
            self.fitness_pbest = self.fitness 
        
        
    def update_velocity(self,pos_best_g, c1, c2, omega) :
        r1 = self.local_state.uniform(size=self.n)
        r2 = self.local_state.uniform(size=self.n)
        #In the following, we use element-wise numpy array multiplication on r_i
        vel_cognitive = r1*(self.position_pbest - self.current_position)
        vel_social = r2*(pos_best_g - self.current_position)
        self.velocity = omega*self.velocity + c1*vel_cognitive + c2*vel_social
        
    def update_position(self,lb,ub):
        self.current_position = self.current_position + self.velocity
        #enforce boundary conditions
        self.current_position[self.current_position < lb] = lb
        self.current_position[self.current_position > ub] = ub