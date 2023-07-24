#!/usr/bin/env python3
import sys
import math

for line in sys.stdin:
    k1, v1 = line.strip().split('\t')
    k2, v2 = sys.stdin.readline().strip().split('\t')

    if k1 != k2:
        continue

    ab1, a1, b1 = map(float, v1.split())
    ab2, a2, b2 = map(float, v2.split())

    if ab1 != ab2:
        continue

    if ab1 < 10.0:
        continue

    print(k1, '\t', ab1 / (math.sqrt(a1+a2) * math.sqrt(b1+b2)))