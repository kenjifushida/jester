#!/usr/bin/env python3
import sys

u, m = map(int, sys.stdin.readline().strip().split("¥t"))

userId = u
movieIds = [m]

for line in sys.stdin:
    u, m = map(int, line.strip().split("¥t"))
    if userId != u:
        print(userId, "¥t", *movieIds);

        userId = u
        movieIds = [m]

    else:
        movieIds.append(m)
        
print(userId, "¥t", *movieIds);