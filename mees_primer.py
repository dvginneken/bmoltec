
class Primers_Maken():
    primer1 = None
    def __init__(self, seq, begin, einde, max):
        self.seq = seq
        self.begin = int(begin)
        self.einde = int(einde)
        self.max = int(max)
        self.uitvoeren()

    def uitvoeren(self):
        seqBegin, seqEinde = self.Knip(self.seq, self.begin, self.einde)
        primerParen = self.maakParen(self.einde, self.CheckSequence(seqBegin), self.CheckSequence(seqEinde), self.max)
        list.sort(primerParen)
        primerParen = primerParen[:10:]
        self.primer1 = primerParen

    def Complementary(self, strand):
        '''dna sequentie word in zijn complimentair overgezet
        :param strand: dna sequentie
        :return: complimentair
        '''
        return strand.translate(str.maketrans('AaTtGgCc', 'TtAaCcGg'))


    def BerekenGcPercentage(self, gc, seq):
        '''
        :param gc: aantal gc van TelBp()
        :param seq: de primer
        :return: gc percentage float met 2 cijfers achter de komma
        '''
        GcPercentage = gc / len(seq)
        return float("%.2f" % GcPercentage)


    def TelBp(self, seq):
        """telt het aantal c+g en a+t in een gegeven sequentie. dit is nodig
        voor de temperatuur te berekenen en om de gc content te berekenen
        :param seq: primer sequentie
        :return at: aantal at in de sequentie
                gc: aantal gc in de sequentie
        """
        seq = seq.lower()
        gc = seq.count('c') + seq.count('g')
        at = len(seq) - gc
        return at, gc


    def Temperatuur(self, gc, at):
        """Berekend de smelt temperatuur
        :param gc: aantal gc van TelBp()
        :param at: aantal at van TelBp()
        :return Tm: smelt temperatuur van de mogelijke primer
        """
        Tm = (2 * at) + (4 * gc)
        return Tm


    def CheckSequence(self, seq):
        """ Checkt elke mogelijke combinatie van 17 tot en met 25 lengte of
        ze voldoen aan de primer dingen
        :param seq: dna sequentie
        :return TopPrimers: Dict met alle mogelijke primers items zijn GC percentage en smeltpunt
        """
        seq = list(seq)
        MaxPrimerLengte = 25
        MinPrimerLengte = 17
        TopPrimers = {}
        for i in range(len(seq)):
            for k in range(MaxPrimerLengte - MinPrimerLengte + 1):
                # TODO: alle foute "primers" toevoegen aan een lijst en checken of nieuwe "primer" al in de lijst zit. Misschien bespaart tijd
                # TODO: eerder checken of een nieuwe "primer" kleiner dan 17 characters bevat
                primer = ''.join(seq[i:k + MinPrimerLengte + i])
                at, gc = self.TelBp(primer)
                GcPercentage = self.BerekenGcPercentage(gc, primer)
                Tm = self.Temperatuur(gc, at)
                if Tm >= 55 and Tm <= 65 and GcPercentage >= 0.50 and \
                        GcPercentage <= 0.60 and len(primer) >= 17:
                    TopPrimers[str(i) + ':' + str(k + MinPrimerLengte + i)] = [
                        primer, GcPercentage, Tm]
        return TopPrimers


    def Knip(self, seq, begin, einde):
        '''haalt het stuk eruit waar niet gezocht mag worden naar een primer en
        geeft de twee buiten sequenties terug
        :param seq: de gehele sequentie
        :param begin: begin van het verbode deel
        :param einde: einden van het verbode deel
        :return: geeft de twee sequenties terug
        '''
        seqBegin = seq[:begin:]
        seqEinde = seq[einde::]
        # Moet seqEinde ook reverse zijn?
        seqEinde = self.Complementary(seqEinde)
        return seqBegin, seqEinde


    def maakParen(self, einde, seqBegin, seqEinde, maxPcr):
        ''' checkt elke begin primer met een eind primer voor of ze matchen
        met bv de tm verschil en of ze niet te ver uit elkaar liggen
        :param einde: einde van het verbode deel van de sequentie
        :param seqBegin: sequentie van voor het verbode deel
        :param seqEinde: sequentie van na het verbode del
        :param maxPcr: maximale lengte wat de pcr mag hebben
        :return: primerparen lijst met elke item alle informatie over een
        primer paar. de informatie de elke item bevat is:
        primerParen[i][0] = integer van aantal basepare verschil
        primerParen[i][1][0] = primer begin seq
        primerParen[i][1][1] = primer begin gc percentage
        primerParen[i][1][2] = primer begin Tm
        primerParen[i][2][0] = primer eind seq
        primerParen[i][2][1] = primer eind gc percentage
        primerParen[i][2][2] = primer eind Tm
        '''
        primerParen = []
        for i in seqBegin:
            bPositie = int(i.split(':')[0])
            for k in seqEinde:
                ePositie = int(k.split(':')[1]) + einde
                verschil = ePositie - bPositie
                tmVerschil = seqBegin[i][2] - seqEinde[k][2]
                if (verschil <= maxPcr) and ((tmVerschil >= -2) and(tmVerschil <= 2)):
                    primerParen.append([verschil,
                                        [i, seqBegin[i][0], seqBegin[i][1],
                                         seqBegin[i][2]],
                                        [k, seqEinde[k][0], seqEinde[k][1],
                                         seqEinde[k][2]]])
        return primerParen

if __name__ == "__main__":
    Primers_Maken()

    # seq = "gaattcgaggacgcggaatttgctgtacgcaatgcctttcgcgacgatctgtggggaggggagt" \
    #       "ctctgcggcgaagcaggcccgtgggaacctcgaccgatccgtagcgggttcgacaagaccaaga" \
    #       "ccgtcccacgccagcccaaaaagaccccggtcacgaagagctgaccgctcgtttgcggctggtg" \
    #       "acagcgttcttaccggcacctctggaccgcgtggcgggggcatcctgacgggggaaggcctggg" \
    #       "ggaggcagcggtggacttcgcgttcgtgtgcggctggtgcggggaggaatgcgtcgtgtggggc" \
    #       "gagcctgtcgtctcttggtggacggacaagtaccgggtgcccgacgacttcgagtgggtcatgt" \
    #       "ggaggcgtcagcacctccccgcctccgctggacgcccgccgactaggcactgtccggcggatca" \
    #       "tgtgaccttctgactggtcgctcgttggttcggtcatgggtcggggggatctgacgaatcgcga" \
    #       "gtggtcgttgcttgagccgcatctgccacctttgggtggccggggcggccggtggaacgaccac" \
    #       "cgcaccgtggtcaacgggatcctgttccgggtccggaccggtgttctggcgtgatctgccggaa" \
    #       "cgctatggctcgtggaagaccatctacgagcggcatcgccgctggtcggcggacggcacctggg" \
    #       "atcggatcctgcagtcggtccaggccgacgccgacctcgccgggcggatcgactggcgatggtc" \
    #       "ggcgtcgactcgacgtcctgccgggcccatcagcacgcggccggcgcccgcaagacccggccgc" \
    #       "gggtcccgaaaaaaggacaacgccccggcaccaccgccccgacgaggactcggacgtcccgggg" \
    #       "cggcctgacctgcaagatccacctcgccggcgaaggcggctgccgcccactggccctcctgctc" \
    #       "acccccggccaatggggcgatgccccgcaactggtcgggtcctggaccggatcagagtcccccg" \
    #       "gccgttgggcgggcgaccccggacccggcccgaccacgtcagcggcgacaaggcatacagctcc" \
    #       "cgccgcaaccgccgctacctgcgaagacccgcatccggcacacgatcccggaaccgaaggacca" \
    #       "gcgggccaaccgccgccgcagaggcagagaaggcggcaggcccgccggcttcgaccgggaccac" \
    #       "taccggcgacgcaacgaggtcgagcgcaccatcaaccggctcaagaacttccgcgccgtggcca" \
    #       "cccgttacgacaagagggcctacgtcttccacggcaccgtcaccgccgcggcgatccgactctg" \
    #       "gctccgacagtgatccgccggacagaacctagaccgcgcggcgagctggtcgacggccacgacg" \
    #       "cggcagggggccggagcaagatcagacgaccggtgaggacaaagggggttcccccgggggagcc" \
    #       "ccggacctcgagg"
    #
    # maxpcr = 420
    # begin = 80
    # einde = 400
    # test = Primers_Maken(seq, begin, einde, maxpcr)
    # primers = test.primer1
    # list.sort(primers)
    # primers = primers[:20:]
    # print(primers)