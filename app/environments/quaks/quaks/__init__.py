from gym.envs.registration import register

register(
    id='Quaks-v0',
    entry_point='quaks.envs.quaks:QuaksEnv',
)
