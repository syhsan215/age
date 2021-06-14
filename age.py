driving = input("請問你有沒有開過車？")
if driving != "有" and driving != "沒有":
	print("只能回答有或是沒有")
	raise SystemExit
age = int(input("請問你幾歲？"))
if driving == "有":
	if age >= 18:
		print("你通過驗證")
	else:
		print("你怎麼會開過車呢")
elif driving == "沒有":
	if age >= 18:
		print("怎麼不考駕照")
	else:
		print("很好，再過幾年你就可以考駕照了")
