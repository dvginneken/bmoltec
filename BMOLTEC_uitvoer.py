""""__Auteurs__ = "Kenrick de Grijs, Daphne van Ginneken, Mees Kerssens"
    __Versie__ = "1.0.1"
    __Klas__ = "Bin2A" """

import wx


class Panel3(wx.Panel):
    primers = None
    def __init__(self, parent):
        """" Hier worden de globale variabelen en de overige functies aangeroepen."""
        wx.Panel.__init__(self, parent, -1)
        final = self.boxCreeren2()
        self.SetSizer(final)



    def boxCreeren2(self):
        """" Deze functie zorgt ervoor dat er ruimte komt tussen alle verschillende
             onderdelen in het 'Uitvoer' paneel."""

        self.empy_box = wx.BoxSizer(wx.VERTICAL)

        self.button1 = wx.Button(self, -1, "Afsluiten")
        self.button2 = wx.Button(self, -1, "Opnieuw")

        dbox = wx.BoxSizer(wx.HORIZONTAL)
        dbox.Add(self.button1, 1, wx.EXPAND)
        dbox.Add(self.button2, 1, wx.EXPAND)

        panel = wx.Panel(self, -1)

        eindbox = wx.BoxSizer(wx.VERTICAL)
        eindbox.Add(panel,1,wx.EXPAND)
        eindbox.Add(self.empy_box,1,wx.EXPAND)
        eindbox.Add(dbox,1,wx.EXPAND)
        return eindbox




    def updatePrimers(self, primers):
        self.primers = primers
        print("primer: " , self.primers)
        aantal_primerparen = 0


        for a in self.primers:
            aantal_primerparen+=1
            print("pcr product: ", a[0], "bp")
            primer1 = a[1]
            primer2 = a[2]
            print("primer 1: ")
            print("positie: ", primer1[0])
            print("sequentie: ", primer1[1])
            print("GC: ", primer1[2])
            print("TM: ", primer1[3])
            print("primer 2: ")
            print("positie: ", primer2[0])
            print("sequentie: ", primer2[1])
            print("GC: ", primer2[2])
            print("TM: ", primer2[3])
            print("\n")

            primerteller = wx.StaticText(self, -1, "Primerpaar "+str(aantal_primerparen))
            lengte = wx.StaticText(self, -1, "Lengte PCR product: "+str(a[0]))
            f_primer = wx.StaticText(self, -1, "Forward Primer: "+str(primer1[1]))
            f_gc = wx.StaticText(self, -1, "GC%: "+str(primer1[2]*100))
            f_tm = wx.StaticText(self, -1, "Tm: "+str(primer1[3]))
            r_primer = wx.StaticText(self, -1, "Reversed Primer: " +str(primer2[1]))
            r_gc = wx.StaticText(self, -1, "GC%: "+str(primer2[2]*100))
            r_tm = wx.StaticText(self, -1, "Tm: "+str(primer2[3])+"\n")

            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            primerteller.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            lengte.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            f_primer.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            f_gc.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            f_tm.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            r_primer.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            r_gc.SetFont(font)
            font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            r_tm.SetFont(font)

            primer_box = wx.BoxSizer(wx.HORIZONTAL)
            primer_box.Add(primerteller, 1, wx.EXPAND)
            primer_box.Add(lengte, 1, wx.EXPAND)

            f_box = wx.BoxSizer(wx.HORIZONTAL)
            f_box.Add(f_primer, 1, wx.EXPAND)
            f_box.Add(f_gc, 1, wx.EXPAND)
            f_box.Add(f_tm, 1, wx.EXPAND)

            r_box = wx.BoxSizer(wx.HORIZONTAL)
            r_box.Add(r_primer, 1, wx.EXPAND)
            r_box.Add(r_gc, 1, wx.EXPAND)
            r_box.Add(r_tm, 1, wx.EXPAND)


            self.empy_box.Add(primer_box, 1, wx.EXPAND)
            self.empy_box.Add(f_box, 1, wx.EXPAND)
            self.empy_box.Add(r_box, 1, wx.EXPAND)

        print(aantal_primerparen)



if __name__ == "__main__":
    class Schermpje(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(5000, 2500))
            self.paneeltje = Panel3(self)
            self.Show(True)


    app = wx.App()
    Schermpje(None, -1, "Uitvoerscherm")
    app.MainLoop()
