import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_negatiivinen_tilavuus_nollataan(self):
        v = Varasto(-1)
        self.assertAlmostEqual(v.tilavuus, 0)
        self.assertAlmostEqual(v.saldo, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.tilavuus, 10)
        self.assertAlmostEqual(v.saldo, 0)

    def test_liian_suuri_alku_saldo_rajoitetaan_tilavuuteen(self):
        v = Varasto(10, 20)
        self.assertAlmostEqual(v.tilavuus, 10)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_eika_ylivuoda(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_otto_palauttaa_nolla_eika_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(3)
        ennen = self.varasto.saldo
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, ennen)

    def test_otto_enemman_kuin_saldo_tyhjentaa_ja_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(4)
        saatu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu, 4)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_paljonko_mahtuu_ei_mene_negatiiviseksi(self):
        self.varasto.lisaa_varastoon(12)  # ylitys -> täyteen
        self.assertTrue(self.varasto.paljonko_mahtuu() >= 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_str_sisaltaa_saldon_ja_tilan(self):
        self.varasto.lisaa_varastoon(5)
        s = str(self.varasto)
        self.assertIn("saldo", s)
        self.assertIn("vielä tilaa", s)
