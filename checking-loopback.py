from netmiko import ConnectHandler
import getpass
import  re

user_name = input('username: ')
passwd = getpass.getpass('Please enter the password: ')

routers = [
    {
        "host": "100.100.0.1",
        "hostname": 'Abuja-core',
    },{
        "host": '100.100.0.4',
        "hostname": "Kano-Core",
    },{
        "host": '100.100.0.9',
        "hostname": 'Lagos-Core',
    },{
        "host": '100.100.0.5',
        "hostname": 'PH-Core',
    },{
        "host": '100.100.0.10',
        "hostname": 'PE-10',
    },{
        "host": '100.100.0.3',
        "hostname": 'PE-3',
    },{
        "host": '100.100.0.12',
        "hostname": 'PE-12',
    },{
        "host": '100.100.0.7',
        "hostname": 'PE-7',
    },{
        "host": '100.100.0.20',
        "hostname": 'PE-20',
    },{
        "host": '100.100.0.11',
        "hostname": 'PE-11',
    },{
        "host": '100.100.0.8',
        "hostname": 'PE-8',
    }
]

for router in routers:
    device = {
        "device_type": "cisco_ios",
        "username": user_name,
        "password": passwd,
        "secret": passwd,
        "host": router['host'],
        
    }
    connection = ConnectHandler(**device)
    connection.enable()
    print(f'logging in to {router["hostname"]}')
    output = connection.send_command('show interface desc')
    print(output)
    config_commands = ['interface lo0', 'descri WAN', 'ip address 1.1.1.1 255.255.255.255', 'exit']
    if re.search('Lo0', output):
        print('loopback0 exist')
    else:
        print("Configuring loopback")
        connection.send_config_set(config_commands)
        connection.send_config_set('end')
        output = connection.send_command('show interface desc')
        print(output)

connection.disconnect()
