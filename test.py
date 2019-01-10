def GC(g_seq):
    gc_teller = 0
    nucleotide_teller = 0
    for nucl in g_seq:
        nucleotide_teller += 1
        if nucl == "g" or nucl == "c":
            gc_teller += 1
    content = gc_teller / nucleotide_teller
    return [content, gc_teller, nucleotide_teller]

def Temperatuur(gc, at):
    tm = (2*at)+(4*gc)
    return tm

def Test(primer):
    gc_perc = GC(primer)[0]
    gc_teller = GC(primer)[1]
    nucleotide_teller= GC(primer)[2]
    if (gc_perc >= 0.5) and (gc_perc <= 0.6):
        tm = Temperatuur(gc_teller, (nucleotide_teller-gc_teller))
        if (tm >= 55) and (tm <= 65):
            return tm
        else:
            return 0
    else:
        return 0

def main():
    sequentie = "gaattcgaggacgcggaatttgctgtacgcaatgcctttcgcgacgatctgtggggaggggagtctctgcggcgaagcaggcccgtgggaacctcgaccgatccgtagcgggttcgacaagaccaagaccgtcccacgccagcccaaaaagaccccggtcacgaagagctgaccgctcgtttgcggctggtgacagcgttcttaccggcacctctggaccgcgtggcgggggcatcctgacgggggaaggcctgggggaggcagcggtggacttcgcgttcgtgtgcggctggtgcggggaggaatgcgtcgtgtggggcgagcctgtcgtctcttggtggacggacaagtaccgggtgcccgacgacttcgagtgggtcatgtggaggcgtcagcacctccccgcctccgctggacgcccgccgactaggcactgtccggcggatcatgtgaccttctgactggtcgctcgttggttcggtcatgggtcggggggatctgacgaatcgcgagtggtcgttgcttgagccgcatctgccacctttgggtggccggggcggccggtggaacgaccaccgcaccgtggtcaacgggatcctgttccgggtccggaccggtgttctggcgtgatctgccggaacgctatggctcgtggaagaccatctacgagcggcatcgccgctggtcggcggacggcacctgggatcggatcctgcagtcggtccaggccgacgccgacctcgccgggcggatcgactggcgatggtcggcgtcgactcgacgtcctgccgggcccatcagcacgcggccggcgcccgcaagacccggccgcgggtcccgaaaaaaggacaacgccccggcaccaccgccccgacgaggactcggacgtcccggggcggcctgacctgcaagatccacctcgccggcgaaggcggctgccgcccactggccctcctgctcacccccggccaatggggcgatgccccgcaactggtcgggtcctggaccggatcagagtcccccggccgttgggcgggcgaccccggacccggcccgaccacgtcagcggcgacaaggcatacagctcccgccgcaaccgccgctacctgcgaagacccgcatccggcacacgatcccggaaccgaaggaccagcgggccaaccgccgccgcagaggcagagaaggcggcaggcccgccggcttcgaccgggaccactaccggcgacgcaacgaggtcgagcgcaccatcaaccggctcaagaacttccgcgccgtggccacccgttacgacaagagggcctacgtcttcca"
    grens_l = 30
    grens_r = 50
    max_lengte = 30



    for lengte in range(17,26):
        links = sequentie[(int(grens_l)-lengte):int(grens_l)]
        print("l: ", links)
        tm_links = Test(links)
        if tm_links != 0:
            print(tm_links)
            for lengte2 in range(17,26):
                rechts = sequentie[grens_r:(grens_r + lengte)]
                print("r: ", rechts)
                tm_rechts = Test(rechts)
                if tm_rechts != 0:
                    print(tm_rechts)
main()
