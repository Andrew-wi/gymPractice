import gym
env = gym.make('Hopper-v1') # create the cart pole environment
# create a number of episodes to go through
for nth_episode in range(20):
	observation = env.reset() # create a new observation based on the environment in
	for x in range(100):
	    env.render() # render the environment again after one new step
	    print(observation) # prints the observations for debugging purposes
	    action = env.action_space.sample() # random action
	    print(action)
	    observation, reward, done, info = env.step(action) # take a new step based on the randomly generated action
	    if done: # check if done; if this is so, then print end of episode
	    	print("finished after {} timesteps".format(x+1))
	    	break


# # from gym documentation itself
# import gym
# env = gym.make('CartPole-v0')
# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break