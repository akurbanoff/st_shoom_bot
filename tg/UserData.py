class UserData:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.booking_date = str()
        self.timeMin = str()
        self.timeMax = str()
        self.name = str()
        self.phone_number = str()

    def get_booking_date(self):
        return self.booking_date

    def set_booking_date(self, value):
        self.booking_date = value

    def get_timeMin(self):
        return self.timeMin

    def set_timeMin(self, value):
        self.timeMin = value

    def get_timeMax(self):
        return self.timeMax

    def set_timeMax(self, value):
        self.timeMax = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, value):
        self.phone_number = value