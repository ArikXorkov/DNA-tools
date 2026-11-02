pair_DNA = {"A": "T","T": "A","G": "C","C": "G"}
pair_RNA = {"A": "U", "U": "A", "G": "C", "C": "G"}
pair_DNA_to_RNA = {"A": "U", "T": "A", "G": "C", "C": "G"}
pair_RNA_to_DNA = {"A": "T", "U": "A", "G": "C", "C": "G"}
value_true = False
cep2 = ""
Unknown = []
enter_DNA_or_RNA = input("Enter a DNA or RNA:\n-->If you need to convert from DNA to RNA, press 3\n-->If you need to convert from RNA to DNA, press 4\n").upper()
if "DNA" in enter_DNA_or_RNA:
    enter = input("Enter a DNA strand\n")
    for strand in enter.upper():
        if strand in pair_DNA:
            cep2+=pair_DNA[strand]
        else:
            Unknown.append(strand)
        value_true = True
elif "RNA" in enter_DNA_or_RNA:
    enter = input("Enter a RNA strand\n")
    for strand in enter.upper():
        if strand in pair_RNA:
            cep2+=pair_RNA[strand]
        else:
            Unknown.append(strand)
        value_true = True
elif "3" in enter_DNA_or_RNA:
    enter = input("Enter a DNA strand\n")
    for strand in enter.upper():
        if strand in pair_DNA_to_RNA:
            cep2+=pair_DNA_to_RNA[strand]
        else:
            Unknown.append(strand)
        value_true = True
elif "4" in enter_DNA_or_RNA:
    enter = input("Enter a RNA strand\n")
    for strand in enter.upper():
        if strand in pair_RNA_to_DNA:
            cep2+=pair_RNA_to_DNA[strand]
        else:
            Unknown.append(strand)
        value_true = True
else: print("You have selected an unknown value")
cep2 = cep2[::-1]
if value_true == True:
    print("Your reverse-complement strand:", cep2)
    print("Unknown values: ", Unknown)
