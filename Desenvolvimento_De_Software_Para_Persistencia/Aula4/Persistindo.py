import pandas as pd


alunos_dic = {
    "nome" : "Jefferson",
    "curso" : "SI",
    "IRA" : 4.5
}

alunos_df = pd.DataFrame([alunos_dic])

alunos_csv = pd.read_csv("../Arquivos/04_Alunos.csv")
#print(alunos_csv)



# Problema: Persistir o alunos_dic em

# Solução 1 - concatenando dois dataframes


# O método concat recebe uma lista de Dataframes
#alunos_csv = pd.concat([alunos_csv, alunos_df], ignore_index = True)

#print(alunos_csv)

#alunos_csv.to_csv("../Arquivos/04_alunos.csv", index = False)

#================================================================================
# Solução 2 - Apendando o objeto no DataFrame


# O método append recebe um objeto para apendar no Dataframe original.
alunos_csv = alunos_csv._append(alunos_dic, ignore_index = True)

print(alunos_csv)

alunos_csv.to_csv("../Arquivos/04_alunos.csv", index = False)