from mysql.connector import Error, connect
from PySide6.QtCore import QSettings, QCoreApplication
from threading import current_thread, Lock


class DB():
    """DB is a singleton for storing connection to DB"""
    _connections = {}
    _pool_size = 6
    _instance = None
    _mutex = Lock()
    is_valid = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)

            settings = QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope,
                                 QCoreApplication.organizationName(),  QCoreApplication.applicationName())

            # add config
            cls.config = {
                'host': settings.value("SQLServer/host", "localhost"),
                'port':  settings.value("SQLServer/port", "3306"),
                'user': settings.value("SQLServer/user", "root"),
                'password': settings.value("SQLServer/password", "toor"),
                'database': settings.value("SQLServer/database", "control")
            }

            try:
                conn = cls.connection()

                if conn.is_connected():
                    cls.status = "Connection established"
                    cls.is_valid = True

            except Error as e:
                cls.status = "Error: Can't connect to DB\n" + repr(e)
        return cls._instance

    @classmethod
    def is_available(cls):
        return len(cls._connections) < cls._pool_size

    @classmethod
    def close(cls):
        with cls._mutex:
            for key in cls._connections:
                if cls.is_valid and cls._connections[key].is_connected():
                    cls._connections[key].close()
                    print(key, " MySQL connection is closed")

    @classmethod
    def close_current(cls):
        with cls._mutex:
            if cls.is_valid and cls._connections[current_thread()].is_connected():
                cls._connections[current_thread()].close()
                del cls._connections[current_thread()]
                print(current_thread(), " finished the job. MySQL connection has been released.")

    @classmethod
    def connection(cls):
        with cls._mutex:
            if current_thread() not in cls._connections:
                cls._connections[current_thread()] = connect(pool_name="pool", pool_size=cls._pool_size, **cls.config)
            return cls._connections[current_thread()]
