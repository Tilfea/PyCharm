import random
answers = ('Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', "Пока неясно, попробуй снова", 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно')
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
print('Привет,', name)
def ans90():
    x = input('Я слушаю твой вопрос!')
    print(random.choice(answers))
ans90()
while True:
    new = input('Хочешь задать еще один вопрос?')
    if new.lower() in ('д', 'да', 'yes', 'y'):
        ans90()
    else:
        break
print('Возвращайся если возникнут вопросы!')