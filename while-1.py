def ask_user():
    questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Где ты?": "Далеко", "Что мне делать?": "Поешь"}

    user_say = ""
    while (user_say).strip() != "Хорошо":
        user_say = input("Как дела?")

    user_question = ""
    while (user_question).strip() != "Stop":
        user_question = input("Задайте вопрос")
        print(questions.get((user_question).strip()))

ask_user()