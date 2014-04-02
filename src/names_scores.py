import string

def get_names_scores(self):    
    names = read_file()

    total_names_scores = 0
    i = 1
    for name in names:
        total_names_scores += get_name_score(name, i)
        i += 1

    return total_names_scores

def read_file():
    f = open('names.txt', 'r')
    raw_names = f.read()
    f.close()

    names = raw_names.split(",")
    names.sort()

    return names

def get_name_score(name, index):
    name_score = 0

    for char in name:
        name_score += string.uppercase.index(char) + 1

    name_score = name_score * index

    return name_score
 
if __name__ == '__main__':
    print get_names_scores(None)