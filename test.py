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
    """"
    sequentie = een stuk dna van de notebook
    grens_l = linkergrens van wat je wilt dupliceren
    grens_r = rechtergrens van wat je wilt dupliceren

    Eerst op zoek naar een linkerprimer door te kijken naar de mogelijke lengtes tussen 17 en 25.
    Primers worden in de functie Test gegooid die aan de hand van de functies GC en Temperatuur checken of deze aan de voorwaardes voldoen,
    zo ja wordt de smelttemperatuur (tm) teruggegeven, zo nee wordt 0 teruggegeven.
    Als er een goede linkerprimer is gevonden gaat hij hetzelfde doen voor de rechterprimer.
    Als er 2 goede primers worden gevonden wordt gekeken of de tm dicht genoeg bij elkaar ligt.


    """

    sequentie = "gaattcgaggacgcggaatttgctgtacgcaatgcctttcgcgacgatctgtggggaggggagtctctgcggcgaagcaggcccgtgggaacctcgaccgatccgtagcgggttcgacaagaccaagaccgtcccacgccagcccaaaaagaccccggtcacgaagagctgaccgctcgtttgcggctggtgacagcgttcttaccggcacctctggaccgcgtggcgggggcatcctgacgggggaaggcctgggggaggcagcggtggacttcgcgttcgtgtgcggctggtgcggggaggaatgcgtcgtgtggggcgagcctgtcgtctcttggtggacggacaagtaccgggtgcccgacgacttcgagtgggtcatgtggaggcgtcagcacctccccgcctccgctggacgcccgccgactaggcactgtccggcggatcatgtgaccttctgactggtcgctcgttggttcggtcatgggtcggggggatctgacgaatcgcgagtggtcgttgcttgagccgcatctgccacctttgggtggccggggcggccggtggaacgaccaccgcaccgtggtcaacgggatcctgttccgggtccggaccggtgttctggcgtgatctgccggaacgctatggctcgtggaagaccatctacgagcggcatcgccgctggtcggcggacggcacctgggatcggatcctgcagtcggtccaggccgacgccgacctcgccgggcggatcgactggcgatggtcggcgtcgactcgacgtcctgccgggcccatcagcacgcggccggcgcccgcaagacccggccgcgggtcccgaaaaaaggacaacgccccggcaccaccgccccgacgaggactcggacgtcccggggcggcctgacctgcaagatccacctcgccggcgaaggcggctgccgcccactggccctcctgctcacccccggccaatggggcgatgccccgcaactggtcgggtcctggaccggatcagagtcccccggccgttgggcgggcgaccccggacccggcccgaccacgtcagcggcgacaaggcatacagctcccgccgcaaccgccgctacctgcgaagacccgcatccggcacacgatcccggaaccgaaggaccagcgggccaaccgccgccgcagaggcagagaaggcggcaggcccgccggcttcgaccgggaccactaccggcgacgcaacgaggtcgagcgcaccatcaaccggctcaagaacttccgcgccgtggccacccgttacgacaagagggcctacgtcttcca"
    grens_l = 130
    grens_r = 330

    for lengte in range(17,26):
        links = sequentie[(int(grens_l)-lengte):int(grens_l)]
        pos_l = int(grens_l)-lengte
        tm_links = Test(links)
        if tm_links != 0:
            for lengte2 in range(17,26):
                rechts = sequentie[grens_r:(grens_r + lengte2)]
                tm_rechts = Test(rechts)
                if tm_rechts != 0:
                    verschil = tm_links - tm_rechts
                    if (verschil >= -2) and (verschil <= 2):
                        print("links:", pos_l, links, tm_links)
                        print("rechts:", rechts, tm_rechts)
main()
