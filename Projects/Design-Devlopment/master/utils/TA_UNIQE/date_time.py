from datetime import datetime

class CurrentDateTime:

    current_date = datetime.now()

    def __init__(self):
        self.month = CurrentDateTime.current_date.strftime('%m')
        self.year = CurrentDateTime.current_date.strftime('%y')

CURRENT_DATETIME = CurrentDateTime()
print(CURRENT_DATETIME.month)
