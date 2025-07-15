"""coco = {'Clavier': 116.66666666666667, 'Écran': 405}

for cle, valeur in coco.items():
    print(lambda v: valeur*2)

    cpu_1 = mean(cpu)
    ram_1 = mean(ram)
    print(f"cpu: {cpu_1}, ram: {ram_1}")


    for cle, valeur in filtrer_donnees.items():
        for element in valeur:
            liste_acceuil_cpu.append(element["cpu"])
        print(liste_acceuil_cpu)
        r_cpu = {cle: mean(liste_acceuil_cpu)}
        print(r_cpu)


def analyse_logs(logs: list):
    # Regroupe les données par serveur
    for element in logs:
        if element["server"] == "srv-01":
            liste_1 = [element]
            print(liste_1)
        elif element["server"] == "srv-02":
            liste_2 = [element]
            print(liste_2)
        elif element["server"] == "srv-03":
            liste_3 = [element]
            print(liste_3)
        finale_liste = [liste_1, liste_2, liste_3]
        print("co", finale_liste)


analyse_logs(logs)

for cl, vale in val.items():
    r = {cl: mean(vale["cpu"])}
    print(vale)"""

do = {
    'server': 'srv-01',
    'timestamp': '2025-07-13T08:00:00',
    'cpu': 88,
    'ram': 74,
    'status': 'OK'
    }
"""for cle, valeur in do.items():
    print(f"{cle} - {valeur}")
if do["server"] == "srv-01":
    print(do["cpu"])"""
c = []
for element in logs:
    if element["server"] == "srv-01":
        print(f"{element['cpu']}, {element['status']}")

nbres_alertes = {cle: len(valeur["alertes"]) for cle, valeur in intermediare_cpu.items() if valeur["alertes"]}
print(nbres_alertes)

tri_alerte = dict(sorted(nbres_alertes.items(), key=lambda x: x[1], reverse=True))
print(tri_alerte)

for key, val in tri_moyen_cpu.items():
    print(f"{key} -> ")


    for cle, valeur in moyenne_cpu.items():
        tri_moyen_cpu = dict(sorted(valeur.items(), key=lambda x: x[1], reverse=True))
        print(tri_moyen_cpu)