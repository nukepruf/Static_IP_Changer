import subprocess
import time

# Type ipconfig in cmd to determine your ethernet adapters name.

# Function takes user input and sets the SiteName variable
print("Please refer to the Systems spread sheet for site names")
SiteName = input("Which site are you at? or type DHCP --> ").lower()  # lower function removes capitalization from input
# Series of if and elif conditionals to sort through user input.
if SiteName == 'Site 1':
    print(SiteName.capitalize(), ", okay great! Setting your static IP address to 192.168.1.2")
    staticIP = '''netsh interface ip set address name="Ethernet 3" static 192.168.1.3 255.255.255.0 192.168.1.1'''
    command1 = staticIP.split()
    subprocess.run(command1)
elif SiteName == 'Site 2':
    print(SiteName.capitalize(), ", okay great! Setting your static IP address to 192.168.1.3")
    staticIP = '''netsh interface ip set address name="Ethernet 3" static 10.65.72.5 255.255.255.0 192.168.1.1'''
    command1 = staticIP.split()
    subprocess.run(command1)
elif SiteName == 'Site 3':
    print(SiteName.capitalize(), ", okay great! Setting your static IP address to 192.168.1.4")
    staticIP = '''netsh interface ip set address name="Ethernet 3" static 10.5.189.5 255.255.255.0 192.168.1.1'''
    command1 = staticIP.split()
    subprocess.run(command1)
elif SiteName == 'new':
    print(SiteName.capitalize(), ", okay great! Setting your static IP address to 192.168.42.5")
    staticIP = '''netsh interface ip set address name="Ethernet 3" static 192.168.42.5 255.255.255.0 192.168.42.1'''
    command1 = staticIP.split()
    subprocess.run(command1)

elif SiteName == 'help':  # Provides help information
    print("It seems like you don't know what you're doing. Type the name of the site you are trying to access.")
    print("Type 'DHCP' to enable... well hopefully you know what this does.")
    print("Type 'new' if you are trying to access a new new server to configure.")
elif SiteName == 'dhcp':  # Sets network adapter back to dhcp mode
    print("Okay! accessing the mainframe now...")
    time.sleep(3)
    print("We're in! That was easy! Setting IP address back to DHCP mode.")
    dhcpCommand = '''netsh interface ip set address "Ethernet 3" dhcp'''
    command = dhcpCommand.split()
    subprocess.run(command)
else:  # handles any other inputs that are not in the elif statements
    print("Hmm I didn't find that one... ")
    time.sleep(1.5)
    print("Typing can be difficult sometimes, are you sure you spelled that right?")
    time.sleep(1.5)
    print("Try it again, you can do it!")
    time.sleep(1)
    print("If you are trying to set your network adapter back to DHCP, type DHCP!")

input("Press enter to exit ;)")
