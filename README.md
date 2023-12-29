### URL Shortening Service

#### Dependencies
 - Postgres SQL
    ```
    brew install postgresql

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

### Frontend will look like this...

![alt text](docs/frontend.png)