def get_sum(num_one, num_two):
    try:
       return (int(num_one)+int(num_two))
    except(ValueError):
        return("Введите числа")

print(get_sum(22, 56))
print(get_sum(4.5, 7))
print(get_sum("что", "5"))
print(get_sum("66", "95"))