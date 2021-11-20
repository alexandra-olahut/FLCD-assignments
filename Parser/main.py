from Grammar import Grammar

g = Grammar()
g.read_from_file('g1.txt')

print(g.isCFG())
print(g.getNonterminas())
print(g.getTerminals())
print("PRODUCTIONS")
for prod in g.getProduction().keys():
    print(str(prod) + "->" + str(g.getProduction()[prod]))
print(' ')
print(g.getProductionsForNonterminal('A'))