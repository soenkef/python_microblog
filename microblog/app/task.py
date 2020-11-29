from app import create_app

app = create_app()
app.app_context().push()

import time
from rq import get_current_job

