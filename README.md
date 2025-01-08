# iris-FastAPI
Deploying ML Model as API using FastAPI

1. **Installing FastAPI**:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Creating basic API using FastAPI.** <br/>
Refer to basic-app.py file

3. **Testing API**:
   ```bash
   uvicorn basic-app:app --reload
   ```
Run the above command and go to http://127.0.0.1:8000/

4. **Deploying the ML Model.** <br/>
    Go to http://127.0.0.1:8000/docs for running the ML model for prediction using FastAPI user interface.
