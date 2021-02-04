#IOMMU Installer for Arch Linux , Identicial Graphics Cards

import fileinput
import re
import sys
print("Enter intel or amd depending on your cpu make")
cpu = input("Please enter your cpu brand:")
file_name = 'grub' #this will be /etc/default/grub once deployed
if cpu == "amd":
    iommu_type = "amd_iommu=on iommu=pt "
elif cpu == "intel":
    iommu_type = "intel_iommu=on iommu=pt "

#Opens grub file, puts each line into an array
with open('grub') as grubfile:
    grubline = [i.strip() for i in grubfile]


#this is the line needing editing
print(grubline[5])

#matching line to make sure the syntax is correct
x = re.search('^GRUB_CMDLINE_LINUX_DEFAULT=".*"', grubline[5])
if x:
    #if syntax is correct then
    print("Yes")
    #replace each '"' occurance in grubline array with iommu
    editgrubbuff = re.sub('"', iommu_type, grubline[5], 1)
    print(editgrubbuff)
else:
    #if the syntax is not correct then
    print("No match")

