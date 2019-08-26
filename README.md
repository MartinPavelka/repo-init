# repo-init
This script serves as a tool to quickly create and initialize a new git repository.

## How to use
install requirements:

	pip install -r requirements.txt
change values:

	path	= "YOUR_LOCAL_PROJECTS_REPOSITORY" # Your local projects directory
	token	= "YOUR_GITHUB_TOKEN" # Your github token
	origin	= r.create_remote('origin', "Your_GITHUB_Address"+ repo_name +".git")
run script:
	
	python repo [option] [name]
### Recommendation

#### Windows users
Associate the correct file group with .py scripts:

	assoc .py=Python.File
Redirect all Python files to the new executable:

	ftype Python.File=C:\Path\to\python.exe "%1" %*
Add script location to Windows environment variables

	Search **Advanced system settings** > **Environment Variables** > **System Variables** > **PATH (edit)** > **Add** > C:\Path\to\script\ > OK

## USAGE: 
	repo [option] [arg]
	
## Options and arguments:
	-w arg	: create a work repository
	-p arg	: create a personal repository
	-h		: open help

## Argument:
	[arg]	: new repository name

## Example of use:
	repo -w bestappever
