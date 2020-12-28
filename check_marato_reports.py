import os
from os import listdir
from shutil import copy2

annotated_reports = "/home/siamakbarzegar/Documents/corpora/annotated_reports"
all_reports = "/home/siamakbarzegar/Documents/corpora/origin/Corpus_Aquas_SonEspases"

marato_repots = "/home/siamakbarzegar/Documents/marato/data/reports.txt"

new_bunch = "/home/siamakbarzegar/Documents/marato/13"

relacio_codis = "/home/siamakbarzegar/Documents/marato/data/excel_ID_stpau_mutua_mar.csv"



relacio_codis_files = open(relacio_codis, "r+")
relacio_codis_list = dict()
for f in relacio_codis_files:
    file_code = f.strip().split(",")
    relacio_codis_list[file_code[0]] = file_code[1]

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


all_report = []
for f in listdir(all_reports):
    all_report.append(f.split(".")[0])

marato_list = relacio_codis_list.keys()


annotated_list = []
for f in listdir(annotated_reports):
    if f not in annotated_list:
        annotated_list.append(f.split(".")[0])

sant_pau = 1
matua = 1
mar = 1

codis_relacio_list = dict()
for marato in marato_list:
    if marato in annotated_list:
        print(marato + " file is annotated")
    else:
        if marato.startswith("son"):
            src = os.path.join(all_reports,  marato + ".txt")
        else:
            src = os.path.join(all_reports, marato + ".utf8.txt")
        if relacio_codis_list[marato] == "sant_pau" and sant_pau <= 37:
            sant_pau += 1
            copy2(src, new_bunch)
        elif relacio_codis_list[marato] == "matua" and matua <= 37:
            matua += 1
            copy2(src, new_bunch)
        elif relacio_codis_list[marato] == "mar" and mar <= 33:
            mar += 1
            copy2(src, new_bunch)


print(sant_pau, matua, mar)
# annotated_list = []
# for f in listdir(annotated_reports):
#     if f not in annotated_list:
#         annotated_list.append(f.split(".")[0])



