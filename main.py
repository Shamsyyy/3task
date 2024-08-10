def number(): 
    number = int(input("Введите целое число: "))   
    if number == 0:
        print("нулевое число")
    else:
        if number < 0:
            description = "отрицательное "
        else:
            description = "положительное "
        if number % 2 == 0:
            description += "четное число"
        else:
            description += "нечетное число"
        print(description)
number()

def word():
    word = input("введи слово из из маленьеких лат. букв ")
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}
    consonant_count = 0
    for char in word:
        if char in vowels:
            vowel_count[char] += 1
        else:
            consonant_count += 1
    if all(count > 0 for count in vowel_count.values()):
        print(f"гласные: {vowel_count}, согласные: {consonant_count}")
    else:
        print(False)
word()

def task3():
    X = int(input("введи минимальную сумму инвестиций: "))
    A = int(input("сколько денег у Майкла?: "))
    B = int(input("сколько денег у Ивана?: "))

    if A >= X and B >= X:
        print(2)
    elif A >= X:
        print("Mike")
    elif B >= X:
        print("Ivan")
    elif A + B >= X:
        print(1)
    else:
        print(0)
task3()