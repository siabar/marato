import os
from os import listdir
from shutil import copy2
import csv

snomed = "/home/siamakbarzegar/Documents/marato/data/SNOMNED_DIC.csv"
ictusnet = "/home/siamakbarzegar/Documents/marato/data/IctusnetDict.csv"

new_snomed = "/home/siamakbarzegar/Documents/marato/data/Updated_SNOMNED_DIC.csv"


etiologia = ["causa ", "d'etiologia ", "de origen ", "etiologia ", "origen ", "perfil "]
etiologia_pro = ["", "probablemente ", "posiblemente "]
ictusnet = open(ictusnet, "r+")
ictusnet_dic = dict()
for f in ictusnet:
    file_code = f.strip().split("|")
    ictusnet_dic[file_code[2] + "#" + file_code[1]] = file_code

snomed = open(snomed, "r+")
snomed_dic = dict()

snomed_reader = csv.reader(snomed, delimiter=',')
line_count = 0
for row in snomed_reader:
    if row[3] == "secundaria a diseccion":
        check = 0
    snomed_dic[row[3] + "#" + row[1]] = row
    if row[1] == "_SUG_Arteria_afectada":
        new_row = row.copy()
        new_row[3] = "arteria " + new_row[3]
        snomed_dic[new_row[3] + "#" + row[1]] = new_row
    if row[1] == "_SUG_Etiologia":
        for eti in etiologia:
            for pro in etiologia_pro:
                new_row = row.copy()
                new_row[3] = eti + pro + new_row[3]
                snomed_dic[new_row[3] + "#" + row[1]] = new_row

new_snomed_file = open(new_snomed, mode='w')
new_snomed_writer = csv.writer(new_snomed_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for variant_variable, row in ictusnet_dic.items():
    if variant_variable in snomed_dic.keys():
        new_snomed_writer.writerow(snomed_dic[variant_variable])
    else:
        if row[1] in ["_SUG_Localizacion", "_SUG_Arteria_afectada", "_SUG_Etiologia", "_SUG_Lateralizacion"]:
            new_snomed_writer.writerow(["", row[1], "", row[2]])
        else:
            new_snomed_writer.writerow(["", row[1], "", row[2]])

# code = relacio_codis_list[marato]
# if code not in codis_relacio_list.keys():
#     codis_relacio_list[code] = [marato]
# else:
#     temp = codis_relacio_list[code]
#     temp.append(marato)
#     codis_relacio_list.update({code: temp})


# marato_files = open(marato_repots, "r+")
# marato_list = []
# for f in marato_files:
#     marato_list.append(f.strip())
