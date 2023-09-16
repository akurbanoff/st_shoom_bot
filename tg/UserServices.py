class UserServices:
    def __init__(self, telegram_id):
        self.telegram_id = telegram_id
        self.main_service = str()
        self.optional_services = list()


    def get_telegram_id(self):
        return self.telegram_id

    def get_main_service(self):
        return self.main_service


    def set_main_service(self, service: str):
        self.main_service = service

    def get_optional_service(self):
        return self.optional_services

    def add_optional_services(self, service):
        self.optional_services.append(service)

    def get_list_of_chosen_items(self, all: bool):
        if all:
            return self.main_service + ', '.join(str(elem) for elem in self.optional_services)
        elif not all:
          return ', '.join(str(elem) for elem in self.optional_services)