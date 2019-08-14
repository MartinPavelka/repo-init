import git
import os
import sys
import subprocess

from pathlib import Path
from github import Github

help = """	This script serves as a tool to quickly create and initialize a new git repository
	
	USAGE: repo [option] [arg]
	
	Options and arguments:
	-w arg	: create a work repository
	-p arg	: create a personal repository
	-h	: open help

	Argument:
	[arg]	: new repository name

	Example of use:
	repo -w bestappever
"""
path = "" # Your local projects directory
repo_name = ""
repo_type = ""
token= "" # Your github token
g = Github(token)
user = g.get_user()

def name_available():
	local_available = True
	git_available = True
	for folder in os.listdir(path):
		if repo_name in os.listdir(path+"/"+folder):
			local_available = False
	for repo in g.get_user().get_repos():
		if repo_name == repo.name:
			git_available = False
	return True if (local_available and git_available) else False

def create_readme():
	readme = open("README.md", 'a')
	readme.write("This is a repository for the project " + repo_name)
	readme.close()

def init_directory():
	repo_path = path+"/"+repo_type+"/"+repo_name
	os.makedirs(repo_path)
	os.chdir(repo_path)
	create_readme()
	r = git.Repo.init(os.getcwd())
	# TO DO: add readme, add remote origin, push -u origin master

def create_repo():
	if name_available():
		repo = user.create_repo(repo_name)
		print("The repo {} was created".format(repo_name))
		init_directory()
	else:
		print("The repository name is already taken")	

if __name__ == "__main__":
	# Handle unexpected parameters
	if "-h" in sys.argv or len(sys.argv) < 3 or len(sys.argv) > 3 or "-w" not in sys.argv or "-p" not in sys.argv: #How the hell do I shorten this
		print(help)
		exit()
	if "-w" == sys.argv[1]:
		repo_type = "Work"
		repo_name = sys.argv[2]
		create_repo()
	if "-p" == sys.argv[1]:
		repo_type = "Personal"
		repo_name = sys.argv[2]
		create_repo()
