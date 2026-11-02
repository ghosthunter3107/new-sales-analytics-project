import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IS_SERVERLESS = bool(
    os.getenv('VERCEL') or
    os.getenv('AWS_LAMBDA_FUNCTION_NAME') or
    not os.access(BASE_DIR, os.W_OK)
)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sales-analysis-secret-key-2026')
    
    # Check for connection URL first (standard on Vercel / Cloud providers)
    db_url = os.getenv('DATABASE_URL') or os.getenv('MYSQL_URL')
    if db_url and (db_url.startswith('mysql://') or db_url.startswith('mysql+pymysql://')):
        parsed = urlparse(db_url)
        DB_HOST = parsed.hostname or 'localhost'
        DB_PORT = parsed.port or 3306
        DB_USER = parsed.username or 'root'
        DB_PASSWORD = parsed.password or ''
        DB_NAME = parsed.path.lstrip('/') or 'sales_db'
        DB_TYPE = os.getenv('DB_TYPE', 'mysql')
    else:
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = int(os.getenv('DB_PORT', 3306))
        DB_USER = os.getenv('DB_USER', 'root')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_NAME = os.getenv('DB_NAME', 'sales_db')
        # Force DB Type: 'mysql' or 'sqlite' or 'auto' (tries MySQL, falls back to SQLite)
        DB_TYPE = os.getenv('DB_TYPE', 'auto')

    # Optional SSL support for Cloud MySQL providers
    DB_SSL = os.getenv('DB_SSL', 'false').lower() in ('true', '1', 'yes')

    # Uploads (serverless environments use /tmp for write access)
    if IS_SERVERLESS:
        UPLOAD_FOLDER = os.path.join('/tmp', 'uploads')
    else:
        UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max
