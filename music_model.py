import discord
from discord.ext import commands
import youtube_dl

# Create an Intents object with the required permissions
intents = discord.Intents.default()
intents.members = True

# Create a discord client and a voice client
client = discord.Client(intents=intents)
voice_client = None

# Set the YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

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

# Function to play the audio from the YouTube video
async def play_audio(voice_client):
    # Create an audio source from the YouTube audio URL
    audio_source = discord.FFmpegPCMAudio(audio_url)
    # Play the audio
    voice_client.play(audio_source)

# Event handler for when the client is ready
@client.event
async def on_ready():
    # Create a global queue for video URLs
    global queue
    queue = []

# Create an Intents object with the required permissions
intents = discord.Intents.default()
intents.members = True

# Create a discord client and a command bot
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def join(ctx):
    print("Received join command")  # Debugging message
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

# Run the Discord client
client.run("MTA1NTk5Njk1NzYzNTY0NTUwMQ.GFw3LI.-CgjmdtbPdwz8pzyTGLhHjRqEGEMELQheGHB5w")