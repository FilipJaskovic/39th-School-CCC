
file = open("level4_example.in", "r")
contents = file.read()

lines = contents.split("\n")

first_two_numbers = [int(lines[0]), int(lines[1])]

list_of_numbers = []
for line in lines[3:]:
    numbers = list(map(int, line.split()))
    list_of_numbers.append(numbers)

length = first_two_numbers[1]
out = ""
for i in range(0, len(list_of_numbers) -1, 2):
  incurr = list_of_numbers[i]
  amounts = list_of_numbers[i+1]
  print(incurr, amounts)
  for a in amounts:
    remaining = a
    currencies = incurr
    results = []
    for currency in currencies[::-1]:
        if (remaining == remaining % currency): 
            continue
        div = remaining // currency
        results.append(f"{div}x{currency}")
        remaining = remaining % currency
    for r in results:
      out += r + " "
    out=out.strip()
    out+="\n"

with open("final_output2.txt", "w") as file:
  file.write(out)