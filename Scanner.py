import re
from utils import readTokens, readProgram
from SymbolTable import SymbolTable
from ProgramInternalForm import PIF

class Scanner:

    def __init__(self) -> None:
        self.operators, self.separators, self.keywords = readTokens("C:/Users/olahu/Desktop/Facultate/Sem5/FLCD/Labs/L3/token.in")

        self.identifiersTable = SymbolTable(100)
        self.constantsTable = SymbolTable(100)
        self.pif = PIF()

        self.errors = []

    def scan(self, file_path):
        program = readProgram(file_path)
        nrLine = 0

        for line in program:
            nrLine +=1
            tokens = self.tokenize(line)
            for token in tokens:
                print(token)
                if self.isReservedWord(token) or self.isOperator(token) or self.isSeparator(token):
                    self.pif.add(token, (-1,-1))
                else:
                    if self.isIdentifier(token):
                        index = self.identifiersTable.add(token)
                        self.pif.add("id", index)
                    elif self.isConstant(token):
                        index = self.constantsTable.add(token)
                        self.pif.add("constant", index)
                    else:
                        self.error(token, nrLine)
        if(len(self.errors) == 0):
            print("Lexically correct")
            self.generateOutput()
        else:
            print("Error")
            for err in self.errors:
                print(err)


    def error(self, token, nrLine):
        self.errors.append("Lexical error at line " + str(nrLine) + ": " + token)

    def generateOutput(self):
        print("PIF")
        print(self.pif)
        print("ST ids")
        print(self.identifiersTable)
        print("ST constants")
        print(self.constantsTable)

        with open("PIF.out", 'w') as file:
            file.write(str(self.pif))
        with open("ST.out", 'w') as file:
            file.write("Ids\n\n")
            file.write(str(self.identifiersTable))
            file.write("\n\n")
            file.write("Constants\n\n")
            file.write(str(self.constantsTable))



    def tokenize(self, line):
        line = line.replace('\n', '').strip()
        if line == '':
            return []

        line, strings = self.search_for_strings(line)
        line = self.search_for_operators(line)

        for separator in self.separators:
            line = line.replace(separator, " "+separator+" ")

        tokens = line.split(" ")
        tokens = [t for t in tokens if t != '']
        print(tokens)
        for i in range(len(tokens)):
            if re.match("^\$[0-9]+\$$", tokens[i]) is not None:
                print(strings[0])
                tokens[i] = strings[int(tokens[i][1:-1])]

        return tokens


    def search_for_operators(self, line):
        result = ""
        i = 0
        while i < len(line):
            if i+1<len(line) and self.isOperator(line[i]+line[i+1]):
                result += " " + line[i]+line[i+1] + " "
                i +=1
            elif self.isOperator(line[i]):
                result += " " + line[i] + " "
            else:
                result += line[i]
            i +=1
        return result

    def search_for_strings(self, line):
        strings = []
        line_without_strings = ""

        i = 0
        isString = False
        string = ""
        while i<len(line):
            if line[i] == '"':
                if isString:
                    string += '\"'
                    strings.append(string)
                    line_without_strings += " $" + str(len(strings)-1) + "$ "
                else:
                    string = '\"'
                isString = not isString
            else:
                if isString:
                    string += line[i]
                else:
                    line_without_strings += line[i]
            i +=1
        if isString:
            strings.append(string)
            line_without_strings += " $" + str(len(strings)-1) + "$ "
        return line_without_strings, strings

    
    def isReservedWord(self, token):
        return token in self.keywords

    def isOperator(self, token):
        return token in self.operators

    def isSeparator(self, token):
        return token in self.separators

    def isToken(self, token):
        return self.isReservedWord(token) or self.isOperator(token) or self.isSeparator(token)


    def isIdentifier(self, token):
        return re.match("^[a-z][\w]*$", token) is not None


    def isConstant(self, token):
        return self.isNumber(token) or self.isString(token)

    @staticmethod
    def isNumber(token):
        return token == "0" or re.match("^-?[1-9][0-9]*$", token) is not None
    @staticmethod
    def isString(token):
        return re.match("^\"[A-Za-z0-9\.\?\!, ]*\"$", token) is not None
    # @staticmethod
    # def isChar(token):
    #     return re.match("^\'[A-Za-z0-9\.\?\!,\s]\'$", token) is not None

