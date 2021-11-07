from FiniteAutomata import FiniteAutomata
from ui import UI

console = UI()
console.run()

id = FiniteAutomata()
id.read_from_file('FA_id.in')
intt = FiniteAutomata()
intt.read_from_file('FA_int.in')