with open("input.txt") as f:
    curr = 50
    password = 0
    for line in f:
        if line[0] == "R":
            new_val = curr + int(line[1:])
            password += new_val // 100
            curr = new_val % 100
        else:
            new_val = curr - int(line[1:])
            if new_val <= 0:
                password += (1 if curr != 0 else 0) + (-new_val) // 100
            curr = new_val % 100
        print(curr, password, line)
    print(password)
