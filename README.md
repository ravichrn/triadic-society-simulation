# 🧬 Triadic Society Simulation

This project is an **agent-based simulation** of a fictional world with a **triadic gender system** built using the [Mesa](https://mesa.readthedocs.io/en/stable/) framework in Python. It models individual agents with unique gender identities, territorial affiliations, and satisfaction levels that evolve through interactions and policy dynamics.

A society with 3 unique genders, each with distinct characteristics, is a random thought I had about 10 years ago. I thought how such a society/world would work, which now turned into a simulation.

## 🌐 World Overview

- **Genders**: Solari, Lunari, Terran
- **Hybrids**: Solari-Lunari, Lunari-Terran, Terran-Solari, Triune
- **Territories**: North, South, East
- **Social Policies**: 
  - `equal_rights` (default) — all genders are treated equally.
  - `favor_solari` — Solari agents are favored, others are penalized.

## 🚀 Features

- Agents interact with each other based on gender and territorial proximity.
- Satisfaction levels evolve with interactions and societal policy effects.
- Visual tracking of:
  - Gender population trends
  - Average societal satisfaction
  - Territorial distribution

## 📦 Requirements

Install Mesa and Matplotlib:

```bash
pip install mesa matplotlib
```

## 🧠 Simulation Logic

- Each agent is initialized with:
  -	A core gender (Solari, Lunari, Terran)
  -	A chance of being a hybrid
  -	Random satisfaction score (0.7 - 1.0)
  -	Assigned to a random territory
  -	Each simulation step:
  -	Agents randomly interact with one another.
  -	Interactions modify satisfaction based on gender and territory.
  -	Policy influences satisfaction at the individual level.
  -	Data is collected for plotting and analysis.

## 🔍 Future Enhancements
-	Add reproduction/mutation mechanics.
-	Implement social mobility across territories.
-	Visualize agent networks and interactions.
-	Allow policy shifts mid-simulation.


## Acknowledgments

This simulation was developed with the assistance of OpenAI’s GPT-4o, using prompt-driven collaboration to explore speculative sociological models and Python agent-based programming with the Mesa framework.
