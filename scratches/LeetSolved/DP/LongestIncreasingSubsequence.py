def LIS(arr):
    L = [1]*len(arr)

    for i in range(len(arr)):
        subproblems = [L[k] for k in range(i) if arr[k] < arr[i]]
        L[i] = 1 + max(subproblems, default=0)

    return max(L, default=0)


def maxHeightOfFiguresStackable(figures):
    figures.sort(key = lambda L: L[0])
    heights = [0] * len(figures)
    for i in range(len(figures)):
        L_i, W_i, H_i = figures[i]
        previousHeights = [
            heights[k] for k in range(i) if figures[k][0] < L_i and figures[k][1] < W_i
            ]

        heights[i] = H_i + max(previousHeights, default=0)

    return max(heights, default=0)

figures = [
    (5, 5, 10),
    (2, 2, 4),  # (L, W, H)
    (3, 3, 3),
    (4, 1, 2)

]

print((maxHeightOfFiguresStackable(figures)))


"""

    optimality proof:
        On the base of DP we are going to calculate the i solution which is local for the i instance of the problem
        and comes recursively on the i-1 istance
        
        complexity
        
        O( k * n )
    Worst case k is equal to n so O(n^2)   



"""



