def getinput():
    first= input("First number")
    operator=input("operator")
    third=input("third Number")
    result=""
    if operator== "+":
        result= int(first) + int(third)
    elif operator== "*":
        result= int(first) * int(third)
    elif operator== "-":
        result= int(first) - int(third)
    elif operator== "/":
        result= int(first) / int(third)

    print(result)
    return result
    

getinput()

#newchange

