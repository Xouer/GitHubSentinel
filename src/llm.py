# src/llm.py

import os
from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI(api_key="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")

    def generate_daily_report(self, markdown_content, dry_run=False):
        prompt = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；:\n\n{markdown_content}"
        if dry_run:
            with open("daily_progress/prompt.txt", "w+", encoding='utf-8') as f:
                f.write(prompt)
            return "DRY RUN"

        print("Before call GPT")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        print("After call GPT")
        print(response)
        return response.choices[0].message.content
