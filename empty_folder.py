import os
folder = '/home/ubuntu/github_files/'
for each_file in os.listdir(folder):
	file_path = os.path.join(folder, each_file)
	if os.path.isfile(file_path):
		os.unlink(file_path)