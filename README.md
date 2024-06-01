<p align="center">Discord Бот, который создает индивидуальный тикет при нажатии на кнопку (работает по типу бота TicketTool)</p>


<p align="center"><img alt="image" src="pictures/image.png" /></p>

## Описание
При нажатии на специальную кнопку, которая отправляется вместе с сообщением, создается индивидуальный тикет

### Использование
`/ping` - команда для проверки работоспособности бота

`/embed` - отправляет сообщение с кнопкой, при нажатии на которую создаётся тикет

### Настройка

Настройка бота осуществляется в файле `config.json`

`token` - токен [Disocrd Бота](https://discord.com/developers/applications/)

`prefix` -  префикс для бота

`ticket_category_name` - название категории, где будут храниться тикеты

`ticket_channel_name` - название тикета (будет как `{name}-{user_id}` - `ABCD-1234`)

`moderator_role_id` - id роли модератора для доступа к тикетам

## Установка и запуск

### Установка

```bash
git clone https://github.com/Bebrowskiy/Ticket-Bot.git
```

### Зависимости

- disnake

```bash
cd Ticket-Bot/
```

```bash
pip install -r requirements.txt
```

### Запуск

```bash
cd Bot
python bot.py
```

<p align="center"> <a href="https://vk.com/bebrow2021">Моя страница в VK</a></p>
