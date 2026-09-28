#EXO 1

ip1 = "192.168.1.1"
ip2 = "10.0.0.1"

ip1, ip2 = ip2, ip1

print("ip1 =", ip1)
print("ip2 =", ip2)

#EXO 2

nombre1 = int(input("Chiffre numero 1 : "))
nombre2 = int(input("Chiffre numero 2 : "))

somme = nombre1 + nombre2
moyenne = (nombre1 + nombre2) / 2

print(f"la somme de {nombre1} et {nombre2} est {somme}" )

print(f"La moyenne de {nombre1} et {nombre2} est {moyenne} ")

#EXO 3

nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

print(f"Bonjour, {prenom} {nom} !")

#EXO 4

age = input("Entrez votre âge : ")

if age > "18":
    print("Accès autorisé")
else:
    print("Accès refusé")

#EXO 5

MotsDePasse = input("Entrez votre mot de passe : ")

if len(MotsDePasse) >= 8:
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")

#EXO 6

for i in range(10):
    print(i * 2)

#EXO 7

nombre = input("Entrez un nombre : ")

for i in range(10):
    resultat = int(nombre) * i
    print(f"{nombre} x {i} = {resultat}")