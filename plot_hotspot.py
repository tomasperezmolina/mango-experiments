import matplotlib.pyplot as plt
import json
from utils import files_in_dir
import statistics

exp_dir = 'old/experiments-release'

def to_int(a_str):
    return int(a_str)

total_durations = []
resource_allocations = []
resource_deallocations = []
exp_sizes = []
for idx, exp in enumerate(sorted(files_in_dir(exp_dir, include_folders=True), key=to_int)):
    print(exp)
    total_durations.append([])
    resource_allocations.append([])
    resource_deallocations.append([])
    exp_sizes.append(int(exp))
    for run in files_in_dir(f'{exp_dir}/{exp}'):
        with open(f'{exp_dir}/{exp}/{run}', 'r') as f:
            run_data = json.load(f)
            total_durations[idx].append(run_data['total_duration'])
            resource_allocations[idx].append(run_data['resource_allocations'][0]['duration'])
            resource_deallocations[idx].append(run_data['resource_deallocations'][0]['duration'])
    

x = exp_sizes

y_duration = [statistics.mean(es) for es in total_durations]
  
plt.plot(x, y_duration, 'bo')
plt.show()

plt.boxplot(total_durations, showfliers=True)
plt.show()

plt.boxplot(resource_allocations, showfliers=False)
plt.show()

plt.boxplot(resource_deallocations, showfliers=False)
plt.show()