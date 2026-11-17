L1 = ['re']
L2 = ['mi']
L3 = ['do']

L4 = L1 + L2

L3.append(L4)
L = L1.append(L3)

print("L1 =", L1)
print("L2 =", L2)
print("L3 =", L3)
print("L4 =", L4)
print("L =", L)

notes = ['do', 're', 'mi']

notes.extend(['fa', 'sol', 'la', 'si'])
notes.insert(6, 'ti')
notes[0] = 'DO'
notes[1:3] = ['RE', 'MI']
notes.remove('ti')

last_note = notes.pop()
notes.pop(2)
del notes[0]

notes.reverse()
notes.sort()
notes.clear()

print("notes =", notes)
print("last_note =", last_note)