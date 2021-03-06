from osim.env import L2M2019Env

if __name__ == "__main__":
    env = L2M2019Env(visualize=True)
    observation = env.reset()
    for i in range(200):
        observation, reward, done, info = env.step(env.action_space.sample())