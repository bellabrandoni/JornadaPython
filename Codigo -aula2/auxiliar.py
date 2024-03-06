#Pegando a posicao do mouse no login 
import pyautogui
import time
#espera 5 segundos na pagina para pegar a posicao do mouse 
time.sleep(5)

#captura aposicao do mouse -> point (x=500, y=388)
print(pyautogui.position())

"""
codigo  ...               obs
0    MOLO000251  ...               NaN
1    MOLO000192  ...               NaN
2    CAHA000251  ...               NaN
3    CAHA000252  ...  Conferir estoque
4    MOMU000111  ...               NaN
..          ...  ...               ...
288  ACAP000192  ...               NaN
289  ACSA0009.3  ...               NaN
290  CEMO000271  ...               NaN
291  FOMO000152  ...               NaN
292  CEMO000223  ...               NaN

"""