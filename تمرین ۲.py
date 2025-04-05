numbers = []
for i in range(4):
    num = float(input(f"عدد {i+1} را وارد کنید: "))
    numbers.append(num)
max_number = max(numbers)
print("بزرگترین عدد وارد شده:", max_number)