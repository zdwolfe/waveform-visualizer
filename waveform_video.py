import ffmpeg

def get_audio_duration(filename):
    try:
        probe = ffmpeg.probe(filename)
        duration = float(probe['format']['duration'])
        return duration
    except ffmpeg.Error as e:
        print(f"An error occurred while probing the audio file: {e}")
        return None

def create_waveform_video(audio_file, video_file, width=1280, height=720, color='blue', bg_color='black', mode='line'):
    """
    Creates a waveform video from an audio file using FFmpeg filters.

    Args:
        audio_file (str): Path to the input audio file.
        video_file (str): Path to the output video file.
        width (int): Width of the output video.
        height (int): Height of the output video.
        color (str): Color of the waveform.
        bg_color (str): Background color of the video.
        mode (str): Waveform display mode ('line', 'cline', 'p2p').
    """
    audio_duration = get_audio_duration(audio_file)
    if audio_duration is None:
        print("Could not get audio duration.")
        return

    audio_input = ffmpeg.input(audio_file)

    waveform = (
        audio_input.audio.filter(
            'showwaves',
            s=f'{width}x{height}',
            mode=mode,
            colors=color
        )
    )

    background = ffmpeg.input(
        f'color=c={bg_color}:s={width}x{height}:d={audio_duration}',
        f='lavfi'
    )

    video = (
        ffmpeg.overlay(background, waveform)
        .filter('format', 'yuv420p')
    )

    out = ffmpeg.output(
        video,
        audio_input.audio,
        video_file,
        vcodec='libx264',
        acodec='aac',
        strict='experimental',
        shortest=None
    )

    out.run(overwrite_output=True)
