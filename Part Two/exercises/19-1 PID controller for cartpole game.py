import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

# PID parameters (adjust for best performance)
Kp = 1  # Proportional gain
Ki = 0.1   # Integral gain
Kd = 0.1   # Derivative gain

# Initialize environment with render_mode
env = gym.make('CartPole-v1', render_mode="human")
episodes = 100
scores = []

for e in range(episodes):
    state, _ = env.reset()
    score = 0
    done = False

    # Initialize PID variables
    integral_error = 0
    previous_error = 0

    while not done:
        pole_angle = state[2]
        pole_velocity = state[3]

        error = -pole_angle 
        integral_error += error
        integral_error = np.clip(integral_error, -10, 10)  
        derivative_error = -pole_velocity  

        control_signal = Kp * error + Ki * integral_error + Kd * derivative_error

        action = 1 if control_signal > 0 else 0

        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        score += reward

    scores.append(score)
    print(f"Episode {e+1}: Score = {score}")

env.close()

plt.figure(figsize=(10, 6))
plt.plot(scores, alpha=0.6, label='Episode scores')

window = 10
rolling_avg = [np.mean(scores[max(0, i - window + 1):i + 1]) for i in range(len(scores))]
plt.plot(rolling_avg, linewidth=2, label=f'{window}-episode average')

plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('PID Controller Performance on CartPole-v1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
