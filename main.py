import random

scale_dict = {
  'C Major' : ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C^'],
  'D Major' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D^'],
  'E Major' : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E^'],
  'F Major' : ['F', 'G', 'A', 'b', 'C', 'D', 'E', 'F'],
  'G Major' : ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G^'],
  'C Minor' : ['C', 'D', 'e', 'F', 'G', 'a', 'b', 'C^']
}


def main():
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
  out = ""
  for i in range(int(measures) * 4):
    next_beat = ''
    note_type = random.randrange(0,100,1)
    if (note_type < 50): # quater note
      next_beat = random.choice(scale)
    elif (note_type < 70): # eighth note
      next_beat = random.choice(scale)
      next_beat += '/' + random.choice(scale)
    elif (note_type < 85): # hold note
      # change to delete the last character first
      out = out[:-1]
      next_beat = '-'
    else:
      next_beat = ' '
    out += next_beat + ','
  print()
  print(out)
  print()

if __name__ == "__main__":
  main()