num1 = float(input("لطفاً عدد اول را وارد کنید: "))
num2 = float(input("لطفاً عدد دوم را وارد کنید: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "قابل تقسیم نیست (تقسیم بر صفر)"
print("\nنتایج عملیات:")
print("مجموع:", sum_result)
print("تفاضل:", difference_result)
print("ضرب:", product_result)
print("تقسیم:", division_result)