text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# count the number of spaces in the source text including whitespaces
spaces_count = text.count(' ') + text.count('\n')

# bring the string to a single lower case format for further work, fix misspelled word
text = text.lower()
text = text.replace(' iz ', ' is ')

# make a nested list of separated sentences and words for further work
lst = [x.split() for x in text.split('.')]

# separate 'Howework:' header
lst.insert(0, [lst[0].pop(0)])

# add sentence with last words of each existing sentence to the end of the 2nd paragraph
lst.insert(3, [i[-1] for i in lst[:-1]])

# Make first words of sentences start from upper case again
for x in lst[:-1]:
    x[0] = x[0].title()

# join lists in sentences
lst = [' '.join(x) for x in lst]

# print the resulting text keeping the paragraphs
print(lst[0] + '\n' + lst[1] + '.\n' + '. '.join(lst[2:5]) + '.\n' + '. '.join(lst[6:8]) + '.\n' + '. '.join(lst[8::]))
print(f"count of spaces: {spaces_count}")
