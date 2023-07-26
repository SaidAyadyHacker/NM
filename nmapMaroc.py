from optparse import *
import socket
import random
sit = random.choice([
'''
    )                         
 ( /(                         
 )\())    )       )           
((_)\    (     ( /(  `  )     
 _((_)   )\  ' )(_)) /(/(     
| \| | _((_)) ((_)_ ((_)_\    
| .` || '  \()/ _` || '_ \)   
|_|\_||_|_|_| \__,_|| .__/    
   *                |_|       
 (  `                         
 )\))(      )  (              
((_)()\  ( /(  )(    (    (   
(_()((_) )(_))(()\   )\   )\  
|  \/  |((_)_  ((_) ((_) ((_) 
| |\/| |/ _` || '_|/ _ \/ _|  
|_|  |_|\__,_||_|  \___/\__|    
''','''

  _   _      __  __      _       ____          
 | \ |"|   U|' \/ '|uU  /"\  u U|  _"\ u       
<|  \| |>  \| |\/| |/ \/ _ \/  \| |_) |/       
U| |\  |u   | |  | |  / ___ \   |  __/         
 |_| \_|    |_|  |_| /_/   \_\  |_|            
 ||   \\,-.<<,-,,-.   \\    >>  ||>>_          
 (_")  (_/  (./  \.) (__)  (__)(__)__)         
  __  __      _       ____    U  ___ u   ____  
U|' \/ '|uU  /"\  uU |  _"\ u  \/"_ \/U /"___| 
\| |\/| |/ \/ _ \/  \| |_) |/  | | | |\| | u   
 | |  | |  / ___ \   |  _ <.-,_| |_| | | |/__  
 |_|  |_| /_/   \_\  |_| \_\\_)-\___/   \____| 
<<,-,,-.   \\    >>  //   \\_    \\    _// \\  
 (./  \.) (__)  (__)(__)  (__)  (__)  (__)(__) 

 ''','''
.-. .-..-.   .-.  .--.  .----.         
|  `| ||  `.'  | / {} \ | {}  }        
| |\  || |\ /| |/  /\  \| .--'         
`-' `-'`-' ` `-'`-'  `-'`-'            
.-.   .-.  .--.  .----.  .----.  .---. 
|  `.'  | / {} \ | {}  }/  {}  \/  ___}
| |\ /| |/  /\  \| .-. \       /\     }
`-' ` `-'`-'  `-'`-' `-' `----'  `---' 
''','''
,--.  ,--.                              
|  ,'.|  |,--,--,--. ,--,--. ,---.      
|  |' '  ||        |' ,-.  || .-. |     
|  | `   ||  |  |  |\ '-'  || '-' '     
`--'  `--'`--`--`--' `--`--'|  |-'      
,--.   ,--.                 `--'        
|   `.'   | ,--,--.,--.--. ,---.  ,---. 
|  |'.'|  |' ,-.  ||  .--'| .-. || .--' 
|  |   |  |\ '-'  ||  |   ' '-' '\ `--. 
`--'   `--' `--`--'`--'    `---'  `---' 
''','''
 ███▄    █  ███▄ ▄███▓ ▄▄▄       ██▓███         
 ██ ▀█   █ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒       
▓██  ▀█ ██▒▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒       
▓██▒  ▐▌██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒       
▒██░   ▓██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░       
░ ▒░   ▒ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░       
░ ░░   ░ ▒░░  ░      ░  ▒   ▒▒ ░░▒ ░            
   ░   ░ ░ ░      ░     ░   ▒   ░░              
         ░        ░         ░  ░                
                                                
 ███▄ ▄███▓ ▄▄▄       ██▀███   ▒█████   ▄████▄  
▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▒██▒  ██▒▒██▀ ▀█  
▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░  ██▒▒▓█    ▄ 
▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██   ██░▒▓▓▄ ▄██▒
▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒░ ████▓▒░▒ ▓███▀ ░
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ░▒ ▒  ░
░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░   ░  ▒   
░      ░     ░   ▒     ░░   ░ ░ ░ ░ ▒  ░        
       ░         ░  ░   ░         ░ ░  ░ ░      
                                       ░   
''','''
 _____                 
|   | |_____ ___ ___   
| | | |     | .'| . |  
|_|___|_|_|_|__,|  _|  
                |_|    
                       
 _____                 
|     |___ ___ ___ ___ 
| | | | .'|  _| . |  _|
|_|_|_|__,|_| |___|___|
''','''
 _   _                       
| \ | |                      
|  \| |_ __ ___   __ _ _ __  
| . ` | '_ ` _ \ / _` | '_ \ 
| |\  | | | | | | (_| | |_) |
\_| \_/_| |_| |_|\__,_| .__/ 
                      | |    
                      |_|    
___  ___                     
|  \/  |                     
| .  . | __ _ _ __ ___   ___ 
| |\/| |/ _` | '__/ _ \ / __|
| |  | | (_| | | | (_) | (__ 
\_|  |_/\__,_|_|  \___/ \___|
''','''
 _  _  __  __    __    ____       
( \( )(  \/  )  /__\  (  _ \      
 )  (  )    (  /(__)\  )___/      
(_)\_)(_/\/\_)(__)(__)(__)        
 __  __    __    ____  _____  ___ 
(  \/  )  /__\  (  _ \(  _  )/ __)
 )    (  /(__)\  )   / )(_)(( (__ 
(_/\/\_)(__)(__)(_)\_)(_____)\___)
''','''
  _  _                    
 | \| |_ __  __ _ _ __    
 | .` | '  \/ _` | '_ \   
 |_|\_|_|_|_\__,_| .__/   
 |  \/  |__ _ _ _|_|_  __ 
 | |\/| / _` | '_/ _ \/ _|
 |_|  |_\__,_|_| \___/\__|
 ''','''
 __ _  _  _   __   ____       
(  ( \( \/ ) / _\ (  _ \      
/    // \/ \/    \ ) __/      
\_)__)\_)(_/\_/\_/(__)        
 _  _   __   ____   __    ___ 
( \/ ) / _\ (  _ \ /  \  / __)
/ \/ \/    \ )   /(  O )( (__ 
\_)(_/\_/\_/(__\_) \__/  \___)
 '''])



print(sit)
import time
time.sleep(3)
parser = OptionParser(f'''

 -h , --help    : To help you 
 -i , --ip      : Enter The IP Address You Want To Scan 
 =====> EX      : nmapMaroc.py -i 127.0.0.1 
 -p , --port    : If You Want To Scan Specific PORTS Only
 =====> EX      : nmapMaroc.py -i 127.0.0.1 -p 12,20,80,443 
 -s , --save    : Enter The Fiel Path To Save The Scan Results
 =====> EX      : nmapMaroc.py -i 127.0.0.1 -s /home/kali/desktop/testScane.txt
 -d , --devices : To Scan Devices Operating On The Network
 =====> EX      : nmapMaroc.py -d 127.0.0.0/24 < To Scan All IP Addresses Within a network >
 		nmapMaroc.py -d 127.0.0.0/1,12,32,22 < TO Specify The endings Of The IP addresses you want To Scan >
''')
group  = OptionGroup(parser,"other options",'''the other options''')
group.add_option('-s','--save',dest='save',type='string')
group.add_option('-d','--devices',dest='Devices',type='string')
parser.add_option_group(group)
parser.add_option('-i','--ip',dest='ip',type='string')
parser.add_option('-p','--port',dest='port',type='string')
(options,args) = parser.parse_args()
ip = options.ip
port = options.port 
file = options.save
strm = options.Devices
def DefMome(ip,port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	sock.settimeout(2)
	result = sock.connect_ex((ip , port))
	if result == 0:
			try:
				m = socket.getservbyport(port)
				print(f"{port}/TCP   OPEN  {m}")
			except OSError as e:
				print(f"{port}/TCP   OPEN  ????")
	else:
			pass
	sock.close()
def scaneAllPort():
	i = 1
	print('PORT     STATE  SERVICE')
	while True:
		DefMome(ip=ip,port=i)
		i = i+1
		if i == 1000:
			break
		else:
			pass
def scanePrtCm():
	k = port.split(',')
	print('PORT     STATE  SERVICE')
	for i in k:
	    i = int(i)
	    DefMome(ip,i)
def scanAllPortAndSave():
	op = open(file,'w')
	op.write(f'command : nmapMaroc.py -i {ip} ')
	op.write('\nscane by nmapMaroc ')
	op.write(f'\n -IP : {ip} \n')
	op.write('==============================> \n')
	op.write('PORT     STATE  SERVICE')
	print('PORT     STATE  SERVICE')
	i = 1
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		result = sock.connect_ex((ip, i))
		if result == 0:
			try:
				m = socket.getservbyport(i)
				print(f"{i}/TCP   OPEN  {m}")
				op.write(f"\n{i}/TCP   OPEN  {m}")
			except OSError as e:
				print(f"{i}/TCP   OPEN  ????")
				op.write(f"\n{i}/TCP   OPEN  ????")
		else:
			pass
		i = i+1 
		if i == 1000:
			break
		sock.close()
	op.close()
def scanCemPortAndSave():
	k = port.split(',')
	op = open(file,'w')
	op.write(f'command : nmapMaroc.py -i {ip} -p {port} ')
	op.write('\nscane by nmapMaroc ')
	op.write(f'\n -IP : {ip} \n')
	op.write(f' -PORT : {k} \n')
	op.write('==============================> \n')
	op.write('PORT     STATE  SERVICE')
	print('PORT     STATE  SERVICE')
	for i in k:
	    i = int(i)
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    sock.settimeout(2)
	    result = sock.connect_ex((ip, i))
	    if result == 0:
	    	try:
	    		m = socket.getservbyport(i)
	    		print(f"{i}/TCP   OPEN  {m}")
	    		op.write(f"\n{i}/TCP   OPEN  {m}")
	    	except OSError as e:
	    		print(f"{i}/TCP   OPEN  ????")
	    		op.write(f"\n{i}/TCP   OPEN  ????")
	    else:
	    	pass
	    sock.close()
	op.close()
def scanSipifyIp():
	portt = int(input('[+] Enter PORT For Scan : '))
	def ds(ip):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		try:
			result = sock.connect_ex((f'{ip}', portt))
			print(f"- Devices Operating In Your Network : {ip}")
		except socket.gaierror as e:
			pass
	#24 == 255
	ip = strm
	newIP = ip.split('/')[0]
	k = ip.split('/')[-1]
	if k == '24':
		ppp = 0
		while True:
			d = newIP.split('.')
			ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{ppp}')
			ppp = ppp + 1
			if ppp == 255:
				ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{ppp}')
				break
	else:
		pory = k.split('-')
		fo = pory[0]
		to = pory[1]
		while True:
			d = newIP.split('.')
			ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{fo}')
			fo = int(fo)
			fo = fo + 1
			to = int(to)
			if fo == to:
				fo = str(fo)
				ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{fo}')
				break
			else:
				fo = str(fo)
				pass
def scanSipifyIpAndSave():
	portt = int(input('[+] Enter PORT For Scan : '))
	op = open(file,'w')
	op.write(f'command : nmapMaroc.py -d {strm} ')
	op.write('\nscane by nmapMaroc ')
	op.write(f'\n -IP : {strm}')
	op.write(f'\n -PORT : {portt} \n')
	op.write('==============================> \n')
	def ds(ip):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		try:
			result = sock.connect_ex((f'{ip}', portt))
			print(f"- Devices Operating In Your Network : {ip}")
			op.write(f"- Devices Operating In Your Network : {ip}\n")
		except socket.gaierror as e:
			pass
	#24 == 255
	ip = strm
	newIP = ip.split('/')[0]
	k = ip.split('/')[-1]
	if k == '24':
		ppp = 0
		while True:
			d = newIP.split('.')
			ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{ppp}')
			ppp = ppp + 1
			if ppp == 255:
				ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{ppp}')
				break
	else:
		pory = k.split('-')
		fo = pory[0]
		to = pory[1]
		while True:
			d = newIP.split('.')
			ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{fo}')
			fo = int(fo)
			fo = fo + 1
			to = int(to)
			if fo == to:
				fo = str(fo)
				ds(ip=f'{d[0]}.{d[1]}.{d[2]}.{fo}')
				break
			else:
				fo = str(fo)
				pass
if ip != None and port == None and file == None and strm == None:
	scaneAllPort()
elif ip != None and port != None and file == None and strm == None:
	scanePrtCm()
elif ip != None and port == None and file != None and strm == None:
	scanAllPortAndSave()
elif ip != None and port != None and file != None and strm == None:
	scanCemPortAndSave()
elif ip == None and port == None and file == None and strm != None:
	scanSipifyIp()
elif ip == None and port == None and file != None and strm != None:
	scanSipifyIpAndSave()
else:
	print('''
 -h , --help    : To help you 
 -i , --ip      : Enter The IP Address You Want To Scan 
 =====> EX      : nmapMaroc.py -i 127.0.0.1 
 -p , --port    : If You Want To Scan Specific PORTS Only
 =====> EX      : nmapMaroc.py -i 127.0.0.1 -p 12,20,80,443 
 -s , --save    : Enter The Fiel Path To Save The Scan Results
 =====> EX      : nmapMaroc.py -i 127.0.0.1 -s /home/kali/desktop/testScane.txt
 -d , --devices : To Scan Devices Operating On The Network
 =====> EX      : nmapMaroc.py -d 127.0.0.0/24 < To Scan All IP Addresses Within a network >
 		nmapMaroc.py -d 127.0.0.0/1,12,32,22 < TO Specify The endings Of The IP addresses you want To Scan >
''')