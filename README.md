# SALTIS ROAD ACCIDENT PREDICTION 
A ML study and app for solving road accident 

## DESCRIPTION
The main.py app is the api service that use the generated model file (.pkl) 
and produce the endpoint /api/predict prediction (A Rest API).
There is two models, the one generated using UK data and the other one simulated through building
a fake dataset
- model.ipynb: The study File to generate the model and analytics
- senfake.ipynb: The file to generate fake data through combining senegal road data and UK accidents data

## FOLDERS
- /datasets: UK data(Accidents.csv, Casualties.csv, Vehicles.csv), Senegal Road Data(senegal_highway.csv),
  fake data *generated(Accidents1.csv)
- /static: images

## INSTALLATION
You need python 3 to run the app:
- Create a virtual environment with python 3 (py -m virtualenv venv)
- Activate venv: Windows ($ venv\scripts\activate)
- Install Necessary Modules: ($ pip install -r requirements.txt)
- For the ipynb files use $ jupyter notebook
- Execute web server: py main.py 
  
  
