day3 = open('input.txt').read().splitlines()

def getbits(data):
  mcbits = []
  lcbits = []
  for x in range(len(data[0])):
    bitlist = [line[x] for line in data]
    onebits = bitlist.count('1')
    zerobits = bitlist.count('0')
    if onebits >= zerobits:
      mcbits.append('1')
      lcbits.append('0')
    elif onebits < zerobits:
      mcbits.append('0')
      lcbits.append('1')

  return mcbits,lcbits

def part1(data):
  mc,lc = getbits(data)
  return int(''.join(mc),2) * int(''.join(lc),2)

print(part1(day3))

def part2(data):
  o2 = list(data)
  co2 = list(data)

  x = 0
  while len(o2) > 1:
    mc,lc = getbits(o2)
    o2 = [line for line in o2 if line[x] == mc[x]]
    x += 1

  x = 0
  while len(co2) > 1:
    mc,lc = getbits(co2)
    co2 = [line for line in co2 if line[x] == lc[x]]
    x += 1

  return int(o2[0],2) * int(co2[0],2)

print(part2(day3))
