from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')

if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

host = conn.getHostname()
print('Hostname: ' + host)

vcpus = conn.getMaxVcpus(None)
print('Maximum supported virtual CPUS: ' + str(vcpus))

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

id = domainsList[0].ID()

if (id == -1):
    print("Domain ain't running!")
else:
    print("Domain is running with id = " + str(id))

vmDom1 = conn.lookupByName("vm1")

print("OS Type of " + vmDom1.name() + " = " + vmDom1.OSType())

print(str(vmDom1.hasCurrentSnapshot()))

print("Has managed save image (vmDom1): " + str(vmDom1.hasManagedSaveImage()))

state, maxmem, mem, cpus, cput = vmDom1.info()

print("The state is (vmDom1) : " + str(state))
print("The max memory is (vmDom1) : " + str(maxmem))
print("The memory is : " + str(mem))
print("The number of CPUs is : " + str(cpus))
print("The CPU time is : " + str(cput))

conn.close()

exit(0)
