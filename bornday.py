burn_pushkin = 1799
date = "26 мая"
qestion = int(input("Введите возраст Пушкина: "))

if qestion == burn_pushkin:
    data_question = input("Введите дату рождения Пушкина: ")

    if data_question == date:
        print("Верно")
    else:
        print("Не верный день рождения")
else:
    print("Не верный год")