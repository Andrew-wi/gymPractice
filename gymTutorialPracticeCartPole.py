import gym
env = gym.make('CartPole-v0') # create the cart pole environment
# create a number of episodes to go through
# store the high score
highscore = 0
for nth_episode in range(20):
	observation = env.reset() # create a new observation based on the environment in
	points = 0 # keep track of the reward per episode
	while True:
	    env.render() # render the environment again after one new step
	    action = 1 if observation[2] > 0 else 0 # if angle positive, move right, if neg, move left
	    if observation[2] < -20 or observation[2] > 20:
	    	break
	    observation, reward, done, info = env.step(action) # take a new step based on the randomly generated action
	    points += reward
	    print(points)
	    if done:
	    	if points > highscore:
	    		highscore = points
		    	# check if done; if this is so, then set highscore = points and break to move to next episode
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