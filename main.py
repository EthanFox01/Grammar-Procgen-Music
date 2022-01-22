import random

# out = ""
#   for i in range(int(measures) * 4):
#     next_beat = ''
#     note_type = random.randrange(0,100,1)
#     if (note_type < 50): # quater note
#       next_beat = random.choice(scale)
#     elif (note_type < 70): # eighth note
#       next_beat = random.choice(scale)
#       next_beat += '/' + random.choice(scale)
#     elif (note_type < 85): # hold note
#       # change to delete the last character first
#       out = out[:-1]
#       next_beat = '-'
#     else:
#       next_beat = ' '
#     out += next_beat + ','
#   print()
#   print(out)
#   print()

scale_dict = {
  'C Major' : ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C^'],
  'D Major' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D^'],
  'E Major' : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E^'],
  'F Major' : ['F', 'G', 'A', 'b', 'C', 'D', 'E', 'F'],
  'G Major' : ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G^'],
  'C Minor' : ['C', 'D', 'e', 'F', 'G', 'a', 'b', 'C^']
}

grammar = {
  "<start>" : "<note><note><expr>",
  "<expr>" : [ "<symbol><expr>" ],
  "<symbol>" : [ "<note>", "<pause>" ],
  "<note>" : [ "<eighth>", "<quarter>" ],
  "<pause>" : [ "*"]
  
} 

def expand_expr(expr):
  expr_list = []
  term = ""
  flag = False
  for char in expr:
    if char == '<':
      flag = True
    if flag:
      term += char
    if char == '>':
      expr_list.append(term)
      term = ""
      flag = False
  return expr_list

def select_note():
  note_type = random.choice(grammar["<note>"])
  note = random.choice(scale_dict['C Major'])
  if note_type == "<eighth>":
    note += '/'
  return note

def remove_symbols(term):
  new_term = ""
  flag = False
  last_note = ''
  for char in term:
    if char == '<':
      flag = True
    if not flag:
      if last_note == '*' and char == '*':
        char = select_note()
      new_term += char
      last_note = char
    if char == '>':
      flag = False
  return new_term

def grammar_fuzzer(scale, measures):
  term = "<expr>"
  max_beats = measures * 4
  beats = 0
  i = 0
  while (beats < max_beats):
    remaining_symbols = expand_expr(term)
    symbol_to_expand = random.choice(remaining_symbols)

    print(term)
    print("I:" + str(i) + "; S_t_E: ", end='')
    print(symbol_to_expand)

    expansions = grammar[symbol_to_expand]
    print(expansions)
    expansion = random.choice(expansions)
    print(expansion)
    new_term = term.replace(symbol_to_expand, expansion, 1) 
    if expansion == "<quarter>":
      scale_note = random.choice(scale_dict[scale])
      new_term = new_term.replace(expansion, scale_note, 1)
      beats += 1
    if expansion == "<eighth>":
      scale_note = random.choice(scale_dict[scale])
      new_term = new_term.replace(expansion, scale_note + '/', 1)
      beats += 0.5
    if expansion == "*":
      beats += 1
    term = new_term
    i += 1
    print()
  print(remove_symbols(term))

def get_user_input():
  print('Standard notes are written as capitals. Sharps have a # appended. Flats are in lowercase. Ex: A, D#, e')
  print('The app assumes 4/4 time. Beatss are separated by commas. A note being held for a beat uses a -. Ex: F--')
  print('Eighth notes are written together in a beat and separated with a /. Ex: A/B, ')
  print("The following scales are available:")
  for key in scale_dict:
    print(key, end=' ')
  print()
  scale_input = input("Enter the key to use: ")
  scale = scale_dict[scale_input]
  measures = input("Enter how many measures you would like to generate: ")
  return (scale, measures)

def main():
  # expand_expr("<note> E <expr>")

  # input = get_user_input()
  # scale, measures = input
  # grammar_fuzzer(scale, measures)
  
  grammar_fuzzer("C Major",3)
  # select_note()
  

if __name__ == "__main__":
  main()