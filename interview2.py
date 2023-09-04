def hammingDistance(x, y):
    # Calculate the XOR of x and y
    xor_result = x ^ y
    
    # Initialize a counter for the number of set bits (1s)
    count = 0
    
    # Count the number of set bits in the XOR result
    while xor_result:
        count += xor_result & 1  # Check the rightmost bit
        xor_result >>= 1  # Right shift to examine the next bit
    
    return count

# Example usage:
x = 1
y = 4
print(hammingDistance(x, y))  # Output: 2
