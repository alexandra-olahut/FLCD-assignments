from Grammar import Grammar


class Node:
    def __init__(self, index, info, parent, leftSibling):
        self.index = index
        self.info = info
        self.parent = parent
        self.left_sibling = leftSibling
        self.processed = False
    
    def __str__(self) -> str:
        return "N: "+ str(self.index)+ "-> "+ str(self.info)+ " p "+ str(self.parent)+ " l "+ str(self.left_sibling)

class Tree:
    def __init__(self, grammar: Grammar, productions):
        self.nodes = []
        self.grammar = grammar
        self.buildTree(productions)

    def buildTree(self, productions):
        start_node = Node(1, self.grammar.start_symbol, 0, 0)
        self.nodes.append(start_node)

        for productionIndex in productions:
            lhs, rhs = self.getProduction(productionIndex)
            for node in self.nodes:
                if node.info == lhs and not node.processed:
                    break
            left = 0
            for rhs_index in range(len(rhs)):
                rhs_part = rhs[rhs_index]
                child = Node(len(self.nodes)+1, rhs_part, node.index, left)
                self.nodes.append(child)
                left = child.index
            node.processed = True

    def printTree(self):
        output = ""
        for node in self.nodes:
            output += "{:<6} | {:<18} | {:<6} | {:<10}".format(node.index, node.info, node.parent, node.left_sibling) + '\n'
            print("{:<6} | {:<18} | {:<6} | {:<10}".format(node.index, node.info, node.parent, node.left_sibling))
        return output

    def getProduction(self, index):
        for key, value in self.grammar.productions.items():
            lhs = key[0]
            for production in value:
                rhs = production[0]
                productionIndex = production[1]
                if productionIndex == index:
                    return (lhs, rhs)


    def reconstructSequence(self):
        parents = [node.parent for node in self.nodes]
        leaves = []
        for node in self.nodes:
            if node.index not in parents:
                leaves.append(node.info)
        return leaves