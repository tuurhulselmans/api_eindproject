# API Project README

Dit project is een API die gebouwd is met FastAPI, waarbij gebruik wordt gemaakt van SQLite als database voor persistentie. De API biedt functionaliteit voor het beheren en bekijken van weersvoorspellingen voor specifieke steden. Ik ben begonnen voor alleen de temperatuur weer te geven maar besliste al snel op een hele weersvoorspelling te maken. 

## Inhoudsopgave

- [Projectstructuur](#projectstructuur)
- [API-endpoints](#api-endpoints)
- [Front-end](#front-end)
- [Screenshots](#screenshots)


## Projectstructuur

De projectstructuur omvat de volgende belangrijke onderdelen:

- `main.py`: Bevat de FastAPI-toepassing en definieert API-endpoints.
- `models.py`: Definieert de database-modellen.
- `crud.py`: Bevat CRUD (Create, Read, Update, Delete) bewerkingen voor de database.
- `schemas.py`: Bevat Pydantic-schemas voor gegevensvalidatie.
- `database.py`: Bevat de configuratie voor de database.
- `static/`: Bevat statische bestanden zoals HTML en JavaScript voor de front-end.


## API-endpoints

- **GET `/weather/`**: Haalt de lijst met weergegevens op.
- **POST `/weather/`**: Creëert nieuwe weergegevens.
- **Get `/weather/{weather_id}`**: Haalt specifieke weergegevens op.
- **DELETE `/weather/{weather_id}`**:  Verwijdert specifieke weergegevens.
- **GET `/temperature/{city}`**: Haalt temperatuurgegevens op voor een specifieke stad.
- **GET `/forecast/`**: Haalt de lijst met weersvoorspellingen op.
- **POST `/forecast/`**: Creëert nieuwe weersvoorspellingsgegevens.
- **GET `/forecast/{forecast_id}`**: Haalt specifieke weersvoorspellingsgegevens op.
- **GET `/forecast_ordered/{city}`**: Haalt geordende voorspellingsgegevens op voor een specifieke stad.

Voor meer gedetailleerde informatie over elk endpoint, bekijk de [API-documentatie](http://localhost:8000/docs) tijdens het uitvoeren van de applicatie.

## Screenshots

Voor de werking van de api te laten zien heb ik wat screenshots gemaakt. 
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/ba6e3ba7-3978-498b-b7c2-62fa74175004)

![image](https://github.com/tuurhulselmans/api_test/assets/106010714/4f99978d-a938-4538-9dd1-e78ba657cf96)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/729184c3-26a6-4fa5-a4d0-da6aa1eef2e0)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/bc55e264-0439-4e90-8958-ff19aec7e705)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/75780b80-bb46-4b2a-b5de-48be5d9b585b)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/8874d141-338d-4b59-adce-e371c3fc00d9)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/3eaa45c4-dc34-4058-a6c5-a0cbf80e44e5)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/7ef64c37-b9cb-490b-91e4-e3e04a7d2959)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/d8beac0e-9b98-4f3b-91a1-25b29536a26d)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/fcc2c2d9-c08c-4edb-bd81-266028ab06c2)

Hier nog wat screenshots van Postman
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/6164f13b-f127-4c34-9b42-6ba135292cda)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/2b7b16ff-24a2-4921-a276-a3e8394934f5)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/3051279c-82d9-4d23-878d-6a427a0935b1)

Als laatste een paar screenshots van de front-end:
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/7243fb92-ae06-4057-96f5-39d83dc5dff5)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/e0d3b9ba-6b02-4362-9070-305f68c5ea94)
![image](https://github.com/tuurhulselmans/api_test/assets/106010714/06f14981-0805-42ed-90ad-830ac4466272)



## Front-end

De front-end is een eenvoudige HTML-pagina (`index.html`) met JavaScript (`script.js`). Je kan een weersvoorspelling toevoegen of je kan er een opvragen. 

https://tuurhulselmans.github.io/api-front-end/
https://github.com/tuurhulselmans/api-front-end
