from datetime import date

from Service.Model.Batteries.Battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, current_date: date, last_service_date: date):
        self._last_service_date: date = last_service_date
        self._current_date: date = current_date

    def needs_service(self) -> bool:
        number_of_year_to_service: date.year = 2
        return self._current_date.year - self._last_service_date.year >= number_of_year_to_service

