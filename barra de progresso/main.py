from tqdm import tqdm 
import time


# exibir barra d progresso 

for i in tqdm(range(100)):
    time.sleep(0.05) # simula um processo demorado
