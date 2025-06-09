

import itertools
import random
import multiprocessing


employees = [
    {'name': 'Paul', 'role': 'Engineer', 'department': 'IT'},
    {'name': 'Alex', 'role': 'Manager', 'department': 'HR'},
    {'name': 'Ama', 'role': 'Analyst', 'department': 'IT'},
    {'name': 'Greg', 'role': 'Cleaner', 'department': 'HR'},
    {'name': 'Kwesi', 'role': 'Analyst', 'department': 'IT'},
    {'name': 'Bright', 'role': 'Cleaner', 'department': 'HR'}
   
]


def generatepairs(data):
    unique_employees = {tuple(e.values()) for e in data}
    giants = list(unique_employees.copy())
    dwarfs = list(unique_employees.copy())
    random.shuffle(giants)
    random.shuffle(dwarfs)
    employee_pairs = list(zip(giants, dwarfs))
    unique_pairs = list(filter(lambda x: x[0][0] != x[1][0], employee_pairs))
    res = [(dwarf[0], giant[0]) for dwarf, giant in unique_pairs]
    return res




def runProgramInChunks(chunksNumber):
    chunk_size = chunksNumber 
    chunks = [employees[i:i + chunk_size] for i in range(0, len(employees), chunk_size)]
    pool = multiprocessing.Pool()
    results = pool.map(generatepairs, chunks)
    flatten_results_list = list(itertools.chain(*results))
    final_result = list(set(flatten_results_list))
    print(final_result)
    


if __name__ == "__main__":
    chunk_size = 100
    runProgramInChunks(chunk_size)