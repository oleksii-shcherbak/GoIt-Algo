import os
import timeit

# FILE LOADING

def read_file(filepath: str, encoding: str = 'windows-1251') -> str:
    """
    Reads a text file with specified encoding.

    Parameters:
        filepath (str): Path to the file.
        encoding (str): Encoding of the file. Default is 'windows-1251'.

    Returns:
        str: File content as string.
    """
    with open(filepath, 'r', encoding=encoding, errors='replace') as f:
        return f.read()

# ALGORITHMS

def boyer_moore(text: str, pattern: str) -> int:
    """
    Boyer-Moore substring search algorithm.
    Returns the position of the first match or -1 if not found.
    """
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    last = {c: i for i, c in enumerate(pattern)}
    i = m - 1
    k = m - 1

    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1

def knuth_morris_pratt(text: str, pattern: str) -> int:
    """
    Knuth-Morris-Pratt substring search algorithm.
    Returns the position of the first match or -1 if not found.
    """
    def compute_prefix(pattern):
        prefix = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = compute_prefix(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1

def rabin_karp(text: str, pattern: str) -> int:
    """
    Rabin-Karp substring search algorithm.
    Returns the position of the first match or -1 if not found.
    """
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            t = (t + q) % q

    return -1

# BENCHMARK

def benchmark(text: str, substring: str, label: str):
    print(f"\nTesting: {label}")
    for algo in [boyer_moore, knuth_morris_pratt, rabin_karp]:
        exec_time = timeit.timeit(lambda: algo(text, substring), number=1)
        print(f"{algo.__name__:<25} {exec_time:.6f} sec")

# MAIN

def main():
    base_path = "/Users/oleksii-shcherbak/Projects/GoIt-Algo/goit-algo-hw-05/"
    file1 = os.path.join(base_path, "стаття 1.txt")
    file2 = os.path.join(base_path, "стаття 2.txt")

    text1 = read_file(file1)
    text2 = read_file(file2)

    real_substring = "алгоритм"
    fake_substring = "AlGoRitHm"

    benchmark(text1, real_substring, label="Article 1 (existing)")
    benchmark(text1, fake_substring, label="Article 1 (non-existing)")
    benchmark(text2, real_substring, label="Article 2 (existing)")
    benchmark(text2, fake_substring, label="Article 2 (non-existing)")

if __name__ == "__main__":
    main()
