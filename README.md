# waveform visualier

Wrapper around ffmpeg waveform visualization


```bash
docker build -t waveform-video-app .
```

```bash
docker run --rm -v "$(pwd)/data":/data waveform-video-app /data/input.wav /data/output.mp4
```
