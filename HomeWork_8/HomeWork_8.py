from datetime import datetime, timedelta

users = [
    {"name": "Barbi", "birthday": "1990-07-15"},
    {"name": "Ken", "birthday": "1987-07-30"},
    {"name": "Bob", "birthday": "1995-08-02"},
    {"name": "Rob", "birthday": "1995-08-01"},
    {"name": "Dmutro", "birthday":"1997-07-31"},
    {"name": "Stef", "birthday":"1997-07-28"},
    {"name": "Keyt", "birthday":"1997-08-03"},
  ]

list_birthday ={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[],'Next Monday':[]}

def create_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def get_birthdays_per_week(users):
    
    current_datetime = datetime.now()
    now_weekday = current_datetime.weekday()
    future_datetime = current_datetime + timedelta(days=7)
    day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}

    for i in users:
        data_birthday = create_datetime(i.get('birthday'))
        data_birthday_this_year = datetime(year=current_datetime.year, month=data_birthday.month, day=data_birthday.day)
        
        if current_datetime.date() <= data_birthday_this_year.date() < future_datetime.date():
            day_name = day_map.get(data_birthday_this_year.weekday(), 'Monday')
            if data_birthday_this_year.weekday() >= 5 and now_weekday == 0:
                day_name = 'Next Monday'
            list_birthday[day_name].append(i.get('name'))           
    
    print_our_list(list_birthday,now_weekday)  


def print_our_list(list_birthday,now_weekday):
    if now_weekday not in (0,5,6):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Next Monday']
        list_birthday = {k: list_birthday[k] for k in days[now_weekday:] + days[:now_weekday]}
    for day, users in list_birthday.items():
        if users:
            print(f"{day:11}:{','.join(users)}")
    


get_birthdays_per_week(users)