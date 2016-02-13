pos_matches = []
with open(r'../data/rosalind_subs.txt','r') as my_file:
    s = my_file.readline().replace('\n','')
    t = my_file.readline().replace('\n','')

    for indx, pos in enumerate(s):
        if s[indx:len(t)+indx] == t:
            pos_matches.append(indx+1)

    print str(pos_matches).replace(',','')
