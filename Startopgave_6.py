# Naam: Valerie Verhalle
# Datum: 
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestandsnaam = "alpaca.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    headers, seqs = lees_inhoud(bestandsnaam)
    #print(headers) # [h, h, h, h]
    #print(seqs) #[s, s, s, s]
    print(70*"-")

    zoekwoord = input("Geef een zoekwoord op: ")
    print(zoekwoord)
    print(70*"-")

    #for elem in seqs:
        #isdnabool = is_dna(elem)
    
    for h in headers:
        if zoekwoord in h:
            seq = seqs[headers.index(h)]
            
            print("header match:",h)
            print("bijbehorende sequentie:",seq)
            print(70*"-")
            
            is_dna(seq)
            print(70*"-")
            
            knipt(seq)
            print(30*"-")
       
def lees_inhoud(bestandsnaam):
    bestand = open(bestandsnaam)
    #print(bestand)
    #file_list = bestand.readlines() #type(list)
    #file_string = bestand.read()#type(string)
    
    headers = []
    seqs = []
    seq = ""

    for line in bestand:
        line = line.strip()
                
        if ">" in line:
            headers.append(line)
            if len(seq) > 0:
                seqs.append(seq)
                seq =""
        else:
            seq += line
    seqs.append(seq)
    #print(headers)  
    #print(seqs)  

    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """

         
    return headers, seqs

    
def is_dna(seqs):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """

    for lines in seqs:
        A = lines.count("A")
        G = lines.count("G")
        C = lines.count("C")
        T = lines.count("T")
        totaal = A + G + C + T
        
    for i in seqs:
        A = (len(lines))
        if A == totaal:
            print("bestand is DNA")
            return True
        if A != totaal:
            print("Bestand is geen DNA")
            return False

def knipt(seqs):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    print(seqs)
    bestand = open("enzymen.txt")
    #print(bestand)
    enzymen = []

    for line in bestand:
        combi = line.split()
        enzymen.append(combi)
        
    for seq in enzymen:
        seq[1] = seq[1].replace('^','')
        #print(enzym);

    i=0
    for seq in enzymen:
        i+=1
        if seq[1] in seqs:
            pos = seqs.index(seq[1])
            A = pos*" " + seq[1]
            print (seqs)
            print(A)
            print ("Match:" ,seq[0],seq[1])
            print('\n')
   
main()
