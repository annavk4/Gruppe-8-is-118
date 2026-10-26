# Introduksjon
# Presenterer historien for spilleren.
print ("Du er Erling og leder arbeidet med kommunens nye medborgerportal.")
print ("Teamet har konflikter, og prototypen skal leveres om tre uker.")

# Poeng viser hvor mye valgene styrker samarbeidet. 
poeng = 0

# Valg 1
# Lagrer spillerens første valg som tekst.
print ("\nSilje og Elias er uenige om teknologi og design.")
print ("1: Snakk med dem hver for seg, og ha deretter et felles møte.")
print ("2: Bestem teknologivalget selv.")
valg1 = input("Valg 1 eller 2: ")

# Spør på nytt hvis spilleren skriver noe annet enn 1 eller 2.
while valg1 != "1" and valg1 != "2":
    valg1 = input("Ugyldig svar. Skriv 1 eller 2: ")

# Viser konsekvensen av valget. Involvering gir ett samarbeidspoeng.
if valg1 == "1":
    print("Begge føler seg hørt, men samtalene tar tid.")
    poeng = poeng + 1
else: 
    print("Arbeidet går videre, men begge føler seg overkjørt.")

# Valg 2
print ("\nHamdi og Hallgeir er uenige om løsningen for digitale folkmøter. ")
print("1: Lag papirmodeller og vurder forslagene sammen. ")
print("2: Valg kommunens eksisterende plattform. ")
valg2 = input("Velg 1 eller 2: ")

while valg2 != "1" and valg2 != "2":
    valg2 = input("Ugyldig svar. Skrive 1 eller 2: ")

if valg2 == "1":
    print("Begge blir hørt og finner en felles løsning, men det tar tid.")
else: 
    print("Temaet kommer raskt videre, men Hallgeir mister motivasjon.")

# Valg 3
print("\nHvordan vil du bevare motivasjonen i teamet?")
print("1: Sett av tid til samtaler og felles planlegging.")
print("2: Prioriter arbeidet med tydelige delmål.")
valg3 = input("Velg 1 eller 2: ")

while valg3 != "1" and valg3 != "2":
    valg3 = input("Ugyldig svar. Skriv 1 eller 2: ")

if valg3 == "1":
    print("Samarbeidet blir bedre, men tiden til utvikling blir knappere.")
    poeng = poeng + 1
elif valg1 == "1" and valg2 == "1":
    print("Det gode samarbeidet gjør at delmålene gir mestring og fremdrift.")
else:
    print("Delmålene gir retning, men spenninger svekker motivasjonen.")

# Avslutning: Et enkelt poengsystem bestemmer utfallet.
# Bruker poengsummen fra alle tre valgene til å bestemme avslutningen.
# 2–3 poeng gir bedre tillit, 1 gir delvis løsning, og 0 gir forsinkelse.
print("\nSlik ender historien:")

if poeng >= 2:
    print("Teamet gjenoppretter tillit og samarbeider bedre. ")
    print("De må fortsatt passe på tiden frem mot levering. ")
elif poeng == 1:
    print("Konfliktene løses delvis, men relasjonene er sårbare.")
else: 
    print("Teamet mister samhold, og prosjektet forsinkes." )
