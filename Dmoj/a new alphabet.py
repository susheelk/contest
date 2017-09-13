letters = list("abcdefghijklmnopqrstuvwxyz")
new = ['@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\\/[]', '[]\\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\\/', '\\/\\/', '}{', '`/', '2']

string = list(raw_input().lower())

for i in range(len(string)):
    if (string[i].isalpha()):
        string[i] = new[letters.index(string[i])]

print "".join(string)
