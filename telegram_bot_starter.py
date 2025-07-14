from bot import TelegramBot
import time

# Main bot loop
def main():
    # Replace with your bot token from @BotFather
    BOT_TOKEN = "7703211959:AAEmP0t5Iv_mLWCzf9yNNG2eFrYSCajP9l4"
    bot = TelegramBot(BOT_TOKEN)
    
    print("Bot started. Send messages to test...")
    
    while True:
        updates = bot.get_updates()
        
        for update in updates:
            if update.message:
                print(f"Received: {update}")
                
                # Echo back a response for text messages

                if update.message.text:
                    bot.send_message(
                        update.message.chat.id, 
                        f"You said: {update.message.text}"
                    )

                # TODO: Students will add handling for voice, photo, and dice messages here
                # For example:
                if update.message.voice:
                    bot.send_voice(
                        update.message.chat.id,
                        update.message.voice.file_id
                    )
                if update.message.photo:
                    bot.send_photo(
                        update.message.chat.id,
                        update.message.photo.file_id
                    )
                if update.message.video:
                    bot.send_video(
                        update.message.chat.id,
                        update.message.video.file_id
                    )
                if update.message.dice:
                    bot.send_dice(
                        update.message.chat.id,
                        update.message.dice.emoji
                    )

        
        time.sleep(1)

if __name__ == "__main__":
    main()
