from Grammar import Grammar
from Parser import Parser
from ParseTree import Tree


class UI:
    def __init__(self) -> None:
        self.grammar = Grammar()
        self.parser = None
        self.cmds = {
            '1': self.printGrammar,
            '2': self.printFirst,
            '3': self.printFollow,
            '4': self.printTable,
            '5': self.parseSequence
        }

    def grammarMenu(self):
        print("\n1. Print grammar")
        print("  Parser:")
        print("    2. First")
        print("    3. Follow")
        print("    4. Table")
        print("    5. Parse a sequence")
        print(" x: back")

    def run(self):
        while True:
            grammarFile = input("\nGrammar file: ")
            if grammarFile == 'x':
                return
            self.chooseGrammar(grammarFile)
            self.grammarRun()

    def grammarRun(self):
        self.grammarMenu()
        while True:
            cmd = input(" > ")
            if cmd == 'x':
                return
            if cmd == 'm':
                self.grammarMenu()
            if cmd in self.cmds:
                print("----------------------------------------------------")
                self.cmds[cmd]()
                print("----------------------------------------------------")
            else:
                print("no")
                continue

    def printGrammar(self):
        print("\n   Terminals: ")
        print(self.grammar.terminals)
        print("\n   Nonterminals: ")
        print(self.grammar.nonterminals)
        print("\n   Start symbol: ", self.grammar.start_symbol)
        print("\n   Productions: ")
        for prod in self.grammar.getProduction().keys():
            print(str(prod[0]) + " -> " + str(self.grammar.getProduction()[prod]))

    def printFirst(self):
        self.parser.printFirst()

    def printFollow(self):
        self.parser.printFollow()

    def printTable(self):
        self.parser.printTable()

    def parseSequence(self):
        sequenceFile = input("Input file: ")
        outFile = input("Output file: ")
        self.parseSequenceFromFile(sequenceFile, outFile)


    def chooseGrammar(self, file_path):
        self.grammar.read_from_file(file_path)
        self.parser = Parser(self.grammar)

    def parseSequenceFromFile(self, inFile, outFile):
        sequence = []
        with open(inFile, 'r') as file:
            lines = file.readlines()
            lines = [line.replace('\n', "").strip() for line in lines]
            for line in lines:
                symbol = line.split(' ')[0].strip()
                sequence.append(symbol)
        
        sequenceString = ' '.join(sequence)
        productionsString = self.parser.parse(sequenceString)
        if productionsString == []:
            return
        parseTree = Tree(self.grammar, productionsString)
        out = parseTree.printTree()
        with open(outFile, 'w') as file:
            file.write(out)

