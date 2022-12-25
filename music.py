import discord

# Function to play the audio from the YouTube video
async def play_audio(voice_client):
    # Create an audio source from the YouTube audio URL
    audio_source = discord.FFmpegPCMAudio(audio_url)
    # Play the audio
    voice_client.play(audio_source)

# Start the audio playback loop
async def audio_loop():
    while True:
        # If the queue is not empty and the voice client is not playing audio
        if queue and not voice_client.is_playing():
            # Get the next audio URL from the queue
            audio_url = queue.pop(0)
            # Play the audio
            await play_audio(voice_client)
        # Sleep for a short period of time before checking the queue again
        await asyncio.sleep(0.5)
