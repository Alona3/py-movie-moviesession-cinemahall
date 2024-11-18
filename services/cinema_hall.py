from django.db import models

from db.models import CinemaHall


def get_cinema_halls() -> models.QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(name: str, rows: int, seats_in_row: int) -> CinemaHall:
    return CinemaHall.objects.create(
        name=name,
        rows=rows,
        seats_in_row=seats_in_row
    )
