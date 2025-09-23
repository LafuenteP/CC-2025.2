# Converta os tipos

# Crie uma Series com os seguintes dados:

# 10, 20, 30, 40, 50

# Converta o tipo de dado da Series para numérico (int32), e calcule a média dos valores

# Dica: use o método Series.astype("int32") para converter todos os elementos

import pandas as pd

converter = pd.Series(["10","20","30","40","50"])

convertido = converter.astype("int32")

print(convertido.mean())


