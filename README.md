# 🚀 Bili2Text-Turbo

聚焦：B站视频转文字. bilibili视频转文字.AI.大模型.

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

## ❓ 常见问题 (FAQ)

### 1. 为什么默认不建议使用 `large-v3` 模型？
虽然 `large-v3` 识别率最高，但其参数量巨大（约 1.5GB），在没有高端显卡的普通电脑（如 Mac Air 或办公本）上运行会占用极高资源，导致系统严重卡顿甚至崩溃。
**Bili2Text-Turbo** 的核心理念是：**让本地干脏活（提取），让云端干细活（纠错）**。使用 `small` 模型配合 `DeepSeek-V3` 纠错，识别准确率完全不输甚至超越 `large-v3` 直接输出的结果，且运行极其流畅。

### 2. DeepSeek API Key 贵吗？
**极其便宜！**
DeepSeek-V3 是目前公认的性价比之王。处理一个 10 分钟视频的文字纠错，消耗的 Token 成本通常不到 **0.01 元人民币**（一分钱都不到）。新用户注册通常还会获赠 1000 万左右的免费 Token，基本等于白嫖。

### 3. 支持哪些视频格式？
由于底层使用了 `yt-dlp` 和 `moviepy`，本项目支持 B 站几乎所有的视频格式，包括 `.mp4`, `.webm`, `.flv`, `.mkv` 等。

### 4. 我可以在其他平台（如 Windows）运行吗？
当然可以！只要安装了 Python 3.9+ 和 FFmpeg，该工具即可在 Windows, macOS, Linux 上完美运行。

---

## 🤝 致谢

本项是在 [lanbinleo/bili2text](https://github.com/lanbinleo/bili2text) 的基础上进行的深度优化与功能重构。感谢原作者提供的出色基础！

## 📄 开源协议
[MIT License](LICENSE)
