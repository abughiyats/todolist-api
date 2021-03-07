# todolist-api

## _Developing TODO List Restful API using Python Flask and MySql_

### Installation

1. Clone this repository to your directory:

```
 git clone https://github.com/abughiyats/todolist-api.git
```

2. Install Libraries

```
pip install -r requirements.txt
```

3. Copy .env-example to .env
4. Start MySql Server
5. Run App

```
 flask run
```

6. Test API in Postman or Imsonia

### API List

- Register
  > [POST] `/register` Body request: name, email, password

- Login
  > [POST] `/login` Body request: email, password

- Logout
  > [DELETE] `/logout_access` Request Token

- Logout refresh
  > [DELETE] `/logout_refresh` Request Token

- Token refresh
  > [DELETE] `/token_refresh` Request Token

- Get List of Projects
  > [GET] `/projects` Request Token

- Create a Project
  > [POST] `/projects` Request Token, Body: name, description, due_date, user_id

- Get Project by Id
  > [GET] `/project/<id>` Request Token 

- Edit Project
  > [PUT] `/project/<id>` Request Token, Body: name, description, due_date, user_id

- Delete Project
  > [DELETE] `/project/<id>` Request Token

- Get List of Tasks
  > [GET] `/tasks` Request Token

- Create a Task
  > [POST] `/Tasks` Request Token, Body: name, description, due_date, project_id

- Get Task by Id
  > [GET] `/task/<id>` Request Token

- Edit Task
  > [PUT] `/task/<id>` Request Token, Body: name, description, due_date, project_id

- Delete Task
  > [DELETE] `/task/<id>` Request Token
