class Concert:
    AVAILABLE_GENRES = ["Metal", "Rock", "Jazz"]

    def __init__(self, genre, audience, ticket_price, expenses, place):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in Concert.AVAILABLE_GENRES:
            raise ValueError("Our group doesn't play {genre}!")

        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        if value < 1:
            raise ValueError("At least one person should attend the concert!")

        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")

        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0.00:
            raise ValueError("Expenses cannot be a negative number!")

        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if value.strip() == "" or len(value) < 2:
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")

        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
