from langchain.tools import tool
from datetime import date,datetime

@tool
def get_date(query:str):
    """
    Return information about today's date.

Accepted query values:

- date

- day

- month

- year
    """
    query = query.lower()
    d = date.today()
    if query == 'date':
        return d
    elif query == 'day':
        return d.day
    elif query == 'month':
        return d.month
    elif query == 'year':
        return d.year
    else:
        return f"Didn't Understand your query."

