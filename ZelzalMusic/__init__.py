

from ZelzalMusic.core.bot import Zelzaly
from ZelzalMusic.core.dir import dirr
from ZelzalMusic.core.git import git
from ZelzalMusic.core.userbot import Userbot
from ZelzalMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
