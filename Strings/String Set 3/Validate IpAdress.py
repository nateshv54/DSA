'''
You are given the text ‘IPAddress’. Your task is to check if the given text ‘IPAddress’ is a valid ‘IPv4’ or not.

Conditions for a valid ‘IPv4’ are:

1. Text form of ‘IPAddress’ must be ‘a.b.c.d’
2. The values of a,b,c and d can vary from ‘0’ to ‘255’ and both ‘0’ and ‘255’ are inclusive.'''
def isValidIPv4(ipAddress):
    k = ipAddress.split(".")
    if len(k) != 4:  # Ensure there are 4 parts in the IP address
        return False
    for part in k:
        if not part.isdigit():  # Check if part is not a digit
            return False
        num = int(part)
        if num < 0 or num > 255:  # Check if part is within the valid range
            return False
    return True

a=input("Enter Ip address :")
print(isValidIPv4(a))