"""Tests for dvnets.environments.environment."""

from absl.testing import absltest

from envs.cliport import tasks
from envs.cliport.environments import environment

ASSETS_PATH = "/home/ajberlier/Dev/hri-rl_research/envs/cliport/environments/assets/"


class EnvironmentTest(absltest.TestCase):
    def test_environment_action(self):
        env = environment.Environment(ASSETS_PATH)
        task = tasks.BlockInsertion()
        env.set_task(task)
        env.seed(0)
        agent = task.oracle(env)
        obs = env.reset()
        info = None
        done = False
        for _ in range(10):
            act = agent.act(obs, info)
            # self.assertTrue(env.action_space.contains(act))
            obs, _, done, info = env.step(act)
            if done:
                break


if __name__ == "__main__":
    absltest.main()
