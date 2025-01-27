'''
Challenge 1: Counting Fuel Cells
Concepts: Loops, Lists, Operators

The player finds a container filled with fuel cells labeled with their energy levels (e.g., [10, 20, 15, 5, 30]).
They must loop through the list, count cells with energy above a certain threshold (e.g., 10), and calculate 
the total energy.
'''
def count_and_sum_fuel_cells(energy_lvl,threshold):
    count = 0
    total_energy = 0
    for energy in energy_lvl:
        if energy > threshold:
            count += 1
            total_energy += energy

    return count,total_energy

energy_lvl = [10,20,5,15,30]
threshold = 10
count,total = count_and_sum_fuel_cells(energy_lvl,threshold)
print(count)
print(total)        
