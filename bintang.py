author    = "Juan Hulu"
instagram = "https://www.instagram.com/juan.hulu.xy", 'name: Juan Hulu'
facebook  = "https://www.facebook.com/Juan.Hulu.X",   'name: Juan Hulu'
tiktok    = "https://tiktok.com/@juanhulu148",        'name: Juan XD'
yotube    = "https://www.youtube.com/@juanhulu09",    'name: Juan Hulu'

from time import sleep
from rich import print # wajib install kalau belum diinstall -> (pip install rich)

def mengetik(text, delay=0.8, color="white"):
    for i in text:print("[bold {}]{}".format(color, i), end="");sleep(delay)

def start():
    daftar_lirik = [
        ("Balonku ada lima hah..\n", 0.1, 0.8),
        ("Rupa rupa warnanya....\n", 0.1, 0.9),
        ("Hijau kuning kelabu...\n", 0.09, 0.9),
        ("Merah muda dan biru...\n", 0.1, 0.8),
        ("  Meletus balon hijau dor\n", 0.1, 0.7),
        ("  Hatiku sangat kacau....\n", 0.1, 0.9),
        ("  Balonku tinggal empat..\n", 0.1, 0.6),
        ("  Ku pegang erat eraaat..\n", 0.2, 0),
    ]
    list_color = ["white", "purple"]
    for ex, (lirik, typing_delay, lirik_delay) in enumerate(daftar_lirik):
        color = list_color[(ex // 4) % len(list_color)]
        mengetik(lirik, typing_delay, color)
        sleep(lirik_delay)

if __name__ == "__main__":
    start()
