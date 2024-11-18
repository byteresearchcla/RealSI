# ignore_security_alert_file RCE
import os
import io
import time
import yt_dlp
import sys


def download_audio(url, output_path, start_time, end_time):
    os.system(f"mkdir -p {output_path}")

    ydl_opts = {
        'format': 'bestaudio/best',  # 选择最佳音频质量
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ss', str(start_time),
            '-to', str(end_time)
        ],
        'outtmpl': str(output_path + '/' + '%(id)s.%(ext)s'),
        'verbose': False,
        'progress_hooks': [download_progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Start Downloading: {url}")
            ydl.download([url])
            print("\nDownload Complete!")

    except Exception as e:
        print(f"Download Error: {str(e)}")
        sys.exit(1)


def download_progress_hook(d):
    if d['status'] == 'downloading':
        if 'total_bytes' in d:
            percentage = d['downloaded_bytes'] / d['total_bytes'] * 100
            print(f"\rDownload Progress: {percentage:.1f}%", end='\t')
        elif 'total_bytes_estimate' in d:
            percentage = d['downloaded_bytes'] / d['total_bytes_estimate'] * 100
            print(f"\rDownload Progress: {percentage:.1f}% ETA", end='')
    elif d['status'] == 'finished':
        print("\nConverting to mp3...")


def download_youtube_video(url, output_path, start_time, end_time, retries=30, delay=5, target_format='FLAC'):
    while retries > 0:
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
            buffer = io.BytesIO()
            stream.stream_to_buffer(buffer)
            buffer.seek(0)
            audio_data = AudioSegment.from_file(buffer, format='webm')
            st, et = time_to_milliseconds(start_time), time_to_milliseconds(end_time)
            audio_data = audio_data[st:et]
            audio_data = audio_data.set_frame_rate(SAMPLE_RATE)
            audio_data.export(output_path, format=target_format, parameters=["-ar", str(SAMPLE_RATE), "-ac", "1"])
            return 
        except Exception as e:
            print(f"Download failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            retries -= 1
    raise Exception(f"Failed to download video after multiple attempts: {url}")


def time_to_milliseconds(time_str):
    h, m, s = map(float, time_str.strip().split(':'))
    return int((h * 3600 + m * 60 + s) * 1000)


video_list_zh = [
    ("zh2en-01-tech", "https://www.youtube.com/watch?v=lhcQkrkTUhc", "lhcQkrkTUhc", "00:00:43 - 00:06:06"),
    ("zh2en-02-health", "https://www.youtube.com/watch?v=D2kmp5jzGH8", "D2kmp5jzGH8", "00:14:35 - 00:17:52"),
    ("zh2en-03-edu", "https://www.youtube.com/watch?v=K-5cM2gaKUU", "K-5cM2gaKUU", "00:03:19.80 - 00:08:15.80"),
    ("zh2en-04-fin", "https://www.youtube.com/watch?v=1bxJKYlP2SQ", "1bxJKYlP2SQ", "00:44:09 - 00:49:31.50"),
    ("zh2en-05-law", "https://www.youtube.com/watch?v=faDmOWyGNxk", "faDmOWyGNxk", "00:07:49 - 00:12:27"),
    ("zh2en-06-env", "https://www.youtube.com/watch?v=EpnR9GZdoDw", "EpnR9GZdoDw", "00:01:00.39 - 00:05:18"),
    ("zh2en-07-ent", "https://www.youtube.com/watch?v=07RvKD801Bo", "07RvKD801Bo", "00:00:11.80 - 00:05:27.75"),
    ("zh2en-08-sci", "https://www.youtube.com/watch?v=f5HARGtfXSQ", "f5HARGtfXSQ", "00:01:40 - 00:06:27"),
    ("zh2en-09-sport", "https://www.youtube.com/watch?v=hp0jN1iawSQ", "hp0jN1iawSQ", "00:46:35 - 00:52:04"),
    ("zh2en-10-art", "https://www.youtube.com/watch?v=98aNJZ0UV-c", "98aNJZ0UV-c", "01:14:17 - 01:20:37"),
]

video_list_en = [
    ("en2zh-01-tech",   "https://www.youtube.com/live/_K-eupuDVEc", "_K-eupuDVEc", "00:37:30 - 00:40:55 "),
    ("en2zh-02-health", "https://www.youtube.com/watch?v=m_OKi0_YrrM", "m_OKi0_YrrM", "00:15:46 - 00:19:20"),
    ("en2zh-03-edu",    "https://www.youtube.com/watch?v=mZHOTfSrox0", "mZHOTfSrox0", "00:00:38 - 00:05:38"),
    ("en2zh-04-fin",    "https://www.youtube.com/watch?v=BPK_qzeH_yk", "BPK_qzeH_yk", "00:17:24 - 00:22:25"),
    ("en2zh-05-law",    "https://www.youtube.com/watch?v=o6bO3zzrBp0", "o6bO3zzrBp0", "00:00:57 - 00:05:55"),
    ("en2zh-06-env",    "https://www.youtube.com/watch?v=jlJijwgtgzI", "jlJijwgtgzI", "00:02:05 - 00:06:29"),
    ("en2zh-07-ent",    "https://www.youtube.com/watch?v=fi1Ke6yAVP4", "fi1Ke6yAVP4", "01:22:48 - 01:28:00"),
    ("en2zh-08-sci",    "https://www.youtube.com/watch?v=hRz0BBmPNDs", "hRz0BBmPNDs", "00:28:00 - 00:33:11"),
    ("en2zh-09-sport",  "https://www.youtube.com/watch?v=sKDwRSuCDZM", "sKDwRSuCDZM", "00:24:35 - 00:28:00"),
    ("en2zh-10-art",    "https://www.youtube.com/watch?v=FbZ_MOWLMu8", "FbZ_MOWLMu8", "00:20:28 - 00:24:45"),
]

if __name__ == "__main__":
    for vid, url, ytb_id, duration in video_list_en:
        out_path = f"data/en2zh/audio"
        if os.path.exists(f"{out_path}/{vid}.mp3"):
            continue
        st, et = duration.split("-", 1)
        print(f"Downloading {vid} to {out_path}")
        download_audio(url, out_path, st.strip(), et.strip())
        os.system(f"mv {out_path}/{ytb_id}.mp3 {out_path}/{vid}.mp3")

    for vid, url, ytb_id, duration in video_list_zh:
        out_path = f"data/zh2en/audio"
        if os.path.exists(f"{out_path}/{vid}.mp3"):
            continue
        st, et = duration.split("-", 1)
        print(f"Downloading {vid} to {out_path}")
        download_audio(url, out_path, st.strip(), et.strip())
        os.system(f"mv {out_path}/{ytb_id}.mp3 {out_path}/{vid}.mp3")
