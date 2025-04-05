n = float(input("لطفاً نمره دانشجو را وارد کنید: "))
if n > 90:
    result = "عالی"
elif n > 70:
    result = "خوب"
elif n > 50:
    result = "متوسط"
else:
    result = "مردود"
print("نمره شما:", result)