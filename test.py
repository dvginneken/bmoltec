def GC(g_seq):
    gc_teller = 0
    nucleotide_teller = 0
    for nucl in g_seq:
        nucleotide_teller += 1
        if nucl == "G" or nucl == "C":
            gc_teller += 1
    content = gc_teller / nucleotide_teller
    return [content, gc_teller, nucleotide_teller]

def Temperatuur(gc, at):
    tm = (2*at)+(4*gc)
    return tm

def Test(links, rechts):
    gc_perc_l = GC(links)[0]
    gc_teller_l = GC(links)[1]
    nucleotide_teller_l= GC(links)[2]
    if (gc_perc_l >= 0.5) and (gc_perc_l <= 0.6):
        tm_l = Temperatuur(gc_teller_l, (nucleotide_teller_l-gc_teller_l))
        gc_perc_r = GC(rechts)[0]
        gc_teller_r = GC(rechts)[1]
        nucleotide_teller_r = GC(rechts)[2]
        print(gc_perc_r)
        if (gc_perc_r >= 0.5) and (gc_perc_r <= 0.6):
            tm_r = Temperatuur(gc_teller_r, (nucleotide_teller_r - gc_teller_r))
            print(tm_r)

def main():
    #file = open("sequence.fasta", "r")
    #sequentie = file.read()
    sequentie = "CCCACGCGTCCGTTCTCTTCCAAGGAACTTTTTGTTTGTTTTATAAAGCAATGGGAAATCCAGAAAACAT\
    CGAAGATGCTTACGTTGCAGTTATTCGTCCAAAGAACACTGCTAGTCTCAACTCCCGGGAGTATAGAGCT\
    AAGTCCTATGAAATTTTATTGCATGAAGTTCCCATTGAAGGACAGAAAAAAAAGCGAAAGAAAGTTTTGC\
    TGGAAACTAAACTTCAAAGCAACAGTGAAATAGCACAAGGCATATTGGACTATGTAGTAGAAACTACCAA\
    ACCAATTTCTCCTGCAAACCAGGGGATTAAAGGGAAACGAGTGGTGCTGATGAGGAAGTTTCCTCTGGAC\
    GGAGAGAAGACAGGCAGAGAAGCAGCACTGTTTATCGTGCCATCAGTTGTCAAAGATAATACTAAATATG\
    CATATACTCCTGGATGCCCAATTTTTTACTGCTTACAAGATATTATGAGAGTTTGTAGTGAATCCAGTAC\
    TCACTTTGCAACACTTACAGCAAGGATGTTAATAGCCTTGGATAAGTGGTTAGATGAACGTCATGCGCAG\
    TCTCACTTTATTCCAGCTTTATTCCGACCTTCTCCCCTTGAACGGATAAAGACAAATGTCATAAACCCTG\
    CGTATGCTGCTGAATTAGGCCAGGTAGACAATTCACTACATATGGGCTATAGTGCACTAGAAATAAAGAG\
    TAAAATGCTAGCCCTAGAGAAAGCAGACACCTGCATTTACAACCCTTTGTTTGGATCAGATCTTCAGTAT\
    ACAAATCGGGTAGATAAAGTGGTAATAAATCCATACTTTGGTCTCGGAGCTCCAGACTACTCAAAAATCC\
    AAATTCCCAAACAGGAAAAATGGCAGCGAAGCATGAGCAGCGTTGTGGAAGACAAAGAACGACAGTGGGT\
    TGATGACTTTCCTTTACATCGAAATGCCTGTGAAGGAGATTCAGAATTACTGAGCCATCTTCTCGATAAA\
    GGACTTTCAGTCAACCAACTAGATAATGACCACTGGGCACCCATTCATTATGCATGCTGAAAGCATCTGT\
    ACCATTGCTTGTCTTCTGAGTATTCTGTTCTGATCTTTTGATTACTGTGTATATGCTGCTGTTCGGAACT"
    grens_l = 30
    grens_r = 50
    max_lengte = 30

    links = sequentie[(int(grens_l)-25):int(grens_l)]
    rechts = sequentie[grens_r:(grens_r+25)]
    Test(links, rechts)
main()
