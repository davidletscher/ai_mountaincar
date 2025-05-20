# Based on Gymnasium MountainCar

import random
from math import sin, pi, fabs

class MountainCar:
	def __init__(self):
		self._gravity = .0025
		self._force = .00075
		
		# x = 0 is bottom of hill, x=-1,1 are tops
		self._x = random.uniform(-.1, .1)
		self._v = 0.
		
		self._iteration = 0
		self._totalReward = 0
		
	def state(self):
		return (self._x, self._v)
	
	def actions(self):
		return [-1,0,1] # Acclerate left, don't accelerate, accelerate right
	
	def observe(self):
		return (self._x, self._v)
		
	def apply(self, action):
		if action not in [-1,0,1]:
			raise ValueError('Invalid action')
			
		self._v += action*self._force - sin(pi*self._x) * self._gravity
		self._v = min(.5, max(-.5, self._v))
		
		self._x += self._v
		self._x = min(.99, max(-.99, self._x))
		
		self._iteration += 1
		
		self._totalReward += self.reward()
		
	def reward(self):
		if self._x <= -.99:
			return -50
		elif self._x >= .99:
			return 100
		else:
			return -.1
			
	def totalReward(self):
		return self._totalReward
		
	def done(self):
		return fabs(self._x) >= .99 or self._iteration == 500
		
	def __str__(self):
		return f'Position = {self._x:.3f}, velocity = {self._v:.3f}'
		
