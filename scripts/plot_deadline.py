import numpy as np, matplotlib.pyplot as plt
plt.rcParams.update({"figure.dpi":600,"savefig.dpi":600,"font.size":9})
load = np.linspace(0.4,1.2,200)
miss_be = 1/(1+np.exp(-20*(load-0.78)))*0.7
miss_det = 1/(1+np.exp(-22*(load-0.92)))*0.35
fig = plt.figure(figsize=(3.4,2.6)); ax = fig.add_subplot(111)
ax.plot(load,miss_be,label="Best-Effort Path")
ax.plot(load,miss_det,label="Deterministic Scheduler")
ax.set(xlabel="Offered Load (normalized)", ylabel="Deadline Miss Rate",
       title="Control Timeliness Under Stress (Illustrative)")
ax.grid(True, linewidth=0.4, alpha=0.5)
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig("figures/deadline_miss_vs_load.png", bbox_inches="tight")
print("Saved figures/deadline_miss_vs_load.png")