#Generating Arithemetic Series and it's sum

def generate_ap_series(a, d, n):
    ap_series = [a + (i * d) for i in range(n)]
    return ap_series

def sum_of_ap_series(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)

a = int(input("Enter the first term (a) of the AP series: "))
d = int(input("Enter the common difference (d) of the AP series: "))
n = int(input("Enter the number of terms (n) in the AP series: "))

ap_series = generate_ap_series(a, d, n)
print("AP Series:", ap_series)


print("Sum of AP series is : ", sum_of_ap_series(a,d,n))
