def change(s):
    d = {"UPPER" : 0, "LOWER" : 0}
    for c in s:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
        else:
            pass
    print(d["UPPER"])
    print(d["LOWER"])
change("School Days are Happy")