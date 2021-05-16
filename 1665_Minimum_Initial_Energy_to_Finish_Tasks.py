class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0], reverse=True)
        init_energy = tasks[0][1]
        energy_left = tasks[0][1] - tasks[0][0]
        i = 1
        while i < len(tasks):
            last_task = tasks[i-1]
            if energy_left < tasks[i][1]:
                init_energy += (tasks[i][1] - energy_left)
                energy_left = tasks[i][1] - tasks[i][0]
            else:
                energy_left -=  tasks[i][0]
            i += 1
        return init_energy
    
