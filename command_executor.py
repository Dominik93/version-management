from subprocess import Popen, PIPE


def run(command):
	process = Popen(command, stdout=PIPE, shell=True)
	while True:
		line = process.stdout.readline().rstrip()
		if process.poll() is not None:
			break
		yield line
