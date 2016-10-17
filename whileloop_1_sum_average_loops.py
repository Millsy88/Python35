n = int(input("Enter a number: "))

sum = 0
count = 1
list1 = []
while count <= n:
    sum = sum + count
    count += 1
    list1.append(count)

print("Sum of 1 until ", n, " : ", sum)
# for some reason av = float(sum / count) does not return a float. So using len
# instead.
av = float(sum / len(list1)) 
print("Average of 1 until ", n, " : ", av)
