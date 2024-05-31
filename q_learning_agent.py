import numpy as np

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay=0.995):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.q_table = np.zeros((state_size, state_size, action_size))

    def choose_action(self, position):
        x, y = position
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_size)
        return np.argmax(self.q_table[x, y])

    def learn(self, position, action, reward, next_position):
        x, y = position
        next_x, next_y = next_position
        best_next_action = np.argmax(self.q_table[next_x, next_y])
        td_target = reward + self.discount_factor * self.q_table[next_x, next_y, best_next_action]
        td_error = td_target - self.q_table[x, y, action]
        self.q_table[x, y, action] += self.learning_rate * td_error

        self.exploration_rate *= self.exploration_decay
