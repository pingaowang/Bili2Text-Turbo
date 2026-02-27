import os
import re
import subprocess
import glob  # 新增导入

def ensure_folders_exist(output_dir):
    if not os.path.exists("bilibili_video"):
        os.makedirs("bilibili_video")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

def download_video(bv_number):
    """
    使用yt-dlp下载B站视频。
    参数:
        bv_number: 字符串形式的BV号（不含"BV"前缀）或完整BV号
    返回:
        文件路径
    """
    if not bv_number.startswith("BV"):
        bv_number = "BV" + bv_number
    video_url = f"https://www.bilibili.com/video/{bv_number}"
    output_dir = f"bilibili_video/{bv_number}" # 下载视频到 bilibili_video/{bv_number} 目录
    ensure_folders_exist(output_dir)
    print(f"使用yt-dlp下载视频: {video_url}")
    try:
        # 使用 yt-dlp 代替 you-get
        # -o 后面是输出模板，这里我们指定到 output_dir
        result = subprocess.run(["yt-dlp", "-o", f"{output_dir}/%(title)s.%(ext)s", video_url], capture_output=True, text=True)
        if result.returncode != 0:
            print("下载失败:", result.stderr)
        else:
            print(result.stdout)
            print(f"视频已成功下载到目录: {output_dir}")
            # 查找视频文件，yt-dlp 可能下载为 mp4, mkv, webm 等
            video_files = glob.glob(os.path.join(output_dir, "*.*"))
            video_files = [f for f in video_files if f.endswith(('.mp4', '.mkv', '.webm', '.flv'))]
            if not video_files:
                print("下载成功但未找到视频文件")
                return ""
    except Exception as e:
        print("发生错误:", str(e))
        return ""
    return bv_number
