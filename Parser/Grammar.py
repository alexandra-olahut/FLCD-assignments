class Grammar:

    def __init__(self) -> None:
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

    def read_from_file(self, file_path):
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.replace('\n', "").strip() for line in lines]

            self.nonterminals = lines[0].split(" ")
            # print(self.nonterminals)
            self.terminals = lines[1].split(" ")
            # print(self.terminals)
            self.start_symbol = lines[2]
            # print(self.start_symbol)
            for index in range(3, len(lines)):
                # read a production
                production = lines[index]
                left, right = production.split('->')
                left = left.strip().split(' ')
                # print(left)
                left = tuple(left)
                right = right.strip().split('|')
                for value in right:
                    values = value.strip().split(' ')
                    if left in self.productions.keys():
                        self.productions[left].append(values)
                    else:
                        self.productions[left] = [values]
            # print(self.productions)

    
    def getTerminals(self):
        return self.terminals

    def getNonterminas(self):
        return self.nonterminals

    def getProduction(self):
        return self.productions

    def getProductionsForNonterminal(self, nonterminal):
        productions = {}
        if self.isCFG():
            for left in self.productions.keys():
                if left[0] == nonterminal:
                    productions[left[0]] = self.productions[left]
        return productions

    def isCFG(self):
        for left in self.productions.keys():
            if len(left) != 1:
                return False
            if left[0] not in self.nonterminals:
                return False
        return True
            