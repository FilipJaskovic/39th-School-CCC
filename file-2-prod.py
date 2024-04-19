file = open("./level2_5.in", "r")
contents = file.read()

lines = contents.split("\n")

first_two_numbers = [int(lines[0]), int(lines[1])]

list_of_numbers = []
for line in lines[3:]:
    numbers = list(map(int, line.split()))
    list_of_numbers.append(numbers)

out = ""
for i in range(0, len(list_of_numbers) -1, 2):
  amounts = list_of_numbers[i+1]
  currency = list_of_numbers[i]
  print(amounts, currency)
  sols = []
  mode = False
  for a in amounts:
    for j in currency:
      for k in currency:
        if a == j + k:
          if not mode:
            sols.append([j, k])
          mode = True
    mode = False
  
  print(sols)
  
  for s in sols:
    out += str(s[0]) + " " + str(s[1]) + "\n"


with open("output5.txt", "w") as file:
  file.write(out)