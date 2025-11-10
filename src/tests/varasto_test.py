"""Yksikkötestit Varasto-luokalle."""
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testiluokka Varasto-luokan toiminnallisuuksille."""

    def setUp(self):
        """Luo oletusvaraston ennen jokaista testiä."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Varaston saldo on aluksi 0."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Varaston tilavuus on mikä konstruktorille annetaan."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Lisäys kasvattaa saldoa oikein."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Lisäys vähentää käytettävissä olevaa tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Ottaminen palauttaa pyydetyn määrän kun saldo riittää."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Ottaminen lisää varaston vapaata tilaa."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        """Negatiivinen tilavuus nollataan."""
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)
        self.assertAlmostEqual(v.saldo, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        """Negatiivinen alkusaldo nollataan."""
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.tilavuus, 10)
        self.assertAlmostEqual(v.saldo, 0)

    def test_liian_suuri_alku_saldo_rajoitetaan_tilavuuteen(self):
        """Liian suuri alkusaldo asetetaan tilavuuden suuruiseksi."""
        v = Varasto(10, 20)
        self.assertAlmostEqual(v.tilavuus, 10)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        """Negatiivinen lisäys ei muuta saldoa."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_eika_ylivuoda(self):
        """Tilavuuden ylittävä lisäys täyttää varaston mutta ei yli."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_otto_palauttaa_nolla_eika_muuta_saldoa(self):
        """Negatiivinen otto palauttaa nollan eikä muuta saldoa."""
        self.varasto.lisaa_varastoon(3)
        ennen = self.varasto.saldo
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, ennen)

    def test_otto_enemman_kuin_saldo_tyhjentaa_ja_palauttaa_kaiken(self):
        """Saldoa suurempi otto tyhjentää varaston."""
        self.varasto.lisaa_varastoon(4)
        saatu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu, 4)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_paljonko_mahtuu_ei_mene_negatiiviseksi(self):
        """Vapaa tila ei koskaan mene negatiiviseksi."""
        self.varasto.lisaa_varastoon(12)
        self.assertTrue(self.varasto.paljonko_mahtuu() >= 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_str_sisaltaa_saldon_ja_tilan(self):
        """__str__ sisältää saldon ja tilatiedon."""
        self.varasto.lisaa_varastoon(5)
        s = str(self.varasto)
        self.assertIn("saldo", s)
        self.assertIn("vielä tilaa", s)
