# инициируем запуск при помощи ввода символа "s"
i = input("print s for start : ") 
# вводим данные для библиотеки в цикле 
while i == "s" or i == "S":
    name = str(input("name: "))
    sex = str(input("sex(w/m): "))
    age = int(input("age: "))
    height = float(input("height, m: "))
    weight = float(input("weight, kg: "))
    bmi_new = {name:{'sex': sex,
      'age y.o': age,
      'height, m': height,
      'weight, kg': weight}}
    bmi = {}
    bmi.update(bmi_new)
    # замена для вывода послания в зависимости от пола
    sex_w = "woman"
    sex_m = "man"
    if sex == "w" or sex == "W" : (sex,sex_w)=(sex_w,sex)
    elif sex == "m" or sex == "M": (sex,sex_m)=(sex_m,sex)
    print(bmi)
    # расчет bmi
    c = round(weight/(height**2))
    # вывод шкалы
    d = float(c-16)
    e = float(50-c)
    print("Scale BMI")
    print("16" + round(d)*"=" + "|" + str(c) + "|" + round(e)*"=" + "50")
    # вывод послания в зависимости от пола и bmi 
    if c < 16: print("for "+ sex +" with Acute underweight needs help doctor")
    elif  16 < c < 18.5: print("for "+ sex +" with Underweight need to eat more ")
    elif  18.6 < c < 25: print("for "+ sex +" with Normal body weight need enjoy life")
    elif  25.1 < c < 30: print("for "+ sex +" with Overweight need start monitoring nutrition ")
    elif  30.1 < c < 35: print("for "+ sex +" with First degree obesity need help doctor")
    elif  35.1 < c < 40: print("for "+ sex +" with Second degree obesity need help doctor")
    elif  c > 40.1: print("for "+ sex +" with Obesity of the third degree need help doctor")