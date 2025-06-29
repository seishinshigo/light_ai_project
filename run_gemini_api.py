#!/usr/bin/env python3
from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai
import os, argparse, sys

load_dotenv(Path(__file__).with_name(".env"))
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("API KEY not found (.env)")

genai.configure(api_key=API_KEY)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prompt", required=True)
    parser.add_argument("-m", "--model", default=os.getenv("GEMINI_MODEL", "gemini-2.5-pro"))
    args = parser.parse_args()

    model = genai.GenerativeModel(args.model)
    res = model.generate_content(args.prompt)
    print(res.text)

if __name__ == "__main__":
    main()
