#######################################################
# Name           : Brute Facebook (BF)                #
# File           : cok.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import requests as r, os, sys, json, time, random, subprocess, urllib

from platform import platform
from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel

# ------ MODULE ------ ####
from data import login_key as xx
from data import lainya as xjs
from data import dump as dup
from data import logo as asy
from data import cokz as sx
from data import cek as cpp

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#---------------------
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
############################ RESPONSE FACEBOOK ######################################
class Brute:
    def __init__(self):
        self.url = []
        self.moch_yayan()

    def hapus_log(self):
        try:os.remove(".token.txt");os.remove(".cokie.txt")
        except:pass

    def moch_yayan(self):
        asy.Logo().log()
        try:
            tokenz = open(".token.txt", "r").read()
            cookie = {'cookie': open(".cokie.txt", "r").read()}
        except FileNotFoundError:
            time.sleep(2);sx.Login()
        try:
            get  = r.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tokenz),cookies=cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
        except r.exceptions.ConnectionError:
            print("");prints(Panel("😔[bold red] Tidak ada koneksi"));exit()
        except KeyError:
            print("");prints(Panel("😢[bold red] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain."));time.sleep(5);self.hapus_log();sx.Login()
        prints(Panel(f"    [{biru_m}+{hapus}] selamat datang [yellow]{nama}{hapus} [{biru_m}+{hapus}]"))
        prints(Panel(f"""[{biru_m}01{hapus}]. Crack dari anggota grup     [{biru_m}06{hapus}]. Crack dari komentar
[{biru_m}02{hapus}]. Crack dari teman publik     [{biru_m}07{hapus}]. Checkpoint detedtor
[{biru_m}03{hapus}]. Crack dari total followers  [{biru_m}08{hapus}]. Fiture lainya
[{biru_m}04{hapus}]. Crack dari like postingan   [{biru_m}09{hapus}]. Upgrade ke [green]premium[/]
[{biru_m}05{hapus}]. Crack dari random id massal [{biru_m}00{hapus}]. Keluar {merah}exit program{hapus}""",title=f'{merah}•{kuning}•{hijau}•{hijau} MENU PILIHAN {hijau}•{kuning}•{merah}•{hapus}'))
        pepek = input(f"  [{O}*{N}] menu : ")
        if pepek in[""," "]:
            print("");prints(Panel("😡[bold red] jangan kosong kentod"));time.sleep(2);self.moch_yayan()
        elif pepek in["1","01"]:
            dup.Dump().dump_grup(cookie, tokenz)
        elif pepek in["2","02"]:
            dup.Dump().dump_prem(cookie, tokenz)
        elif pepek in["3","03"]:
            dup.Dump().followers(cookie, tokenz)
        elif pepek in["4","04"]:
            dup.Dump().like_post(cookie)
        elif pepek in["5","05"]:
            dup.Dump().rendem(cookie, tokenz)
        elif pepek in["6","06"]:
            dup.Dump().komentar(cookie)
        elif pepek in["7","07"]:
            cpp.Cek_has().gabut()
        elif pepek in["8","08"]:
            xjs.Xnxx(cookie, tokenz)
        elif pepek in["9","09"]:
            print("")
            prints(Panel(f"  >>> Dapatkan user premium untuk menikmati semua fiture!!<<"))
            upd = input("  [?] apakah ingin upgrade ke premium [Y/t]: ")
            if upd =="":
                exit(f"  {N}[{M}×{N}] Y/t memek!")
            elif upd in["Y","y"]:
                exit(subprocess.Popen(["am","start","https://licensi.yayandev.my.id/login/"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
            elif upd in["T","t"]:
                exit(f"{B}  Good byee:)")
            else:
                exit(f"  {N}[{M}×{N}] Y/t memek!")
        elif pepek in["0","00"]:
            titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
            for x in titik:
                sys.stdout.write(f"\r  [{M}×{N}] menghapus cookie {N}{x}{N}");sys.stdout.flush()
                time.sleep(1)
            self.hapus_log()
            print("");prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus cookie"));exit()
        else:
            print("");prints(Panel(f"😡 memu [bold red]{pepek}[/] tidak ada, cek menu nya!"));time.sleep(2);self.moch_yayan()
