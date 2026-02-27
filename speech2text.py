from faster_whisper import WhisperModel
import os

whisper_model = None

def load_whisper(model="small"):
    global whisper_model
    # Mac (Apple Silicon) 上使用 CPU 或 MPS (如果支持)，faster-whisper 默认在 CPU 上也非常快
    # device="cpu", compute_type="int8" 是最通用的加速配置
    print(f"正在加载 Faster-Whisper 模型: {model}...")
    whisper_model = WhisperModel(model, device="cpu", compute_type="int8")
    print("Faster-Whisper 模型加载成功！")

def run_analysis(filename, model="small", prompt="以下是普通话的句子。"):
    global whisper_model
    if whisper_model is None:
        load_whisper(model)
        
    # 读取列表中的音频文件
    audio_dir = f"audio/slice/{filename}"
    audio_list = os.listdir(audio_dir)
    
    # 过滤并排序音频文件
    audio_files = sorted(
        [f for f in audio_list if f.endswith(".mp3")],
        key=lambda x: int(os.path.splitext(x)[0])
    )
    
    os.makedirs("outputs", exist_ok=True)
    output_path = f"outputs/{filename}.txt"
    
    # 清空旧文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("")

    print(f"正在转换文本，共 {len(audio_files)} 个分片...")

    for i, fn in enumerate(audio_files, 1):
        file_path = os.path.join(audio_dir, fn)
        print(f"正在转换第 {i}/{len(audio_files)} 个音频... {fn}")
        
        # initial_prompt 很有用，可以引导模型使用正确的术语和标点
        segments, info = whisper_model.transcribe(file_path, initial_prompt=prompt, beam_size=5)
        
        text_content = "".join([segment.text for segment in segments])
        print(text_content)

        with open(output_path, "a", encoding="utf-8") as f:
            f.write(text_content + "\n")
    
    return output_path
