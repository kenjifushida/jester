#!/usr/bin/env python3
import sys

for line in sys.stdin:
    userId, jokeIds = line.strip().split("\t")
    userId = int(userId)
    jokeIds = list(map(int, jokeIds.split()))
    for jokeId in jokeIds:
        jids = jokeIds.copy()
        jids.remove(jokeId)
        print(jokeId, "\t", *jids)