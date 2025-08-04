import paramiko
import time

host = "192.168.30.34"        
username = ""          
password = ""  

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, password=password)

cli = ssh.invoke_shell()
time.sleep(1)
cli.recv(1000)

def send_cmd(cmd, delay=0.3):
    cli.send(cmd + "\n")
    time.sleep(delay)
    output = cli.recv(5000).decode()
    print(output)
    return output

send_cmd("enable")
send_cmd("configure terminal")
send_cmd("interface port17")

while True:
    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 10")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 100")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed 1000")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")

    send_cmd("shutdown")
    send_cmd("speed auto")
    send_cmd("no shutdown")
