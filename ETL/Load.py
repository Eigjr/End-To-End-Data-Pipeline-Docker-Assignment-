import os
import psycopg2
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine as ce
from clean_and_transform import movies, items, users_data


load_dotenv()

# Load environment variables from .env file
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

#connecting to postgres using sqlalchemy
def create_engine():
    try:
        engine = ce(
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
        print("Engine created successfully.")
        return engine
    except Exception as e:
        print(f"Error creating engine: {e}")
        return None

movies.to_sql("movies", con=create_engine(), if_exists="replace", index=False)
items.to_sql("items", con=create_engine(), if_exists="replace", index=False)
users_data.to_sql("users_data", con=create_engine(), if_exists="replace", index=False)

#close the connection
def close_connection(engine):
    try:
        if engine:
            engine.dispose()
            print("Connection closed successfully.")
    except Exception as e:
        print(f"Error closing connection: {e}")
