from mysql.connector import Error, connect
from PySide6.QtCore import QSettings, QCoreApplication
from threading import current_thread, Lock


class DB():
    """DB is a singleton for storing connection to DB"""
    _instance = None
    _mutex = Lock()
    is_valid = False
    status = ""

    def __new__(cls):
        with cls._mutex:
            if cls._instance is None:
                cls._instance = super(DB, cls).__new__(cls)
                cls._init_config()
                cls._init_connection()
        return cls._instance

    def _init_config(cls):
            settings = QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope,
                                 QCoreApplication.organizationName(),  QCoreApplication.applicationName())

            # add config
            @classmethod
            cls.config = {
                'host': settings.value("SQLServer/host", "localhost"),
                'port':  settings.value("SQLServer/port", "3306"),
                'user': settings.value("SQLServer/user", "root"),
                'password': settings.value("SQLServer/password", "toor"),
                'database': settings.value("SQLServer/database", "control")
                'pool_name': "db_pool",
                'pool_size': 6
            }
            @classmethod
            def _init_connection(cls):
                try:
                    conn = connect(**cls.config)
                    if conn.is_connected():
                    cls.status = "Connection established"
                    cls.is_valid = True
            except Error as e:
                cls.status = "Error: Can't connect to DB\n" + str(e)

    @classmethod
    def connection(cls):
         if cls.is_valid:
            return connect(**cls.config)
        else:
            raise ConnectionError("Database connection is not available.")

    @classmethod
    def close(cls):
        # Closing logic if needed, for individual connections or pool
        pass

    @classmethod
    def status(cls):
        return cls.status
