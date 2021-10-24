import os


tasknums=[3,5,5]

for i in range(0,3):
    for j in range(0,tasknums[i]):
        os.system(f'python3 ACcode_.py < ./tasks/{i+1}_{j+1}.in > ./tasks/{i+1}_{j+1}.ans')
