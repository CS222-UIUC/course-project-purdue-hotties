#! /usr/bin/python3
from lib.game import Game
import numpy as np
import argparse
from tqdm import tqdm
import multiprocessing


NUM_PROCESSES = 20
ITER_PER_PROCESS = 50


def benchmark_helper(res, proc_id):
    options = {"portal": True, "block": True, "bot": True}
    game = Game(options)
    for i in tqdm(range(ITER_PER_PROCESS)):
        res[i + (proc_id * ITER_PER_PROCESS)] = game.one_iter()


def benchmark():
    arr = multiprocessing.Array('i', [0] * (ITER_PER_PROCESS * NUM_PROCESSES))
    processes = [None] * NUM_PROCESSES
    for i in range(NUM_PROCESSES):
        processes[i] = multiprocessing.Process(
            target=benchmark_helper, args=(arr, i,))

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    res = np.array(arr)
    print(res)
    print("Mean:", np.mean(res))
    print("Median:", np.median(res))
    print("Std:", np.std(res))
    print("Max:", np.amax(res))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--benchmark', action="store_true")
    args = parser.parse_args()

    if args.benchmark:
        benchmark()
    else:
        options = {"portal": True, "block": True, "bot": False}
        game = Game(options)
        game.game_start()
