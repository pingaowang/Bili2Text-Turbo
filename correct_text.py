import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件中的配置
load_dotenv()

class AICorrector:
    """
    通过 AI API 进行智能纠错和排版。
    """
    def __init__(self):
        self.api_key = os.getenv("AI_API_KEY")
        self.base_url = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")
        self.model = os.getenv("AI_MODEL", "gpt-4o-mini")
        
        if not self.api_key:
            print("警告: 未在 .env 中找到 AI_API_KEY，将跳过智能纠错。")
            self.client = None
        else:
            self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def correct(self, text):
        if not self.client:
            return text
            
        try:
            prompt = """你是一个专业的视频文字编辑。请对以下由 Whisper 自动生成的音频识别稿进行智能纠错。
            要求：
            1. 修正文中的错别字，尤其是中文同音字（例如：习得性无助、拖延、权衡等）。
            2. 补全缺失的标点符号，根据语意进行分段，提高可读性。
            3. 保持原意不变，不要随意删减视频内容。
            4. 如果文中包含重复或语气助词，可以适当修饰使其更书面化。
            5. 直接返回修正后的文本。
            
            待纠错文本：
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个高效且准确的文本纠错专家。"},
                    {"role": "user", "content": prompt + text}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI 纠错过程中发生错误: {e}")
            return text

def ai_correct_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # 检查是否有 API Key
    load_dotenv()
    if not os.getenv("AI_API_KEY"):
        print("错误: 请先在 .env 文件中设置 AI_API_KEY")
        return file_path

    print(f"--- 正在使用 AI ({os.getenv('AI_MODEL')}) 对全文进行智能纠错与排版 ---")
    
    with open(file_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    # 简单切分处理（如果文本极长，API 可能会有限制，这里暂按全文处理）
    corrector = AICorrector()
    corrected_text = corrector.correct(full_text)

    # 保存纠错后的版本
    base, ext = os.path.splitext(file_path)
    new_path = f"{base}_corrected{ext}"
    
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(corrected_text)
    
    print(f"纠错完成！已保存至: {new_path}")
    return new_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ai_correct_file(sys.argv[1])
    else:
        print("Usage: python correct_text.py <file_path>")
