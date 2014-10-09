import itertools

def get_all_permutations(items, index):
    print items
    permutations = list(itertools.permutations(items))
    lexicographic_permutations = []
    for i in permutations:
        #print i
        this_permutation = ''.join(map(str, i))
        #print this_permutation
        lexicographic_permutations.append(this_permutation)
    print sorted(lexicographic_permutations)[index]
    
if __name__ == '__main__':
    items = range(0, 10)
    print get_all_permutations(items, 999999)