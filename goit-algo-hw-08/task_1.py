import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        print(f"Connecting cables of lengths {first} and {second}")
        cost = first + second
        print(f"Cost of this connection: {cost}")
        total_cost += cost
        print(f"Total cost so far: {total_cost}")
        heapq.heappush(cables, cost)

    return total_cost

# Example usage
cables = [8, 4, 6, 12]
print(f"Minimum total connection cost: {min_connection_cost(cables)}")
