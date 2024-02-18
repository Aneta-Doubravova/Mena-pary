from tkinter import *  # Importování všech funkcí z modulu tkinter

import requests  # Importování modulu requests pro provádění HTTP požadavků
# Barvy
hlavni_barva = "#14085f"  # Definice hlavní barvy pro uživatelské rozhraní

# Okno
okno = Tk()  # Vytvoření instance třídy Tk pro vytvoření hlavního okna aplikace
okno.minsize(400, 120)  # Nastavení minimální velikosti okna
okno.resizable(False, False)  # Zakázání možnosti změny velikosti okna
okno.title("Převod měn")  # Nastavení titulku okna
okno.config(bg=hlavni_barva)  # Nastavení barvy pozadí okna

# Funkce
def prepocitat():  # Definice funkce pro přepočítání měn
    try:  # Začátek bloku try pro zachycení výjimek
        mena_z = roleta_z.get()  # Získání hodnoty z rolety pro výchozí měnu
        mena_na = roleta_na.get()  # Získání hodnoty z rolety pro cílovou měnu
        castka = int(vstup_uzivatele.get())  # Získání částky z uživatelského vstupu a převedení na celé číslo

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={mena_na}&from={mena_z}&amount={castka}"  # Sestavení URL pro API pro převod měn

        payload = {}  # Případné další data pro požadavek
        headers = {"apikey": "ZzrIAAjwBUB9uwB5PvqgFemTl5JB9fK0"}  # Hlavička s API klíčem pro autentizaci

        odpoved = requests.request("GET", url, headers=headers, data=payload)  # Odeslání HTTP GET požadavku na API

        kod_stavu = odpoved.status_code  # Získání stavového kódu odpovědi
        data_vysledek = odpoved.json()  # Zpracování JSON odpovědi
        vysledek_label.config(text=round(data_vysledek["result"], 2))  # Zobrazení výsledku v GUI s dvěma desetinnými místy
        upozorneni_label.config(text="")  # Nastavení textu upozornění na prázdný řetězec
    except:  # Zpracování výjimky
        upozorneni_label.config(text="Zadejte prosím částku")  # Nastavení textu upozornění na chybu při zpracování vstupu

# Uživatelský vstup
vstup_uzivatele = Entry(width=20, font=("Arial", 12), justify=CENTER)  # Vytvoření vstupního pole pro zadání částky
vstup_uzivatele.insert(0, "0")  # Vložení výchozí hodnoty do vstupního pole
vstup_uzivatele.grid(row=0, column=0, padx=10, pady=(10, 0))  # Umístění vstupního pole v prvním řádku a prvním sloupci

# Roletka z jaké měny
roleta_z = StringVar(okno)  # Vytvoření objektu pro výběr výchozí měny
roleta_z.set("CZK")  # Nastavení výchozí hodnoty pro roletu
moznosti_rolety_z = OptionMenu(okno, roleta_z, "CZK", "EUR", "USD", "CHF", "GBP", "RUB", "JPY")  # Vytvoření rolety s možnostmi měn
moznosti_rolety_z.grid(row=0, column=1, padx=10, pady=(10, 0))  # Umístění rolety v prvním řádku a druhém sloupci

# Roletka - na jakou měnu
roleta_na = StringVar(okno)  # Vytvoření objektu pro výběr cílové měny
roleta_na.set("CZK")  # Nastavení výchozí hodnoty pro roletu
moznosti_rolety_na = OptionMenu(okno, roleta_na, "CZK", "EUR", "USD", "CHF", "GBP", "RUB", "JPY")  # Vytvoření rolety s možnostmi měn
moznosti_rolety_na.grid(row=1, column=1, padx=10, pady=(10, 0))  # Umístění rolety v druhém řádku a druhém sloupci

# Tlačítko přepočtu
tlacitko_prepocitani = Button(text="Přepočítat", font=("Arial", 12), command=prepocitat)  # Vytvoření tlačítka pro přepočet měn
tlacitko_prepocitani.grid(row=0, column=2, padx=10, pady=(10, 0))  # Umístění tlačítka v prvním řádku a třetím sloupci

# Label pro zobrazení výsledku převodu
vysledek_label = Label(text=0, bg=hlavni_barva, fg="white", font=("Arial", 12))  # Vytvoření labelu pro zobrazení výsledku převodu
vysledek_label.grid(row=1, column=0)  # Umístění labelu v druhém řádku a prvním sloupci

# Upozorňující label
upozorneni_label = Label(bg=hlavni_barva, fg="white", font=("Arial", 12))  # Vytvoření labelu pro zobrazení upozornění
upozorneni_label.grid(row=2, column=0)  # Umístění labelu v třetím řádku a prvním sloupci

# Hlavní cyklus
okno.mainloop()  # Spuštění hlavní smyčky aplikace
