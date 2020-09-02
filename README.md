# mobile-metrics
Bootstrap for a CRUD backend system targeted at mobile apps metrics.

## Server

All backend logic is inside the `backend` folder. It has been developed using **Node JS 12 LTS** using **MS SQL** as default database (to comply with most of the corporates requirements). 

You can change the SQL configuration in [backend/app/config/db.config.js](backend/app/config/db.config.js).

### Development

1. Install SQL Server using Docker on Unix: https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-linux-2017&pivots=cs1-bash 

2. Create a `.env` file in the root of the repo with the local database settings:
    ```bash
    DB_HOST=localhost
    DB_USER=sa
    DB_PASS=YourStrong@Passw0rd1
    DB_PORT=1401
    SERVER_PORT=3000
    ```
3. Run the server locally with `npm run debug`

     To kill existing open instances of the server do:
    ```bash
    sudo lsof -i :3000
    kill -9 <PID>
    ```

    The project is structured to be easily debugged using VS Code with a preconfigured launch command

4. Test the APIs using this Postman collection:

    [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d0dbb85e24c41bbcfa42)