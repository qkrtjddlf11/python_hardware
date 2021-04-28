import time
import os
import sys
import socket
# import psutil # pip install psutil
import platform
import datetime
import subprocess

class Ibat():
    # Get Serial Number
    def getSerial_Num(self):
        popen = subprocess.Popen("dmidecode -t system | grep Manufac | awk -F ':' '{print $2}' | awk -F ' ' '{print $1}'",
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdOutData = popen.communicate()

        if stdOutData == 'eSlim' or stdOutData == 'eslim':
            popen = subprocess.Popen("dmidecode -t system | grep -i serial | awk -F ':' '{print $2}'",
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdOutData = popen.communicate()
            data = stdOutData[0].strip()

            print('Serial Number : %s' % data.decode('ascii'))

        else:
            popen = subprocess.Popen("dmidecode -t baseboard | grep -i serial | awk -F ':' '{print $2}'",
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdOutData = popen.communicate()
            data = stdOutData[0].strip()

            print('Serial Number : %s' % data.decode('ascii'))

    # Get Hostnmae
    def getHostname(self):
        hostname = socket.gethostname()

        print('Hostname : %s' % hostname.strip())

    # Get OS Version
    def getOS_Version(self):
        ps = platform.system()

        if ps == 'Linux':
            popen = subprocess.Popen("cat /etc/redhat-release", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdOutData = popen.communicate()
            data = stdOutData[0].strip()

            if data == '':
                popen = subprocess.Popen("pveversion | awk -F '/' '{print $2}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                stdOutData = popen.communicate()
                data = stdOutData[0].strip()
            print('OS Version : %s' % data.decode('ascii'))

        elif ps == 'FreeBSD':
            pass

    # Get IP Address Info
    def getIP_Address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ipaddress = s.getsockname()[0]
        except Exception:
                ipaddress = '127.0.0.1'

        print('IP Address : %s' % ipaddress.strip())

    # Get CPU Info
    def getCPU_Info(self):
        popen = subprocess.Popen("dmidecode | grep -i intel | grep -i version | awk -F ':' '{print $2}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdOutData = popen.communicate()
        data = stdOutData[0].strip().replace('\t', '')

        print('CPU Info : ')
        print('%s' % data.decode('ascii'))

    # Get RAM Info
    def getMem_Info(self):
        popen = subprocess.Popen("dmidecode -t 17 | egrep 'Manufac|Size|Speed' | egrep -vi 'Unknown|No|Configured'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdOutData = popen.communicate()
        data = stdOutData[0].strip().replace('\t', '')

        print('Mem Info : ')
        print('%s' % data.decode('ascii'))

    # Get HDD Info

    # Get NIC Info
    def getNIC_Info(self):
        popen = subprocess.Popen("lspci | grep -i ethernet | awk -F ':' '{print $3}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdOutData = popen.communicate()
        data = stdOutData[0].strip()

        print('NIC Info : ')
        print('%s' % data.decode('ascii'))

    # Get Raid Card Info
    def getRaid_Info(self):
        popen = subprocess.Popen("lspci | grep LSI | awk -F ':' '{print $3}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdOutData = popen.communicate()
        data = stdOutData[0].strip()

        print('Raid Info : ')
        print(data.decode('ascii'))

def main():
    ibat = Ibat()

    ibat.getSerial_Num()

    ibat.getHostname()

    ibat.getOS_Version()

    ibat.getIP_Address()

    ibat.getCPU_Info()

    ibat.getNIC_Info()

    ibat.getRaid_Info()

    ibat.getMem_Info()

if __name__ == '__main__':
    main()

