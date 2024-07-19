#!/usr/bin/python3



def calculate_bmi():

    weight = float(input("ادخل وزنك بالكيلوغرام: "))
    height = float(input("ادخل طولك بالمتر: "))
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        msg = "لديك نقص في الوزن كل اكثر ياصديقي"
    elif 18.5 <= bmi < 25:
        msg = "وزنك جيد حافظ عليه"
    elif 25 <= bmi < 30:
        msg = "لديك زيادة في الوزن تمرن اكثر"
    else: 
        msg = "تعاني من السمنة راجع طبيب مختص"

    print("Your BMI: ", bmi)
    print(msg)

calculate_bmi()

