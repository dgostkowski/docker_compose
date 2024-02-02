# Installation steps:

## Backend
1. Verify the Python version; any version from 3.x should be suitable.
2. Run a Python virtual environment (venv) – optional but recommended.
3. Install the required pip packages listed in requirements.txt.
4. Create a user and a PostgreSQL database with names specified in the app.py file (check the `SQLALCHEMY_DATABASE_URI` variable). You can modify default values, but ensure you update them in the app.py file.
5. Grant the newly created user privileges to the database.
6. Run the backend using the command 'python (path to file)app.py'. (Note: Please replace `(path to file)` in the commands with the actual path to the file.) You should see similar output:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. 
Use a production WSGI server instead.
 * Running on http://10.0.0.1:8888
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 12-456-789
```
## Frontend
1. Install node.js from dnf.
2. Run `npm install`.
3. Run `npm start`. You should get similar output:
```
> frontend@1.0.0 start
> http-server -p 8080

Starting up http-server, serving ./
Available on:
  http://10.0.0.1:8080
  http://127.0.0.1:8080
Hit CTRL-C to stop the server
```
