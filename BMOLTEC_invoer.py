""""__Auteurs__ = "Kenrick de Grijs, Daphne van Ginneken, Mees Kerssens"
    __Versie__ = "1.0.1"
    __Klas__ = "Bin2A" """

import wx


class Panel2(wx.Panel):
    def __init__(self, parent):
        """" Hier worden de globale variabelen en de overige functies aangeroepen."""
        wx.Panel.__init__(self, parent, -1)
        self.global_vars()
        self.boxCreeren1()
        final = self.boxCreeren2()
        self.SetSizer(final)




    def global_vars(self):
        """" Hier worden de teksten van het 'Invoer' panel gecreëerd en de mogelijkheid
             om zelf tekst in te voeren aangemaakt."""
        self.tekst1 = wx.StaticText(self, -1, "DNA sequentie plakken of uploaden")
        self.tekst2 = wx.StaticText(self, -1, "Linkergrens:")
        self.tekst3 = wx.StaticText(self, -1, "Rechtergrens:")
        self.tekst4 = wx.StaticText(self, -1, "Maximale lengte van PCR product:")
        font = wx.Font(25, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst1.SetFont(font)
        font2 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst2.SetFont(font2)
        font3 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst3.SetFont(font3)
        font4 = wx.Font(15, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.tekst4.SetFont(font4)
        self.button1 = wx.Button(self, -1, "Bladeren")
        self.button2 = wx.Button(self, -1, "Afsluiten")
        self.button3 = wx.Button(self, -1, "Velden legen")
        self.button4 = wx.Button(self, -1, "Help")
        self.button5 = wx.Button(self, -1, "Maak primers")
        self.invultekst1 = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # Sequentie
        self.invultekst2 = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # Startpositie
        self.invultekst3 = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # Stoppositie
        self.invultekst4 = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # Maximale lengte PCR product



    def boxCreeren1(self):
        """" Deze functie creëert de UI van de 'Invoer' panel. De onderkant slaat op hoe
             de indeling eruit gaat zien onder het sequentie invoer onderdeel."""
        posities = wx.BoxSizer(wx.HORIZONTAL)  # Start en stop posities
        posities.Add(self.tekst2, 1, wx.EXPAND)
        posities.Add(self.invultekst2, 1, wx.EXPAND)
        posities.Add(self.tekst3, 1, wx.EXPAND)
        posities.Add(self.invultekst3, 1, wx.EXPAND)
        posities2 = wx.BoxSizer(wx.HORIZONTAL)
        posities2.Add(self.tekst4, 1, wx.EXPAND)
        posities2.Add(self.invultekst4, 1, wx.EXPAND)
        onderkant1 = wx.BoxSizer(wx.VERTICAL)  # Tekst + posities
        onderkant1.Add(posities, 1, wx.EXPAND)
        self.onderkant2 = wx.BoxSizer(wx.VERTICAL)
        self.onderkant2.Add(posities2, 1, wx.EXPAND)
        self.onderkant = wx.BoxSizer(wx.HORIZONTAL)  # Gehele onderkant
        self.onderkant.Add(onderkant1, 1, wx.EXPAND)

    def boxCreeren2(self):
        """" Deze functie zorgt ervoor dat er ruimte komt tussen alle verschillende
             onderdelen in het 'Invoer' paneel."""
        dbox = wx.BoxSizer(wx.HORIZONTAL)
        dbox.Add(self.button2, 1, wx.EXPAND)
        dbox.Add(self.button3, 1, wx.EXPAND)
        dbox.Add(self.button4, 1, wx.EXPAND)
        dbox.Add(self.button5, 1, wx.EXPAND)
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
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box2.Add(self.tekst1, 5, wx.EXPAND)
        box2.Add(self.button1, 1, wx.EXPAND)
        box.Add(box2, 1, wx.EXPAND)
        box.Add(self.invultekst1, 4, wx.EXPAND)
        box.Add(hbox, 1, wx.EXPAND)
        box.Add(self.onderkant, 1, wx.EXPAND)
        box.Add(cbox, 1, wx.EXPAND)
        box.Add(self.onderkant2, 1, wx.EXPAND)
        box.Add(fbox, 1, wx.EXPAND)
        box.Add(dbox, 2, wx.EXPAND)
        return box


if __name__ == "__main__":
    class Schermpje(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(500, 400))
            self.paneeltje = Panel2(self)
            self.Show(True)


    app = wx.App()
    Schermpje(None, -1, "invoerscherm")
    app.MainLoop()

