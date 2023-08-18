def base(number, ibase, fbase):
    snum = str(number)
    integer, _, decimal = snum.partition(".")
    
    integer10 = 0
    power = 0
    for i in integer[::-1]:
        if i.isdigit():
            integer10 += int(i) * (ibase ** power)
        else:
            integer10 += (ord(i.upper()) - ord('A') + 10) * (ibase ** power)
        power += 1
    
    decimal10 = 0.0
    power = -1
    for i in decimal:
        if i.isdigit():
            decimal10 += int(i) * (ibase ** power)
        else:
            decimal10 += (ord(i.upper()) - ord('A') + 10) * (ibase ** power)
        power -= 1
    
    integerf = ""
    while integer10 > 0:
        rem = int(integer10) % fbase
        if rem >= 10:
            integerf = chr(ord('A') + rem - 10) + integerf
        else:
            integerf = str(rem) + integerf
        integer10 //= fbase
    if integerf == "":
        integerf = "0"
    
    decimalten = decimal10
    decimalf = ""
    count = 0
    while count < 10 and decimalten != 0:
        count += 1
        decimalten *= fbase
        digit = int(decimalten)
        if digit >= 10:
            decimalf += chr(ord('A') + digit - 10 - 1)  # Use 'A' + digit - 10 - 1 for symbols 'A', 'B', 'C', ...
        else:
            decimalf += str(digit)
        decimalten -= digit
    
    if decimalf:
        result = integerf + "." + decimalf
    else:
        result = integerf
    
    return result

# Test the function
number = float(input("Enter the real number: "))
ibase = int(input("Enter the initial base: "))
fbase = int(input("Enter the final base: "))

fnumber = base(number, ibase, fbase)
print(number, "in base", ibase, "is", fnumber, "in base", fbase)
