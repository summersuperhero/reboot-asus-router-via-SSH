import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()

client.connect('192.168.1.1',
                port=1234, 
                username="asusadmin", 
                password="password_here",
                timeout=10
                )
client.exec_command('reboot')