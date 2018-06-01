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
        