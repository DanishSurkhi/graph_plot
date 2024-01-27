import numpy as np
import matplotlib.pyplot as plt

time=np.linspace(0,40,100)

distance_of_first_sample=2.5*time
distance_of_secound_sample=3.5*(time-5)

fig, ax = plt.subplots()
plt.title("distance of when the samples intersect")
plt.xlabel("Distance")
plt.ylabel("time")
ax.set_xlim([0,40])
ax.set_ylim([0,100])
ax.plot(time, distance_of_first_sample,c="green")
ax.plot(time, distance_of_secound_sample, c="blue")
plt.axvline(x=17.66, color='purple', linestyle='--')
_ = plt.axhline(y=44.5, color='purple', linestyle='--')

plt.show()