# frame

Create a Ramdisk:

$ free to see amount of ram available, size accordingly

1/ create a folder to be the ramdisk
sudo mkdir /mnt/ramdisk

2/ use the mount command to create RAM disk

mount -t [TYPE] -o size=[SIZE] [FSTYPE] [MOUNTPOINT]

[TYPE] is type of RAM disk:
    ramfs: create an in memory file system using the same storage mechanism as Linux for caching file systems. ramfs cannot be limited in size and will continue using memory until the system runs out of RAM and crashes

    tmpfs : can specify a max size which will give a disk full error when limit is reached. It is also possible to check husage by using df -h /mnt/ramdisk
    
[SIZE] size to use for the file system. ramfs cannot be limited so that would be starting size

[FSTYPE] type of RAM disk to use: tmpfs, ramfs, ext4 etc

Example:
    mount -t tmpfs -o size=512m tmpfs /mnt/ramdisk

3/ add entry to /etc/fstab so ramdisk persits over reboots

vi /etc/fstab

tmpfs       /mnt/ramdisk tmpfs nodev,nosuid,noexec,nodiratime,size=512M 0 0