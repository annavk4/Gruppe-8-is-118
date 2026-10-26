import sys

print("Velkommen til IS-118, Gruppe 8 sin innlevering. Markus sitt utkast.\n")

print("Ditt navn er Erling. Du er prosjektleder for utviklingen av kommunens nye medborgerportal.\n"
"Du har satt sammen et team bestående av medlemmer med ulik bakgrunn og kunnskap.\n"
"Dere har nå jobbet sammen i seks uker, og er godt i gang med prosjektet.\n"
"Det har startet bra, med høy intensitet og motivasjon for å nå målet som et fellesskap.\n")
print("Teamet har blitt bedre kjent, og dere er nå inne i storming-fasen av teamutviklingen.\n"
"Her kommer deres faglige perspektiver og personlige preferanser mer til syne, og konflikter har oppstått.\n"
"Gruppen står nå overfor to ulike konflikter, og det er tre uker til prototypen må leveres.\n")
print("Disse må du, som Erling, vurdere for å sikre videre fremdrift i prosjektet.\n"
"Formålet med denne fortellingen er å være Erling og vurdere konfliktene, slik at han kan sette i gang tiltak.\n")


print("\nErling hører at Silje og Elias står i en konflikt.\n"
"Tidligere så husker Erling at de snakket om at de hadde en uenighet om teknologivalg og design.\n"
"Erling tenker: \"Dette er det vi kaller for en sakskonflikt som har utviklet seg til en personkonflikt.\n"
"Uenigheten handler om mål, oppgaver og ansvar.\"\n"
"Erling husker at dette kan skje i en argumentasjon, og at personkonflikter i større grad handler om\n"
"relasjonen mellom partene, samtidig som følelsene blir sterkere.\n")

print("Erling tenker på to løsninger:\n")

print("Løsning 1:\n"
"\"Jeg kan ta et møte med Silje og Elias hver for seg, og deretter et felles møte med begge to.\n"
"Da kan de begge komme med sine perspektiver og synspunkter til meg,\n"
"og deretter kan jeg forklare deres tanker og ideer til hverandre for å legge et\n"
"felles grunnlag som drar de tilbake til prosjektet.\"\n")

print("Løsning 2:\n"
"\"Siden vi har dårlig tid, så er det kanskje bedre å bare ta en rask beslutning om teknologivalget.\n"
"Jeg beslutter bare at vi tar Silje sitt forslag, siden min mening som prosjektleder er overordnet.\n"
"Så får vi kommet oss forbi denne krangelen, og raskt tilbake på skinner.\"\n")

FirstSolution = input("Hva bør Erling gjøre?\n"
"Skriv [1] for \"Løsning 1\" eller [2] for \"Løsning 2\".\n")

if FirstSolution == "1":
    print("Samtalene har bedret kommunikasjonen mellom Silje og Elias.\n"
    "Det har tatt tid fra arbeidet, og fristen for levering av prototypen nærmer seg.\n")
elif FirstSolution == "2":
    print("Etter denne raske beslutningen kommer teamet raskt tilbake til arbeidet med utviklingen av prototypen.\n"
    "Både Silje og Elias opplever at Erling tok en beslutning uten å høre tilstrekkelig på deres perspektiver.\n"
    "Begge deltar derfor mindre i diskusjoner.\n")
else:
    sys.exit("Vennligst begynn på nytt og skriv [1] eller [2].\n")


print("\nEtter å ha tatt tak i konflikten mellom Silje og Elias må Erling gå videre til uenigheten mellom Hallgeir og Hamdi.\n"
"Han hører at de har ulike tanker om hvordan innbyggere skal kunne delta i digitale folkemøter.\n"
"\"Det høres ut som Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.\n"
"Hallgeir, derimot, ønsker et mer åpent dialogbasert system med rom for spontane innspill.\" tenker Erling.\n"
"Konflikten er mer lavmælt, men Erling må håndtere uenigheten slik at de kan komme videre.\n")

print("Erling står overfor to valg:\n")

print("Valg 1:\n"
"Erling tenker på å bruke kommunens eksisterende platform for å spare tid.\n"
"\"Å bruke den eksisterende prototypen gjør at Hamdi får det som han vil.\n"
"Det gjør kanskje Hallgeir litt lei seg, men vi får i hvert fall kommet raskere tilbake på jobb.\"\n")

print("Valg 2:\n"
"\"Kanskje Silje kan hjelpe oss i å lage papirmodeller for å forklare tankegangen bak\n"
"Hamdi og Hallgeir's løsninger?\"\n"
"Erling innser at dette alternativet gir begge muligheten til å uttrykke sine\n"
"forsalg på en konstruktiv måte. Modellene kan hjelpe teamet med å holde diskusjonen\n"
"strukturert og gjøre det lettere å sammenligne forslagene.")

SecondChoice = input("Hva bør Erling velge?\n"
"Skriv [1] for \"Valg 1\" eller [2] for \"Valg 2\".\n")

if SecondChoice == "1":
    print("Erling valgte å gå videre med forslaget til Hamdi.\n"
    "Hallgeir opplever at hans perspektiv ikke ble tilstrekkelig hørt.\n"
    "Han bidrar derfor mindre aktivt i arbeidet fremover, og motivasjonen hans har blitt svekket.\n"
    "Teamet kommer raskt videre med arbeidet, men samarbeidet er fortsatt sårbart.\n")
elif SecondChoice == "2":
    print("Arbeidet med å lage papirmodeller har ført til at både Hallgeir og Hamdi føler seg hørt,\n"
    "og med hjelp fra Silje kom de til en felles løsning.\n"
    "Prosessen har tatt tid fra utviklingen, og teamet har mindre tid til videre utvikling.\n")
else:
    sys.exit("Vennligst begynn på nytt og skriv [1] eller [2].\n")


print("\nNå som Erling har håndtert de to konfliktene, må han finne ut hvordan han skal\n"
"kunne bevare motivasjonen for hele teamet.\n"
"Erling mumler til seg selv: \"Mine tidligere valg kan ha styrket samarbeidet i gruppen,\n"
"men også ha etterlatt spenninger. Det er bare 3 uker til første prototype skal leveres,\n"
"så jeg bør ta hensyn til både relasjoner og fremdrift.\"\n")

print("Erling kan nå gå frem med to forskjellige alternativ:\n")

print("Alternativ 1:\n"
"\"Jeg tror det er best å sette av tid til å diskutere samarbeider og avklare forventingene til alle sammen.\"\n"
"Erling prøver å bringe inn alle medlemmene i planleggingen av arbeidet, og det tar litt mer tid enn forventet.\n")

print("Alternativ 2:\n"
"\"Jeg tenker det er best å sette tydelige og realistiske delmål.\"\n"
"Erling mener at det å prioritere arbeidet med den første prototypen,\n"
"og fordeler oppgaver og følger opp fremdriften slik at teamet vet hva de\n"
"skal oppnå før levering er sentralt.\n")

ThirdAlternative = input("Hvilket alternativ går Erling for?\n"
"Skriv [1] for \"Alternativ 1\" eller [2] for \"Alternativ 2\".\n")

if ThirdAlternative == "1":
    print("Teamet har gjennom relasjonsbyggingen fått en mer åpen kommunikasjon og bedre samarbeid.\n"
    "De jobber bedre sammen, men samtalene har tatt tid fra utviklingen.\n"
    "Det er derfor mindre tid til å ferdigstille prototypen før levering.\n")
elif ThirdAlternative == "2":
    print("Teamet får raskt rettet oppmerksomheten mot prosjektet og ferdigstilling av prototypen.\n"
    "Hvis de tidligere konfliktene fortsatt preger samarbeidet, er motivasjonen svekket og arbeidet går sakte fremover.\n"
    "Dersom samarbeidet er styrket, gir delmålene medlemmene mestring og de får raskere fremdrift.\n")
else:
    sys.exit("Vennligst begynn på nytt og skriv [1] eller [2].\n")

if FirstSolution == "1" and SecondChoice == "2":
    print("\nErling valgte å ha samtaler med Silje og Elias, og lage papirmodeller med Hallgeir og Hamdi.\n"
    "Dette gav teamet et godt grunnlag videre, om de så hadde relasjonsbyggende tidsbruk for å bevare motivasjonen\n"
    "eller prioriterte fremdrift med tydelige mål.\n"
    "Medlemmene følte seg hørt, som bidro til at kommunikasjonen ble mer åpen og at samarbeidet ble bedre.\n"
    "Denne positive utviklingen ga bedre fremdrift i prosjektet, og gjorde at teamet leverte prototypen innen tidsfristen.\n")

    print("Teamet bevegde seg fra storming-fasen til norming-fasen.\n")
elif FirstSolution == "2" and SecondChoice == "1" and ThirdAlternative == "2":
    print("\nErling valgte å bruke lite tid på å forstå og løse samarbeidsproblemene, og tok heller raske beslutninger.\n"
    "uten særlig involvering.\n"
    "Samarbeidet ble svekket, og medlemmene føler seg overkjørt.\n")
    
    print("Kommunikasjonen og motivasjonen er dårlig, og det oppstår flere misforståelser, mer omarbeid, og en forsinket levering.\n")
else:
    print("\nErling valgte enten:\n"
    "Å avklare de faglige valgene, men brukte lite tid på å bygge tillit og styrke realsjonene.\n"
    "Teamet kom videre i prosjektet, men tilliten ble ikke gjenopprettet.\n"
    "Medlemmene følger beslutningene tatt av Erling, men de føler seg ikke sett og hørt.\n"
    "Arbeidet kan fortsette, men det kan bli en risiko for at nye konflikter oppstår under tidspress fram mot levering.\n")
          
    print("Eller å ta raske avgjørelser uten mye involvering, men brukte deretter litt tid på relasjonsbygging.\n"
    "Tilliten mellom teammedlemmene ble ikke gjenopprettet, men de kom seg videre i prosjektet.\n"
    "Silje og Elias følger beslutningen tatt av Erling, og det samme gjør Hamdi og Hallgeir.\n"
    "Arbeidet fortsetter, men ikke alle føler seg hørt, sett, og involvert.\n")

    print("Erling fikk avklart de faglige uenighetene, men ikke spenningene blant medlemmene.\n")