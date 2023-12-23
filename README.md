# API Project README

Voor het eindprojecet van API heb ik net zoals vorig project gebruik gemaakt van Fastapi, waarbij gebruik wordt gemaakt van SQLite als database voor persistentie. De API biedt functionaliteit voor het beheren en bekijken van weersvoorspellingen voor specifieke steden. Daarnaast kun je ook nog locatie opladen en aanvragen maar dit was meer als bijproduct. 

## Inhoudsopgave

- [Projectstructuur](#projectstructuur)
- [API-endpoints](#api-endpoints)
- [Front-end](#front-end)
- [Screenshots](#screenshots)
- [Besluit](#Besluit/punten)


## Projectstructuur

De projectstructuur omvat de volgende belangrijke onderdelen:

- `main.py`: Bevat de FastAPI-toepassing en definieert API-endpoints.
- `models.py`: Definieert de database-modellen.
- `crud.py`: Bevat CRUD (Create, Read, Update, Delete) bewerkingen voor de database.
- `schemas.py`: Bevat Pydantic-schemas voor gegevensvalidatie.
- `database.py`: Bevat de configuratie voor de database.
- `auth.py`: Bevat de functies en configuratie voor authenticatie en autorisatie in het systeem. Dit omvat functionaliteit zoals het hashen en verifiëren van wachtwoorden, het genereren van JWT-tokens voor gebruikersauthenticatie en het controleren van gebruikersreferenties.
- `test_endpoints.py`: Bevat tests voor de API-eindpunten van het systeem. Dit omvat verschillende tests voor het maken van een gebruiker, inloggen, het plaatsen van een weersvoorspelling, het ophalen van weersvoorspellingen en gebruikersgegevens op basis van ID's en het ophalen van gebruikersgegevens.


## API-endpoints

- **POST `/forecast/`**: Creëert nieuwe weersvoorspellingsgegevens.
- **GET `/forecast/`**: Haalt de lijst met weersvoorspellingen op.
- **GET `/forecast/{forecast_id}`**: Haalt specifieke weersvoorspellingsgegevens op.
- **PUT `/forecast/{forecast_id}`**: Update specifieke weersvoorspellingsgegevens.
- **DELETE `/forecast/{forecast_id}`**: Verwijdert specifieke weersvoorspellingsgegevens.
- **GET `/forecast_ordered/{city}`**: Haalt geordende voorspellingsgegevens op voor een specifieke stad.
- **POST `/locations/`**: Creëert nieuwe locatiegegevens.
- **GET `/locations/{location_id}`**: Haalt specifieke locatiegegevens op.
- **POST `/token`**: Genereert een toegangstoken voor authenticatie.
- **POST `/users/`**: Creëert een nieuwe gebruiker.
- **GET `/users/`**: Haalt de lijst met gebruikers op.
- **GET `/users/{user_id}`**: Haalt specifieke gebruikersgegevens op.


## Screenshots

Voor de werking van de api te laten zien heb ik wat screenshots gemaakt. 

**Dit is mijn /docs**
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/106f15c8-a4ec-4cf6-9e62-223c57b9ce65)

Get forecast
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/28f2aac5-5957-416e-8c8d-cf0ca40b0769)

User aanmaken
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/3eccf990-7407-40b4-9dc7-137494056d14)

Login
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/9f8c6f23-2c05-4837-a3e4-922a7adf1ae9)

![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/77bf45ca-5a5e-4076-8acd-a4d2de331450)

Create forecast

![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/0eb4a705-b873-4067-93bd-f336294aab20)

![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/e5ca4f81-52c1-4a42-a193-127585540bd1)


update forecast

![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/fb9087fc-009e-440b-92fb-89f33f641eb6)

Delete forecast

![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/8fef79e0-e48b-4365-910a-5ebb06d6c0a8)


**Okteto**
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/c7e6ff64-9a8a-4aca-a66e-9eec142356b6)



**Hier nog wat screenshots van Postman**
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/f592bd2a-cce0-4cb7-beab-f7cb56ec8fb2)
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/7a632d88-1225-4834-b3b0-0353ad7124b1)
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/5f2f04cc-865a-4c0c-a8ef-c6ff989cf086)

**Testing**
Ik heb een testing file gemaakt, hier kan je deze locaal zien:
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/228af308-f31d-4c49-8bc0-f9f8cf7fb4cf)

De test file zit ook in de github actions:
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/e35ca491-1254-46bc-9fd8-fb23e245c5e1)


**Netlify/frontend**
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/889a24ae-f713-4d39-aae2-381112dce5d2)
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/b2f85e97-9112-49e8-8139-6146251d5906)
![image](https://github.com/tuurhulselmans/api_eindproject/assets/106010714/156580ad-c139-4a78-a30f-1e9207d58af7)



## Front-end

De front-end is een HTML-pagina (`index.html`) met JavaScript (`script.js`) en wat CSS. Je kan een weersvoorspelling toevoegen of je kan er een opvragen. Voor een weersvoorspelling toe te voegen, moet je wel een account aanmaken en inloggen. Ik heb dit dan op github gezet en daarna met netlify gehost. Ik had nog een domein naam van een vorig project eraan gekoppeld heb.

https://github.com/tuurhulselmans/frontend_api_eindproject
https://dancing-melba-034ff1.netlify.app/
https://techchips.be/

## Besluit

Ik heb de algemene eisen volbracht. Daarnaast heb ik ook een front-end met mijn get/post-endpoints. Ik vind zelf dat deze een mooie stijl heeft, toch voor iemand dat CCS doet. Als laatste heb ik mijn test file draaiende op github actions. 

Dit allemaal komt uit op een maximum van 90%. 

