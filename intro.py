import os
import gym
from gym import wrappers
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import animation
from stable_baselines3 import PPO
from pyvirtualdisplay import Display

# user defined variables
task = 'execute'  # train, execute
algorithm = 'PPO'  # PPO
if task == 'execute':
    stamp = '20220925-123523'
elif task == 'train':
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
cp_dir = f'logs/checkpoints/{algorithm}/{stamp}/'
# cp_dir = f'logs/checkpoints/{algorithm}/20220918-221234/'
model_file = f'90000'
tboard_dir = 'logs/tensorboard'
# render_dir = f'{models_dir}{model_file[:-4]}_render/'
# render_file = f'{model_file[:-4]}.gif'
timesteps = 10000
episodes = 10

# virtual_display = Display(visible=0, size=(1400, 900))
# virtual_display.start()

# env = gym.make('LunarLander-v2')  # continuous: LunarLanderContinuous-v2
env = 

# env = wrappers.Monitor(env, render_dir)
env.reset()

if task == 'train':
    if not os.path.exists(cp_dir):
        os.makedirs(cp_dir)
    if not os.path.exists(tboard_dir):
        os.makedirs(tboard_dir)

    if algorithm == 'PPO':
        model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=tboard_dir)
    else: 
        print('WARNING: algorithm is not supported running random')
    # train and save
    for i in range(1, episodes):
        model.learn(total_timesteps=timesteps, reset_num_timesteps=False, tb_log_name=algorithm)
        model.save(f'{cp_dir}/{timesteps*i}')

if task == 'execute':
    model = PPO.load(cp_dir+model_file, env=env)
    for ep in range(episodes):
        obs = env.reset()
        done = False
        while not done:
            env.render()
            action, _ = model.predict(obs)
            obs, reward, done, info = env.step(action)

env.close()

