
########### IF RUNNING IN VS CODE, it may prompt you about the venv and 
#a workspace folder for it. You can select 'Yes'. 


#Ensure venv is installed before creating and initating it
pip install venv

python -m venv .venv 
#Activate venv. This is used to keep packages separated and prevent contracticting version dependencies from applications
.venv\Scripts\Activate.ps1

#Ensure all external packages are downloaded
python -m pip install -r .\requirements.txt

#Run set up
python "CustomerCoreService\Installation\setup.py"


fastapi dev CustomerCoreService\main.py #Set for dev while testing
