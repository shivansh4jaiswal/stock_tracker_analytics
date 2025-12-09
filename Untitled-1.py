def calculate_worth(s):
    return sum(ord(c) - ord('a') + 1 for c in s)

def solve(idx, budget, chosen_mask, cost, worth, contradictions, memo):
    if idx == len(cost):
        return 0
    if (idx, budget, chosen_mask) in memo:
        return memo[(idx, budget, chosen_mask)]
    
    # Option 1: skip current string
    max_worth = solve(idx + 1, budget, chosen_mask, cost, worth, contradictions, memo)
    
    # Option 2: include current string if no contradictions and budget allows
    # Check contradiction by bitwise AND with contradictory mask
    if budget >= cost[idx] and (chosen_mask & contradictions[idx]) == 0:
        included_worth = worth[idx] + solve(idx + 1, budget - cost[idx], chosen_mask | (1 << idx), cost, worth, contradictions, memo)
        if included_worth > max_worth:
            max_worth = included_worth
    
    memo[(idx, budget, chosen_mask)] = max_worth
    return max_worth

def main():
    N, M = map(int, input().split())
    strings = input().split()
    costs = list(map(int, input().split()))
    
    # Precompute contradiction masks
    contradictions = [0] * N
    for _ in range(M):
        a, b = input().split()
        i, j = strings.index(a), strings.index(b)
        contradictions[i] |= (1 << j)
        contradictions[j] |= (1 << i)
    
    budget = int(input())
    worths = [calculate_worth(s) for s in strings]
    
    memo = {}
    max_worth = solve(0, budget, 0, costs, worths, contradictions, memo)
    print(max_worth)

if __name__ == "__main__":
    main()
