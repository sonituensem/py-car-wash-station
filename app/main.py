from typing import List


class Car:
<<<<<<< HEAD
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
=======
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
>>>>>>> 7816b8b (Fixed flake8 issues)
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
<<<<<<< HEAD
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
=======
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
>>>>>>> 7816b8b (Fixed flake8 issues)
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
<<<<<<< HEAD
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
=======
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
>>>>>>> 7816b8b (Fixed flake8 issues)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

<<<<<<< HEAD
    def rate_service(self, new_rating: int) -> None:
=======
    def rate_service(self, new_rating: float) -> None:
>>>>>>> 7816b8b (Fixed flake8 issues)
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
