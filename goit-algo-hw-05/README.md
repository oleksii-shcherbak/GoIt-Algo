# Substring Search Algorithm Benchmark

## Objective

Compare the performance of three substring search algorithms on two Ukrainian-language technical articles:

- **Boyer–Moore**
- **Knuth–Morris–Pratt (KMP)**
- **Rabin–Karp**

Each algorithm is tested on:
- A **real substring** (`"алгоритм"`) — known to exist in the texts
- A **fake substring** (`"AlGoRitHm"`) — guaranteed to not exist

Benchmarking is done using Python's `timeit` module.

---

## Dataset

- **Article 1:** `стаття 1.txt` (originally in Windows-1251, converted to UTF-8)
- **Article 2:** `стаття 2.txt` (UTF-8)

Each file contains academic text related to algorithms and data structures.

---

## Benchmark Results

### Article 1

#### Substring Exists
| Algorithm            | Time (sec) |
|----------------------|------------|
| Boyer–Moore          | 0.000009   |
| Knuth–Morris–Pratt   | 0.000017   |
| Rabin–Karp           | 0.000031   |

#### Substring Missing
| Algorithm            | Time (sec) |
|----------------------|------------|
| Boyer–Moore          | 0.000132   |
| Knuth–Morris–Pratt   | 0.000568   |
| Rabin–Karp           | 0.001569   |

---

### Article 2

#### Substring Exists
| Algorithm            | Time (sec) |
|----------------------|------------|
| Boyer–Moore          | 0.000375   |
| Knuth–Morris–Pratt   | 0.001734   |
| Rabin–Karp           | 0.003947   |

#### Substring Missing
| Algorithm            | Time (sec) |
|----------------------|------------|
| Boyer–Moore          | 0.000339   |
| Knuth–Morris–Pratt   | 0.001529   |
| Rabin–Karp           | 0.004112   |

---

## Observations

- **Article 1** (shorter and simpler text):
  - **Boyer–Moore** is fastest in both existing and missing cases.
  - **KMP** is stable but slower on fake substrings.
  - **Rabin–Karp** lags significantly on non-matches.

- **Article 2** (larger and more complex):
  - **Boyer–Moore** remains the most efficient across the board.
  - **Rabin–Karp** becomes disproportionately slower — likely due to hash collisions or overhead.
  - **KMP** is ~4× slower than Boyer–Moore on both match types.

---

## Conclusion

- **Best Overall:** Boyer–Moore — consistently fastest, efficient on large and small texts.
- **KMP** is acceptable but loses to Boyer–Moore in real usage.
- **Rabin–Karp** is the worst performer, especially on long texts or absent substrings.

**Recommendation:** Use **Boyer–Moore** for most practical string search tasks in text-heavy datasets.
