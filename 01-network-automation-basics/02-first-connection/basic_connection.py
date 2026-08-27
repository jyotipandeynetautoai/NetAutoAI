from netmiko import ConnectHandler


device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",
    "username": "admin",
    "password": "your_password",
}


connection = ConnectHandler(**device)

output = connection.send_command("show version")

print(output)

connection.disconnect()