class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


class Actor(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, role={self.role})"


class Director(Person):
    def __init__(self, name, age, genre):
        super().__init__(name, age)
        self.genre = genre

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, genre={self.genre})"


class Movie:
    def __init__(self, title, year, director, actors):
        self.title = title
        self.year = year
        self.director = director
        self.actors = actors

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title}, year={self.year}, director={self.director}, actors={self.actors})"


# Приклад використання класів
director = Director(name="Christopher Nolan", age=50, genre="Sci-Fi")
actor1 = Actor(name="Leonardo DiCaprio", age=45, role="Cobb")
actor2 = Actor(name="Joseph Gordon-Levitt", age=40, role="Arthur")

movie = Movie(title="Inception", year=2010, director=director, actors=[actor1, actor2])

print(movie)
