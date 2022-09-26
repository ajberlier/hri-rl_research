import gym

# hri-rl research
from agents.ppo import PPOAgent

env = gym.make("Pendulum-v0")
model = PPOAgent(env)
model.learn(10000)
