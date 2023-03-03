
# Scripts for generating openai text and uploading it to the WordPress site






## Installation

Clone repo and create venv in folder:

```bash
  python -m venv venv
```

activate venv:

```bash
  cd venv/Scripts/
  ./Activate
```

```bash
  ./Activate
```

```bash
  cd ../..
```

Install all requirements:

```bash
  pip install -r requirements.txt
```

Create .env file in folder


## .env variables

You need to add all variables in .env file:

```bash
    #API openai
    API_KEY = 'sk-'
    #Model for openai
    MODEL = 'text-davinci-003'
    #temperature for openai
    TEMPERATURE = 0
    #max size for text block in tokens
    MAX_TOKEN_TEXT_BLOCK = 2000
    TOP_P = 1
    FREQUENCY_PENALTY = 0
    PRESENCE_PENALTY = 0

    #
    ROOT = 'https://site.com/'
    user = 'admin'
    password = 'password' 
```

P.S. Your WordPress site must work with API. 


## Fill input.xls file

For bulk content create u need to fill excel file. 

Required fields:

```bash
    language
    title
    text_block_1
    param_
```

you need to use at least one text_block coulmn for prompt OpenAI. To build some custom prompts you can add param colums in text_blocks. 


## Usage/Examples

Generate texts. it will be save in results folder.
```bash
   python Text-OpenAI.py
```

Upload texts to WordPress site:

```bash
   python wp-api.py
```
