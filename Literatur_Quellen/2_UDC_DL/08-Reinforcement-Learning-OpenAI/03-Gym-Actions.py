import gym
env = gym.make('CartPole-v0')
# print(	)
# #> Discrete(2) 0 - 1 links und rechts
# print(env.observation_space)
# #> Box(4,) [Horizontale Position, Horizontale Geschwindigkeit, Polwinkel, Winkelgeschwindigkeit]
observation = env.reset()

for t in range(1000):

    env.render()

    cart_pos , cart_vel , pole_ang , ang_vel = observation # unpack tuple

    # Move Cart Right if Pole is Falling to the Right

    # Angle is measured off straight vertical line
    if pole_ang > 0: # Positiver Winkel fällt der stab fällt nach links
        # Move Right
        action = 1
    else: # negative fällt der stop nach rechts
        # Move Left
        action = 0

    # Perform Action
    observation , reward, done, info = env.step(action)



