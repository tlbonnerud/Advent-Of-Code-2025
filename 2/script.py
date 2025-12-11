with open('data.txt', 'r') as file:
    content = file.readline().strip()

# Parse the ranges
ranges = content.split(',')

def is_repeated_pattern(num_str):
    """Check if a number is made of a pattern repeated at least twice"""
    length = len(num_str)
    
    # Try all possible pattern lengths (from 1 to half the string length)
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:  # String can be evenly divided
            pattern = num_str[:pattern_length]
            repetitions = length // pattern_length
            
            # Check if the pattern repeated creates the original string
            if pattern * repetitions == num_str and repetitions >= 2:
                return True
    
    return False

total_invalid_sum = 0

for range_str in ranges:
    start_str, end_str = range_str.split('-')
    start = int(start_str)
    end = int(end_str)
    
    print(f"Checking range {start}-{end}")
    
    for num in range(start, end + 1):
        if is_repeated_pattern(str(num)):
            print(f"  Invalid ID found: {num}")
            total_invalid_sum += num

print(f"\nTotal sum of invalid IDs: {total_invalid_sum}")
