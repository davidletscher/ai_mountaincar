import sys, importlib, argparse
from mountaincar import *

def run(car, agent, visualizer):
	print('Starting simulation')
	while not car.done():
		action = agent.chooseAction(car.observe(), car.actions())
		car.apply(action)
		reward = car.totalReward()
		if visualizer:
			visualizer.update(car, action, reward)
		obs = car.observe()
		print(f'Iteration {car._iteration}.  State is {car}.  Observing ({obs[0]:.3f}, {obs[1]:.3f}), choosing action {action} and total reward {reward:.2f}.')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description ='Simulate the Mountain Car.')
	parser.add_argument('agent_file')
	parser.add_argument('-g', type=int, help="size of graphics window")
	parser.add_argument('-d', type=float, help="time delay between steps")
	args = parser.parse_args()

	try:
		agentModule = importlib.import_module(args.agent_file.split('.')[0])
	except:
		print('Invalid agent module')
		sys.exit()
	  
	if args.g:
		from visualizer import *
		if args.d:
			visualizer = Visualizer(args.g, args.d)
		else:
			visualizer = Visualizer(args.g)
	else:
		visualizer = None
  
	car = MountainCar()
	agent = agentModule.Agent()

	run(car, agent, visualizer)

