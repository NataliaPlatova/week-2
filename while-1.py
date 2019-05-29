def ask_user():
    questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Где ты?": "Далеко", "Что мне делать?": "Поешь"}

    user_say = ""
    try:
        while (user_say).strip() != "Хорошо":
            user_say = input("Как дела?")

        user_question = input("Задайте вопрос")
        print(questions.get((user_question).strip()))
    except(KeyboardInterrupt):
        print("Пока!")


ask_user()