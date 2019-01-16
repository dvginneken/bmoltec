""""__Auteurs__ = "Kenrick de Grijs, Daphne van Ginneken, Mees Kerssens"
    __Versie__ = "1.0.1"
    __Klas__ = "Bin2A" """

import wx


class Panel1(wx.Panel):
    def __init__(self, parent):
        """" Hier word de UI van de 'Welkom' panel in elkaar gezet."""
        wx.Panel.__init__(self, parent)
        self.panel1 = wx.Panel(self, -1)
        self.button1 = wx.Button(self, -1, "Afsluiten")
        self.button2 = wx.Button(self, -1, "Help")
        self.button3 = wx.Button(self, -1, "Volgende")
        dbox = wx.BoxSizer(wx.HORIZONTAL)
        dbox.Add(self.button1, 1, wx.EXPAND)
        dbox.Add(self.button2, 1, wx.EXPAND)
        dbox.Add(self.button3, 1, wx.EXPAND)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.panel1)
        self.panel2 = wx.Panel(self, -1)
        cbox = wx.BoxSizer(wx.HORIZONTAL)
        cbox.Add(self.panel2)
        self.welkomtekst = wx.StaticText(self, -1, "Welkom bij $W@GG@ primerprogramma")
        font = wx.Font(40, wx.DEFAULT, wx.ITALIC, wx.BOLD)
        self.welkomtekst.SetFont(font)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, 3, wx.EXPAND)
        vbox.Add(self.welkomtekst, 5, wx.ALIGN_CENTER, wx.EXPAND)
        vbox.Add(cbox, 2, wx.EXPAND)
        vbox.Add(dbox, 2, wx.EXPAND)
        self.SetSizer(vbox)
        self.Show(True)


if __name__ == "__main__":
    class Schermpje(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(500, 400))
            self.paneeltje = Panel1(self)
            self.Show(True)


    app = wx.App()
    Schermpje(None, -1, "Welkomscherm")
    app.MainLoop()




