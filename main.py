#IOMMU Installer for Arch Linux , Identicial Graphics Cards

import fileinput
import re
import sys
print("Enter intel or amd depending on your cpu make")
cpu = input("Please enter your cpu brand:")
file_name = 'grub' #this will be /etc/default/grub once deployed
if cpu == "amd":
    iommu_type = '"amd_iommu=on iommu=pt '
elif cpu == "intel":
    iommu_type = '"intel_iommu=on iommu=pt '

#Opens grub file, puts each line into an array
with open('grub') as grubfile:
    grubline = [i.strip() for i in grubfile]


#this is the line needing editing
print(grubline[5])
#looping through array
for y in grubline:
    #matching needed line with looped array
    x = re.search('^GRUB_CMDLINE_LINUX_DEFAULT=".*"', y)
    if x:
        #if syntax is correct then stored needed string in editedgrub
        print("Yes")
        #replace each '"' occurance in grubline array with iommu
        editedgrub = re.sub('"', iommu_type, y, 1)
        print(editedgrub)
        for line in fileinput.FileInput('grub', inplace=1):
            line=line.replace(y, editedgrub)
            print(line.strip())

        else:
            #if the syntax is not correct then
            print("No match")

