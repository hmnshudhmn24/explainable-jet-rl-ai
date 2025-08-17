import numpy as np
from jet_env import JetEnv
from explainable_agent import ExplainableAgent

env = JetEnv()
agent = ExplainableAgent(state_dim=4, action_dim=3)

episodes = 50
for ep in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, explanation = agent.explain_action(state)
        print(f"Episode {ep}, State {state}, Action {action}, Explanation {explanation}")
        next_state, reward, done, _ = env.step(action)
        agent.store_transition((state, action, reward, next_state, done))
        agent.train()
        state = next_state
        total_reward += reward
        env.render()
    print(f"Episode {ep} finished with reward {total_reward}")
env.close()
