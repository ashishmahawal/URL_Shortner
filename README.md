### URL Shortening Service

#### Dependencies
 - Postgres SQL
    ```
    brew install postgresql
    brew services start postgresql

    1. CREATE ROLE testUser WITH LOGIN PASSWORD 'password';

    2. ALTER ROLE testUser CREATEDB;

    Now login again to db with testuser    

    3. CREATE DATABASE url;

    4. Now type this to select DB ---> \c url

    5. CREATE TABLE url_mapping (
    id BIGINT PRIMARY KEY,
    short_url VARCHAR(255) NOT NULL,
    long_url VARCHAR(1024) NOT NULL
    );
    ```

### How to run application on local ?
#### Backend
```
cd backend
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt

uvicorn --reload app:app
```

Backend will be accessible at http://localhost:8000

OpenAPI docs at http://localhost:8000/docs

#### Frontend

```
cd frontend
npm run dev
```
App will be accessible at http://localhost:3000

### Frontend will look like this...

![alt text](docs/frontend.png)