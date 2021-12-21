from Grammar import Grammar
import copy


class Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar

        self.FIRST = self.buildFirst()
        self.FOLLOW = self.buildFollow()

        self.table = self.buildTable()


    def concatenation1(self, l1, l2):
        result = set()
        for element1 in l1:
            if element1 != "eps" or len(l2) == 0:
                result.add(element1)
            else:
                for element2 in l2:
                    if element2 == "eps":
                        result.add("eps")
                    else:
                        result.add(element2)
        return result

    def concatenateAll(self, first, rhs):
        sets = []
        for element in rhs:
            if element == "eps" or element in self.grammar.getTerminals():
                sets.append({element})
            else:
                sets.append(first[element])

        result = self.concatenation1(sets[0], set())
        for i in range(1, len(sets)):
            result = self.concatenation1(result, sets[i])
        return result

    def isCalculated(self, first, rhs):
        for element in rhs:
            if element in self.grammar.getTerminals() or element == "eps":
                continue
            if len(first[element]) == 0:
                return False
        return True



    def buildFirst(self):
        # initialize first(nonterminals) with empty sets
        first = {nonterminal: set() for nonterminal in self.grammar.nonterminals}
        # * first(terminal) = terminal

        # initialize F0
        for key, value in self.grammar.productions.items():
            lhs = key[0]
            for production in value:
                rhs = production[0]
                if rhs[0] in self.grammar.getTerminals() or rhs[0] == "eps":
                    first[lhs].add(rhs[0])

        # repeat until there is no change
        keepGoing = True
        while keepGoing:
            new_first = copy.deepcopy(first)

            for key, value in self.grammar.productions.items():
                lhs = key[0]
                for production in value:
                    rhs = production[0]
                    if self.isCalculated(first, rhs):
                        new_first[lhs] = new_first[lhs].union(self.concatenateAll(first, rhs))
            
            if new_first == first:
                keepGoing = False
            first = new_first

        return first

        

    def buildFollow(self):
        # initialization
        follow = {nonterminal: set() for nonterminal in self.grammar.nonterminals}
        follow[self.grammar.start_symbol].add('eps')

        keepGoing = True
        while keepGoing:
            new_follow = copy.deepcopy(follow)

            for key, value in self.grammar.productions.items():
                lhs = key[0]
                for production in value:
                    rhs = production[0]

                    for i in range(len(rhs)):
                        if rhs[i] in self.grammar.getNonterminas():
                            nonterminal = rhs[i]
                            if i == len(rhs) -1:
                                new_follow[nonterminal] = new_follow[nonterminal].union(follow[lhs])
                            else:
                                next = rhs[i+1:]
                                firstOfNext = self.concatenateAll(self.FIRST, next)
                                for element in firstOfNext:
                                    if element == "eps":
                                        new_follow[nonterminal] = new_follow[nonterminal].union(follow[lhs])
                                    else:
                                        new_follow[nonterminal].add(element)

            if new_follow == follow:
                keepGoing = False
            follow = new_follow

        return follow



    def buildTable(self):
        table = {}

        # rule 1
        for key, value in self.grammar.productions.items():
            lhs = key[0]
            for production in value:
                rhs = production[0]
                productionIndex = production[1]

                firstRhs = self.concatenateAll(self.FIRST, rhs)
                for element in firstRhs:
                    if element == "eps":
                        for followElement in self.FOLLOW[lhs]:
                            if followElement == "eps":
                                followElement = "$"
                            if (lhs, followElement) in table:
                                print("Conflict: ", (lhs, followElement), "   productions: ", table[(lhs, followElement)], (rhs, productionIndex))
                                return {}
                            table[(lhs, followElement)] = (rhs, productionIndex)
                    else:
                        if (lhs, element) in table:
                            print("Conflict: ", (lhs, element), "   productions: ", table[(lhs, element)], (rhs, productionIndex))
                            return {}
                        table[(lhs, element)] = (rhs, productionIndex)


        # rule 2
        for terminal in self.grammar.getTerminals():
            table[(terminal, terminal)] = "pop"
        
        # rule 3
        table[("$", "$")] = "acc"

        return table


    def parse(self, sequence):
        w = sequence.split(' ')
        w.append("$")
        stack = [self.grammar.start_symbol, "$"]
        productions = []
        config = (w, stack, productions)

        keepGoing = True
        while keepGoing:
            print("----")
            print(w)
            print(stack)
            print(productions)
            if w[0] == stack[0]:
                if w[0] == "$":
                    # acc
                    return productions
                else:
                    # pop
                    w.pop(0)
                    stack.pop(0)
            elif (stack[0], w[0]) in self.table:
                production = self.table[(stack[0], w[0])]
                rhs = production[0]
                index = production[1]

                stack.pop(0)
                for i in range(len(rhs) - 1, -1, -1):
                    if rhs[i] != "eps":
                        stack.insert(0, rhs[i])
                productions.append(index)
            else:
                print("Not accepted")
                return []


    def printTable(self):
        for pair in self.table:
            print(pair, "    =>   ", self.table[pair])

    def printFirst(self):
        for pair in self.FIRST:
            print(pair, "    =>   ", self.FIRST[pair])
            
    def printFollow(self):
        for pair in self.FOLLOW:
            print(pair, "    =>   ", self.FOLLOW[pair])
