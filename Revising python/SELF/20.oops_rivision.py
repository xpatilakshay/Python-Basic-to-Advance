class Movie:
    def __init__(self,title,genre,available_seats):
        self.title = title
        self.genre = genre
        self.available_seats = available_seats

    def book_ticket(self,no_of_seats):
        if no_of_seats > self.available_seats:
            print(f"Sorry! Seats not available you can book {self.available_seats} seats")
        else:
            print(f"Available seats are {self.available_seats}")
            print(f"Congratulations! {no_of_seats} Tickets Has been booked successfully!..")
            self.available_seats = self.available_seats - no_of_seats
            print(f"Now Available seats are {self.available_seats}")


movie = Movie("Chavaa","Historical",100)
no_of_seats = int(input("Enter the no of seats to be booked : "))
if no_of_seats >= 1:
    movie.book_ticket(no_of_seats)
else:
    print("Please Enter number grateer than or equals to 1")