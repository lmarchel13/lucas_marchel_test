def overlapping(firstLine, secondLine):
  if firstLine[0] > firstLine[1]:
    firstLine = (firstLine[1],firstLine[0])

  if secondLine[0] > secondLine[1]:
    secondLine = (secondLine[1],secondLine[0])
  
  return firstLine[1] >= secondLine[0] and secondLine[1] >= firstLine[0]

