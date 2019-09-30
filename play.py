from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play



# plays sound


song = AudioSegment.from_wav("delme_rec_unlimited_77oamvb6.wav")
play(song)
