from typing import Callable
from contextlib import contextmanager, AbstractContextManager

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config.settings import settings
from core.logger import init_logger


logger = init_logger(__name__)

Base = declarative_base()


class Database:
    def __init__(self) -> None:
        self._engine = create_engine(settings.db.database_url, echo=False)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception as ex:
            logger.exception(ex)
            session.rollback()
            raise
        finally:
            session.close()
