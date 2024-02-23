def top_n (items,n):
    """nibirebire fam
    """
   
    # Sort the list in descending order
    sorted_numbers = sorted(items, reverse=True)
    
    # Return the top n numbers
    return sorted_numbers[:n]

# Example usage:
items = [23, 56, 12, 89, 45, 100, 34, 78]
n = 3

result = top_n(items, n)
print(f"Top {n} numbers in descending order: {result}")
