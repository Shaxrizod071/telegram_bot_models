class User:
    def __init__(self, user_data):
        self.id = user_data.get("id")
        self.is_bot = user_data.get("t_name")
        self.last_name = user_data.get("last_nais_bot", False)
        self.first_name = user_data.get("firsme")
        self.username = user_data.get("username")
        self.language_code = user_data.get("language_code")

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, name={self.first_name} {self.last_name})"


class Chat:
    def __init__(self, chat_data):
        self.id = chat_data.get("id")
        self.type = chat_data.get("type")
        self.title = chat_data.get("title")
        self.username = chat_data.get("username")
        self.first_name = chat_data.get("first_name")
        self.last_name = chat_data.get("last_name")

    def __str__(self):
        return f"Chat(id={self.id}, type={self.type}, title={self.title})"


class Message:
    def __init__(self, message_data):
        self.message_id = message_data.get("message_id")
        self.date = message_data.get("date")
        self.text = message_data.get("text")
        # Parse user and chat objects
        if message_data.get("from"):
            self.from_user = User(message_data["from"])
        else:
            self.from_user = None

        if message_data.get("chat"):
            self.chat = Chat(message_data["chat"])
        else:
            self.chat = None
        # TODO: Students need to add parsing for voice, photo, and dice here
        if message_data.get("voice"):
           self.voice=Voice(message_data["voice"])
        else:
            self.voice=None
        if message_data.get("photo"):
            self.photo=Photo(message_data[0]["photo"])
        else: 
            self.photo = None
        if message_data.get("video"):
            self.video=Video(message_data["video"])
        else:
            self.video = None
        if message_data.get("dice"):
            self.dice=Dice(message_data["dice"])
        else:
            self.dice = None

    def __str__(self):
        return (
            f"Message(id={self.message_id}, text={self.text}, from={self.from_user},chat={self.chat},voice={self.voice},photo={self.photo},video={self.video},dice={self.dice})"
        )


class Update:
    def __init__(self, update_data):
        self.update_id = update_data.get("update_id")

        if update_data.get("message"):
            self.message = Message(update_data["message"])
        else:
            self.message = None
    def __str__(self):
        return f"Update(id={self.update_id}, message={self.message})"
    
class Voice:
    def __init__(self, voice_data):
        self.file_id = voice_data.get("file_id")
        self.file_unique_id = voice_data.get("file_unique_id")
        self.duration = voice_data.get("duration")
            
    def __str__(self):
        return f"Voice(file_id={self.file_id}, file_unique_id={self.file_unique_id}, duration={self.duration})"
class Photo:
    def __init__(self,photo_data):
        self.file_id = photo_data.get("file_id")

    def __str__(self):
        return f"Photo(file_id={self.file_id})"

class Video:
    def __init__(self,video_data):
        self.duration = video_data.get("duration")
        self.file_id = video_data.get("file_id")
        self.file_unique_id = video_data.get("file_unique_id")
        self.width = video_data.get("width")
        self.height = video_data.get("height")

    def __str__(self):
        return f"Video(file_id={self.file_id}, file_unique_id={self.file_unique_id}, width={self.width},height={self.height})"

class Dice:
    def __init__(self,dice_data):
        self.chat_id = dice_data.get('chat_id')
        self.emoji = dice_data.get("emoji")

    def __str__(self):
        return f"Dice(chat_id={self.chat_id}, emoji={self.emoji})"



  