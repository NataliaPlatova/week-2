def ask_user():
    questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Где ты?": "Далеко", "Что мне делать?": "Поешь"}

    user_say = ""
    try:
        while (user_say).strip() != "Хорошо":
            user_say = input("Как дела?")

        x = 1
        while x!=0:
            user_question = input("Задайте вопрос")
            if user_question.strip() in questions:
                print(questions.get((user_question).strip()))
    except(KeyboardInterrupt):
        print("Пока!")


ask_user()