from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
DEBUG = os.environ.get('DEBUG')
TEST_TOKEN = os.environ.get('TEST_TOKEN')