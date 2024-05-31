import numpy as np
from environment import Environment
from q_learning_agent import QLearningAgent

def main():
    # Define the grid size and obstacles
    grid_size = 10
    obstacles = [[1, 2], [2, 3], [3, 4]]

    # Create the environment and agent
    env = Environment(grid_size, obstacles)
    agent = QLearningAgent(grid_size, 4)

    # Training the agent
    num_episodes = 1000
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            current_position = env.car_position
            action = agent.choose_action(current_position)
            next_state, reward, done = env.step(action)
            next_position = env.car_position
            agent.learn(current_position, action, reward, next_position)
            total_reward += reward

            # Debug: Print the car's position, action, and reward
            print(f"Episode: {episode}, Position: {current_position}, Action: {action}, Reward: {reward}, Done: {done}")

        if episode % 100 == 0:
            print(f"Episode: {episode}, Total Reward: {total_reward}")

    # Save the trained Q-table
    np.save('q_table.npy', agent.q_table)

if __name__ == "__main__":
    main()
