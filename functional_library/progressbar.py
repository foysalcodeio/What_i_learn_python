# $ pip3 install tqdm

from tqdm import tqdm
from time import sleep

for el in tqdm([1, 2, 3], desc="Nasa Hacked by foysal"):
    sleep(1)

