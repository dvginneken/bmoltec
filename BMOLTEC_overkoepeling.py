""""__Auteurs__ = "Kenrick de Grijs, Daphne van Ginneken, Mees Kerssens"
    __Versie__ = "1.0.1"
    __Klas__ = "Bin2A" """

import wx
import sys
import webbrowser
import easygui

from BMOLTEC_welkom import Panel1
from BMOLTEC_invoer import Panel2
from BMOLTEC_uitvoer import Panel3
from BMOLTEC_primers import Primers_Maken

class Schermpje(wx.Frame):
    def __init__(self, parent, id, title):
        """" Hier worden de andere panels aangeroepen. Het invoer en
             uitvoer scherm zijn verborgen zodat het welkom scherm als eerste verschijnt."""
        wx.Frame.__init__(self, parent, id, title, size=(1500, 800))
        self.welkom = Panel1(self)
        self.invoer = Panel2(self)
        self.uitvoer = Panel3(self)
        self.totbox = wx.BoxSizer()
        self.totbox.Add(self.welkom, 1, wx.EXPAND)
        self.totbox.Add(self.invoer, 1, wx.EXPAND)
        self.totbox.Add(self.uitvoer, 1, wx.EXPAND)
        self.SetSizer(self.totbox)
        self.invoer.Hide()
        self.uitvoer.Hide()
        self.knoppenBinden()
        self.Centre()
        self.Show(True)

    def knoppenBinden(self):
        """" Hier worden de buttons geactiveerd en de knoppen gebonden voor de verschillende panels."""
        self.welkom.button1.Bind(wx.EVT_BUTTON, self.onButtonExit)
        self.welkom.button2.Bind(wx.EVT_BUTTON, self.onButtonHelp)
        self.welkom.button3.Bind(wx.EVT_BUTTON, self.onButtonVolgende)
        self.invoer.button1.Bind(wx.EVT_BUTTON, self.onButtonBladeren)
        self.invoer.button2.Bind(wx.EVT_BUTTON, self.onButtonExit)
        self.invoer.button3.Bind(wx.EVT_BUTTON, self.onButtonVeldenlegen)
        self.invoer.button4.Bind(wx.EVT_BUTTON, self.onButtonHelp)
        self.invoer.button5.Bind(wx.EVT_BUTTON, self.onButtonMaakprimers)
        self.uitvoer.button1.Bind(wx.EVT_BUTTON, self.onButtonExit)
        self.uitvoer.button2.Bind(wx.EVT_BUTTON, self.onButtonOpnieuw)

    def onButtonExit(self, event):
        """" Deze functie zorgt ervoor dat wanneer er op de 'Exit' knop word gedrukt
             het programma word beëindigd."""
        event.GetEventObject().GetLabel()
        sys.exit()

    def onButtonVeldenlegen(self, event):
        """" Deze functie maakt alle velden leeg in het invoerscherm wanneer er
             op de knop 'Velden legen' word gedrukt."""
        event.GetEventObject().GetLabel()
        self.invoer.invultekst1.Clear()
        self.invoer.invultekst2.Clear()
        self.invoer.invultekst3.Clear()
        self.invoer.invultekst4.Clear()


    def onButtonBladeren(self, event):
        """" Deze functie zorgt ervoor dat wanneer er op de knop 'Bladeren' word gedrukt
             in het invoerscherm, er een document gekozen kan worden om te gebruiken als
             DNA sequentie input. Ook word dit veld leeg gemaakt mocht er al informatie staan"""
        event.GetEventObject().GetLabel()
        file = easygui.fileopenbox()
        txt = ParseFile(file)
        self.invoer.invultekst1.Clear()
        self.invoer.invultekst1.write(txt)


    def onButtonVolgende(self, event):
        """" Deze functie verbergd het welkomscherm en laat het invoerscherm zien
             wanneer er op de knop 'Volgende' word gedrukt.."""
        event.GetEventObject().GetLabel()
        self.welkom.Hide()
        self.invoer.Show()
        self.totbox.Layout()

    def onButtonHelp(self, event):
        """" Deze functie opent het help document wanneer er op de 'Help' knop gedrukt word."""
        webbrowser.open("Help.txt")


    def onButtonMaakprimers(self, event):
        """" Deze functie verbergd het invoerscherm en laat het uitvoerscherm zien wanneer
             er op de knop 'Primers maken' gedrukt word.

             De 4 variabelen (sequentie, start, stop en max)
             uit het invoerscherm worden opgehaald. De klasse Primers_Maken wordt aangeroepen en de 4
             variabelen worden daar aan meegegeven.

             De functie updatePrimers uit Panel3 wordt uitgevoerd om de primerparen op te slaan in dat scherm."""
        event.GetEventObject().GetLabel()
        self.sequentie = self.invoer.invultekst1.GetValue()
        self.start = self.invoer.invultekst2.GetValue()
        self.stop = self.invoer.invultekst3.GetValue()
        self.max = self.invoer.invultekst4.GetValue()
        self.primers = Primers_Maken(self.sequentie, self.start, self.stop, self.max)
        self.invoer.Hide()
        self.uitvoer.updatePrimers(self.primers.primer1)
        self.uitvoer.Show()
        self.totbox.Layout()


    def onButtonOpnieuw(self, event):
        """" Deze functie verbergd het uitvoerscherm en laat het invoerscherm zien wanneer
             er op de knop 'Opnieuw' gedrukt word. Ook worden alle velden van het invoerscherm
             leeg gemaakt."""
        event.GetEventObject().GetLabel()
        self.invoer.invultekst1.Clear()
        self.invoer.invultekst2.Clear()
        self.invoer.invultekst3.Clear()
        self.invoer.invultekst4.Clear()
        self.uitvoer.Hide()
        self.invoer.Show()
        self.totbox.Layout()

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

if __name__ == "__main__":
    app = wx.App()
    Schermpje(None, -1, "Primerprogramma")
    app.MainLoop()
