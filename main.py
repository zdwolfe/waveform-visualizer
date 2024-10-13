import argparse
import waveform_video

def main():
    parser = argparse.ArgumentParser(description='Create a waveform video from an audio file.')
    parser.add_argument('audio_file', help='Input audio file.')
    parser.add_argument('video_file', help='Output video file.')
    parser.add_argument('--width', type=int, default=1280, help='Width of the output video.')
    parser.add_argument('--height', type=int, default=720, help='Height of the output video.')
    parser.add_argument('--color', default='blue', help='Color of the waveform.')
    parser.add_argument('--bg_color', default='black', help='Background color of the video.')
    parser.add_argument('--mode', default='line', choices=['line', 'cline', 'p2p'], help='Waveform display mode.')

    args = parser.parse_args()

    waveform_video.create_waveform_video(
        audio_file=args.audio_file,
        video_file=args.video_file,
        width=args.width,
        height=args.height,
        color=args.color,
        bg_color=args.bg_color,
        mode=args.mode
    )

if __name__ == '__main__':
    main()
