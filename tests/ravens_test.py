# TODO: add to config

N_EPISODES = 10
ASSETS_ROOT = 'ravens/environments/assets/'

# initialize environment
env = Environment(
    FLAGS.assets_root,
    disp=FLAGS.disp,
    shared_memory=FLAGS.shared_memory,
    hz=480)

for i in range(N_EPISODES):
    print(f'Environment Test: {i + 1}/{N_EPISODES}')
    env.set_task(task)
    obs = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.render()