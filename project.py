
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")
file.close()


file = open("sample.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()


file = open("sample.txt", "a")
file.write("This is an appended line.\n")
file.close()

file = open("sample.txt", "r")
print("\nReading line by line:")
for line in file:
   print(line.strip())
file.close()


file = open("sample.txt", "r")
lines = file.readlines()
num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)

print("\nNumber of lines:", num_lines)
print("Number of words:", num_words)

file.close()