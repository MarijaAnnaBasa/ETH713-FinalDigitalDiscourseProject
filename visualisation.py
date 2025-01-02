import matplotlib.pyplot as plt
import numpy as np

categories_inclusive = ["General", "Cohesive", "Restrictive", "Ambiguous"]
values_inclusive = [23, 17, 0, 2]

group_exclusive = ["Group-restrictive", "Personal", "Regional"]
values_exclusive = [11, 34, 9]

total_inclusive = sum(values_inclusive)
total_exclusive = sum(values_exclusive)

x_inclusive = np.arange(len(categories_inclusive))
x_exclusive = np.arange(len(group_exclusive))

fig, ax = plt.subplots(1, 2, figsize=(12, 7), sharey=True) 

ax[0].bar(x_inclusive, values_inclusive, color='skyblue', alpha=0.8)
ax[0].set_xticks(x_inclusive)
ax[0].set_xticklabels(categories_inclusive, rotation=45, ha="right")
ax[0].set_ylabel("Absolute Frequency")
ax[0].set_xlabel("Inclusive We-Type Usage")
for i, v in enumerate(values_inclusive):
    ax[0].text(i, v + 1, str(v), ha="center", va="bottom", fontsize=10, color="blue")
ax[0].text(1.5, max(total_inclusive, total_exclusive) + 5, f"Total: {total_inclusive}", ha="center", va="bottom", color="blue", fontsize=12)

ax[1].bar(x_exclusive, values_exclusive, color='orange', alpha=0.8)
ax[1].set_xticks(x_exclusive)
ax[1].set_xticklabels(group_exclusive, rotation=45, ha="right")
ax[1].set_ylabel("Absolute Frequency")
ax[1].set_xlabel("Exclusive We-Type Usage")
for i, v in enumerate(values_exclusive):
    ax[1].text(i, v + 1, str(v), ha="center", va="bottom", fontsize=10, color="orange")
ax[1].text(1, max(total_inclusive, total_exclusive) + 5, f"Total: {total_exclusive}", ha="center", va="bottom", color="orange", fontsize=12)

plt.tight_layout()
plt.show()
