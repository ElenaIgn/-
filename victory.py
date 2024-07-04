# Создаем словарь с именами знаменитостей и их годом рождения
celebrities = {
    "Леонардо Ди Каприо": 1974,  # 1974
    "Рианна": 1988,  # 1988
    "Эмма Уотсон": 1990,  # 1990
    "Брэд Питт": 1963,  # 1963
    "Анджелина Джоли": 1975  # 1975
}


def quiz_game():
    correct_answers = 0
    wrong_answers = 0

    for celebrity, birth_year in celebrities.items():
        user_answer = int(input(f"Введите год рождения {celebrity}: "))
        if user_answer == birth_year:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неправильно!")
            wrong_answers += 1

    total_questions = len(celebrities)

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    print(f"Процент правильных ответов: {correct_answers * 100 / total_questions}%")
    print(f"Процент неправильных ответов: {wrong_answers * 100 / total_questions}%")

    play_again = input("\nХотите ли вы начать игру снова? (да/нет): ")
    if play_again.lower() == "да":
        quiz_game()


quiz_game()