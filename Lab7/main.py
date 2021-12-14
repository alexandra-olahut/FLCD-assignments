from Grammar import Grammar
from Parser import Parser
from ParseTree import Tree
from ui import UI


ui = UI()
ui.run()


# g = Grammar()
# g.read_from_file('L5\\my.txt')
# # S -> aSbS -> acbS -> acbc
# p = Parser(g)

# p.printFirst()
# p.printFollow()
# p.printTable()
# # print(p.parse("{ for id from ( id , id , id ) { if id > constant { id <- constant ; } ; } ; }"))
# prod = p.parse("{ declare id : int ; declare id : array ( string ) ; id <- constant * constant ; read ( id ) ; write ( constant ) ; for id from ( constant , constant , id ) { if id <= constant { id <- constant * constant / id + id ; } ; } ; }")
# print(prod)
# # # prod = p.parse("a c b c")
# # prod = p.parse("( int ) + int")

# t = Tree(g, prod)
# t.printTree()
# print(t.reconstructSequence())
# print(p.parse("( int ) + int"))

# print(p.concatenation1({"aa","bb","eps"}, {"00", "01"}))
# print(p.concatenation1(("aa","bb","eps"), ("00", "01")))
# print(p.concatenateAll(( ("aa","bb","eps"), ("01", "eps"), ("y", "eps"), ("o", "eps") )))
# clea# print("---------------")
# # first = p.buildFirst()
# follow = p.buildFollow()
# p.printTable()
# print(p.parse("( int ) + int"))
# for f in follow:
#     print(f)
#     print(follow[f])

# print(p.concatenation1({"int"}, {"00", "01"}))
# print(p.concatenateAll(({'int'}, {'eps', '*'})))

# print(g.isCFG())
# print(g.getNonterminas())
# print(g.getTerminals())
# print("PRODUCTIONS")
# for prod in g.getProduction().keys():
#     print(str(prod) + "->" + str(g.getProduction()[prod]))
# print(' ')
# print(g.getProductionsForNonterminal('A'))