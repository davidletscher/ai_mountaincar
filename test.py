import sys, importlib, argparse
from mountaincar import *
from run import *

parser = argparse.ArgumentParser(description ='Simulate the Mountain Car.')
parser.add_argument('agent_file')
parser.add_argument('-n', type=int, default=100, help="number of tests")
args = parser.parse_args()

try:
	agentModule = importlib.import_module(args.agent_file.split('.')[0])
except:
	print('Invalid agent module')
	sys.exit()

totalScore = 0
for i in range(args.n):
	car = MountainCar()
	car._x = -1 + i/args.n
	agent = agentModule.Agent()

	run(car, agent, None)
	print(f'Pass {i+1}, score = {car.totalReward()}')
	totalScore += car.totalReward()
	
print(f'\nAverage = {totalScore/args.n:.2f}')
	


