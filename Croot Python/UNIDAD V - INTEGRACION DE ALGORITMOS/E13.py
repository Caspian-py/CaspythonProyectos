"""
    **Convertidor interactivo: monedas, longitudes, temperaturas.**
"""
import os
def main():
    while True:
        print("=" * 40)
        print("CONVERTIDOR INTERACTIVO")
        print("=" * 40)
        print("CONVERTIR:")
        print("-> MONEDAS")
        print("-> LONGITUDES")
        print("-> TEMPERATURAS")
        print()
        print("-> SALIR")
        print("-" * 40)
        option = input("OPTION -> ").lower()
        match option:
            case "monedas":
                main_monedas()
                break
            case "longitudes":
                main_longitudes()
                break
            case "temperaturas":
                main_temperaturas()
                break
            case "salir":
                break
            case _:
                print("Opcion no valida.")


def main_monedas():
    while True:
        os.system("cls")
        print("MONEDAS")
        print("=" * 40)
        print("Opciones: ")
        print("1) (PEN) -> (USD)")
        print("2) (BTC) -> (PEN)")
        print("3) (USD) -> (PEN)")
        print("4) (EUR) -> (PEN)")
        print("5) (USD) -> (BTC)")
        print("6) (PEN) -> (EUR)")
        print()
        print("0) REGRESAR AL MENU")
        print("-" * 40)
        option = int(input("Opcion -> "))
        match option:
            case 1:
                os.system("cls")
                penausd()
                break
            case 2:
                os.system("cls")
                btcapen()
                break
            case 3:
                os.system("cls")
                usdapen()
                break
            case 4:
                os.system("cls")
                eurapen()
                break
            case 5:
                os.system("cls")
                usdabtc()
                break
            case 6:
                os.system("cls")
                penaeur()
                break
            case 0:
                os.system("cls")
                main()
                break
            case _:
                print("Opcion no valida.")

def penausd():
    while True:
        print("PEN -> USD")
        print("=" * 40)
        print("Regresar atras (0)")
        pen = float(input("PEN: "))
        if pen == 0:
            main_monedas()
            break
        usd = pen / 3.70
        print(f"{pen} PEN en USD es {usd} USD.")
        print("-" * 40)

def btcapen():
    while True:
        print("BTC -> PEN")
        print("=" * 40)
        print("Regresar atras (0)")
        btc = float(input("BTC: "))
        if btc == 0:
            main_monedas()
            break
        pen = btc *  250000
        print(f"{btc} BTC en PEN es {pen} PEN.")
        print("=" * 40)

def usdapen():
    while True:
        print("USD -> PEN")
        print("=" * 40)
        print("Regresar atras (0)")
        usd = float(input("USD: "))
        if usd == 0:
            main_monedas()
            break
        pen = usd / 0.27
        print(f"{usd} USD en PEN es {pen} PEN.")
        print("=" * 40)

def eurapen():
    while True:
        print("EUR -> PEN")
        print("=" * 40)
        print("Regresar atras (0)")
        eur = float(input("EUR: "))
        if eur == 0:
            main_monedas()
            break
        pen = eur * 4
        print(f"{eur} EUR en PEN es {pen} PEN.")
        print("=" * 40)

def usdabtc():
    while True:
        print("USD -> BTC")
        print("=" * 40)
        print("Regresar atras (0)")
        usd = float(input("USD: "))
        if usd == 0:
            main_monedas()
            break
        btc = usd / 67000
        print(f"{usd} USD en BTC es {btc} BTC.")
        print("=" * 40)

def penaeur():
    while True:
        print("PEN -> EUR")
        print("=" * 40)
        print("Regresar atras (0)")
        pen = float(input("PEN: "))
        if pen == 0:
            main_monedas()
            break
        eur = pen * 0.25
        print(f"{pen} PEN en EUR es {eur} EUR.")
        print("=" * 40)


def main_longitudes():
    while True:
        os.system("cls")
        print("LONGITUDES")
        print("=" * 40)
        print("Opciones: ")
        print("1) CM -> M")
        print("2) KM -> CM")
        print("3) M -> FT")
        print("4) MI -> KM")
        print("5) IN -> CM")
        print("6) M -> YD")
        print("7) YD -> M")
        print()
        print("0) REGRESAR AL MENU")
        print("-" * 40)
        option = int(input("Opcion -> "))
        match option:
            case 1:
                os.system("cls")
                cmam()
                break
            case 2:
                os.system("cls")
                kmacm()
                break
            case 3:
                os.system("cls")
                maft()
                break
            case 4:
                os.system("cls")
                miakm()
                break
            case 5:
                os.system("cls")
                inacm()
                break
            case 6:
                os.system("cls")
                mayd()
                break
            case 7:
                os.system("cls")
                ydam()
                break
            case 0:
                os.system("cls")
                main()
                break
            case _:
                print("Opcion no valida.")

def cmam():
    while True:
        print("CM -> M")
        print("=" * 40)
        print("Regresar atras (0)")
        cm = float(input("CM: "))
        if cm == 0:
            main_longitudes()
            break
        m = cm / 100
        print(f"{cm} CM en M es {m} M")
        print("=" * 40)

def kmacm():
    while True:
        print("KM -> CM")
        print("=" * 40)
        print("Regresar atras (0)")
        km = float(input("KM: "))
        if km == 0:
            main_longitudes()
            break
        cm = km * 100000
        print(f"{km} KM a CM es {cm} CM.")
        print("=" * 40)

def maft():
    while True:
        print("M -> FT")
        print("=" * 40)
        print("Regresar atras (0)")
        m = float(input("M: "))
        if m == 0:
            main_longitudes()
            break
        ft = m * 3.28084
        print(f"{m} M a FT es {ft} FT.")
        print("=" * 40)

def miakm():
    while True:
        print("MI -> KM")
        print("=" * 40)
        print("Regresar atras (0)")
        mi = float(input("MI: "))
        if mi == 0:
            main_longitudes()
            break
        km = mi * 1.60934
        print(f"{mi} MI en KM es {km} KM.")
        print("=" * 40)

def inacm():
    while True:
        print("IN -> CM")
        print("=" * 40)
        print("Regresar atras (0)")
        inp = float(input("IN: "))
        if inp == 0:
            main_longitudes()
            break
        cm = inp * 2.54
        print(f"{inp} IN a CM es {cm} CM.")
        print("=" * 40)

def mayd():
    while True:
        print("M -> YD")
        print("=" * 40)
        print("Regresar atras (0)")
        m = float(input("M: "))
        if m == 0:
            main_longitudes()
            break
        yd = m * 1.09361
        print(f"{m} M a YD es {yd} YD.")
        print("=" * 40)

def ydam():
    while True:
        print("YD -> M")
        print("=" * 40)
        print("Regresar atras (0)")
        yd = float(input("YD: "))
        if yd == 0:
            main_longitudes()
            break
        m = yd / 1.09361
        print(f"{yd} YD a M es {m} M.")
        print("=" * 40)


def main_temperaturas():
    while True:
        os.system("cls")
        print("TEMPERATURAS")
        print("=" * 40)
        print("Opciones:")
        print("1) °C → °F")
        print("2) °F -> °C")
        print("3) °C -> K")
        print("4) K -> °C")
        print("5) °F -> K")
        print("6) K -> °F")
        print()
        print("0) REGRESAR AL MENU")
        print("-" * 40)
        option = int(input("Option -> "))
        match option:
            case 1:
                os.system("cls")
                caf()
                break
            case 2:
                os.system("cls")
                fac()
                break
            case 3:
                os.system("cls")
                cak()
                break
            case 4:
                os.system("cls")
                kac()
                break
            case 5:
                os.system("cls")
                fak()
                break
            case 6:
                os.system("cls")
                kaf()
                break
            case 0:
                os.system("cls")
                main()
                break
            case _:
                print("Opcion no valida.")

def caf():
    while True:
        print("°C -> °F")
        print("=" * 40)
        print("Regresar atras (0)")
        c = float(input("°C: "))
        if c == 0:
            main_temperaturas()
            break
        f = (c * (9 / 5)) + 32
        print(f"{c} °C a °F es {f} °F.")
        print("=" * 40)

def fac():
    while True:
        print("°F -> °C")
        print("=" * 40)
        print("Regresar atras (0)")
        f = float(input("°F: "))
        if f == 0:
            main_temperaturas()
            break
        c = (f - 32) * (5 / 9)
        print(f"{f} °F a °C es {c} °C.")
        print("=" * 40)

def cak():
    while True:
        print("°C -> K")
        print("=" * 40)
        print("Regresar atras(0)")
        c = float(input("°C: "))
        if c == 0:
            main_temperaturas()
            break
        k = c + 273.15
        print(f"{c} °C a K es {k} K.")
        print("=" * 40)

def kac():
    while True:
        print("K -> °C")
        print("=" * 40)
        print("Regresar atras(0)")
        k = float(input("K: "))
        if k == 0:
            main_temperaturas()
            break
        c = k - 273.15
        print(f"{k} K a °C es {c} °C.")
        print("=" * 40)

def fak():
    while True:
        print("°F -> K")
        print("=" * 40)
        print("Regresar atras(0)")
        f = float(input("°F: "))
        if f == 0:
            main_temperaturas()
            break
        k = (f - 32) * (5 / 9) + 273.15
        print(f"{f} °F a K es {k} K.")
        print("=" * 40)

def kaf():
    while True:
        print("K -> F")
        print("=" * 40)
        print("Regresar atras(0)")
        k = float(input("K: "))
        if k == 0:
            main_temperaturas()
            break
        f = (k - 273.15) * (9 / 5) + 32
        print(f"{k} K a °F es {f} °F.")
        print("=" * 40)

main()





