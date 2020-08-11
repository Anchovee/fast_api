#fastapi.tiangolo.com ##docs https://www.youtube.com/watch?v=q8jaJ4Y3H7E
from fastapi import fastapi

app = FastAPI()

#home route
@app.get("/") #"/" url route
def dashboard():
	return {"Dashboard": "Homepage"}

#runs with "uvicor main:app --reload" ##main is main.py and app=FastAPI
@app.post("/stock") 
def create_stock():
	return{
		"code": "success"
		"message": "stock created" #PTLarry uses 'insomnia' client (command line utility --- 'curl ')
	}