def job(age):
    if age < 7:
        return("Ходит в детский сад")
    elif age < 18:
        return("Учится в школе")
    elif age < 22:
        return ("Учится в ВУЗе или работает")
    elif age >= 22:
        return ("Работает")

your_age = int(input("Введите ваш возраст"))
my_job = job(your_age)
print(my_job)