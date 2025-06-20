


class TermostatLearningAgent:
    def __init__(self, initial_setpoint=20.0, learning_rate=0.1):
        self.setpoint = initial_setpoint
        self.learning_rate = learning_rate
        self.history = []

    def perceive(self, current_temperature):
        return current_temperature

    def decide(self, current_temperature):
        if current_temperature < self.setpoint:
            return 'heating_on'
        else:
            return 'heating_off'

    def act(self, decision):
        if decision == 'heating_on':
            print("Azioni: 🔥 Riscaldamento acceso")
        elif decision == 'heating_off':
            print("Azioni: ❄️ Riscaldamento spento")

    def evaluate_reward(self, current_temperature):
        # reward assegantion to get into confort zone (20 - 22 C)
        if 20.0 <= current_temperature <= 22.0:
            return 1.0  # high reinforcement
        else:
            return -1.0  # low reinforcement

    def learn(self, current_temperature):
        reward = self.evaluate_reward(current_temperature)
        error = reward

        if current_temperature < 20.0:
            self.setpoint += self.learning_rate * abs(error)
        elif current_temperature > 22.0:
            self.setpoint -= self.learning_rate * abs(error)

        self.history.append((current_temperature, self.setpoint, reward))

        print(f"[Learning] Nuovo setpoint: {self.setpoint:.2f}°C | Reward: {reward}")

agent = TermostatLearningAgent()


temperature_readings = [18.5, 19.0, 21.0, 22.5, 20.0, 19.5]

for temp in temperature_readings:
    print(f"\nTemperatura percepita: {temp}°C")
    current_temp = agent.perceive(temp)
    decision = agent.decide(current_temp)
    agent.act(decision)
    agent.learn(current_temp)


