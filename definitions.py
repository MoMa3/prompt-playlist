from dotenv import load_dotenv
import os

# Load variables from the .env file into the environment
load_dotenv()

# Access the variables using os.getenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
