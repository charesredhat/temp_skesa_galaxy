import sys

from pathlib import Path

path1 = sys.argv[1]

cores = sys.argv[2]

memory = sys.argv[2]

print(path1)

#print(path2)

pathlist = Path(path1).glob('*fastq*')

i = 0
skcmd = []

skcmd.append("skesa ")

for path in pathlist:
    # because path is object not string-wq
    i += 1
    path_in_str = str(path)
    if i == 2:
        skcmd.append("," + path_in_str)
        #print("," + path_in_str)
        i = 0
    if i == 1:
        skcmd.append(" --fastq " + path_in_str)
        #print(" --fastq " + path_in_str) 

    

if cores != 0:
    skcmd.append(" --cores " + cores)
    

skcmd.append(" --memory " + memory)

skcmds = ''.join(skcmd)
print(skcmds) 
