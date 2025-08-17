# ✈️ Explainable Deep RL Jet Agent in Pygame 🕹️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/yourusername/explainable-jet-rl-ai?style=social)](https://github.com/yourusername/explainable-jet-rl-ai/stargazers)

---

## 📖 Overview

This project implements a **Deep Reinforcement Learning (DRL) Agent** flying a fighter jet in a **Pygame** environment.  
What makes it special? 🤔 It's **Explainable AI (XAI)** — the agent doesn't just act, it tells you **why** it chose that action by showing alternative Q-values (counterfactuals).

---

## 🎯 Features

- 🕹️ **Custom Jet Environment** built with `pygame` + `gym`
- 🧠 **Deep Q-Network (DQN)** agent with training loop
- 🔍 **Explainable Decisions**: shows Q-values for all possible actions
- 🚀 **Visualization**: watch the jet dodge enemies in real time
- 📈 **Reinforcement Learning Training** included

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/explainable-jet-rl-ai.git
cd explainable-jet-rl-ai

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the training loop:

```bash
python train.py
```

### Example Output

```
Episode 0, State [0.5, 0.875, 0.3, 0.125], Action 2, Explanation {'Action 0': -0.04, 'Action 1': 0.15, 'Action 2': 0.87}
Episode 0 finished with reward 1.0
```

---

## 📂 Project Structure

```
explainable-jet-rl-ai/
│── jet_env.py            # Jet environment in Pygame
│── explainable_agent.py  # DQN with explainability
│── train.py              # Training loop
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## 🚀 Roadmap

- [ ] Add weapons & combat mechanics 🔫
- [ ] Add multiple enemy jets 🛩️
- [ ] Save and load trained models 💾
- [ ] Integrate with `stable-baselines3` for advanced RL 🧠

---

## 🧑‍💻 Contributing

Contributions welcome! 🙌 Fork, improve, and open a PR 🚀

---

## ⭐ Support

If you like this project, **star ⭐ the repo** — it motivates me to build more awesome AI projects!

---

## 📜 License

This project is under the **MIT License**.
