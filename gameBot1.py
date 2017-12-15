# imports two libraries: gym, which is from open ai and supports a bunch of
# machine learning stuff, and universe, which im not too sure does
# ah there it is, univers let syou run s many environmetns as you want in parallel
import gym
import universe
# random is essential for randomly generating movements that will be sifted through for optimal score/distance
import random

# using neon racers as the test environment; this just configures the env based on gym syntax
env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) # creates a local docker container
# i guess creating this container makes it portable. i dont really know lol
# also id guess you HAVE TO HAVE docker running while this is running as well

# env.reset() generates an observation that is specific to the environment (number of pixels,
# score, etc.) - this initiates theenvironment and gets a list of the observatiosn of its initial state
observation_n = env.reset()

# creating variables which the ai uses to control the vehicle; if a key was previously pressed, needs to set it false
# so that if can be changed and does not conflict with the left/right movement
goLeft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), 
			('KeyEvent', 'ArrowRight', False)]
goLeft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), 
			('KeyEvent', 'ArrowRight', True)]

# with nitro
goLeft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), 
			('KeyEvent', 'ArrowRight', False), ('KeyEvent', 'n', True)]

# set variables (initialize with 0)
sum_reward = 0
turn = 0
rewards = []
buffer_size = 100
action = boostForward

# just an infinite loop where up arrow is pressed for all observations
while True:

	turn -= 1
	if turn <= 0:
		action = boostForward
		turn = 0
	# choose action based on speed
	action_n = [action for ob in observation_n] # this is the agent

	observation_n, reward_n, done_n, info = env.step(action_n) # reinforcement learning action by agent
	print('observation: ', observation_n) # prints out the observation information for debugging purposes
	# and so we can understand what exactly the observation_n is itself
	print('reward: ', reward_n) # see if the reward was +/-1

	sum_reward += reward_n[0]

	rewards += [reward_n[0]]

	# try going towards one side for a while for some time if you get stuck
	if len(rewards) >= buffer_size:
		mean = sum(rewards)/len(rewards)

		if mean == 0:
			turn = 25
			if random.random > 0.5:
				action = goLeft
			else:
				action = goRight
		rewards = []

	env.render() # run agent on environment - i suppose that this needs to be run every time, because
	# the agent must be run every time its in the loop (thats how the agent keeps running)


# stuff from 100DaysOfCode
# import gym
# import universe # register the universe environments
# import random

# env = gym.make('flashgames.NeonRace-v0')
# env.configure(remotes=1) # automatically creates a local docker container
# observation_n = env.reset()

# # Create variable for moving the car
# goleft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
#         ('KeyEvent', 'ArrowRight', False)]
# goright = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
#          ('KeyEvent', 'ArrowRight', True)]

# # Move the car forward with nitroboost 
# boostforward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowRight', False),
#        ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'n', True)]


# sum_reward = 0
# turn = 0
# rewards = []
# buffer_size = 100
# action = boostforward

# while True:
    
#     turn -= 1
#     if turn <= 0:
#         action = boostforward
#         turn = 0
#     # choose action based on speed
#     action_n = [action for ob in observation_n]
    
#     # perform action
#     observation_n, reward_n, done_n, info = env.step(action_n)

#     sum_reward += reward_n[0]
    
#     rewards += [reward_n[0]]
#     #if stuck, try going one side for some time
#     if len(rewards) >= buffer_size:
#         mean = sum(rewards)/len(rewards)
        
#         if mean == 0:
#             turn = 25 
#             if random.random() < 0.5:
#                 action = goleft
#             else:
#                 action = goright
        
#         rewards = []

#     env.render()