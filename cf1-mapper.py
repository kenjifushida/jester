#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    if len(line.split(',')) != 4:
        continue

    userId, movieId, rating, timestamp = line.split(',')

    if userId == 'userId':
        continue

    if float(rating) < 4.0:
        continue

    print(userId, "¥t", movieId)