#!/usr/bin/env python3
import sys

line = sys.stdin.readline().strip().split("\t")
j = int(line[0])
if len(line) == 1:
    js = [] 
else:
    js = list(map(int, line[1].split()))

jokeId = j
jokeIds = js
n = 1

for line in sys.stdin:
    line = line.split("\t")
    j = int(line[0])
    if len(line) == 1:
        js = [] 
    else:
        js = list(map(int, line[1].split()))

    if jokeId != j:
        for j1 in set(jokeIds):
            print(jokeId, j1, "\t", jokeIds.count(j1), n, 0)
            print(j1, jokeId, "\t", jokeIds.count(j1), 0, n)
        
        jokeId = j 
        jokeIds = js
        n = 1
    
    else:
        jokeIds.extend(js)
        n += 1

for j1 in set(jokeIds):
    print(jokeId, j1, "\t", jokeIds.count(j1), n, 0)
    print(j1, jokeId, "\t", jokeIds.count(j1), 0, n)