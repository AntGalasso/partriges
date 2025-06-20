import random
import time

class TermostatAgent:
    def __init__(self, setpoint):
        self.setpoint = setpoint

    def perceive(self, current_temperature):
        return current_temperature

    def decide(self, current_temperature):
        if current_temperature <= self.setpoint:
            return 'heating_on'
        else:
            return 'heating_off'

    def act(self, decision):
        return "Azioni: 🔥 Riscaldamento acceso" if decision == 'heating_on' else "Azioni: ❄️ Riscaldamento spento"



def simulate_environment(agent, initial_temperature, steps=10):
    temperature = initial_temperature
    for step in range(steps):
        print(f"\n[Step {step+1}] Temperatura attuale: {temperature:.1f}°C")
        perceived = agent.perceive(temperature)
        decision = agent.decide(perceived)
        agent.act(decision)


        if decision == 'heating_on':
            temperature += random.uniform(0.2, 0.5)  # il riscaldamento alza la temperatura
        else:
            temperature -= random.uniform(0.1, 0.3)  # il freddo la abbassa

        time.sleep(0.5)


agent = TermostatAgent(setpoint=20.0)
simulate_environment(agent, initial_temperature=18.0)
