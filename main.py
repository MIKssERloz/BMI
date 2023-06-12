m=int(input("Масса тела в килограммах:"))
h=float(input("Рост в метрах:"))
bmi=m /(h * h)
int_bmi=int(bmi)
if bmi <16:
  print("Выраженный дефицит массы тела")
if bmi <=18.5 and bmi > 16:
  print("Недостаточная (дефицит) масса тела")
if bmi <=25 and bmi > 18.5:
  print("Норма")
if bmi <=30 and bmi > 25:
  print("Избыточная масса тела (предожирение)")
if bmi <=35 and bmi > 30:
  print("Ожирение 1 степени")
if bmi <=40 and bmi > 35:
  print("Ожирение 2 степени")
if bmi > 40:
  print("Ожирение 3 степени")
