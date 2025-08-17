import gym
from gym import spaces
import numpy as np
import pygame

class JetEnv(gym.Env):
    def __init__(self):
        super(JetEnv, self).__init__()
        self.width, self.height = 400, 400
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(3)  # [0: left, 1: straight, 2: right]
        self.reset()
        
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def reset(self):
        self.jet_x, self.jet_y = self.width // 2, self.height - 50
        self.enemy_x, self.enemy_y = np.random.randint(50, 350), 50
        return self._get_obs()

    def _get_obs(self):
        return np.array([self.jet_x/self.width, self.jet_y/self.height,
                         self.enemy_x/self.width, self.enemy_y/self.height], dtype=np.float32)

    def step(self, action):
        if action == 0:
            self.jet_x -= 10
        elif action == 2:
            self.jet_x += 10

        self.enemy_y += 5
        if self.enemy_y > self.height:
            self.enemy_y = 50
            self.enemy_x = np.random.randint(50, 350)

        done = False
        reward = -0.01

        if abs(self.jet_x - self.enemy_x) < 20 and abs(self.jet_y - self.enemy_y) < 20:
            reward = 1
            done = True

        obs = self._get_obs()
        return obs, reward, done, {}

    def render(self, mode="human"):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.jet_x, self.jet_y, 20, 20))  # Jet
        pygame.draw.rect(self.screen, (255, 0, 0), (self.enemy_x, self.enemy_y, 20, 20))  # Enemy
        pygame.display.flip()
        self.clock.tick(30)

    def close(self):
        pygame.quit()
