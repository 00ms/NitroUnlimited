import random
import string
import time
import requests


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.HEADER}"  """" 

$$\   $$\ $$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\        $$\   $$\ $$\   $$\ $$\       $$$$$$\ $$\      $$\ $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
$$$\  $$ |\_$$  _|\__$$  __|$$  __$$\ $$  __$$\       $$ |  $$ |$$$\  $$ |$$ |      \_$$  _|$$$\    $$$ |\_$$  _|\__$$  __|$$  _____|$$  __$$\ 
$$$$\ $$ |  $$ |     $$ |   $$ |  $$ |$$ /  $$ |      $$ |  $$ |$$$$\ $$ |$$ |        $$ |  $$$$\  $$$$ |  $$ |     $$ |   $$ |      $$ |  $$ |
$$ $$\$$ |  $$ |     $$ |   $$$$$$$  |$$ |  $$ |      $$ |  $$ |$$ $$\$$ |$$ |        $$ |  $$\$$\$$ $$ |  $$ |     $$ |   $$$$$\    $$ |  $$ |
$$ \$$$$ |  $$ |     $$ |   $$  __$$< $$ |  $$ |      $$ |  $$ |$$ \$$$$ |$$ |        $$ |  $$ \$$$  $$ |  $$ |     $$ |   $$  __|   $$ |  $$ |
$$ |\$$$ |  $$ |     $$ |   $$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |\$$$ |$$ |        $$ |  $$ |\$  /$$ |  $$ |     $$ |   $$ |      $$ |  $$ |
$$ | \$$ |$$$$$$\    $$ |   $$ |  $$ | $$$$$$  |      \$$$$$$  |$$ | \$$ |$$$$$$$$\ $$$$$$\ $$ | \_/ $$ |$$$$$$\    $$ |   $$$$$$$$\ $$$$$$$  |
\__|  \__|\______|   \__|   \__|  \__| \______/        \______/ \__|  \__|\________|\______|\__|     \__|\______|   \__|   \________|\_______/ 



""")
time.sleep(0.3)
print("NO PROXIES NEEDED  \n")
time.sleep(0.4)
print("CHECKER IN BUILT \n")
time.sleep(0.5)
print("IF YOU PAYED FOR THIS TOOL YOU GOT SCAMMED LMAO \n")
time.sleep(0.7)
print("DEVELEOPED BY DISCODANCER212 \n")
time.sleep(0.8)
print("NORMALLY TAKES 30 MINUTES TO FIND ONE WORKING CODE \n")

num = input('How many codes to generate??: ')

f = open("Codes.txt", "w", encoding='utf-8')

print(f"{bcolors.OKBLUE}" + "GENERATING!")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

with open("Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"{bcolors.OKGREEN}" + "HOORAYYYY {} " .format(line.strip("\n")))
            break
        else:
            print(f"{bcolors.WARNING}" + "NOT VALID {} " .format(line.strip("\n")))
