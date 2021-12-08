from Grammar import Grammar
from Parser import Parser

g = Grammar()
g.read_from_file('L5\\test10.txt')

p = Parser(g)

p.printFirst()
p.printFollow()
p.printTable()
# print(p.parse("{ for ID from ( ID , ID , ID ) { if ID > CONST { ID <- CONST ; } ; } ; }"))
# print(p.parse("{ declare ID : int ; declare ID : array ( string ) ; ID <- CONST * CONST ; read ( ID ) ; write ( CONST ) ; for ID from ( CONST , CONST , ID ) { if ID <= CONST { ID <- CONST * CONST / ID + ID ; } } }"))
print(p.parse("( int ) + int"))

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