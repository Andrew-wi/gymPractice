import gym
env = gym.make('CartPole-v0') # create the cart pole environment
env.reset() # generate the environment
for _ in range(1000):
    env.render() # render the environment again after one new step
    env.step(env.action_space.sample()) # take a random action