import argparse
import sys
import re
import os
from utils import download_video
from exAudio import process_audio_split
import speech2text

def extract_bv(input_str):
    pattern = r'BV[A-Za-z0-9]+'
    matches = re.findall(pattern, input_str)
    if matches:
        return matches[0]
    return None

def main():
    parser = argparse.ArgumentParser(description="Bili2Text CLI Tool")
    parser.add_argument("input", help="Bilibili video URL or BV number")
    parser.add_argument("--model", default="small", choices=["tiny", "base", "small", "medium", "large", "large-v3"], help="Whisper model size (default: small)")
    parser.add_argument("--prompt", default="以下是普通话的句子。", help="Initial prompt for Whisper (default: 以下是普通话的句子。)")
    parser.add_argument("--correct", action="store_true", help="Enable AI correction (currently a placeholder for integration)")
    
    args = parser.parse_args()
    
    bv_number = extract_bv(args.input)
    if not bv_number:
        print(f"Error: Could not extract BV number from '{args.input}'")
        sys.exit(1)
    
    print(f"Target BV: {bv_number}")
    
    # 1. Download
    print("=" * 20)
    print("Step 1: Downloading video...")
    file_id = download_video(bv_number)
    if not file_id:
        print("Error: Failed to download video.")
        sys.exit(1)
        
    # 2. Process Audio
    print("=" * 20)
    print("Step 2: Processing audio (extracting and splitting)...")
    try:
        folder_name = process_audio_split(file_id)
    except Exception as e:
        print(f"Error processing audio: {e}")
        sys.exit(1)
        
    # 3. Transcribe
    print("=" * 20)
    print(f"Step 3: Transcribing with Faster-Whisper ({args.model})...")
    speech2text.load_whisper(model=args.model)
    output_file_raw = speech2text.run_analysis(folder_name, model=args.model, prompt=args.prompt)
    
    print("=" * 20)
    print(f"Success! Raw transcription saved to: {output_file_raw}")

    # 4. Correct
    if args.correct:
        from correct_text import ai_correct_file
        output_file_final = ai_correct_file(output_file_raw)
        print(f"Corrected transcription saved to: {output_file_final}")

if __name__ == "__main__":
    main()
