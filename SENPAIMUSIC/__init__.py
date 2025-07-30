from SENPAIMUSIC.core.bot import SENPAI
from SENPAIMUSIC.core.dir import dirr
from SENPAIMUSIC.core.git import git
from SENPAIMUSIC.core.userbot import Userbot
from SENPAIMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SENPAI()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"
