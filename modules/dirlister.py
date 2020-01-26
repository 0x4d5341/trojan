import os 

def run(**args):
	print("[*] In DirLister module.")
	files = os.listdir(".")

	return str(files)