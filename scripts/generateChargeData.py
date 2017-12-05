import numpy as np
import sys
from random import *
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]


acid_list = ['E','D']
base_list = ['R','K','H']

if len(sys.argv) < 3:
    sys.exit("ERROR. Enter: python generateChargeData.py pathToSeqFile outputPath")
else:
    seq_file_dir = sys.argv[1]
    out_file_dir = sys.argv[2]
    
seq_file = open(seq_file_dir, 'r')
seq_str = ''
for line in seq_file:
    seq_str = line
    break
seq_file.close()

# Removal of \n
if seq_str[-1] == '\n':
    seq_str = seq_str[:-1]

# Random Initial Charges
charges = randBinList(len(seq_str) + 2) 

# Output file
out_file = open(out_file_dir + '/CHARGE.data', 'w')

# Header
header_str = '#PosInSeq(1 to N+2)\t\tLetter\t\tAcidOrBase(-1 or 1)\t\tInitialCharge\t(N+1,Nter,letter X. N+2,Cter,letter Z)'
out_file.write(header_str + '\n')


total_res_charged = 0
for idx,res in enumerate(seq_str):
    if res in acid_list:
        rnd_chrg = -1 * charges[idx]
        out_file.write(str(idx+1)+'\t\t\t\t'+res+'\t\t'+'-1'+'\t\t\t\t'+str(rnd_chrg)+ '\n')
        total_res_charged += 1
    elif res in base_list:
        rnd_chrg = charges[idx]
        out_file.write(str(idx+1)+'\t\t\t\t'+res+'\t\t'+'1'+'\t\t\t\t'+str(rnd_chrg)+ '\n')
        total_res_charged += 1

# N-terminal and C-terminal
last_position = len(seq_str)

rnd_chrg = charges[last_position] 
out_file.write(str(last_position + 1)+'\t\t\t\t'+'X'+'\t\t'+'1'+'\t\t\t\t'+str(rnd_chrg)+ '\n')
total_res_charged += 1

rnd_chrg = -1 * charges[last_position + 1] 
out_file.write(str(last_position + 2)+'\t\t\t\t'+'Z'+'\t\t'+'-1'+'\t\t\t\t'+str(rnd_chrg)+ '\n')
total_res_charged += 1

print('Total charged residues: '+str(total_res_charged))
out_file.close()
