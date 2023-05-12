def mutate_string(string, position, character):
    l=list(s)
    l[i]= c
    s=''.join(l)
    return
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print (string)
