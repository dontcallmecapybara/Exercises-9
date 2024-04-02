class MorseMsg:
    def __init__(self, morse):
        self.morse = morse
        self.rus = {
            '.-': 'А',
            '-...': 'Б',
            '.--': 'В',
            '--.': 'Г',
            '-..': 'Д',
            '.': 'Е',
            '...-': 'Ж',
            '--..': 'З',
            '..': 'И',
            '.---': 'Й',
            '-.-': 'К',
            '.-..': 'Л',
            '--': 'М',
            '-.': 'Н',
            '---': 'О',
            '.--.': 'П',
            '.-.': 'Р',
            '...': 'С',
            '-': 'Т',
            '..-': 'У',
            '..-.': 'Ф',
            '....': 'Х',
            '-.-.': 'Ц',
            '---.': 'Ч',
            '----': 'Ш',
            '--.-': 'Щ',
            '.--.-.': 'Ъ',
            '-.--': 'Ы',
            '-..-': 'Ь',
            '...-...': 'Э',
            '..--': 'Ю',
            '.-.-': 'Я'
        }
        self.eng = {
            '.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z'
        }
        self.ru_vowels = ['А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
        self.ru_consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 
                              'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 
                              'Х', 'Ц', 'Ч', 'Ш', 'Щ']
        self.eng_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
        self.eng_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 
                               'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
                               'S', 'T', 'V', 'W', 'X', 'Z']

    def eng_decode(self):
        '''
        Decodes morse to english.
        '''
        elems = self.morse.split()
        eng_text = ''
        for letter in elems:
            eng_text += self.eng[letter] + ' '
        return eng_text
    
    def ru_decode(self):
        '''
        Decodes morse to russian and returns it.
        '''
        elems = self.morse.split()
        ru_text = ''
        for letter in elems:
            ru_text += self.rus[letter] + ' '
        return ru_text
    
    def vowels(self, lang):
        '''
        Gets vowels and returns them in the target language.
        '''
        vow = []
        letters = self.morse.split()

        if lang == 'eng':
            for element in letters:
                if self.eng[element] in self.eng_vowels:
                    vow.append(self.eng[element])
        
        elif lang == 'ru':
            for element in letters:
                if self.rus[element] in self.ru_vowels:
                    vow.append(self.rus[element])
        
        return vow
    
    def consonants(self, lang):
        '''
        Gets consonants and returns them in the target language.
        '''
        cons = []
        letters = self.morse.split()
        text = ''

        if lang == 'eng':
            for element in letters:
                if self.eng[element] in self.eng_consonants:
                    cons.append(self.eng[element])
        
        elif lang == 'ru':
            for element in letters:
                if self.rus[element] in self.ru_consonants:
                    cons.append(self.rus[element])
        
        for item in cons:
            text += item + ' '
        
        return text


message1 = MorseMsg('.... . .-.. .-.. ---')
message2 = MorseMsg('.--. .-. .. .-- . -')

print(message1.eng_decode())
print(message2.ru_decode())
print(message1.vowels('eng'))
print(message2.vowels('ru'))
print(message1.consonants('eng'))
print(message2.consonants('ru'))
