import discord

# Import the bot object and the queue list from the bot.py file
from bot import bot, queue

# Import the music functions from the music.py file
from music import play_audio, audio_loop

# Command handler for the "join" command
@bot.command()
async def join(ctx):
    # Get the voice channel to join
    voice_channel = ctx.author.voice.channel
    # Join the voice channel
    global voice_client
    voice_client = await voice_channel.connect()
    # Play the audio from the first video in the queue
    await play_audio(voice_client)

# Command handler for the "leave" command
@bot.command()
async def leave(ctx):
    # Disconnect from the voice channel
    await voice_client.disconnect()

# Command handler for the "volume" command
@bot.command()
async def volume(ctx, volume: int):
    # Set the volume of the voice client
    voice_client.source.volume = volume / 100

# Command handler for the "play" command
@bot.command()
async def play(ctx, video_url: str):
    # Get the voice channel to join
    voice_channel = ctx.author.voice.channel
    # Join the voice channel
    global voice_client
    voice_client = await voice_channel.connect()
    # Use youtube_dl to extract the audio from the YouTube video
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        audio_url = info["url"]
    # Create an audio source from the YouTube audio URL
    audio_source = discord.FFmpegPCMAudio(audio_url)
    # Play the audio
    voice_client.play(audio_source)

# Command handler for the "add" command
@bot.command()
async def add(ctx, video_url: str):
    # Extract the audio from the YouTube video
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        audio_url = info["url"]
    # Add the audio URL to the queue
    queue.append(audio_url)
