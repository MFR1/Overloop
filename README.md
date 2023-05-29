# Django Tech Test Backend

## Running with Docker

- A sample Dockerfile and a docker-compose is provided to run the application in an isolated environment
- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build and run the container: `docker-compose up`
- Start making some requests: `curl http://localhost:8000/articles/`

## Running with a virtual environment

- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment for 3.9.6
- Check you have the pyenv version you need: `pyenv versions`
- You should see 3.9.6
- If you do not have the correct version of Python, install it like this: `pyenv install 3.9.6`
- On command line do this: `~/.pyenv/versions/3.9.6/bin/python -m venv env`
- This creates a folder called env. Then do this to activate the virtual environment: `source env/bin/activate`
- Lastly do this to check that you are now on the correct Python version: `python --version`
- You can install the dependencies with `pip install -r requirements.txt`
- You should run `python setup_and_seed.py` to get a local database setup and seeded with lookup data
- You can then run the app with `python manage.py runserver 0.0.0.0:8000` in the root directory

## Project Structure Notes

- There are two django apps installed `articles` and `regions`
- Django is used as a RESTful API, no html rendering is required
- Marshmallow is used to serialize and deserialize django object instances

## Postman Outputs
### API Collection
![image](https://github.com/MFR1/Overloop/assets/37844263/fe612bc6-756a-44ba-b1a4-4f9f14b7f3f5)

### Get all entities
For Articles:
![image](https://github.com/MFR1/Overloop/assets/37844263/40a5a07b-6686-49f8-9354-344a4c7efd0d)

For Authors:
![image](https://github.com/MFR1/Overloop/assets/37844263/818d82c6-86e1-4383-bd7e-65d29c7635b0)

For Regions:
![image](https://github.com/MFR1/Overloop/assets/37844263/949c6acc-0677-4aab-947f-d229b1f60afc)

## Create a single entity
For Articles:
![image](https://github.com/MFR1/Overloop/assets/37844263/a2c9f50e-9935-40e1-8efe-050fd92203a2)

For Authors:
![image](https://github.com/MFR1/Overloop/assets/37844263/2fcd2282-5543-4e01-ba5c-bf58c3e9f106)

For Regions:
![image](https://github.com/MFR1/Overloop/assets/37844263/67be2370-7b3b-490b-ab8c-b2019d92c2e0)

## Get a single entity
For Articles:
![image](https://github.com/MFR1/Overloop/assets/37844263/c5446629-8046-4487-9caf-fbd0868192ff)

For Authors:
![image](https://github.com/MFR1/Overloop/assets/37844263/ccd443f3-f30b-4fa4-a727-b80ecef385e1)

For Regions:
![image](https://github.com/MFR1/Overloop/assets/37844263/71590070-4aba-4f0e-8aaf-82bc946e009f)

## Update a single entity
For Articles:
![image](https://github.com/MFR1/Overloop/assets/37844263/8a5e4833-8331-432e-a499-4d427d0239b2)

For Authors:
![image](https://github.com/MFR1/Overloop/assets/37844263/264f51b6-1f22-4228-86c8-a19f3f5e58c0)

For Regions:
![image](https://github.com/MFR1/Overloop/assets/37844263/33176582-bc23-4137-a4ff-56fee5e56783)

## Delete a single entity
For Articles:
![image](https://github.com/MFR1/Overloop/assets/37844263/fada18fa-4157-4129-a11a-9f5d6da4f160)

For Authors:
![image](https://github.com/MFR1/Overloop/assets/37844263/8451b85c-4dd0-4e2f-a5f3-99b7a35a655b)

For Regions:
![image](https://github.com/MFR1/Overloop/assets/37844263/c2223a33-5938-42f9-8e90-2163e7524012)




