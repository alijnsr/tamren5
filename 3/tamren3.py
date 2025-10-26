#تمرین دوم مقلوب عدد
#مقلوب عدد یعنی نوشتن عدد از راست به چپ
shomare = int(input("دورقمی "))
#خیلی فرق ها دارن / با// تکی معمولی هست 2 تایی صحیح
ten = shomare // 10
#%باقیمانده تقسیم 
amaleat = shomare % 10
shomaremakos = amaleat * 10 + ten
print("عدد معکوس :", shomaremakos)