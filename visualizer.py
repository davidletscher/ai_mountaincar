from cs1graphics import *
from math import cos, pi
import time

class Visualizer:
	def __init__(self, size, delay=.01):
		self._size = size
		self._canvas = Canvas(size, 1.2*size)
		self._delay = delay

		self._canvas.setBackgroundColor('skyblue')
		self._canvas.setTitle('Mountain Car')
		
		p = Polygon([Point(size,1.2*size), Point(0,1.2*size)])
		p.setFillColor('green')
		for x in [ .01*i for i in range(-100,101) ]:
			y = -cos(pi*x)
			p.addPoint(self.pt(x,y))
			
		self._canvas.add(p)
		
		self._car = Circle(.025*size, self.pt(0,-1))
		self._car.setFillColor('red')
		self._canvas.add(self._car)
		
		self._score = Text('0', int(.1*size), self.pt(0,1))
		self._canvas.add(self._score)
		0
		self._neutral = Path([Point(.4*size, .3*size), Point(.6*size, .3*size)])
		self._neutral.setBorderWidth(.01*size)
		self._neutral.setBorderColor('purple')
		self._canvas.add(self._neutral)
		
		self._right = Path([Point(.55*size, .25*size), Point(.6*size, .3*size), Point(.55*size, .35*size)])
		self._right.setBorderWidth(.01*size)
		self._right.setBorderColor('purple')
		self._canvas.add(self._right)
		
		self._left = Path([Point(.45*size, .25*size), Point(.4*size, .3*size), Point(.45*size, .35*size)])
		self._left.setBorderWidth(.01*size)
		self._left.setBorderColor('purple')
		self._canvas.add(self._left)
		
			
	def pt(self, x, y):
		return Point(.5*(x+1)*self._size, .5*(-y+1)*self._size + .1*self._size)

	def update(self, car, action, reward):
		pos = car.observe()
		x = pos[0]
		y = -cos(pi*x)
		pt = self.pt(x,y)
		self._car.moveTo(pt.getX(), pt.getY())
		
		self._score.setMessage(f'{reward:.2f}')
		
		if action == -1:
			self._right.setBorderColor('transparent')
			self._left.setBorderColor('purple')
		elif action == 0:
			self._right.setBorderColor('transparent')
			self._left.setBorderColor('transparent')
		elif action == 1:
			self._right.setBorderColor('purple')
			self._left.setBorderColor('transparent')
		
		time.sleep(self._delay)
