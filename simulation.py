from mesa import Agent, Model
from mesa.datacollection import DataCollector
import random
import matplotlib.pyplot as plt

# Define triad genders and hybrids
GENDERS = ["Solari", "Lunari", "Terran"]
HYBRIDS = ["Solari-Lunari", "Lunari-Terran", "Terran-Solari", "Triune"]

# Agent class
class TriadicAgent(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.gender = random.choice(GENDERS)
        self.hybrid = random.choice(HYBRIDS) if random.random() < 0.2 else None
        self.satisfaction = random.uniform(0.7, 1.0)

    def step(self):
        # Random fluctuation in satisfaction
        self.satisfaction += random.uniform(-0.05, 0.05)
        self.satisfaction = max(0.0, min(1.0, self.satisfaction))  # Clamp to [0, 1]

# Model class
class TriadicSociety(Model):
    def __init__(self, N=100):
        super().__init__()
        self.num_agents = N

        # Create agents
        for _ in range(self.num_agents):
            TriadicAgent(self)

        # Data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Solari": lambda m: m.count_gender("Solari"),
                "Lunari": lambda m: m.count_gender("Lunari"),
                "Terran": lambda m: m.count_gender("Terran"),
                "Hybrids": self.count_hybrids,
                "AverageSatisfaction": self.average_satisfaction,
            }
        )

    def count_gender(self, gender):
        return sum(1 for a in self.agents if a.gender == gender)

    def count_hybrids(self):
        return sum(1 for a in self.agents if a.hybrid is not None)

    def average_satisfaction(self):
        return sum(a.satisfaction for a in self.agents) / self.num_agents

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")  # Randomly activate agents

# Run the simulation
model = TriadicSociety(N=100)
for _ in range(30):
    model.step()

# Visualize the result
results = model.datacollector.get_model_vars_dataframe()
results.plot(title="Triadic Society Simulation (Mesa 3.2.0)", figsize=(10, 6))
plt.xlabel("Time Step")
plt.ylabel("Population / Satisfaction")
plt.grid(True)
plt.tight_layout()
plt.show()
