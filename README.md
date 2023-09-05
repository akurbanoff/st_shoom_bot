# О проекте
Необходимо было реализовать телеграм-бота для популярной фотостудии,
тк осуществляется большое количество броней и собственница тратит на это много времени.

## Что было реализовано и какие технологии применялись
Все было осуществлено на асинхронном фреймворке aiogram, были использованы state`s и inline-кнопки. Также был использован google api client для
работы с google calendar.


### Запуск бота
Вам неоходимо иметь google api client а также secret key полученный в credentials. После этого вы подключаете своего бота к своему гугл календарю(ссылка на видео как это сделать - https://youtu.be/zAUv09DzrK4)
```
git clone git@github.com:Uspesh/tg.git
pip install -r requirements.txt
```
Создайте файл .env и добавте туда API_TOKEN - токен телеграм бота.
Перейдите на файл main и запустите бота.

### Прочее

Работу бота вы можете посмотреть в телеграм - https://t.me/st_shoom_bot