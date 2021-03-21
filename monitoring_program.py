from __future__ import print_function
import sys
import libvirt
import time

# Getting a connection to the hypervisor
connToHypervisor = libvirt.open('qemu:///system')

if connToHypervisor == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

domainName = 'vm1'

dom = conn.lookupByName(domainName)

if dom == None:
    print("Failed to get the domain object", file=sys.stderr)

print(dom)

domainIDList = conn.listDomainsID()

if (domainIDList == None):
    print("Failed to get a list of domain IDs", file=sys.stderr)
print("\nActive domain IDs:")


if (len(domainIDList) == 0):
    print("None")
else:
    for domainID in domainIDList:
        print(" " + str(domainID))

domainNamesList = conn.listDefinedDomains()

print("\nAll domain names:")

if (len(domainNamesList) == 0):
    print("None")
else:
    for domainName in domainNamesList:
        print(domainName)

domainsList = conn.listAllDomains(0)

print(domainsList)

id = domainsList[1].ID()

if (id == -1):
    print("Domain ain't running!")
else:
    print("Domain is running with id = " + str(id))

vmDom1 = conn.lookupByName("vm1")

print("OS Type of " + vmDom1.name() + " = " + vmDom1.OSType())

# Obtaining the CPU time for vm1
cpuStats1 = vmDom1.getCPUStats(True)

print('CPU time (vm1) : ' + str(cpuStats1[0]['cpu_time']))
print('System time (vm1) : ' + str(cpuStats1[0]['system_time']))
print('User time (vm1) : ' + str(cpuStats1[0]['user_time']))

time.sleep(0.1)

cpuStats2 = vmDom1.getCPUStats(True)

cpuUsage = (100*(cpuStats2[0]['cpu_time'] - cpuStats1[0]['cpu_time']))/(10 ** 8)

print('CPU Usage : ' + str(cpuUsage))

conn.close()

exit(0)
