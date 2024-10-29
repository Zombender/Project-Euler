letters = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g': 7,
    'h' : 8,
    'i' : 9,
    'j': 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' :14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
}
def names_scores(file):
    with open(file,'r') as f:
        info = f.read()
        info = info.split(',')
        info = list(map(lambda x : x[1:len(x)-1].lower(),info))
        info = sorted(info) 
        info = list(map(lambda x : map_names(x,info.index(x)+1),info))
        print(sum(info))

def map_names(name,pos):
    sum_char_name = sum(letters[char] for char in name)
    return sum_char_name * pos


file = r'Page 1\22. Names Scores\0022_names.txt'
names_scores(file)
