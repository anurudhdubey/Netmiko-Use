# Netmiko-Use
Using Netmiko Library to access cisco devices to get the required output and also configure the device

Intial Requirement is to have Netmiko library installed
we will create a basic Python Program that will perform tasks as below  :
1) Function  get_devices_info() will read the file and get the device loopback details
2) Function connect() will connect the devices using ssh (ConnectHandler used from library Netmiko)
3) Function  device_output(net_connect) will provide the required output , here we have given command"sh ip int brief" .Command can be changed as per your requirement
4) Function evice_config_file(filename ) will config the devices as per the configuration present in specfic files stored as the <loopback0>.txt ,Here we are just configuring then ew loopback 10 and assigning Ip address .Further configuration lines can be add as per requirement.
5)Output will be displayed as below:

root@NetworkAutomation-1:~# python  devices3.py

===========Router Loopback 1.1.1.1============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.0.1     YES NVRAM  up                    up
FastEthernet1/0        10.10.12.1      YES NVRAM  up                    up
FastEthernet2/0        10.10.13.1      YES NVRAM  up                    up
Loopback0              1.1.1.1         YES NVRAM  up                    up
Loopback10             unassigned      YES unset  up                    up
['interface lo10\n', 'ip address 10.10.10.10 255.255.255.255\n', 'exit\n', '\n', '\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
Delhi(config)#interface lo10
Delhi(config-if)#ip address 10.10.10.10 255.255.255.255
Delhi(config-if)#exit
Delhi(config)#
Delhi(config)#
Delhi(config)#end
Delhi#
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.0.1     YES NVRAM  up                    up
FastEthernet1/0        10.10.12.1      YES NVRAM  up                    up
FastEthernet2/0        10.10.13.1      YES NVRAM  up                    up
Loopback0              1.1.1.1         YES NVRAM  up                    up
Loopback10             10.10.10.10     YES manual up                    up

===========Router Loopback 2.2.2.2============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES NVRAM  administratively down down
FastEthernet1/0        10.10.12.2      YES NVRAM  up                    up
FastEthernet2/0        10.10.23.2      YES NVRAM  up                    up
Loopback0              2.2.2.2         YES NVRAM  up                    up
['interface lo10\n', 'ip address 20.20.20.20 255.255.255.255\n', 'exit\n', '\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
Bangalore(config)#interface lo10
Bangalore(config-if)#ip address 20.20.20.20 255.255.255.255
Bangalore(config-if)#exit
Bangalore(config)#
Bangalore(config)#end
Bangalore#
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES NVRAM  administratively down down
FastEthernet1/0        10.10.12.2      YES NVRAM  up                    up
FastEthernet2/0        10.10.23.2      YES NVRAM  up                    up
Loopback0              2.2.2.2         YES NVRAM  up                    up
Loopback10             20.20.20.20     YES manual up                    up

===========Router Loopback 3.3.3.3============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        10.10.13.3      YES NVRAM  up                    up
FastEthernet1/0        unassigned      YES NVRAM  administratively down down
FastEthernet2/0        10.10.23.3      YES NVRAM  up                    up
Loopback0              3.3.3.3         YES NVRAM  up                    up
['interface loopback10\n', 'ip address 30.30.30.30 255.255.255.255\n', 'exit\n', '\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#interface loopback10
R3(config-if)#ip address 30.30.30.30 255.255.255.255
R3(config-if)#exit
R3(config)#
R3(config)#end
R3#
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        10.10.13.3      YES NVRAM  up                    up
FastEthernet1/0        unassigned      YES NVRAM  administratively down down
FastEthernet2/0        10.10.23.3      YES NVRAM  up                    up
Loopback0              3.3.3.3         YES NVRAM  up                    up
Loopback10             30.30.30.30     YES manual up                    up
root@NetworkAutomation-1:~#
root@NetworkAutomation-1:~#
root@NetworkAutomation-1:~#

