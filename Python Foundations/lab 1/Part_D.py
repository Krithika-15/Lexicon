#Part D- String investigation

# 1
print("Q-1")
sentence = "Programming"
print(len(sentence))
print(sentence[1:10]) # prints from index position 1 to 9
print(sentence[-7:-1]) # prints from index position -7 to -1
print(sentence[-3:-12:-1])  #-1 towards left starts from -3 and goes till -12 because of negative stepping
print(sentence[1:47:3]) #no IndexError: string index out of range in slicing
print(sentence[:-1]) # prints from default 0 position and excludes only last
print(sentence[:-1:2]) # prints from default 0 position and excludes only last , also prints alternatives
print(sentence[::-2]) #backwards every second string
print(sentence[:3:-1]) #start is last position as step is negative and stop is 3 excluded
print(sentence[3::-1]) #starts at 3rd index and no stop so goes till last in reverse as step is negative
print(sentence[5:2]) #forward step, stop before start so prints nothing
print(sentence[3:3]) #start == stop so prints nothing
print(sentence[2:][:3]) #chained slicing first takes this result sentence[2:] as "ogramming" and from this [:3] is performed gives "ogr"
print()


# 2
print("Q-2")
word = "Artificial Intelligence"
print(word[:10]) #first word only, index 0 up to (not including) 10 = "Artificial"
print(word[11:]) #second word only, index 11 to the end = "Intelligence"
print(word[:-1]) #whole string minus the last character
print(word[1:-1]) #whole string minus the first and last characters
print(word[::1]) #whole word
print(word[:]) #whole word
print(word[9::-1]) #starts at index 9 ('l') and goes backward to index 0, reverses "Artificial"
print(word[0:12:11]) #0 and 11 only , two capitals
print()


# 3
print("Q-3")
print("split() breaks one string into list of pieces")
alphabets = "a,b,,d"
alphabets_list = alphabets.split(",")
print(f"Alphabets : {alphabets}")
print(f"List of Alphabets : {alphabets_list}")

print("\nstrip() removes unwanted characters from the two ends only")
print("    hello   ".strip()) #removes leading/trailing whitespaces
print("\n\t  data \n\t".strip()) #newlines and tabs count as whitespace
print("xxxxhelloxxx".strip("x")) #removes x characters from both ends
print("...done!!!!".strip(".!"))
print("mississippi".strip("ips")) # gives m as a result, so basically result will never have ips characters at starting or at the end

print("\nreplace() swaps every occurence of one substring for another")
print("cat cat cat".replace("cat", "dog"))
print("cat cat cat".replace("cat", "dog", 1))
print("a-b-c".replace("-",""))

print("\nin checks whether a substring is present results in bool")
print("cat" in "concatenate")
print("dog" in "concatenate")
print("CAT" in "concatenate") #case sensitive
print()


# 4
print("Q-4")
word = "python"
# word[0] ="P"
print("word[0] ='P' gives TypeError: 'str' object does not support item assignment")
new_word = word[0].upper() + word[1:]
print(new_word)
