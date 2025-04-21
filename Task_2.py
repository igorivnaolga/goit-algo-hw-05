def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return iterations, upper_bound
 
        
arr = [1.1, 2.3, 3.5, 4.8, 5.6, 7.0]
x = 4.0
result = binary_search(arr, x)

print(f"Iterations: {result[0]}")
print(f"Upper bound: {result[1]}")