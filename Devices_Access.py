#!/usr/bin/python

#Import ConnectHandler from Netmiko library
from netmiko import ConnectHandler

#Function defined to read device file located on same path having loopback addresses of devices to be access
def get_devices_info():
    with open("devices.txt") as f:
        dev_out = f.readlines()
        return dev_out
        

#Function defined  to Connect to devices using ConnectHandler 
def connect(device_type,ip,username,password):
    R1_dic = {
            'device_type': device_type,
            'ip':ip,
            'username':username,
            'password':password,
            }
    net_connect = ConnectHandler(**R1_dic)
    return net_connect
    
    
# Function defined to get the "sh ip int brief" output from devices,can replace the command with any valid other command to get required output
def device_output(net_connect):
    out = net_connect.send_command("sh ip int brief")
    return out

#Function defined to open config file and implement config present in specfic filename saved as " device loopack.txt"
def device_config_file(filename ):
    with open ("{}".format(filename)) as f1:
        out2 =f1.readlines()
        print(out2)
        write_conf = net_connect.send_config_set(out2,delay_factor=2)
        return write_conf
        
 
#Main function
if __name__ == "__main__":
    dev_out = get_devices_info()
    for line in dev_out:
        line =line.strip("\n")
        net_connect= connect("cisco_ios",line,"cisco","cisco")
        output = device_output(net_connect)
        print("\n===========Router Loopback {}============================\n".format(line))
        print(output)
        write_conf = device_config_file("{}.txt".format(line))
        print(write_conf)
        output1 = device_output(net_connect)
        print(output1)

