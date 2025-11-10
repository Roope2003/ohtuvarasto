"""Varasto-luokka, joka mallintaa yksinkertaista varastoa."""

class Varasto:
    """Varasto, joka sisältää tilavuuden ja saldon."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston tilavuuden ja alkusaldon.

        Tilavuus ja alkusaldon arvot tarkastetaan:
        - negatiivinen tilavuus -> 0
        - negatiivinen alku_saldo -> 0
        - liian suuri alku_saldo -> asetetaan tilavuuteen
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa, kuinka paljon varastoon mahtuu."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon annetun määrän, jos se on positiivinen.

        Jos lisättävä määrä ylittää vapaan tilan, varasto täytetään
        mutta ei ylitetä tilavuutta.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo += maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta pyydetyn määrän.

        Negatiivinen otto palauttaa 0.
        Jos otettava määrä ylittää saldon, palautetaan koko saldo
        ja varasto tyhjennetään.
        """
        if maara < 0:
            return 0.0

        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo -= maara
        return maara

    def __str__(self):
        """Palauttaa varaston saldon ja vapaan tilan tekstimuodossa."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
