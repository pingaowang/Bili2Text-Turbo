# 🚀 Bili2Text-Turbo

> **本地轻量提取 + 云端 AI 智能精修：B 站视频转文字的最优解。**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://www.python.org/)

## 🌟 为什么选择 Bili2Text-Turbo?

市面上的 B 站转文字工具要么需要昂贵的显卡跑大模型，要么识别出的文字（如 Whisper Small/Tiny）错别字满篇，无法直接阅读。

**Bili2Text-Turbo** 采用了创新的“双轮驱动”方案：
1. **轻量本地提取**：使用 `Faster-Whisper` (Small) 模型，在普通电脑上即可实现秒级响应，完全不卡顿。
2. **云端智能精修**：利用 `DeepSeek-V3` 等顶级 LLM 进行语义纠错。它能听懂上下文，自动修复同音字，补全标点，甚至为你自动分段。

---

## 📊 震撼的对比演示 (Demo)

以 BV1fj6GBhEP5 (心理学相关) 为例：

| 阶段 | 识别内容片段 (部分) | 质量评估 |
| :--- | :--- | :--- |
| **Whisper 原始稿** | "...有几封状态描述的**惊人的遗址**...心理学上这叫**喜德性无助**...**毫补战编**..." | ❌ 惨不忍睹，无法阅读 |
| **Turbo AI 修正后** | "...有几封状态描述**惊人地一致**...心理学上这叫**习得性无助**...**毫不沾边**..." | ✅ 完美精校，直接发布 |

---

## ✨ 核心特性

- ✅ **稳定下载**：弃用 `you-get`，升级为 `yt-dlp`，完美支持 B 站各种视频格式。
- ✅ **极速识别**：基于 `Faster-Whisper` 引擎，速度提升 4 倍以上。
- ✅ **语义纠错**：一键调用 DeepSeek / OpenAI 接口，自动修复同音字、口头禅。
- ✅ **智能排版**：AI 自动分段、添加标点，将凌乱的语音流转化为结构化的文章。
- ✅ **CLI 友好**：支持链接/BV号直接输入，方便集成。

---

## 🛠️ 安装与使用

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/Bili2Text-Turbo.git
cd Bili2Text-Turbo
```

### 2. 环境配置
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 3. 配置 AI 密钥
复制 `.env.example` 为 `.env`，填入你的 DeepSeek 或 OpenAI API Key。
```bash
cp .env.example .env
```

### 4. 运行
```bash
python bili2text_cli.py "https://www.bilibili.com/video/BV1fj6GBhEP5" --model small --correct
```

---

## 🤝 致谢

本项是在 [lanbinleo/bili2text](https://github.com/lanbinleo/bili2text) 的基础上进行的深度优化与功能重构。感谢原作者提供的出色基础！

## 📄 开源协议
[MIT License](LICENSE)
