import random

def main():
  notes = ['A', 'A#', 'a', 'B', 'B#', 'b', 'C', 'C#', 'c', 'D', 'D#', 'd', 'E', 'E#', 'e', 'F', 'F#', 'f', 'G', 'G#', 'g']
  modifiers = ['#', '_']
  out = ""
  for i in range(16):
    nextBeat = ''
    noteType = random.randrange(0,100,1)
    if (noteType < 50): # quater note
      nextBeat = random.choice(notes)
    elif (noteType < 70): # eighth note
      nextBeat = random.choice(notes)
      nextBeat += '/' + random.choice(notes)
    elif (noteType < 85): # hold note
      # change to delete the last character first
      out = out[:-1]
      nextBeat = '-'
    else:
      nextBeat = ' '
    out += nextBeat + ','
  print()
  print(out)
  print()

if __name__ == "__main__":
  main()