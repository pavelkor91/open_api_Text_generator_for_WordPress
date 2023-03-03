import openai
import os
import pandas as pd
from dotenv import load_dotenv 


load_dotenv()
df = pd.read_excel('input.xlsx')

openai.api_key = os.getenv('API_KEY')


model = os.getenv('MODEL')
temperature = float(os.getenv('TEMPERATURE'))
max_tokens_text = int(os.getenv('MAX_TOKEN_TEXT_BLOCK'))
max_toke_title = os.getenv('MAX_TOKEN_TITLE')
top_p = int(os.getenv('TOP_P'))
frequency_penalty = float(os.getenv('FREQUENCY_PENALTY'))
presence_penalty = float(os.getenv('PRESENCE_PENALTY'))
stop = None


def openAI_generate(promt):
    successful = False
    while not successful:
        try:
            text = openai.Completion.create(
                engine=model,
                prompt=promt,
                temperature=temperature,
                max_tokens=max_tokens_text,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop
            )
            successful = True
            return text.choices[0].text
        except Exception as e:
                print(e)
                successful = False
     

def generate_texts():
    for index, row in df.iterrows():
        title_promt =(
            f'Please write an interesting title on the topic {row["title"]}.'
            f'Use only {row["language"]} language.'
        )
        title = openAI_generate(title_promt)
        text_blocks = []
        params_blocks = {}
        for k,v in enumerate(row):
            if 'text_block' in df.columns.values[k]:
                text_blocks.append(v)
            elif 'param' in df.columns.values[k]:
                params_blocks[df.columns.values[k]] = str(v)
        title = title.replace('\n','')
        text = f'TITLE{title}!TITLE'
        for text_block in text_blocks:
            for word, replacement in params_blocks.items():
                text_block = text_block.replace(word,replacement)
    
            text += f'\n {openAI_generate(text_block)}'
        
        with open(f'results/{index}.txt', 'w', encoding='utf-8') as f:
            f.write(text)
            
if __name__ == '__main__':
    generate_texts()