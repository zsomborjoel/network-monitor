import paramiko
from .logs import add_to_log

def connect(host, port, username, password):
    """
    :param host: hostname
    :param port: port number
    :param username: login user
    :param password: user's password
    :return: ssh connection
    """

    add_to_log("In connect")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    add_to_log("Ssh was successful")
    return ssh

def run_command(ssh, command):
    """
    :param ssh: ssh connection
    :param command: linux command
    :return: stdout of linux command
    """

    add_to_log("In run command")
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.readlines()
