# ✈️ Explainable Deep RL Jet Agent in Pygame 🕹️

## 📖 Overview  

This project implements a **Deep Reinforcement Learning (DRL) Agent** that simulates a **fighter jet** in a custom **Pygame + Gym environment**.  

The unique twist? 🤔 It’s **Explainable AI (XAI)**.  
Not only does the agent make decisions, but it also **explains why** — by comparing Q-values for *all possible actions* (counterfactual reasoning).  

✅ Great portfolio project for **AI/ML engineers**  
✅ Combines **Game AI, RL, and Explainability**  
✅ Built with **Python, PyTorch, Gym, and Pygame**  



## 🎯 Features  

- 🕹️ **Custom Jet Environment** built with Pygame  
- 🧠 **Deep Q-Network (DQN)** agent with training loop  
- 🔍 **Explainable Decisions**: shows Q-values for each possible action  
- 🚀 **Live Visualization**: watch your jet dodge enemies in real time  
- 📊 **Reinforcement Learning Training** loop included  



## 🛠️ Installation  

Clone the repo & install dependencies:  

```bash
git clone https://github.com/yourusername/explainable-jet-rl-ai.git
cd explainable-jet-rl-ai
pip install -r requirements.txt
```



## ▶️ Usage  

Run the training loop:  

```bash
python train.py
```

Example console output:  

```
Episode 0, State [0.5, 0.875, 0.3, 0.125], 
Action 2, Explanation {'Action 0': -0.04, 'Action 1': 0.15, 'Action 2': 0.87}
Episode 0 finished with reward 1.0
```

👆 The agent chose **Action 2 (Right)** because its Q-value (0.87) was higher than the alternatives.  



## 📂 Project Structure  

```
explainable-jet-rl-ai/
│── jet_env.py            # Jet environment (Pygame + Gym)
│── explainable_agent.py  # DQN + Explainability logic
│── train.py              # Training loop with explanations
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```



## 🚀 Roadmap  

- [ ] Add jet weapons & combat mechanics 🔫  
- [ ] Add multiple enemy jets 🛩️  
- [ ] Save & load trained models 💾  
- [ ] Integrate with `stable-baselines3` for advanced RL 🧠  
