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


class User:
    """User is a singleton class for storing all user information securely."""
    _instance = None
    is_valid = False

    def __new__(cls):
        """Create or return the singleton instance of User."""
        if cls._instance is None:
            cls._instance = super(User, cls).__new__(cls)
        return cls._instance

    @classmethod
    def login(cls, login: str, password: str) -> bool:
        """Attempt to log in a user with given credentials."""
        try:
            with DB.connection().cursor(prepared=True) as cursor:
                query = """
                    SELECT id, login, last_name, first_name, middle_name, department, position, access, level, shift
                    FROM user
                    WHERE login = %s AND password = %s AND deleted IS NULL
                """
                cursor.execute(query, (login, password))
                record = cursor.fetchone()

                if record:
                    cls.is_valid = True
                    for index, (column_name, *_) in enumerate(cursor.description):
                        setattr(cls, column_name, record[index] if record[index] is not None else "")
                    return True
                return False
        except Exception as e:
            print(f"Failed to log in: {e}")  # Consider logging instead of printing
            return False

    @classmethod
    def full_name(cls) -> str:
        """Return the full name of the user."""
        return f"{cls.last_name} {cls.first_name} {cls.middle_name}"

    @classmethod
    def short_name(cls) -> str:
        """Return the abbreviated name of the user."""
        return f"{cls.last_name} {cls.first_name[0]}. {cls.middle_name[0]}."

    @classmethod
    def access(cls, action: Access) -> bool:
        """Check if user has the required access rights."""
        return bool(Access(cls.access) & action)

    @classmethod
    def set_new_password(cls) -> bool:
        """Method stub for setting a new password."""
        # Add password update logic here
        return NotImplemented

    @classmethod
    def set_new_info(cls) -> bool:
        """Method stub for updating user information."""
        # Add info update logic here
        return NotImplemented
