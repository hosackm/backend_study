from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class MenuItem(Base):
    __tablename__ = "menu_item"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "course": self.course,
        }

if __name__ == "__main__":
    engine = create_engine("sqlite:///restaurantmenu.db")
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    [session.add(Restaurant(name=n)) for n in ("Montella Pizzeria",
                                               "Alma",
                                               "Fruitlandia",
                                               "El Farolito",
                                               "La Taqueria")]
    session.commit()
