qestion = int(input("Введите год рождения Пушкина: "))
burn_pushkin = 1799
date = "26 мая"
while True:
    if qestion == burn_pushkin:
        data_question = input("Введите дату рождения Пушкина: ")
        if data_question == date:
            print("Верно")
            break
        else:
            print("Не верный день рождения")

    else:
        print("Не верный год")

