def print_pattern(n):
    for i in range(1, n + 1):
        # Print asterisks
        print('*' * i, end='\t')

        # Print repeating 1s in increasing order
        print('1' * i, end='\t')

        # Print the repeated numbers in decreasing length
        print(str(i) * (n + 1 - i), end='\t')

        # Print alphabet pattern (A, AB, ABC, ...)
        print(''.join(chr(65 + j) for j in range(i)))

# Call the function with n=5 to match the provided pattern
print_pattern(5)
