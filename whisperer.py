from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_path, mp3_path):
    video_clip = VideoFileClip(mp4_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_path)
    audio_clip.close()
    video_clip.close()

# Example usage
mp4_file = "./BCI_approaches.mp4"  
mp3_file = "audio.mp3"
convert_mp4_to_mp3(mp4_file, mp3_file)


import whisper

model = whisper.load_model("base")

result = model.transcribe("audio.mp3")


for segment in result["segments"]:
    print(f"{segment['start']:.2f} - {segment['end']:.2f}: {segment['text']}")


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

srt_filename = mp4_file.rsplit(".", 1)[0] + ".srt"
with open(srt_filename, "w", encoding="utf-8") as srt_file:
    for i, segment in enumerate(result["segments"], start=1):
        start_time = format_time(segment["start"])
        end_time = format_time(segment["end"])
        
        srt_file.write(f"{i}\n")
        srt_file.write(f"{start_time} --> {end_time}\n")
        srt_file.write(f"{segment['text'].strip()}\n\n")