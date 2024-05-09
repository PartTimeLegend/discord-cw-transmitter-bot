from database_manager import DatabaseManager


class DatabaseManagerFactory:
    @staticmethod
    def create_database_manager(config):
        return DatabaseManager(config)

