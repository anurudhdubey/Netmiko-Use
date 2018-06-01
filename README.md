# Netmiko-Use
Using Netmiko Library to access cisco devices to get the required output and also configure the device

Intial Requirement is to have Netmiko library installed
we will create a basic Python Program that will perform tasks as below  :
1) Function  get_devices_info() will read the file and get the device loopback details
2) Function connect() will connect the devices using ssh (ConnectHandler used from library Netmiko)
3) Function  device_output(net_connect) will provide the required output , here we have given command"sh ip int brief" .Command can be changed as per your requirement
4) Function evice_config_file(filename ) will config the devices as per the configuration present in specfic files stored as the <loopback0>.txt ,Here we are just configuring the device hostname.Further configuration lines can be add as per requirement.
5)Output will be displayed as below:

===========Router Loopback 1.1.1.1============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.0.1     YES NVRAM  up                    up
FastEthernet1/0        10.10.12.1      YES NVRAM  up                    up
FastEthernet2/0        10.10.13.1      YES NVRAM  up                    up
Loopback0              1.1.1.1         YES NVRAM  up                    up
['hostname Delhi\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#hostname Delhi
R1(config)#end
Delhi#

===========Router Loopback 2.2.2.2============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES NVRAM  administratively down down
FastEthernet1/0        10.10.12.2      YES NVRAM  up                    up
FastEthernet2/0        10.10.23.2      YES NVRAM  up                    up
Loopback0              2.2.2.2         YES NVRAM  up                    up
['hostname Bangalore\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#hostname Bangalore
R2(config)#end
Bangalore#

===========Router Loopback 3.3.3.3============================

Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        10.10.13.3      YES NVRAM  up                    up
FastEthernet1/0        unassigned      YES NVRAM  administratively down down
FastEthernet2/0        10.10.23.3      YES NVRAM  up                    up
Loopback0              3.3.3.3         YES NVRAM  up                    up
['hostname Mumbai\n']
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#hostname Mumbai
R3(config)#end
R3#
