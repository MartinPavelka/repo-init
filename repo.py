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
path = "YOUR_LOCAL_PROJECTS_REPOSITORY" # Your local projects directory
repo_name = ""
repo_type = ""
token= "YOUR_GITHUB_TOKEN" # Your github token
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
	subprocess.Popen('explorer "%s"' %os.path.normpath(repo_path))
	git_push(os.getcwd())
	# assert not empty_repo.delete_remote(origin).exists()
	# TO DO: add readme, add remote origin, push -u origin master

def git_push(cwd):
	r = git.Repo.init(cwd, 'empty')
	new_file_path = os.path.join(r.working_tree_dir, 'README.md')
	r.index.add([new_file_path])                        # add it to the index
	# Commit the changes to deviate masters history
	r.index.commit("Added a new file in the past - for later merege")
	origin = r.create_remote('origin', "Your_GITHUB_Address"+ repo_name +".git")
	assert origin.exists()
	assert origin == r.remotes.origin == r.remotes['origin']
	origin.fetch()
	r.git.push('--set-upstream', 'origin', 'master')
	origin.push()

def create_repo():
	if name_available():
		repo = user.create_repo(repo_name) #create github repository
		print("The repo {} was created".format(repo_name))
		init_directory()
	else:
		print("The repository name is already taken")	

if __name__ == "__main__":
	# Handle unexpected parameters
	if "-h" == sys.argv[1] or len(sys.argv) < 3 or len(sys.argv) > 3:
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
