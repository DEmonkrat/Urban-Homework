# Task 1
import os
with open(r'.\SE_FileSystem\file_1.txt', 'r') as f:
    info = [line.strip() for line in f.readlines()]
print(*info[:3], sep = '\n')
