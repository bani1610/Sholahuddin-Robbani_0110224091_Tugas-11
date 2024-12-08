class Gempa():
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def Dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif self.skala >=2 and self .skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala >4 and self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        elif self.skala >6:
            print("Dampak gempa bangunan roboh dan perpotensi tsunami")

        print(f'Lokasi gempa: {self.lokasi}')
        print(f'Skala gempa: {self.skala}')