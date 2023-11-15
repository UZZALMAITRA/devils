import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/gsriyad11')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf devils_3nc')
except:
    pass
os.system('rm -rf devils_3nc')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m COMMAND OFF/COMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('devils_3nc'):
        os.system('curl -L https://github.com/UZZALMAITRA/devils/blob/main/devils_3nc.cpython-311.so?raw=true -o devils_3nc') 
        import devils_3nc  
    else:
        import devils_3nc
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
