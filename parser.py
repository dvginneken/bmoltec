def ParseFile(filename):
    '''
    Parsed files op formaat die als voorbeeld is gegeven op onenote
    :param filename: naam van de file die geopend moet worden
    :return: string van met een sequentie
    '''
    file = open(filename,'r')
    seq = file.readlines()
    seqfasta = [item.strip() for item in seq] #haalt enters eruit
    seq = []
    for i in seqfasta:
        if i: #checkt of i leeg is. Anders geeft hij een error bij de volgende if
            if not(i[0] == '>'): #check of het een fasta header is
                seq.append(i)
    seq = ''.join(seq)
    seq = ''.join([i for i in seq if not i.isdigit()]) #haalt getallen eruit
    return seq

print(ParseFile('testgen1.txt'))
print(ParseFile('testgen2.txt'))
print(ParseFile('testgen3.txt'))
print(ParseFile('testgen4.txt'))