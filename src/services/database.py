import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise AssertionError("DATABASE_URL is not defined")

engine = create_engine(DATABASE_URL)

session_factory = sessionmaker(bind=engine)

logger = logging.getLogger()


# Override all the session methods to add some security (like rollback on error)
# NOTE: don't instantiate this class, use `session` instance below instead
class DatabaseSession:
    def __init__(self):
        self._session = scoped_session(session_factory)

        self._session.begin()

    def merge(self, instance):
        return self._session.merge(instance)

    def add(self, instance):
        return self._session.add(instance)

    def execute(self, query):
        return self._session.execute(query)

    def query(self, query):
        return self._session.query(query)

    # Rollback if commit fails
    def commit(self):
        try:
            self._session.commit()
        except Exception as e:
            logger.error(e)
            self._session.rollback()


session = DatabaseSession()
