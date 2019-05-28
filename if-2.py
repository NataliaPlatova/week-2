def two_strings(one, two):
    if isinstance(one, str) and isinstance(two, str):
        if one == two:
            return(1)
        elif len(one)>len(two) and two != "learn":
            return (2)
        elif one != two and two == "learn":
            return (3)
    else:
        return(0)

print(two_strings(1, "rrrrr"))
print(two_strings("ddd", "ddd"))
print(two_strings("rrrr", "rr"))
print(two_strings("rrrrrr", "learn"))
print(two_strings("learn", "learn"))