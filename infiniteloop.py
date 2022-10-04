def is_power_of_two(n):
    while n % 2 == 0:
        n = n/2
        n-=1   
    if n == 1:
        return True
    return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False