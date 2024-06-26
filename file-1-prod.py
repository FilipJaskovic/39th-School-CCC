file = open("./level1_5.in", "r")
contents = file.read()

lines = contents.split("\n")

first_three_numbers = [int(lines[0]), int(lines[1]), int(lines[2])]

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
  file.write(out)