from enum import Flag, auto, unique
from .db import DB


@unique
class Access(Flag):
    ADD = auto()
    FIX = auto()
    CONFIRM = auto()
    EDIT = auto()
    _RESERVED4 = auto()
    _RESERVED5 = auto()
    _RESERVED6 = auto()
    ADMIN = auto()


class User():
    """User is a singleton for storing all information about user"""
    _instance = None
    is_valid = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(User, cls).__new__(cls)
        return cls._instance

    @classmethod
    def login(cls, login: str, pasword: str) -> bool:
        cursor = DB.connection().cursor(prepared=True)
        query = """
                SELECT id, login, last_name, first_name, middle_name, department, position, access, level, shift 
                FROM user
                WHERE (login = %s and password = %s AND deleted IS NULL)
                """
        params = (login, pasword)

        cursor.execute(query, params)
        record = cursor.fetchone()
        description = cursor.description
        cursor.close()

        if record:
            cls.is_valid = True
            for index, column_info in enumerate(description):
                setattr(cls, column_info[0], record[index] if record[index] is not None else "")

        return bool(record)

    @classmethod
    def full_name(cls) -> str:
        return cls.last_name + " " + cls.first_name + " " + cls.middle_name

    @classmethod
    def short_name(cls) -> str:
        return cls.last_name + " " + cls.first_name[0] + ". " + cls.middle_name[0] + "."

    @classmethod
    def access(cls, action: Access) -> bool:
        return bool(Access(cls._access) & action)

    @classmethod
    def set_new_password(cls) -> bool:
        Ellipsis

    @classmethod
    def set_new_info(cls) -> bool:
        Ellipsis
