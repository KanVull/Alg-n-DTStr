class FSM_Model:
    '''
        Класс автомата, хранящий возможные состояния автомата,
        потоки ввода и вывода, текущее состояние автомата, и 
        функции переходов в состояния конечного автомата.
    '''

    def __init__(self, input, output):
        self.__input = input
        self.__output = output
        self.__currentState = self.StateType[0]

    # S0 (0) - Начальное состояние автомата (Ожидание первого символа)
    # NXTLIT (1) - Ожидание следующей литеры идентификатора 
    # STOP (2) - Конец текста (Завершиющее состояние)
    # ERR (3) - Ошибка (Завершающее состояние)
    StateType = ['S0', 'NXTLIT', 'STOP', 'ERR']

    __input = None
    __output = None
    __currentState = None

    def Start(self):
        litera = Litera()
        ident = Lexema()

        while True:
            litera.GetLit(self.__input)

            if self.__currentState == self.StateType[0]:
                self.Process_S0(litera, ident)
            elif self.__currentState == self.StateType[1]:
                self.Process_NXTLIT(litera, ident)
            elif self.__currentState in self.StateType[2]:
                self.Process_STOP()
                break
            elif self.__currentState in self.StateType[3]:
                self.Process_ERR()
                break        

    def Process_S0(self, litera, ident):
        synterm = litera.GetSynterm()
        
        if synterm == 'SPACE':
            self.__currentState = self.StateType[0]
        elif synterm == 'LETTER':
            ident.LexFirst(litera)
            self.__currentState = self.StateType[1]    
        elif synterm == 'ENDFILE':
            self.__currentState = self.StateType[2]
        else:
            self.__currentState = self.StateType[3]    
        
    def Process_NXTLIT(self, litera, ident):
        synterm = litera.GetSynterm()
        
        if synterm == 'SPACE':
            ident.LexStop()
            ident.Print(self.__output)
            self.__output.write('\n')
            self.__currentState = self.StateType[0]
        elif synterm in ['LETTER', 'DIGIT']:
            ident.LexNext(litera)
            self.__currentState = self.StateType[1]    
        elif synterm == 'ENDFILE':
            ident.LexStop()
            ident.Print(self.__output)
            self.__output.write('\n')
            self.__currentState = self.StateType[2]
        else:
            self.__currentState = self.StateType[3]  

    def Process_STOP(self):
        self.__output.write('Stopped successfully\n')

    def Process_ERR(self):
        self.__output.write('Stopped in error state\n')


class Litera:
    '''
        Класс, хранящий входные сигналы автомата, считывающий 
        литеры и определяющей синтерму (продвижение по входной 
        цепочке конечного автомата).
    '''

    def __init__(self):
        self.value = None
        self.__synterm = None

    def GetLit(self, input):
        self.value = input.read(1)
        if not self.value:
            self.__synterm = 'ENDFILE'
        elif self.value.isspace():
            self.__synterm = 'SPACE'
        elif self.value.isdigit():
            self.__synterm = 'DIGIT'
        elif self.value.isalpha():
            self.__synterm = 'LETTER'
        else:
            self.__synterm = 'NOALP'
        return self.__synterm

    def GetSynterm(self):
        return self.__synterm    


class Lexema:
    '''
        Даныный класс предназначен для регистрации
        очередной лексемы и вывода их в выходной поток.
    '''

    def __init__(self):
        self.__value = ''
        self.__ix = self.__ixLast = 0

    def LexFirst(self, litera):
        self.__ix = 0
        self.__ixLast = 30
        self.__value = litera.value

    def LexNext(self, litera):
        if self.__ix != self.__ixLast:
            self.__ix += 1
            self.__value += litera.value

    def LexStop(self):
        self.__ix += 1
        self.__value += '\0'       

    def Print(self, outputFile):
        outputFile.write(self.__value)


if __name__ == '__main__':
    try:
        fileInput = open('1 - input.txt', 'r')
    except:
        print('Error while oppening file')
        exit()

    fileOutput = open('1 - output.txt', 'w')
    FiniteStateMachine = FSM_Model(fileInput, fileOutput)
    FiniteStateMachine.Start()

    fileInput.close()
    fileOutput.close()


'''
    Example of correct usage:

        '1 - input.txt' contains
            'Text for testing program number n1'

        This program will make a file '1 - output.txt'
            'Text
            for
            texting
            program
            number
            n1
            Stopped successfully
            ' 

    Example of usage with error state:

        '1 - input.txt' contains
            'Text for testing program number 1'

        This program will make a file '1 - output.txt'
            'Text
            for
            texting
            program
            number
            Stopped in error state
            ' 
'''    