import os
import time
import subprocess as sp

def color(n):
	os.system('tput setaf {}'.format(n))

os.system("clear")
color(3)
print("\n\t\t\t\t################  Task 7.1  ################")
print("\n")
color(2)
print("\n\t\t---------------------------------------------------------------------------")
print("\t\t\t\tWelcome To Logical Volume Management Menu !!")
print("\t\t---------------------------------------------------------------------------")
color(6)
while True:
    color(6)
    option = input('''\nChoose the below option listed below to perform specific action -
	Choose 1 - Display all available storage devices attached
	Choose 2 - Display information about Physical Volumes(PVs)
	Choose 3 - Display information about Volume Groups(VGs)
	Choose 4 - Display information about Logical Volumes(LVs)
	Choose 5 - Create Physical Volume(PV)
	Choose 6 - Create Volume Group(VG)
	Choose 7 - Create Logical Volume(LV)
	Choose 8 - Resize Logical Volume(LV)
	Choose 9 - Resize Volume Group(VG)
	Choose 10 - Remove Logical Volume(LV)
	Choose 11 - Remove Volume Group(VG)
	Choose 12 - Remove Physical Volume(PV)
	Choose 13 - Create file and display
	Choose 14 - Display file content''')

    if option>'9' or option<'1':
        color(1)
        print("Action Not Supported...!!!")
        color(6)
        exit()

    option = int(option)

    if option == 1:
        color(2)
        os.system("fdisk -l")
        color(6)
    
    elif option == 2:
        pv = input("Choose one particular Physical Volume [PV] (default all):")
        os.system("pvdisplay" + pv)
        color(6)

    elif option == 3:
        vg = input("Choose one particular Volume Groups [VG] (default all):")
        color(2)
        os.system("vgdisplay" + vg)
        color(6)

    elif option == 4:
        lv = input("Choose one particular Logical Volume [LV] (default all):")
        color(2)
        os.system("lvdisplay" + lv)
        color(6)

    elif option == 5:
        pv = input("Enter the storage device name you want to convert to Physical Volume [PV] :")
        color(4)
        os.system("pvcreate" + pv)
        color(2)
        print("Created PV...")
        color(6)

    elif option == 6:
        vg = input("Enter the name of  Volume Groups [VG] you want to create:")
        pv1 = input("Enter the name of Physical Volume [PV] 1 :")
        pv2 = input("Enter the value of Physical Volume [PV] 2 :")
        color(4)
        os.system("vgcreate" + vg +''+ pv1 +''+ pv2)
        color(2)
        print("created VG...")
        color(6)

    elif option == 7:
        lv = input("Enter the name of the Logical Volume [LV] that you want to create :")
        size = input("Enter the size of Logical Volume [LV] :")
        vg = input("Enter the name of Volume Group [VG] where you want to create the Logical volume [LV] :")
        path = input("Enter the path to the folder where you want to mount the Logical volume [LV] created :")
        color(4)
        os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
        os.system('mkfs.ext4 /dev/{}/{}'.format(size,lv,vg))
        os.system("mkdir {}".format(path))
        os.system("mount /dev/{}/{} {}".format(vg,lv,path))
        os.system('lvcreate --size {} --name {} {}'.format(size,lv,vg))
        color(2)
        print("Created LV !!! Ready to store files...Mounted in Folder {}".format(path))
        color(6)

    elif option == 8:
        choice = input("Enter the choice(R/E) :- \n 1.Reduce(R) The LV\n 2.Extend(E) the LV ")
        vg = input("Enter the name of the Volume Group [VG] in which the Logical Volume [LV] is created :")
        lv = input("Enter the name of the Logical Volume [LV] that you want to resize :")
        if choice == 'R':
            size1 = input("Enter the size you want to change the  LV side :")
            size2 = input("Enter the final desired size of the LV :")
            path = input("Enter the path of the folder in which LV is mounted :")
            a="reduce"
            b="-"
            os.system('umount /dev/{}/{}'.format(vg,lv))
            os.system("e2fsck -f /dev/{}/{}".format(vg,lv))
            os.system("resize2fs /dev/{}/{} {}".format(vg,lv,size2))
            os.system("lv{} --size {}{} /dev/{}/{}".format(a,b,size1,vg,lv))
            os.system("mount /dev/{}/{} {}".format(vg,lv,path))
        else:
            a="extend"
            b="-"
            size = input("Enter the size by which you want to excedd the LV Size :")
            os.system("lv{} --size {}{} /dev/{}/{}".format(a,b,size,vg,lv))
            os.system("resize2fs /dev/{}/{}".format(vg,lv))
        color(2)
        print("Logical Volume Resized !!!")
        color(6)

    elif option == 9:
        choice = input("Enter the choice(R/E) :- \n 1.Reduce(R) The VG\n 2.Extend(E) the VG ")
        vg = input("Enter the name of the Volume Group [VG] that you want to resize :")
        if choice == 'R':
            pv = input('Enter name of the PV you want to remove from VG: ')
            os.system("pvmove {}".format(pv))
            os.system("vgreduce {} {}".format(vg,pv))
        else:
            pv = input('Enter name of the PV you want to add to VG: ')
            os.system("vgextend {} {}".format(vg,pv))
        color(2)
        print("Volume Group Resized !!!")
        color(6)

    elif option == 10:
        path = input("Enter path to Logical Volume [LV] that you want to remove :")
        color(2)
        os.system("unmount {}".format(path))
        os.system("lvremove {}".format(path))
        color(6)
    
    elif option == 11:
        vg = input("Enter the name of Volume Group [VG] you want to remove :")
        color(2)
        os.system("vgremove {}".format(vg))
        color(6)

    elif option == 12:
        path = input("Enter the Physical Volume [PV] you want to remove :")
        color(2)
        os.system("pvremove {}".format(path))
        color(6)

    elif option == 13:
        path = input("Enter the path to the folder :")
        file = input("Enter the File Name :")
        color(4)
        os.system("cat > {}/{}".format(path,file))
        color(2)
        print("\n File Created...")
        os.system("cat {}/{}".format(path,file))
        color(6)

    elif option == 14:
        path = input("Enter the Path To the folder :")
        file = input("Enetr The File Name :")
        color(2)
        os.system("cat {}/{}".format(path,file))
        print()
        color(6)


    else:
        color(1)
        print("Wrong Choice !!!")
        color(6)
        break
    input("Press Enter To Continue...")