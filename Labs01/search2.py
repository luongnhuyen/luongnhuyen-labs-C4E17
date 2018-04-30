nums = [3, 4, -99, 78, 4, -99, 3]
x = int(input("Enter an integer: "))

# found= False
# for num in nums:
#     if num == x:
#         found = True
#         break
# if found:
#     print("Found")
# else:
#     print("Not found")

for num in nums:
    if num == x:
        print("Found")
        break
else:
    print("Not found")
