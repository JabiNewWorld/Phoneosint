import ctypes
from stat import FILE_ATTRIBUTE_ARCHIVE
import sys
from tabnanny import check
import phonenumbers
import phonenumbers.carrier
from phonenumbers import timezone
import time
from phonenumbers import geocoder
import os
from colorama import Fore

os.system("cls")

os.system("mode con: cols=100  lines=25")
ctypes.windll.kernel32.SetConsoleTitleW("PHONE OSINT | LA RECALLIE")

print(f"""
                  {Fore.GREEN}d ss.  d    d   sSSSs   d s  b d sss     sSSSs     sss. d d s  b sss sssss       
                  S    b S    S  S     S  S  S S S        S     S  d      S S  S S     S          
                  S    P S    S S       S S   SS S       S       S Y      S S   SS     S          
                  S sS'  S sSSS S       S S    S S sSSs  S       S   ss.  S S    S     S          
                  S      S    S S       S S    S S       S       S      b S S    S     S          
                  S      S    S S       S S    S  S       S       P S S    S     S     P     
                  P      P    P   "sss"   P    P P sSSss   "sss"   ` ss'  P P    P     P{Fore.RESET}

                           {Fore.RED}LA RCALLIE THE HACKING GROUP ACTIVE FOR EVERYTHING{Fore.RESET}
                                     SCRIPT CREADO POR BL4CKHATJ
                {Fore.RED}{Fore.RED}{Fore.RED}{Fore.RED}{Fore.RED}{Fore.RED}                                                                
                d      d s.        d ss.  d sss   d s.     sSSs. d s.   d      d      d d sss   
                S      S  ~O       S    b S       S  ~O   S      S  ~O  S      S      S S       
                S      S   `b      S    P S       S   `b S       S   `b S      S      S S       
                S      S sSSO      S sS'  S sSSs  S sSSO S       S sSSO S      S      S S sSSs  
                S      S    O      S   S  S       S    O S       S    O S      S      S S       
                s      S    O      S    S S       S    O  S      S    O S      S      S S       
                P sSSs P    P      P    P P sSSss P    P   "sss' P    P P sSSs P sSSs P P sSSss 
                {Fore.RED}{Fore.RED}{Fore.RED}{Fore.RED}"""+Fore.RESET)

number_object = None
number = input("CUAL ES EL TELEFONO A BUSCAR : ")
os.system("cls")
time.sleep(2)
print("=====================")
number=phonenumbers.parse(number, None)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}", number)
time.sleep(2)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}{Fore.GREEN} LA ZONE DE {number} ES {timezone.time_zones_for_number}"+Fore.RESET)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}",timezone.time_zones_for_number(number))
time.sleep(3)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}{Fore.RESET}FORMATOS DIFERENTES PARA{Fore.RESET}", number)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL))
time.sleep(1)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
time.sleep(1)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}",phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164))
time.sleep(1)
print(f"{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET}EL NUMERO DE TELEFONO", number,"PODRIA SER VALIDO?")
print(f"{Fore.GREEN}10%==={Fore.RESET}")
time.sleep(2)
print(f"{Fore.GREEN}30%==========={Fore.RESET}")
time.sleep(2)
print(f"{Fore.GREEN}50%===================={Fore.RESET}")
time.sleep(2)
print(f"{Fore.GREEN}70%======================================={Fore.RESET}")
time.sleep(2)
print(f"{Fore.GREEN}100%==================================================={Fore.RESET}")
time.sleep(2)
print(f"{Fore.GREEN}======LISTO====={Fore.RESET}")
print(phonenumbers.is_possible_number(number))

carrier = phonenumbers.carrier.name_for_number(number, "en")
print(carrier)

file = open("PhoneInfo.txt", "w")
file.write(f"\n{number}")
file.write(f"\nLA ZONE DE {number} ES {timezone.time_zones_for_number}")
file.write(f"\n====FORMATOS DE NUMERO====")
file.write(f"\n><><><><><><><><><><><><><>")
file.write(phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL))
file.write(f"\nFORMATO NACIONAL")
file.write(phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
file.write(f"\nFORMATO INTERNACIONAL")
file.write(phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164))
file.write(f"\nOTRO TIPO DE FORMATO")
file.write(f"\nEL NUMERO DE TELEFONO {number} PODRIA SER VALIDO?")
file.write(f'\nphonenumbers.is_possible_number{number}')


file.write("\n>=NUEVO INFORMACION DE NUMERO=<")

file.close()
