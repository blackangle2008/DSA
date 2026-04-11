def mergeIntervals(intervals):
    # Step 1: Sort intervals
    intervals.sort()

    result = []

    # Step 2: Start with first interval
    result.append(intervals[0])

    # Step 3: Traverse remaining intervals
    for i in range(1, len(intervals)):
        # If overlapping
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result


# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

ans = mergeIntervals(intervals)

print("Merged Intervals:")
for it in ans:
    print(f"[{it[0]}, {it[1]}]", end=" ")