from datetime import datetime


def inject_year_preproc():
    return {'now': datetime.utcnow()}
