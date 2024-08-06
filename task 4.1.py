import re
text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def count_characters(text, *args):
    # this function returns sum of counts of characters specified as args
    count = 0
    for x in args:
        count += text.count(x)
    return count


def normalise_letter_case(text):
    # this function forms two lists: list a with letters after the dots and newlines
    # list b with same fragments but fixed letter case
    # then it replaces fragments from list a to the corresponding fragments of list b
    text = text.capitalize()
    a = re.findall(r'.\. +.', text)
    a += (re.findall(r'\n +.', text))
    b = []
    for x in a:
        b.append(x.replace(x[-1], x[-1].upper()))
    for i, m in enumerate(a):
        text = text.replace(m, b[i])
    return text


def fix_misspelled_words(text, input, result):
    # this function replaces input fragment with the expected result not considering letter cases
    a = re.findall(input, text, re.IGNORECASE)
    for x in a:
        text = text.replace(x, result)
    return text


def insert_sentence(text, line, sentence):
    # this function inserts specified sentence at the end of specified line
    lst = text.splitlines()
    lst.insert(line, lst.pop(line) + ' ' + sentence)
    return '\n'.join(lst)


# here all four functions are called with parameters
spaces_count = count_characters(text, ' ', '\n')
text = normalise_letter_case(text)
text = fix_misspelled_words(text, ' iz ', ' is ')
text = insert_sentence(text, 4, ' '.join(x[-1] for x in [x.split() for x in text.split('.')][:-1]).capitalize() + '.')

print(text)
print(f"Count of spaces: {spaces_count}")