

<h1 align="center">Test for Bluestorm selection process</h1>

# ✅ Project Description

Fastapi private REST API that aloes a financial sector to access information about  patients, pharmacies and transactions between those. 

# ✅ Features

- [x] Protected API, that requires JWT to make requests
- [x] Unit tests to check routes and token validation
- [x] Can be ran on containers

# ✅ How to run the app

You can run this API with docker, by using the command, this will create a local container with a connection to port 8000

```bash
  docker compose up
```

You can also run this app locally, you need python 3.10, and run the commands bellow: 

#### create a virtual environment:
```bash
  python -m venv venv
```

#### activate your virtual environment:
```bash
  activate venv/bin/activate
```

#### install requirements:
```bash
  pip install -r requirments.txt
```

#### run main file:
```bash
  uvicorn app.main:app --reload
```
# ✅ Routes

You can enter your localhost:8000/docs after running your app to check swagger generated API docs

## User routes

#### POST create user
```bash
  url/users
```
##### body
```bash
  {
		"username": "john"
		"password": "securepassword"
	}
```
#### POST login
```bash
  url/login
```
##### form data
```bash
  {
		"username": "john"
		"password": "securepassword"
	}
```
##### response body
```bash
{
  "access_token": "token string",
  "token_type": "bearer"
}
```

## Protected routes

### header with token:
```bash
{
  "Authorization": "Bearer tokenstring" 
}
```

## Patients

#### Get list of patients
```bash
  url/patients
```
#### filters
##### you can pass first_name and last_name as query strings to filter results
```bash
  url/patients?first_name=string&last_name=string
```

##### response body
```bash
[
  {
    "uuid": "PATIENT0001",
    "first_name": "JOANA",
    "last_name": "SILVA",
    "date_of_birth": "1996-10-25T00:00:00"
  }
]
```

## Pharmacies

#### Get list of pharmacies
```bash
  url/pharmacies
```

##### response body
```bash
[
	{
    "uuid": "PHARM0001",
    "name": "DROGA MAIS",
    "city": "RIBEIRAO PRETO"
	}
]
```

## Transactions

#### Get list of Transactions
```bash
  url/transactions
```

##### response body
```bash
[
	{
    "uuid": "TRAN0001",
    "patient_uuid": "PATIENT0045",
    "pharmacy_uuid": "PHARM0008",
    "amount": 3,
    "timestamp": "2020-02-05T07:49:03"
	}
]
```



# ✅ Project status

<h3 align="center">
    🚀 Concluded 🚀
</h3>

# 🖥️ Dev

- Made with ❤️ by [Lucas Gasque](https://www.linkedin.com/in/lucasgasque/