pair = {"A": "T","T": "A","G": "C","C": "G"}
cep2 = ""
neizvestnoe = []
enter = input("Enter a DNA strand\n")
for i in enter.upper():
    if i in pair:
        cep2 = cep2 + pair[i]
    else:
        neizvestnoe.append(i)
cep2 = cep2[::-1]
print("Your reverse-complement DNA strand:", cep2)
print("Unknown values: ", neizvestnoe)
