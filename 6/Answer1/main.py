from queue import Queue


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class Node:
    def __init__(self, level, profit, bound, weight, selected_items):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight
        self.selected_items = selected_items


def compare(a, b):
    r1 = float(a.value) / a.weight
    r2 = float(b.value) / b.weight
    if r1 > r2:
        return -1
    elif r1 < r2:
        return 1
    else:
        return 0


def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profitBound = u.profit
    j = u.level + 1
    totWeight = u.weight

    while j < n and totWeight + arr[j].weight <= W:
        totWeight += arr[j].weight
        profitBound += arr[j].value
        j += 1

    if j < n:
        profitBound += (W - totWeight) * arr[j].value / arr[j].weight

    return profitBound


# to solve the 0-1 Knapsack problem
def knapsack_solution(W, arr, n):
    arr.sort(key=lambda item: compare(item, item), reverse=True)

    q = Queue()
    u = Node(-1, 0, 0, 0, [])
    q.put(u)

    maxProfit = 0
    selected_items = []

    while not q.empty():
        u = q.get()
        if u.level == -1:
            v = Node(0, 0, 0, 0, [])

        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit + arr[u.level + 1].value, 0, u.weight + arr[u.level + 1].weight,
                 u.selected_items + [u.level + 1])

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit
            selected_items = v.selected_items

        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:
            q.put(v)

        v = Node(u.level + 1, u.profit, 0, u.weight, u.selected_items)

        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:
            q.put(v)

    return maxProfit, selected_items


if __name__ == '__main__':
    W = 13
    arr = [
        Item("Item1", 2, 20),
        Item("Item2", 5, 30),
        Item("Item3", 7, 35),
        Item("Item4", 3, 12),
        Item("Item5", 1, 3)
    ]
    n = len(arr)

    maxProfit, selected_items = knapsack_solution(W, arr, n)

    print('Maximum possible profit =', maxProfit)
    print('Selected items:')
    for i in selected_items:
        print(arr[i].name)
