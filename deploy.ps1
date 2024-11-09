
#Ensure venv is installed before creating and initating it
pip install venv

python -m venv .venv 
#Activate venv. This is used to keep packages separated and prevent contracticting version dependencies from applications
.venv\Scripts\Activate.ps1

#Ensure all external packages are downloaded
python -m pip install -r .\requirements.txt

fastapi dev .\CustomerCoreService\main.py #Set for dev while testing
