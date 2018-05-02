import os
import paramiko

class CNNsftp:
	def __init__(self, ip, user, password):
		self.ssh = paramiko.SSHClient()
		self.ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
		self.ssh.connect(ip, port=22, username=user, password=password)
		self.counter = 0

	def send(self,sourcepath,destpath):
		sftp = self.ssh.open_sftp()
		sftp.put(sourcepath,destpath)		
		sftp.close()

	def __del__(self):
		self.ssh.close()


if __name__ == '__main__':
	sftp = CNNsftp("192.168.43.183", "pi", "mowmow")
	sftp.send("/home/darthkrenth/PythonWorkspace/mowmowCNN/CNNsftp.py", "/home/pi/Desktop/MowMow/CNNsftp.py")
