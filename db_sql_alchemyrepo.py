from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    name = Column(String(350), nullable=False)
    year_of_production = Column(Integer(), nullable=True)


def db_init():
    db_engine = create_engine('sqlite:///db_movies.db')
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    movies_list = [
        'Gospodar prstenova',
        'Hobit',
        'Batman',
        'Matrix',
        'Sam u kuci',
        'Druzba Pere Kvrzice'
    ]
    for movie in movies_list:
        movie_entry = (
            session.query(Movie)
            .filter(Movie.name == movie)
            .one_or_none()
        )

        if movie_entry is None:
            movie_entry = Movie(
                name = movie,
                year_of_production = 2001
            )
            session.add(movie_entry)

    session.commit()


def get_all_data():
    db_engine = create_engine('sqlite:///db_movies.db')

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    return session.query(Movie).all()


def get_data(id: int):
    db_engine = create_engine('sqlite:///db_movies.db')

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    movie_from_db = (session.query(Movie)
                    .filter(Movie.id == id)
                    .one_or_none())

    return movie_from_db