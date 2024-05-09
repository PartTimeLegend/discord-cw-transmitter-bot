from radio_controller import RadioController


class RadioControllerFactory:
    @staticmethod
    def create_radio_controller():
        return RadioController()