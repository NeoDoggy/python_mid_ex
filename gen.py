import os


tasknums=[3,5,5]

for i in range(0,3):
    for j in range(0,tasknums[i]):
        os.system(f'> ./tasks/{i+1}_{j+1}.in')
        os.system(f'> ./tasks/{i+1}_{j+1}.out')
