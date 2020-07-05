import logging

logging.basicConfig(level=logging.DEBUG)
calc_type=int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie : "))
first_value=int(input("Podaj składnik 1: "))
second_value=int(input("Podaj składnik 2: "))


if calc_type == 1:
    logging.info(f"Dodaję {first_value} i {second_value}")
    logging.info(f"Wynik to {first_value + second_value}")
if calc_type == 2:
    logging.info(f"Odejmuję {first_value} i {second_value}")
    logging.info(f"Wynik to {first_value - second_value}")
if calc_type == 3:
    logging.info(f"Mnożę {first_value} i {second_value}")
    logging.info(f"Wynik to {first_value * second_value}")
if calc_type == 4:
    logging.info(f"Dzielę {first_value} i {second_value}")
    logging.info(f"Wynik to {first_value / second_value}")