
List = []
with open("words.txt") as f:
   for line in f:
      for word in line.split():
          List.append(word) # add only first word
revwords = List[::-1]
print(revwords)
