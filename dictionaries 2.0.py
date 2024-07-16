shtetet = {
    "Kosova": {
        "Kryeqyteti" : "Prishtina",
        "Popullsia" : 1800000
    },
    "Shqiperia": {
        "Kryeqyteti" : "Tirana",
        "Popullsia" : 2000000
     },
    "Maqedonia e Veriut": {
        "Kryeqyteti" : "Shkupi",
        "Popullsia" : 2100000
    }
}
print(shtetet["Kosova"]["Kryeqyteti"])
#--------------------------------------------------------#
produktet = {
    "tv" : 300,
    "mouse" : 50,
    "laptop" : 1000,
    "keyboard" : 50
}
#print(sorted(produktet)) qishtu i bon sort atributet jo qmimet
print(sorted(produktet.values()))
print(f"Produkti me qmimin me te vogel eshte", min(produktet.values()))
