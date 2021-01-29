# lower method on string
# empty dictionary
# convert string to list
# loop through list and check is list item is a letter
# check to see if the letter has a key that is the same letter
# if key does not exist, add key with empty list and add first letter
# if key exists add letter to list

text = "Like the castle in its corner in a medieval game, I foresee a terrible trouble and I stay here just the same."
counter = {}
text_list = list(text.lower())
text_list.sort()

for i in text_list:
    if i.isalpha():
      if i in counter.keys():
        counter[i].append(i)
      else:
        counter[i] = [i]

print(counter)      