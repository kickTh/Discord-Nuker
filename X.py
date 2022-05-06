
import os,sys,time
import discord,time
import requests
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
try:
        import requests
        import pyfiglet
except ImportError:
        os.system("clear")
        time.sleep(1)
        print('\033[91mข้อผิดพลาด !! : ไม่ได้ติดตั้งการพึ่งพาบางรายการ')
        os.system("clear")
        print('\033[91mโปรแกรมกำลังแก้ปัญหา:โปรดรอ.')
        time.sleep(1)
        print('\033[91mโปรแกรมกำลังแก้ปัญหา:โปรดรอ..')
        time.sleep(1)
        print('\033[92mโปรแกรมกำลังแก้ปัญหา:โปรดรอ...')
        time.sleep(1)
        os.system("clear")
        os.system("termux-setup-storage")
        os.system("atp upgrade -y")
        os.system("pkg update")
        os.system("apt install python -y")
        os.system("apt install python2 -y")
        os.system("apt install php -y")
        os.system("apt install python-dev -y")
        os.system("apt install python3 -y")
        os.system("apt install java -y")
        os.system("apt install git -y")
        os.system("apt install perl -y")
        os.system("apt install bash")
        os.system("apt install nano -y")
        os.system("apt install curl -y")
        os.system("apt install openssl -y")
        os.system("apt install openssh -y")
        os.system("apt install wget -y")
        os.system("apt install clang -y")
        os.system("apt install nmap -y")
        os.system("apt install w3m -y")
        os.system("apt install hydra -y")
        os.system("apt install ruby -y")
        os.system("apt install macchanger -y")
        os.system("apt install host -y")
        os.system("apt install dnsutils -y")
        os.system("apt install coreutils -y")
        os.system("pip install pip & pip install discord & pip install requests & pip install pyfiglet & pip install logging & pip install pystyle & pip install tqdm & pip install colorama & pip install datetime & pip install dhooks")
        os.system("pip install uncompyle6==3.8.0 & pip install uncompyle6==3.7.4 & pip install uncompyle6==3.7.3 & pip install uncompyle6==3.7.2 & pip install uncompyle6==3.7.1 & pip install uncompyle6==3.7.0 & pip install uncompyle6==3.6.7 & pip install uncompyle6==3.6.6 & pip install uncompyle6==3.6.5 & pip install uncompyle6==3.6.4 & pip install uncompyle6==3.6.3")
        os.system("clear")
        print('\033[92mระบบแก้ไขปัญหา:สำเร็จ')
        time.sleep(1)
        print('\033[92mโปรดรันอีกครั้ง')
        



os.system("clear")
def Discord():
   Discord = pyfiglet.figlet_format("Discord")
   print(f"\033[1;91m{Discord}")
   print("""
  \033[1;91m
 ────────────────────────────────────────────────────────
  \033[1;91m[\033[0m1\033[1;91m] \033[1;91m สร้างหมวดหมู่
  \033[1;91m[\033[0m2\033[1;91m] \033[1;91m สร้างช่องข้อความ
  \033[1;91m[\033[0m3\033[1;91m] \033[1;91m สร้างช่องพูด
  \033[1;91m[\033[0m4\033[1;91m] \033[1;91m สแปมแชท
  \033[1;91m[\033[0m5\033[1;91m] \033[1;91m สร้างบทบาท
  \033[1;91m[\033[0m6\033[1;91m] \033[1;91m ทั้งหมด ( รวมทุกฟังก์ชั่น )
  \033[1;91m[\033[0mT\033[1;91m] \033[1;91m ยูทูปผู้สร้าง
  \033[1;91m[\033[0mX\033[1;91m] \033[1;91m ดิสคอสผู้สร้าง
  \033[1;91m[\033[0mY\033[1;91m] \033[1;91m รีโปรแกรม
  \033[1;91m[\033[0m0\033[1;91m] \033[1;91m ออกจากโปรแกรม
  \033[1;91m
 ────────────────────────────────────────────────────────
  """)
  
  


token = input('\033[1;91m Token Account :\033[1;92m')
os.system("clear")
Discord()
Settings = input("\033[1;96m» \033[1;91mโปรดเลือก : \033[1;94m")

#Sreate A Channel
if Settings == "1":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        
        Guilds_Sreate_A_Channel = input("\033[1;96m» \033[1;92m ID กิลด์ : \033[1;91m#")
        Name_Sreate_A_Channel = input("\033[1;96m» \033[1;92m ตั้งชื่อ  : \033[1;91m")
        Settings_1 = int(input("\033[1;96m» \033[1;92m  จำนวน : \033[1;91m"))
        def Discord_Settings_1_Sreate_A_Channel():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_Sreate_A_Channel}/channels",headers={"authorization": token},json={"name":Name_Sreate_A_Channel,"type":4})

        for i in range(Settings_1):
                Discord_Settings_1_Sreate_A_Channel()
                
                

#Create A Speech Channel
if Settings == "2":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        
        Guilds_Create_A_Speech_Channel = input("\033[1;96m» \033[1;92m ID กิลด์ : \033[1;91m#")
        Name_Create_A_Speech_Channel = input("\033[1;96m» \033[1;92m ตั้งชื่อ : \033[1;91m")
        Settings_2 = int(input("\033[1;96m» \033[1;92m  จำนวน : \033[1;91m"))
        

        def Discord_Settings_2_Sreate_A_Channel():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_Sreate_A_Channel}/channels",headers={"authorization": token},json={"name":Name_Sreate_A_Channel,"type":0})
   
        for i in range(Settings_2):
                Discord_Settings_2_Create_A_Speech_Channel()
                
                
                
#Create Category                
if Settings == "3":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        
        Guilds_Create_Category = input("\033[1;96m» \033[1;92m ID กิลด์ : \033[1;91m#")
        Name_Create_Category = input("\033[1;96m» \033[1;92m ตั้งชื่อ : \033[1;91m")
        Settings_3 = int(input("\033[1;96m» \033[1;92m  จำนวน : \033[1;91m"))
        

        def Discord_Settings_3_Create_Category():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_Create_Category}/channels",headers={"authorization": token},json={"name":Name_Create_Category,"type":2})

        for i in range(Settings_3):
                Discord_Settings_3_Create_Category()
                
                
#Chat Spam
if Settings == "4":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        
        ID_Channel_Chat_Spam = input("\033[1;96m» \033[1;92m ID ช่องแชท : \033[1;91m#")
        Message_Chat_Spam = input("\033[1;96m» \033[1;92m ข้อความที่สแปมแชท : \033[1;91m")
        Settings_4 = int(input("\033[1;96m» \033[1;92m  จำนวน : \033[1;91m"))
        
        

        def Discord_Settings_4_Chat_Spam_1():
                requests.post(f"https://discord.com/api/v9/channels/{ID_Channel_Chat_Spam}/messages",headers={"authorization": token},json={"content":Message_Chat_Spam})

        for i in range(Settings_4):
                Discord_Settings_4_Chat_Spam_1()
                
                
#Create Role
if Settings == "5":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        
        Guilds_Create_Role = input("\033[1;96m» \033[1;92m ID กิลด์ : \033[1;91m#")
        Settings_5 = int(input("\033[1;96m» \033[1;92m  จำนวน : \033[1;91m"))
        

        def Discord_Settings_5_Create_Role():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_Create_Role}/roles",headers={"authorization": token})

        for i in range(Settings_5):
                Discord_Settings_5_Create_Role()
                
                



#ALL
if Settings == "6":
        os.system("clear")
        Discord = pyfiglet.figlet_format("xNero")
        print(f"\033[1;91m{Discord}")
        print(f"\033[1;91m---------------------------------------------")
        
        Guilds_ALL = input("\033[1;96m» \033[1;92m ID กิลด์ : \033[1;91m#")
        Name_ALL = input("\033[1;96m» \033[1;92m ข้อความ : \033[1;91m")
        
        print(f"\033[1;91m---------------------------------------------")
        Settings_ALL = int(input("\033[1;96m» \033[1;92m  จำนวนการสร้างรวมทั้งหมด : \033[1;91m"))
        

        def Discord_Settings_ALL_1():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_ALL}/channels",headers={"authorization": token},json={"name":Name_ALL,"type":0})
        def Discord_Settings_ALL_2():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_ALL}/channels",headers={"authorization": token},json={"name":Name_ALL,"type":2})
        def Discord_Settings_ALL_3():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_ALL}/channels",headers={"authorization": token},json={"name":Name_ALL,"type":4})
        def Discord_Settings_ALL_4():
                requests.post(f"https://discord.com/api/v9/guilds/{Guilds_ALL}/roles",headers={"authorization": token})

        for i in range(Settings_ALL):
                Discord_Settings_ALL_1()
                Discord_Settings_ALL_2()
                Discord_Settings_ALL_3()
                Discord_Settings_ALL_4()
                
                
              



if Settings == "T" or Settings == "t":
        os.system("termux-open-url https://youtube.com/channel/UCJ4IYmknpJYFpdx1P1xogiA")

if Settings == "X" or Settings == "x":
        os.system("termux-open-url https://discord.gg/KvVGVv6QPW")

if Settings == "Y" or Settings == "y":
        os.system("clear")


if Settings == "0":
        os.system("clear")
        exit()

