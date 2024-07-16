def calculate(first, operator, third):
    result=""
    if operator== "+":
        result= int(first) + int(third)
    elif operator == "-":
        result= int(first) - int(third)
    elif operator == "x":
        result= int(first) * int(third)
    elif operator == "/":
        result= int(first) / int(third)

    return result


def calcFile():
    file = open("calcs.txt", "r")
    file_rd = file.read()
    lines = file_rd.splitlines()


    total = 0

    for line in lines:
        print(line)
        parts = line.split(" ")
        operator = parts[1]
        first = parts[2]
        third = parts[3]
        answer =  calculate(first, operator, third)
        print(answer)
        total = total + answer

    print(total)

calcFile()    
    