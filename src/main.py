import os
from pathlib import Path
from dotenv import load_dotenv

if __name__ == "__main__":
    env_path = Path('.') / '.env.development'
    load_dotenv(dotenv_path=env_path)
    print(os.getenv('SENDGRID_API_KEY'))