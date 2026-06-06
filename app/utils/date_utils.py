from datetime import date,timedelta

def get_start_date():

    return (
        date.today()
        -
        timedelta(days=10)
    ).isoformat()