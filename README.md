<p align="center">A Discord Bot that creates an individual ticket when a button is pressed (similar to TicketTool bot)</p>

<p align="center"><img alt="image" src="pictures/image.png" /></p>

## Description
When a special button sent with a message is pressed, an individual ticket is created.

### Usage
`/ping` - command to check if the bot is working

`/embed` - sends a message with a button that creates a ticket when pressed

### Configuration

The bot is configured in the `config.json` file.

- `token` - [Discord Bot Token](https://discord.com/developers/applications/)
- `prefix` - bot prefix
- `ticket_category_name` - name of the category where tickets will be stored
- `ticket_channel_name` - name of the ticket (formatted as `{name}-{user_id}` - e.g., `ABCD-1234`)
- `moderator_role_id` - ID of the moderator role for access to tickets

## Installation and Launch

### Installation

```bash
git clone https://github.com/Bebrowskiy/Ticket-Bot.git
```

### Dependencies

```bash
cd Ticket-Bot/
```
```bash
pip install -r requirements.txt
```

### Launch

```bash
cd Bot/
```
```bash
python bot.py
```

<p align="center"><a href="https://vk.com/bebrow2021">My VK Page</a></p>
