""""__Auteurs__ = "Kenrick de Grijs, Daphne van Ginneken, Mees Kerssens"
    __Versie__ = "1.0.1"
    __Klas__ = "Bin2A" """

import wx
#from BMOLTEC_overkoepeling import Schermpje
from mees_primer import Primers_Maken


class Panel3(wx.Panel):
    primers = None
    def __init__(self, parent):
        """" Hier worden de globale variabelen en de overige functies aangeroepen."""
        wx.Panel.__init__(self, parent, -1)
        self.global_vars()
        self.boxCreeren1()
        final = self.boxCreeren2()
        self.SetSizer(final)


    def global_vars(self):
        """" Hier worden de teksten van het 'Uitvoer' panel gecreëerd samen met de buttons."""
        #string = "output: " + self.primers
        self.tekst1 = wx.StaticText(self, -1, "poep")
        self.tekst2 = wx.StaticText(self, -1, "GC%:")
        self.tekst3 = wx.StaticText(self, -1, "TM:")
        self.tekst4 = wx.StaticText(self, -1, "Reverse primer:")
        self.tekst5 = wx.StaticText(self, -1, "GC%:")
        self.tekst6 = wx.StaticText(self, -1, "TM:")
        self.tekst7 = wx.StaticText(self, -1, "Lengte van PCR product:")
        font = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst1.SetFont(font)
        font2 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst2.SetFont(font2)
        font3 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst3.SetFont(font3)
        font4 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst4.SetFont(font4)
        font5 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst5.SetFont(font5)
        font6 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst6.SetFont(font6)
        font7 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst7.SetFont(font7)
        self.button1 = wx.Button(self, -1, "Afsluiten")
        self.button2 = wx.Button(self, -1, "Opnieuw")

    def boxCreeren1(self):
        """" Deze functie creëert de UI van de 'Uitvoer' paneel. De onderkant slaat op hoe
             de totale indeling eruit gaat zien."""
        posities1 = wx.BoxSizer(wx.HORIZONTAL)  # Start en stop posities
        posities1.Add(self.tekst1, 1, wx.EXPAND)
        posities2 = wx.BoxSizer(wx.HORIZONTAL)
        posities2.Add(self.tekst2, 1, wx.EXPAND)
        posities3 = wx.BoxSizer(wx.HORIZONTAL)
        posities3.Add(self.tekst3, 1, wx.EXPAND)
        posities4 = wx.BoxSizer(wx.HORIZONTAL)
        posities4.Add(self.tekst4, 1, wx.EXPAND)
        posities5 = wx.BoxSizer(wx.HORIZONTAL)
        posities5.Add(self.tekst5, 1, wx.EXPAND)
        posities6 = wx.BoxSizer(wx.HORIZONTAL)
        posities6.Add(self.tekst6, 1, wx.EXPAND)
        posities7 = wx.BoxSizer(wx.HORIZONTAL)
        posities7.Add(self.tekst7, 1, wx.EXPAND)
        onderkant1 = wx.BoxSizer(wx.VERTICAL)  # Tekst + posities
        onderkant1.Add(posities1, 1, wx.EXPAND)
        onderkant1.Add(posities2, 1, wx.EXPAND)
        onderkant1.Add(posities3, 1, wx.EXPAND)
        onderkant1.Add(posities4, 1, wx.EXPAND)
        onderkant1.Add(posities5, 1, wx.EXPAND)
        onderkant1.Add(posities6, 1, wx.EXPAND)
        onderkant1.Add(posities7, 1, wx.EXPAND)
        self.onderkant = wx.BoxSizer(wx.HORIZONTAL)  # Gehele onderkant
        self.onderkant.Add(onderkant1, 1, wx.EXPAND)

    def boxCreeren2(self):
        """" Deze functie zorgt ervoor dat er ruimte komt tussen alle verschillende
             onderdelen in het 'Uitvoer' paneel."""
        dbox = wx.BoxSizer(wx.HORIZONTAL)
        dbox.Add(self.button1, 1, wx.EXPAND)
        dbox.Add(self.button2, 1, wx.EXPAND)
        self.panel1 = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.panel1)
        self.panel2 = wx.Panel(self, -1)
        cbox = wx.BoxSizer(wx.HORIZONTAL)
        cbox.Add(self.panel2)
        self.panel3 = wx.Panel(self, -1)
        fbox = wx.BoxSizer(wx.HORIZONTAL)
        fbox.Add(self.panel3)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.onderkant, 4, wx.EXPAND)
        box.Add(dbox, 1, wx.EXPAND)
        return box

    def updatePrimers(self, primers):
        self.primers = primers
        print("primer: " , self.primers)


if __name__ == "__main__":
    class Schermpje(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(800, 400))
            self.paneeltje = Panel3(self)
            self.Show(True)


    app = wx.App()
    Schermpje(None, -1, "Uitvoerscherm")
    app.MainLoop()
