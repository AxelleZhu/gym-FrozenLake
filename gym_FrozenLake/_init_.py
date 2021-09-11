from gym.envs.registration import register

register(
    id='FrozenLake-v0',
    entry_point='gym_FrozenLake.envs:FrozenLakeEnv',
)
