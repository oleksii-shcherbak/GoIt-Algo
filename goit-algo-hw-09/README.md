# Coin Change Algorithms: Greedy vs Dynamic Programming

## Task

I implemented two algorithms to compute the change for a given amount using a fixed set of coin denominations:

- **Greedy algorithm**: Always picks the largest possible coin first.
- **Dynamic programming**: Finds the combination of coins that uses the minimum total number of coins.

Coin denominations used in both algorithms: `[50, 25, 10, 5, 2, 1]`

---

## Example Result for Amount = 113

- **Greedy result**:  
  `{50: 2, 10: 1, 2: 1, 1: 1}`

- **Dynamic programming result**:  
  `{1: 1, 2: 1, 10: 1, 50: 2}`

Both return valid change. The dynamic programming result guarantees the minimal number of coins.

---

## Time Complexity Comparison

| Algorithm             | Time Complexity           |
|-----------------------|---------------------------|
| Greedy                | O(n)                      |
| Dynamic Programming   | O(amount × n)             |

Where `n` is the number of coin denominations and `amount` is the target value to make change for.

The greedy algorithm simply iterates over the list of coins once, making it extremely fast even for large sums.  
The dynamic programming algorithm builds a solution table up to the target amount and considers every coin for each sub-amount, which makes it slower but guarantees the minimum number of coins.

---

## Performance on Large Amounts

- The **greedy algorithm** is extremely fast and uses constant space. It performs well even on very large sums, but it **does not guarantee** the minimal number of coins unless the coin system is canonical (which `[50, 25, 10, 5, 2, 1]` is).
- The **dynamic programming algorithm** finds the optimal solution but consumes much more time and memory. For large amounts (e.g., 10,000+), execution slows down due to the growing DP table.

---

## Conclusion

- **Use the greedy algorithm** when execution speed is critical and the coin system is known to be canonical (like modern currencies).
- **Use dynamic programming** when the goal is to minimize the number of coins and the coin set is arbitrary or non-standard.
