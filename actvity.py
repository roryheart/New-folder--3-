with open('Codingal.txt', 'w') as file:
  file.write("hi i am meera and im 14")
file.close()


with open('Codingal.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

