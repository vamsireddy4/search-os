#!/usr/bin/env python3
"""Did an AEO change work? Compare share-of-voice change in test vs control questions.

Usage: sov_experiment.py results.csv     (columns: question,group,before,after)
       sov_experiment.py --selftest

group is "test" or "control"; before/after are share of voice in 0..1
(fraction of tracked answers that mention you). Prints the mean change per group,
the lift (test minus control) and a one-sided permutation-test p-value. Stdlib only.
"""
import csv
import random
import statistics
import sys


def lift(test, control):
    return statistics.fmean(test) - statistics.fmean(control)


def permutation_p(test, control, n=10000, seed=0):
    observed = lift(test, control)
    pooled, k = test + control, len(test)
    rng = random.Random(seed)
    hits = 0
    for _ in range(n):
        rng.shuffle(pooled)
        if lift(pooled[:k], pooled[k:]) >= observed:
            hits += 1
    return (hits + 1) / (n + 1)


def load(path):
    groups = {"test": [], "control": []}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            g = row["group"].strip().lower()
            if g not in groups:
                raise SystemExit(f"bad group {row['group']!r} for {row.get('question')!r}")
            groups[g].append(float(row["after"]) - float(row["before"]))
    if min(len(v) for v in groups.values()) < 2:
        raise SystemExit("need at least 2 questions in each group")
    return groups["test"], groups["control"]


def report(test, control):
    p = permutation_p(test, control)
    print(f"test    n={len(test):4d}  mean change {statistics.fmean(test):+.3f}")
    print(f"control n={len(control):4d}  mean change {statistics.fmean(control):+.3f}")
    print(f"lift {lift(test, control):+.3f}  p={p:.4f}  ->",
          "likely real, now repeat it" if p < 0.05 else "not distinguishable from noise")


def selftest():
    rng = random.Random(1)
    control = [rng.gauss(0.02, 0.05) for _ in range(100)]
    real = [rng.gauss(0.12, 0.05) for _ in range(100)]
    null = control[::-1]  # same values as control: lift is exactly 0
    assert permutation_p(real, control, 2000) < 0.01
    assert permutation_p(null, control, 2000) > 0.05
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif len(sys.argv) == 2:
        report(*load(sys.argv[1]))
    else:
        sys.exit(__doc__)
