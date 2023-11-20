# LowriderBulwark
This bot will ban any discord user who dares to queue Low Rider by WAR using pancake from a discord server. 

# On Ready
For the bot to send a notification when it appears online, you will need to first enable discord developer mode. Once enabled, you can retrieve a text-channel's channel ID and assign it to `channel_id` in `on_ready()`.

# Bot Token
Create your discord bot in [the discord bot developer portal](https://discord.com/developers/docs/intro).
Retrieve the bot token from the Bot section in the selected bot's settings. Replace the placeholder in `bot.run()` with your token.

# Execute
Before running the bot, make sure you have added your bot token and channel ID to the code. If you do not want the bot to send a message when appearing online, you can delete the `on_ready()` function.
Run this bot by navigating to the directory containing `LowriderBulwark.py`. Enter `python .\LowriderBulwark.py` to run the bot. Create your URL and add the bot to your desired server. You will now never hear those retched cow bells again. 
