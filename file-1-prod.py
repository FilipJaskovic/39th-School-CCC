file = open("./level1_5.in", "r")
contents = file.read()

# Split the input string by newline character
lines = contents.split("\n")

# Extract the first two numbers
first_three_numbers = [int(lines[0]), int(lines[1]), int(lines[2])]

# Extract the list of numbers
list_of_numbers = []
for line in lines[3:-1]:
    numbers = list(map(int, line.split()))
    list_of_numbers.append(numbers)

print(list_of_numbers)

out = ""
for currency in list_of_numbers:
  min = currency[0]
  max = currency[-1]
  for i in range(min, max):
    if i not in currency:
      out += str(i) + "\n"
      break

with open("output5.txt", "w") as file:
  # Write the string to the file
  file.write(out)