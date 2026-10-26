# introduksjon
print("Du er Erling, prosjektleder for medborgerportalen.")
print("Det har gått seks uker siden teamet startet.")

# Beslutning 1: Silje og Elias
print()
print("BESLUTNING 1: Konflikten mellom Silje og Elias")
print("A: Individuelle samtaler, deretter felles møte")
print("B: Ta en rask beslutning om teknologivalget")

# Lagrer valget og spør på nytt til svaret er A eller B
valg1 = input("Ditt valg (A/B): ").upper().strip()
while valg1 !="A" and valg1 !="B":
    print("Ugyldig valg. Skriv A eller B.")
    valg1 = input("Ditt valg (A/B): ").upper().strip()

# Konsekvenser av valg 1
if valg1 == "A":
    print("Samtalene har bedret kommunikasjonen mellom Silje og Elias.")
    print("Det har tatt tid fra arbeidet, og fristen nærmer seg.")
else: 
    print("Teamet er raskt tilbake i arbeidet med prototypen.")
    print("Men Silje og Elias føler seg overkjørt og deltar mindre.")
input("Trykk Enter for å gå videre til neste beslutning...")
print()

# Beslutning 2: Hamdi og Hallgeir
print("BESLUTNING 2: Uenigheten mellom Hamdi og Hallgeir")
print("A: Lage papirmodeller og ta en felles vurdering")
print("B: Bestemme at kommunens eksisterende plattform skal brukes")

# lagrer valget og spør på nytt til svaret er A eller B
valg2 = input("Ditt valg (A/B): ").upper().strip()
while valg2 !="A" and valg2 != "B": 
    print("Ugyldig valg. Skriv A eller B. ")
    valg2 = input("Ditt valg (A/B): ").upper().strip()
   
# Konsekvenser av valg 2
if valg2 =="A":
        print("Papirmodellene gjør at både Hamdi og Hallgeir føler seg hørt.")
        print("Prosessen tok tid, så teamet har mindre tid igjen til utviklingen.")
else:
        print("Teamet kommer raskt videre, men Hallgeir føler seg ikke hørt.")
        print("Han bidrar mindre, og samarbeidet er fortsatt sårbart.")

# Teller hvor mange av de to første valgene som styrket relasjonen (0, 1 eller 2)
tillit = 0
if valg1 == "A":
    tillit = tillit + 1
if valg2 == "A":
    tillit = tillit + 1

input("Trykk Enter for å gå videre til neste beslutning...")

# Beslutning 3: motivasjon i teamet
print()
print ("BESLUTNING 3: Å bevare motivasjonen i teamet")
if tillit == 2:
     print("Samarbeidet er styrket, men tiden begynner å bli knapp.")
elif tillit == 1: 
    print("Noe er løst, men det er fortsatt spenninger i teamet.")
else: 
     print("Du har avklart de faglige valgene, men flere føler seg overkjørt.")
print("A: Sette av tid til relasjonsbygging og involvering av teamet")
print("B: Prioritere fremdrift med tydelige delmål")

valg3 = input ("Ditt valg (A/B): ").upper().strip()
while valg3 != "A" and valg3 != "B": 
     print("Ugyldig valg. Skriv A eller B.")
     valg3 = input("Ditt valg (A/B): ").upper ().strip()

# Konsekvenser av valg 3, teksten avhenger av tillit
if valg3 == "A":
    if tillit == 2:
        print("Samarbeidet er styrket, og samtalene gjør teamet enda tryggere.")
        print("Samtalene har likevel tatt tid fra utviklingen av prototypen.")
    
    elif tillit == 1: 
         print("Samtalene bedrer samarbeidet, men noen spenninger gjenstår.")
         print("Samtalene har likevel tatt tid fra utviklingen av prototypen.")
    else: 
         print("Samtalene gir åpnere kommunikasjon, men tilliten er lav.")
         print("Samtalene har likevel tatt tid fra utviklingen av prototypen.")

else: 
     if tillit == 2:
        print("De tydeligere delmålene gir mestring, og teamet får rask fremdrift.")
     elif tillit == 1:
          print("Delmålene holder fokuset, men teamet må fortsatt jobbe med tillit og samarbeid.")
     else: 
          print("Erling prioriterer fremdrift, men flere føler seg oversett.")
          print("Konfliktene påvirker samarbeidet, og prosjektet risikerer å bli forsinket.")

# Utfall basert på valgene
print()
input("Trykk Enter for å se hvordan prosjektet ender...")
print()
print("RESULTAT AV DINE BESLUTNINGER")

if tillit == 2:
     # A i begge de to første valgene, uansett valg 3
     print("TEAMET GJENOPPRETTER TILLIT")
     print("Medlemmene føler seg hørt, og teamet går videre til norming-fasen.")
elif tillit == 0 and valg3 == "B":
     # B i alle tre valgene
     print("TEAMET MISTER SAMHOLD OG PROSJEKTET FORSINKES")
     print("Medlemmene føler seg overkjørt, og leveringen blir forsinket.")
else: 
     # alle andre kombinasjoner 
     print("KONFLIKTEN LØSES DELVIS, MEN RELASJONENE ER SÅRBARE")
     print("Prosjektet kommer videre, men ikke alle føler seg hørt.")




