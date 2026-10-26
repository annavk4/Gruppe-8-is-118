print("Velkommen til Erlings prosjekt!")
print("Du er Erling, prosjektleder for kommunens nye digitale medborgerportal.")
print("Etter seks uker har det oppstått konflikter i teamet.")
print("Du må ta tre viktige beslutninger for å hjelpe prosjektet videre.")

print(" ")
print("Beslutning 1: Konflikten mellom Silje og Elias")
print("1. Erling tar individuelle samtaler med dem, deretter et felles møte.")
print("2. Erling tar en rask beslutning om teknologivalg, og krav til videre samarbeid.")

valg1 = input("Hva velger du? Skriv 1 eller 2: ")

while valg1 != "1" and valg1 != "2":
    valg1 = input("Ugyldig valg! Prøv igjen. Skriv 1 eller 2: ")

if valg1 == "1": 
    print("Erling snakker med Silje og Elias hver for seg.")
    print("Begge føler seg hørt, og konflikten roer seg.")

elif valg1 == "2":
    print("Erling tar rask beslutning om teknologivalg, og krav til videre samarbeid..")
    print("Diskusjonen blir opphetet, og konflikten eskalerer.")

else: 
    print("Ugyldig valg. Vennligst velg 1 eller 2.")

print()
input("Trykk Enter for å fortsette til neste beslutning...")

print(" ")
print("Beslutning 2: Konflikten mellom Hamdi og Hallgeir.")
print("1. Erling arrangerer at de lager papirmodeller og tar en felles vurdering.")
print("2. Erling velger å bruke kommunens eksisterende platform.")

valg2 = input("Hva velger du? Skriv 1 eller 2: ")

while valg2 != "1" and valg2 != "2":
    valg2 = input("Ugyldig valg! Prøv igjen. Skriv 1 eller 2: ")

if valg2 == "1": 
    print("Erling arrangerer at de lager papirmodeller og tar en felles vurdering.")
    print("Hamdi og Hallgeir finner en løsning og samarbeider bedre.")

elif valg2 == "2":
    print("Erling velger å bruke kommunens eksisterende platform.")
    print("Konflikten eskalerer, og prosjektet lider som følge av dårlig samarbeid.")

else:
    print("Ugyldig valg. Vennligst velg 1 eller 2.")

print()
input("Trykk Enter for å fortsette til neste beslutning...")

print(" ")
print("Beslutning 3: Motivasjon i teamet.")
print("1. Erling prioriterer relasjonsbygging og involvering.")
print("2. Prioritere fremdrift, med tydlige delmål.")

valg3 = input("Hva velger du? Skriv 1 eller 2: ")

while valg3 != "1" and valg3 != "2":
    valg3 = input("Ugyldig valg! Prøv igjen. Skriv 1 eller 2: ")

if valg3 == "1":
    print("Erling prioriterer relasjonsbygging og involvering.")
    print("Teamet blir mer motivert og samarbeider bedre, noe som forbedrer prosjektets fremdrift.")    

elif valg3 == "2":
    print("Erling prioriterer fremdrift og setter tydelige delmål.")

    if valg1 == "1" and valg2 == "1":
        print("Samarbeidet er godt, og delmålene gir teamet mestring og bedre fremdrift.")
    else:
        print("Tidligere konflikter påvirker fortsatt samarbeidet, og motivasjonen kan bli svekket.")
 

else: 
    print("Ugyldig valg. Vennligst velg 1 eller 2.")

print()
input("Trykk Enter for å se hvordan dine valg påvirket prosjektet...")

poeng = 0

if valg1 =="1": 
    poeng = poeng + 1

if valg2 == "1": 
    poeng = poeng + 1

if valg3 == "1": 
    poeng = poeng + 1

if poeng == 3 or (valg1 == "1" and valg2 == "1"): 
    print("Gruppa opplever god tillit og samarbeidet og kommunikasjonen blir bedre, de beveger seg mot norming.")

elif poeng >= 1: 
    print("Gruppa opplever noen utfordringer, men samarbeidet og kommunikasjonen blir bedre.")

else: 
    print("Konfliktene i teamet fortsetter, og prosjektet blir forsinket.")

