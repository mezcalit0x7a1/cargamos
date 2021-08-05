import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

from config import app

if __name__ == '__main__':
    port = os.getenv("FLASK_RUN_PORT", 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
