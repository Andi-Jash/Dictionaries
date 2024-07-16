person = {
    "Emri":"Elon",
    "Mbiemri":"Musk",
    "Kompania":"SpaceX",
    "Titull":"CEO",
    "Mosha":48
}
#emri = person["Emri"]
#print(emri)
                            #different ways to print
#x = person.get("Emri")
#print(x)

person["Kompania"] = "Tesla"

for i in person:
    print(person[i])
#ose
for i in person.values():
    print(i)

if "Kompania" in person:
    print("Po eshte")
else:
    print("Jo nuke eshte")