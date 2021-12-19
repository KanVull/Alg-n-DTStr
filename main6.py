import hashlib
import matplotlib.pyplot as plt

class HashTable():
    def __init__(self, hashFunction) -> None:
        self.table = {}
        self.hashFunction = hashFunction

    def add(self, key: any, value: any) -> None:
        hashKey = self.hashFunction(key)
        if hashKey is None:
            print('Hash Function returned None on', key)
            return None
        if hashKey in self.table:
            if self.table[hashKey] is not None:
                if key not in [key_value[0] for key_value in self.table[hashKey]]:
                    # Создаём коллизию
                    self.table[hashKey].append([key, value])
                else:
                    # Обновляем значение
                    for index, key_value in enumerate(self.table[hashKey]):
                        if key_value[0] == key:
                            self.table[hashKey][index][1] = value
                            break           
            else:
                # Добавляем значение к существующему ключу
                self.table[hashKey] = [[key, value]]    
        else:
            # Добавляем новый ключ
            self.table[hashKey] = [[key, value]]

    def search(self, key) -> any:
        hashKey = self.hashFunction(key)
        if hashKey is None:
            print('Hash Function returned None on', key)
            return None
        if hashKey in self.table:
            if self.table[hashKey] is not None:
                if len(self.table[hashKey]) == 1:
                    print(self.table[hashKey][0][1])
                    print(f'Founded by key [{hashKey}]')
                    print('There are no more data under this key')
                    print('\t', self.table[key])
                    return self.table[hashKey][0][1]
                else:
                    for key_value in self.table[hashKey]:
                        if key_value[0] == key:
                            print(key_value[1])
                            print(f'Founded by key [{hashKey}]')
                            print('There are more data under this key')
                            for key_val in self.table[hashKey]:
                                print(f'\t{key_val[0]}: {key_val[1]}')
                            return key_value[1]
        print('Not found')
        return None

    def delete(self, key) -> None:
        hashKey = self.hashFunction(key)
        if hashKey is None:
            print('Hash Function returned None on', key)
            return None
        if hashKey in self.table:
            if len(self.table[hashKey]) > 1:
                for index, key_value in enumerate(self.table[hashKey]):
                    if key_value[0] == key:
                        self.table[hashKey].pop(index)
            else:
                self.table[hashKey] = None 
        else:
            print(f'There is no {key} in hash-table')                                     

    def count_load_factor(self) -> float:
        n, k = 0, 0
        for value in self.table.values():
            n += 1
            if value is not None:
                k += 1
        return k/n        

    def hist(self) -> None:
        index = [i for i in range(len(self.table.keys()))]
        values = []
        for key in self.table.keys():
            if self.table[key] is None:
                values.append(0)
            else:
                values.append(len(self.table[key]))    
        plt.bar(index, values)
        plt.show()


# Хэш-функция выдающая первую букву слова
def hashByFirstLetter(word) -> str:
    if word != '':
        if word[0].isalpha():
            return word[0].lower()
    return None

class HashTableFirstLetter(HashTable):
    def __init__(self) -> None:
        super().__init__(hashByFirstLetter)
        self.table = {chr(ord('a') + c): None for c in range(0, 26)}

# Хэш-функция берёт первые три буквы слова, складывает их коды и берёт остаток от деления на 50
def hashByModuling(word):
    if word != '':
        if len(word) > 2:
            for letter in word[0:3]:
                if not letter.isalpha():
                    return None
            return sum(ord(letter) for letter in word[0:3]) % 50
    return None

class HashTableModuling(HashTable):
    def __init__(self) -> None:
        super().__init__(hashByModuling)
        self.table = {i: None for i in range(0, 50)}

#Хэш-функция SHA256
def hashBySHA256(word):
    return hashlib.sha256(word.encode())

class HashTableSHA(HashTable):
    def __init__(self) -> None:
        super().__init__(hashBySHA256)

    def add(self, key: any, value: any):
        hashKey = self.hashFunction(key).hexdigest()
        if hashKey is None:
            print('Hash Function returned None on', key)
            return None
        if hashKey in self.table:
            if self.table[hashKey] is not None:
                if key not in [key_value[0] for key_value in self.table[hashKey]]:
                    # Создаём коллизию
                    self.table[hashKey].append([key, value])
                else:
                    # Обновляем значение
                    for index, key_value in enumerate(self.table[hashKey]):
                        if key_value[0] == key:
                            self.table[hashKey][index][1] = value
                            break           
            else:
                # Добавляем значение к существующему ключу
                self.table[hashKey] = [[key, value]]    
        else:
            # Добавляем новый ключ
            self.table[hashKey] = [[key, value]]    

if __name__ == '__main__':
    hashTableFirstLetter_Lorem = HashTableFirstLetter()
    hashTableModuling_Lorem = HashTableModuling()
    hashTableSHA_Lorem = HashTableSHA()

    print(hashTableFirstLetter_Lorem.table)
    print(hashTableFirstLetter_Lorem.count_load_factor())

    # Запихиваю Рыба-текст в таблицу, которая ключами выделяет первые буквы слов
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            hashTableFirstLetter_Lorem.add(word, index)
    print(hashTableFirstLetter_Lorem.table)
    print(hashTableFirstLetter_Lorem.count_load_factor())
    hashTableFirstLetter_Lorem.hist()
    # Результат в файле "6 - First letter.png"

    # Запихиваю Рыба-текст в таблицу, которая ключами выделяет остаток от деления
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            hashTableModuling_Lorem.add(word, index)
    print(hashTableModuling_Lorem.table)
    print(hashTableModuling_Lorem.count_load_factor())  
    hashTableModuling_Lorem.hist()
    # Результат в файле "6 - Moduling.png"

    # Запихиваю Рыба-текст в таблицу, которая ключами выделяет результат функции sha256
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            hashTableSHA_Lorem.add(word, index)
    print(hashTableSHA_Lorem.table)
    print(hashTableSHA_Lorem.count_load_factor())  
    hashTableSHA_Lorem.hist()   
    # Результат в файле "6 - SHA.png"        


'''

Генерация пустой таблицы, заполняя ключи как первые буквы слов
{'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None, 'i': None, 'j': None, 'k': None, 'l': None, 'm': None, 'n': None, 'o': None, 'p': None, 'q': None, 'r': None, 's': None, 't': None, 'u': None, 'v': None, 'w': None, 'x': None, 'y': None, 'z': None}
0.0

Заполнение FirstLetter
Коэффициент заполненности
{'a': [['amet', 46], ['adipiscing', 6], ['aliquet', 10], ['at', 12], ['auctor', 18], ['a', 41], ['Aliquam', 48]], 'b': [['blandit', 28]], 'c': [['consectetur', 5], ['convallis', 16]], 'd': [['dolor', 21], ['diam', 27], ['Donec', 31]], 'e': [['elit', 7], ['eu', 34], ['est', 44], ['ex', 47], ['erat', 49]], 'f': [['facilisi', 30], ['fermentum', 36], ['finibus', 39]], 'g': None, 'h': None, 'i': [['ipsum', 1], ['imperdiet', 13]], 'j': None, 'k': None, 'l': [['Lorem', 0], ['lectus', 43]], 'm': [['Mauris', 19], ['metus', 40], ['malesuada', 32], ['mauris', 33]], 'n': [['Nam', 8], ['nec', 25], ['Nulla', 29], ['nisi', 37]], 'o': [['odio', 38]], 'p': [['porttitor', 42]], 'q': [['quam', 14]], 'r': None, 's': [['sit', 45], ['sed', 9], ['sodales', 26]], 't': None, 'u': [['urna', 
11], ['ullamcorper', 17]], 'v': [['Vivamus', 15], ['vulputate', 24]], 'w': None, 'x': None, 'y': None, 'z': None}
0.6153846153846154

Hash Function returned None on at
Hash Function returned None on eu
Hash Function returned None on a
Hash Function returned None on ex
Возвращает None т.к. должно быть минимум три буквы в слове
Заполнение Moduling
Коэффициент заполненности
{0: None, 1: [['Lorem', 0]], 2: [['adipiscing', 6], ['diam', 27]], 3: [['blandit', 28], ['Nulla', 29]], 4: None, 5: None, 6: None, 7: [['amet', 46]], 8: [['lectus', 43]], 9: [['Vivamus', 15]], 10: [['aliquet', 10], ['nec', 25]], 11: None, 12: [['erat', 49]], 13: [['auctor', 18]], 14: [['elit', 7], ['malesuada', 32]], 15: None, 16: [['sed', 9], ['odio', 38]], 17: [['fermentum', 36], ['finibus', 39]], 18: None, 19: [['dolor', 21]], 20: [['consectetur', 5], ['convallis', 16]], 21: None, 22: None, 23: [['mauris', 33]], 24: None, 25: None, 26: [['imperdiet', 13], ['metus', 40], ['sodales', 26]], 27: [['quam', 14]], 28: [['Aliquam', 48]], 29: None, 30: [['nisi', 37]], 31: None, 32: [['ipsum', 1], ['est', 44]], 33: [['ullamcorper', 17]], 34: [['Nam', 8]], 35: None, 36: [['sit', 45]], 37: [['porttitor', 42]], 38: None, 39: [['Donec', 31]], 40: None, 41: [['urna', 11], ['Mauris', 19]], 42: None, 43: [['vulputate', 24]], 44: None, 45: None, 46: None, 47: None, 48: [['facilisi', 30]], 49: None}
0.56

Заполнение SHA
Коэффициент заполненности
{'1b7f8466f087c27f24e1c90017b829cd8208969018a0bbe7d9c452fa224bc6cc': [['Lorem', 0]], '0417c537e65d8e41ee92b7257726086854a8f41cd884842f52dcf05caf4109a4': [['ipsum', 1]], '67f047db155161e99851908ba03fe13c23320f561940787b5e94e8fe7adefda5': [['dolor', 21]], '584178e5e3517ddcebc66340917adc3a27ce4be359a29aa827563d481ff5d67a': [['sit', 45]], '7e085b4198b6bc904d8489968fc9a8054c476c578e4de3dbf820832b458de9e7': [['amet', 46]], '70e88c7a26a5e6daca0dc1c611bbf05e26b7e1d645faeaa30c1d316c67ed9869': [['consectetur', 5]], 'cb9c78bcfd08c48d2e2575f222cb647c9ccf150b571ffe9e05f6a78345ba10d3': [['adipiscing', 6]], 'e083bcc078b96ea652eeab2dcb44eab848c5be481edeb86e5abb197a695898b9': [['elit', 7]], '22dd59c8a41bb6fc7c23cf9c354a606641ee04e852bbdd0398bac848e8e92ead': [['Nam', 8]], '5f53b0a2be22e28dc4b056f663910c046a33f9b2d779eaf997ea771fe1881a13': [['sed', 9]], 'e1a05ccdaffd9eab50416d85db59d64c8200e6e7c5e1c55fb8c2ec5738f0b1b2': [['aliquet', 10]], 'b12c09a40023f45e247afc5b659adcc42514fa75652317edb3f513d9cb064326': [['urna', 11]], 'b1d6b91b67c2afa5e322988d9462638d354ddf8a1ef79dba987f815c22b4baee': [['at', 12]], '8748eadaa89e97f2db20e7c5e344597ef32dcc2bdcb76cb6b2e2fefb7a9a41d1': [['imperdiet', 13]], '62f3263ee766168d9ca94c147b932d037054f9a03ef142fb6c5b173d2332da87': [['quam', 14]], '5a2cabfb2a9ee7551153d32575f0530b2ea5504c4464ee9a2c289c494952b138': [['Vivamus', 15]], '36d6abd26060700ded60652473c56f83a912fd98de31851dfe1e872686cb80c4': [['convallis', 16]], '04e86ce40f04aa9da5cbbf105b2f4b603a57bf1e57a792ede8992cd5b98c8abc': [['ullamcorper', 17]], '95c22d91602b48972a12e798d0f40c9c99fc59da3b07b0fcdc86d73feb82d8ee': [['auctor', 18]], 'e656c10320fb87015dd3052edd1983e5001e3720c0590f63bf9e0f1041c255cf': [['Mauris', 19]], '25cac4ecd57285cc3772ddfe355ff961d9a7a5fd4ea2e512c622beb90863e663': [['blandit', 28]], '9d9b90817fc39231aedf8f19d5e19acde3e9421afff1018d942ecf9f2676176a': [['nec', 25]], 'eece0893c512262d3e48516ed72dc27480e834c607a61cb168151c163e000880': [['metus', 40]], '5bc67d321759fcc8e51ab71ddf3cdffb360e702459afd83924efb867ee841563': [['vulputate', 24]], '18a96e45a5cd770507d824b4f765a93ce6433e457d3ff62bae90c85d80a5fc30': [['sodales', 26]], '52903730d5e4bfd5c2064be0645126ed64f1209cef013bd6768387546ecce5c6': [['diam', 27]], '9f797d41b33a0c4ec784737e69292f5dffb7dbafcceeab2557a6d0168eedd779': [['Nulla', 29]], '49c781115cb272e9bb9e0d4d52b08f2b4373a7f75d993dc585d794cee8d51721': [['facilisi', 30]], '3c38df9f9f457035ddf03d957de6fe38e4c8d86151cb674dd33a7987d7a658e8': [['Donec', 31]], '505144fc0c5226b0d52e37a0f2130eee4dffcc2f1e57b7ddae66714c429407c5': [['malesuada', 32]], '38b190e5fac5c3009bd46b8f3f32aef057d2a39a12b514058553b0686b63c7ed': [['mauris', 33]], '4d0282941aaf2d694ddaa24fca75e503c73ab16fff3884cac12f39f882bc60cb': [['eu', 34]], '96b89566a42535eadd4986e8f1d859c0e4e58e159ed050b956490dc3ee200498': [['porttitor', 42]], 'e9c039e6387ef3469feed2a39a7dca642510fcaea8fdc3616d778408b12fa949': [['fermentum', 36]], '72ddd2cc4594aa1134b8eaa9da845a31e70ad31ef81b0968f6d58b310c9a9926': [['nisi', 37]], '87aa4e6ae23ebf93e9b357cc34ce12a7f0708265b8128a3fa835d14649d7e083': [['odio', 38]], '5a2d6d1c57d1ef5e6ed65f401be08a3cbc14d743b766cac7e471035a539fb9aa': [['finibus', 39]], 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb': [['a', 41]], '54d91626c21fe2d55a4d438421f032792daba1d4b03fc0f817f2eb983435b36a': [['lectus', 43]], 'b6cf348bc9b1a71d9db0ce76c3b2645a3d57e2a6b2119b58a236adbef5e05c43': [['est', 44]], '5312fb609f60384731fcfcb95deef3602239bf61f865a07bd8e08d818d22e9fa': [['ex', 47]], '0e9b46c3f5ed20ec56489cbdfe1c771d1719d88668465bb88b7a8668abc25a69': [['Aliquam', 48]], 'e806ddc0bf66b8caa0555eed38881e0c7f15afa9e0fb06767c26daec4cbadc2d': [['erat', 49]]}
1.0

Как итог - чем круче функция Hash, тем больше коэффициент заполненности И! меньше коллизий
(коэффициет может быть 1.0, а по факту в таблице один ключ и все данные там)

'''