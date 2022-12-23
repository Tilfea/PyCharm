# Constants
digits = ('0123456789')
lowercase_letters = ('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
punctuation = ('!#$%&*+-=?@^_')

chars = ''

# Quetions
kol = int(input('Сколько паролей нужно сгенерировать?'))
length = int(input('Какова длина каждого пароля?'))
cif = input('Включать ли цифры 0123456789?')
if cif.lower() in ('д', 'да', 'yes', 'y'):
    chars += digits
prop = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if prop.lower() in ('д', 'да', 'yes', 'y'):
    chars += uppercase_letters
stroch = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
if stroch.lower() in ('д', 'да', 'yes', 'y'):
    chars += lowercase_letters
simv = input('Включать ли символы !#$%&*+-=?@^_?')
if simv.lower() in ('д', 'да', 'yes', 'y'):
    chars += punctuation
neo = input('Исключать ли неоднозначные символы il1Lo0O?')
if neo.lower() in ('д', 'да', 'yes', 'y'):
    for j in 'il1Lo0O':
        chars = chars.replace(j, '')


def generate_password(chars, length):
    import random
    for _ in range(kol):
        a = random.sample(chars, length)
        return a


for _ in range(kol):
    print(*(generate_password(chars, length)), sep='')
