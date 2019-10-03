from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import contextlib
class DBSession(object):
    ''' Creating thread safe and managed sessions using SQLAlchemy. 
        The sessions that are created are expected to be:
        - thread safe
        - handle committing
        - handle rolling back on errors
        - handle session removal/releasing once context or thread is closed.

        so every thread will use this object to do this step:
        1. connect to the engine
        2. create a "scoped session"
        3. use this session
        4. close the session before terminate the thread
    '''
    def __init__(self, uri, **kwargs):
        self.engine = create_engine(uri, **kwargs)
        self.session_factory = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=self.engine,expire_on_commit=False))

    @contextlib.contextmanager
    def ManagedSession(self):
        """Get a session object whose lifecycle, commits and flush are managed for you.

        Expected to be used as follows:
        ```
        with ManagedSession() as session:            # multiple db_operations are done within one session.
            db_operations.select(session, **kwargs)  # db_operations is expected not to worry about session handling.
            db_operations.insert(session, **kwargs)  # after the with statement, the session commits to the database.
        ```
        """
        session = self.session_factory()
        try:
            yield session
            session.commit()
            session.flush()
        except Exception:
            session.rollback()
            # When an exception occurs, handle session session cleaning,
            # but raise the Exception afterwards so that user can handle it.
            raise
        finally:
            # source: https://stackoverflow.com/questions/21078696/why-is-my-scoped-session-raising-an-attributeerror-session-object-has-no-attr
            self.session_factory.remove()