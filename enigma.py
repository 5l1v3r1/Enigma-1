try:
	from colorama import init
	import os
	import time
	import sys
	from colorama import Back, Style, Fore
except ImportError as ie:
	print(ie)

init()
os.system("clear")
print(Style.BRIGHT + "")

print(Fore.BLUE + "___________              .__         .__  __            __________                    ")
print(Fore.CYAN + "\_   _____/__  _________ |  |   ____ |__|/  |_          \____    /____   ____   ____  ")
print(Fore.BLUE + " |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\  ______   /     //  _ \ /    \_/ __ \ ")
print(Fore.CYAN + " |        \>    < |  |_> >  |_(  <_> )  ||  |   /_____/  /     /(  <_> )   |  \  ___/ ")
print(Fore.RED + "/_______  /__/\_ \|   __/|____/\____/|__||__|           /_______ \____/|___|  /\___  >")
print(Fore.BLUE + "        \/      \/|__|                                          \/          \/     \/ ")

print(Fore.YELLOW + """
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 #				User It Responsibly				    #
 #				Made By Antoine Zayat				    #
 #                              Github: hacker900123				    #
 #    		I Hold No Responsibility For Any Damage Done By My Tool!	    #
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")



print(Fore.MAGENTA + """
				[1]  Ntp Server Scan
				[2]  Dns Server Scan
				[3]  Chargen Server Scan
				[4]  TS3 Server Scan
""")

try:
	scan = input(Fore.GREEN  + ">> [?] Enter Choice: ")
	if(len(scan) == 0):
		print("Invalid Choice!")
		sys.exit()
	else:
		if(scan == "1"):
			ips = input(Fore.BLUE + ">> [?] Enter Ip Start Range(eg: 1.0.0.0): ")
			ipe = input(Fore.BLUE + ">> [?] Enter Ip End Range(eg: 255.255.255.255): ")
			outfile = input(Fore.BLUE + ">> [?] Enter Outfile(in txt): ")
			threads = input(Fore.BLUE + ">> [?] Amount Of Threads(eg: 40): ")
			delay = input(Fore.BLUE + ">> [?] Delay In Ms(eg: 1): ")
			os.system("./ntpscan %s %s %s %s %s" % (ips, ipe, outfile, threads, delay))
		if(scan == "2"):
			startclass = input(Fore.BLUE + ">> [?] Start Class(eg: 1): ")
			endclass = input(Fore.BLUE + ">> [?] End Class(eg: 2): ")
			outfile = input(Fore.BLUE + ">> [?] Enter Outfile(in txt): ")
			threads = input(Fore.BLUE + ">> [?] Amount Of Threads(eg: 40): ")
			delay = input(Fore.BLUE + ">> [?] Delay In MS(eg: 1): ")
			os.system("./dnsscan %s %s %s %s %s" % (startclass, endclass, outfile, threads, delay))
		if(scan == "3"):
			startclassch = input(Fore.BLUE + ">> [?] Enter Ip Start Range(eg: 1.0.0.0): ")
			endclassch = input(Fore.BLUE + ">> [?] Enter Ip End Range(eg: 255.255.255.255): ")
			outfilech = input(Fore.BLUE + ">> [?] Enter Outfile(in txt): ")
			threadsch = input(Fore.BLUE + ">> [?] Amount Of Threads(eg: 40): ")
			delaych = input(Fore.BLUE + ">> [?] Delay In MS(eg: 1): ")
			os.system("./chargenscan %s %s %s %s %s" % (startclassch, endclassch, outfilech, threadsch, delaych))
		if(scan == "4"):
			startclassts3 = input(Fore.BLUE + ">> [?] Enter Ip Start Range(eg: 1.0.0.0): ")
			endclassts3 = input(Fore.BLUE + ">> [?] Enter Ip End Range(eg: 255.255.255.255): ")
			outfilets3 = input(Fore.BLUE + ">> [?] Enter Outfile(in txt): ")
			threadsts3 = input(Fore.BLUE + ">> [?] Amount Of Threads(eg: 40): ")
			delayts3 = input(Fore.BLUE + ">> [?] Delay In MS(eg: 1): ")
			os.system("./ts3scan %s %s %s %s %s" % (startclassts3, endclassts3, outfilets3, threadsts3, delayts3))

		else:
			print(Fore.RED + ">> [-] Invalid Option!")
			sys.exit()
except KeyboardInterrupt as ki:
	print(Fore.RED + ">> [!] Exiting.....")
	time.sleep(2)
	sys.exit()
