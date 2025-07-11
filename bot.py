"""
Telegram Bot API Client Module

This module provides a TelegramBot class for interacting with the Telegram Bot API.
It handles basic operations like receiving updates and sending messages.

Students should extend this class with additional methods as part of their homework.
"""

import requests
from pprint import pprint

from models import Update

class TelegramBot:
    """
    A client for the Telegram Bot API.

    This class provides methods to interact with Telegram's Bot API including
    receiving updates from users and sending messages back. Students will extend
    this class with additional functionality for handling different message types.

    Attributes:
        token (str): The bot token obtained from @BotFather
        base_url (str): The base URL for Telegram Bot API requests
        last_update_id (int): The ID of the last processed update (for polling)
    """

    def __init__(self, token):
        """
        Initialize the TelegramBot with a bot token.

        Args:
            token (str): The bot token obtained from @BotFather on Telegram.
                        Format: "123456789:ABCdefGhIJKlmNoPQRstUVwxyz"
        """
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.last_update_id = 0

    def get_updates(self):
        """
        Retrieve new updates from Telegram using long polling.

        This method polls the Telegram API for new messages and other updates.
        It uses the 'offset' parameter to only get updates newer than the last
        processed one, preventing duplicate processing.

        Returns:
            list[Update]: A list of Update objects representing new messages,
                         inline queries, callback queries, etc. Returns empty
                         list if no updates or if an error occurs.

        Note:
            This method automatically updates self.last_update_id to track
            the most recently processed update.
        """
        url = f"{self.base_url}/getUpdates"
        params = {"offset": self.last_update_id + 1, "timeout": 30}
        response = requests.get(url, params=params)
        data = response.json()
        pprint(data)
        updates=[]
        try:
            response = requests.get(url, params=params)
            data = response.json()
           
            if data["ok"]:
                updates = []
                for update_data in data["result"]:
                    update = Update(update_data)
                    updates.append(update)
                    self.last_update_id = update.update_id
                return updates
            else:
                print(f"Error getting updates: {data['description']}")
                return []
        except Exception as e:
            print(f"Exception while getting updates: {e}")
            return []

    def send_message(self, chat_id, text):
        """
        Send a text message to a specific chat.

        Args:
            chat_id (int or str): Unique identifier for the target chat or
                                 username of the target channel (in the format @channelusername)
            text (str): Text of the message to be sent, 1-4096 characters after
                       entities parsing

        Returns:
            dict or None: The response from Telegram API as a dictionary if successful,
                         None if an error occurred. Successful response contains
                         information about the sent message.

        Example:
            bot = TelegramBot("your_token")
            response = bot.send_message(123456789, "Hello, World!")
            if response and response.get('ok'):
                print("Message sent successfully!")
        """
        url = f"{self.base_url}/sendMessage"
        data = {"chat_id": chat_id, "text": text}
        pprint(data)

        try:
            response = requests.post(url, data=data)
            return response.json()
        except Exception as e:
            print(f"Exception while sending message: {e}")
            return None

    # ============================================================================
    # ECHO BOT METHODS: Methods for echoing back different media types
    # ============================================================================

    def send_dice(self, chat_id, emoji="🎲"):
        """
        Send a dice roll animation to a chat.

        This method sends an animated emoji that shows a dice rolling animation.
        The bot will echo back dice messages using this method.

        Args:
            chat_id (int or str): Unique identifier for the target chat
            emoji (str): Emoji on which the dice throw animation is based.
                        Currently supports: 🎲 🎯 🏀 ⚽ 🎳 🎰

        Returns:
            dict or None: The response from Telegram API as a dictionary if successful,
                         None if an error occurred.

        Note:
            Students should implement this method to make a POST request to
            f"{self.base_url}/sendDice" with chat_id and emoji parameters.
        """
        
        r=requests.post(
            self.base_url+"/sendDice",
            params={
                "chat_id":chat_id,
                "emaji":emoji,
            },
        )
        return r.json()

    def send_voice(self, chat_id, voice_file_id):
        """
        Send a voice message by forwarding an existing voice file.

        This method echoes back a voice message by sending the same voice file
        that was received from a user.

        Args:
            chat_id (int or str): Unique identifier for the target chat
            voice_file_id (str): File identifier of the voice message to echo back

        Returns:
            dict or None: The response from Telegram API as a dictionary if successful,
                         None if an error occurred.

        Note:
            Students should implement this method to make a POST request to
            f"{self.base_url}/sendVoice" with chat_id and voice parameters.
        """
        r=requests.post(
            self.base_url+"/senVoice",
            params={
                "chat_id":chat_id,
                "voice":voice_file_id,
            },
        )
        return r.json()

    def send_photo(self, chat_id, photo_file_id, caption=None):
        """
        Send a photo by forwarding an existing photo file.

        This method echoes back a photo message by sending the same photo file
        that was received from a user, optionally with a caption.

        Args:
            chat_id (int or str): Unique identifier for the target chat
            photo_file_id (str): File identifier of the photo to echo back
            caption (str, optional): Photo caption, 0-1024 characters after entities parsing

        Returns:
            dict or None: The response from Telegram API as a dictionary if successful,
                         None if an error occurred.

        Note:
            Students should implement this method to make a POST request to
            f"{self.base_url}/sendPhoto" with chat_id, photo, and optional caption.
        """
        r=requests.post(
            self.base_url+"/sendPhoto",
            params={
                "chat_id":chat_id,
                "photo":photo_file_id,
                "caption":caption,
            },
        )
        return r.json()
    def send_video(self, chat_id, video_file_id, caption=None):
        """
        Send a video by forwarding an existing video file.

        This method echoes back a video message by sending the same video file
        that was received from a user, optionally with a caption.

        Args:
            chat_id (int or str): Unique identifier for the target chat
            video_file_id (str): File identifier of the video to echo back
            caption (str, optional): Video caption, 0-1024 characters after entities parsing

        Returns:
            dict or None: The response from Telegram API as a dictionary if successful,
                         None if an error occurred.

        Note:
            Students should implement this method to make a POST request to
            f"{self.base_url}/sendVideo" with chat_id, video, and optional caption.
        """
        r=requests.post(
            self.base_url+"/sendVedio",
            params={
                "chat_id":chat_id,
                "video":video_file_id,
                "caption":caption,
            },
        )
        return r.json()
