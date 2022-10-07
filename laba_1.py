# task 1
import random

class Generator():
    def __init__(self):
        self.list_of_passwords = []
        self.password = ' '
        self.symbols = [
    "а"," б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я",
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    '!', '–', '$', '%', '&', '‘', '(', ')', '*', '{', '}'
]

    def generate(self):
        for i in range(9):
            self.password += str(random.choice(self.symbols))
        return self.password

    def clear_password(self):
        self.password = " "

    # def print(self):
    #     print(self.password)


# task 2
class GeneratorWithId():

    def __init__(self):
        self.Password_2 = ''
        self.Answer = ''
        self.ListOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.ListOfEnglishLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.ListOfSpecialsymbols = ['!', '–', '$', '%', '&', '‘', '(', ')', '*', '{', '}']
        self.AmountOfNumbers = 2
        self.UsersIdentifier = " "
        self.LengthOfIdentifier = int
        self.AmountOfEnglishLetters = int
        self.AmountOfSpecialSymbols = int

    def Clear_Password(self):
        self.Answer = ' '

    def get_password_policy(self):
        self.LengthOfIdentifier = len(self.UsersIdentifier)
        self.AmountOfEnglishLetters = int(self.LengthOfIdentifier // 8 + 3)
        self.AmountOfSpecialsymbols = int(11 - (self.LengthOfIdentifier // 8) + 4)

    def create_password(self):
        for i in range(self.AmountOfNumbers):
            self.Password_2 += str(random.choice(self.ListOfNumbers))

        for j in range(self.AmountOfEnglishLetters):
            self.Password_2 += str(random.choice(self.ListOfEnglishLetters))

        for k in range(self.AmountOfSpecialsymbols):
            self.Password_2 += str(random.choice(self.ListOfSpecialsymbols))

        for i in self.Password_2:
            self.Answer += i
        
    # def print_password(self):
    #     print(f"Password for {self.UsersIdentifier}: {self.Answer}")

# gwi = Generator_with_id()

# gwi.get_user_id()
# gwi.get_password_policy()
# gwi.create_password()
# gwi.print_password()