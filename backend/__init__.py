# __init__.py
import logging
from main import app

if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)
    
app.logger.setLevel(logging.INFO)
app.logger.info('VOTEGPT startup')