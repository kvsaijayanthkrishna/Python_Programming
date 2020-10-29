#5. Write a Python function that takes a list of words and returns the length of the longest one.
string=input("enter list of words with spaces\t:")
words_list=string.split()
length=len(words_list[0])
longest=""
for word in words_list:
    if len(word)>length:
        length=len(word)
        longest=word
print('longest word in "{0}" is {1} and length {2}'.format(string,longest,length))
    
