# Project1-restaurant_api
Getting started:
create github repo
create ssh key on your machine
ssh-keygen -t rsa
add ssh to github
clone your repo git clone ssh-link
created a virtualenv 
python3 -m virtualenv nameofenvironment
open the project in vscode
created a .gitignore file add virtualenv folder name add .env
created a requirements file to add dependencies for your project
activate environment: source nameofenvironment/bin/activate
we are going to install project dependencies using pip 
pip install nameofdependency
pip freeze > requirements.txt ==> copies whatever you installed to requirements file
note: pip install -r requirements.txt


Code describe:
This is a Python code that creates a web application using the Flask framework. The code creates a RESTful API for a restaurant menu with the following endpoints:
"/" returns a list of all restaurants with their details.
"/restaurant/int:restaurant_id/" returns the menu of a specific restaurant.
"/restaurant/int:restaurant_id/order" returns a form to place an order for a specific restaurant. This endpoint supports both GET and POST requests.
The code also uses the render_template method from the Flask library to render HTML templates for each endpoint. The restaurants and their menu data are stored in a list of dictionaries, with each restaurant having a unique ID, name, cuisine, and menu items.

First Page for the Restaurant List:
<img width="471" alt="截圖 2023-02-08 上午1 54 13" src="https://user-images.githubusercontent.com/70717089/217460035-9d9ea00d-2485-48a2-90ae-06c95eb84401.png">

Second Page for the Menu(by click the restaurant):
<img width="471" alt="截圖 2023-02-08 上午1 54 21" src="https://user-images.githubusercontent.com/70717089/217460090-67cb4163-43d3-44b0-835b-9480c2bc3367.png">


architectural diagram:
![IMG_40A4300EDDCF-1](https://user-images.githubusercontent.com/70717089/217460103-e049690b-e4bc-46b3-bad1-e59a25b7b2fd.jpeg)





