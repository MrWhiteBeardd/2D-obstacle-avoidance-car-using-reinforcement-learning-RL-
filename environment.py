import numpy as np

class Environment:
    def __init__(self, grid_size, obstacles):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.goal = [grid_size - 1, grid_size - 1]
        self.reset()

    def reset(self):
        self.car_position = [0, 0]
        self.state = np.zeros((self.grid_size, self.grid_size))
        for obs in self.obstacles:
            self.state[obs[0], obs[1]] = -1
        self.state[self.goal[0], self.goal[1]] = 1
        return self.state

    def step(self, action):
        next_position = self.car_position.copy()
        if action == 0:  # up
            next_position[0] = max(next_position[0] - 1, 0)
        elif action == 1:  # down
            next_position[0] = min(next_position[0] + 1, self.grid_size - 1)
        elif action == 2:  # left
            next_position[1] = max(next_position[1] - 1, 0)
        elif action == 3:  # right
            next_position[1] = min(next_position[1] + 1, self.grid_size - 1)

        reward = -1  # default penalty for each move
        if next_position == self.goal:
            reward = 100  # reward for reaching the goal
            done = True
        elif next_position in self.obstacles:
            reward = -100  # penalty for hitting an obstacle
            done = True
        else:
            done = False

        self.car_position = next_position
        return self.state, reward, done

    def get_state(self):
        state = np.zeros((self.grid_size, self.grid_size))
        for obs in self.obstacles:
            state[obs[0], obs[1]] = -1
        state[self.goal[0], self.goal[1]] = 1
        state[self.car_position[0], self.car_position[1]] = 2
        return state
