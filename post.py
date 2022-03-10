from datetime import datetime
from db_kark import Db


class Post:
    def __init__(self, id, kategori, bruker, dato, treff,
                 tittel, ingress, oppslagstekst, kat_id, kat_navn):
        self.id = id
        self.kategori = kategori
        self.tittel = tittel
        self.ingress = ingress
        self.oppslagstekst = oppslagstekst
        self.bruker = bruker
        self.dato = dato
        self.treff = treff
        self.kat_id = kat_id
        self.kat_navn = kat_navn
