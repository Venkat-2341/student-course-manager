import os
import uvicorn
from art import tprint
from dotenv import load_dotenv

if __name__ == "__main__":
    try:
        tprint("Courses-Manager")
        load_dotenv()
        
        host = os.environ["UVICORN_HOST"]
        port = int(os.environ["UVICORN_PORT"])
        
        app = "college.api:app"
        
        uvicorn.run(app, host=host, port=port)
        
    except Exception as error:
        print(f"Error ocurred, Details : {error}")
        
        raise