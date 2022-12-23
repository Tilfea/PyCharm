print('Добро пожаловать в числовую угадайку')

def new_game():
    def is_valid(a):
        return a.isdigit() and 1 <= int(a) <= int(x)

    x = input('До какого числа будем угадывать?')
    import random

    num = random.randint(1, int(x))
    total = 0
    print('Введите число от 1 до', x)
    m = input()
    while True:
        if is_valid(m) is False:
            print('А может быть все-таки введем целое число от 1', 'до', x,'?')
        else:
            m = int(m)
            if m < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                total+=1
            elif m > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                total+=1
            else:
                print('Вы угадали, поздравляем!')
                total += 1
                print('Количество ваших попыток равно', total)
                break
        print('Введите число от 1 до', x)
        m = input()

new_game()
while True:
    new = input('Хотите поиграть еще раз?')
    if new.lower() in ('д', 'да', 'yes', 'y'):
        new_game()
    else:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')