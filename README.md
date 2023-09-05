
![Logo](https://github.com/beephole/BulkPromptGen/assets/118709832/3f5c5d3e-e8cc-411b-85bb-58cd8ae3257d)



# BulkPromptGen

This repository provides a Python script to generate images using prompts from a CSV file via the Bing Image Creator CLI tool.
You can generate different prompts using Ai Chats and simply paste them in csv file and run the script !

## Demo


https://github.com/beephole/BulkPromptGen/assets/118709832/93d555c8-0f78-49ed-9b21-a5621fb0a33e



## Features

- Reads prompts from a CSV file
- Generates 4 images per prompt using Bing Image Creator
- Light/dark mode toggle
- Saves images to a directory named with today's date
- Adds a timeout between requests to avoid issues
- Tracks total number of images generated across runs

### Before Installing
#### Grab the Bing _U Cookie
Before we install we need to get the _U Cookie , Go to [Bing.com](https://www.bing.com/search?form=WSBCTB&toWww=1&redig=A5BDD77E0AC143EBB9DB7E15C688C0E3&q=What+can+the+new+Bing+chat+do%3f&showconv=1) and pres F12 for developer tool, then under Application , under Cookies , get the _U cookie and paste it to the script as in vid below !

https://github.com/beephole/BulkPromptGen/assets/118709832/c3c25bf6-0e71-459f-b20b-f6be1cbb2025


## Install and Run Locally

Clone the project

```bash
  git clone https://github.com/beephole/BulkPromptGen.git
```

Go to the project directory

```bash
  cd BulkPromptGen
```

Install dependencies

```bash
  pip install -r requirements.txt
```
```bash
  pip3 install --upgrade BingImageCreator
```
Start the app

```bash
  python main.py
```


# Hi, I'm [Beephole](https://twitter.com/b33ph0l3!) 👋



## 🚀 About Me
Will you soar high as the king of the sky or buzz right by like a fly on the shit pie?

### 🔗 Links

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/b33ph0l3)


### Acknowledgements

  Credits goes [ @acheong08 ](https://github.com/acheong08) for making BingImageCreator CLI tool
 
 - Install  [BingImageCreator](https://github.com/acheong08/BingImageCreator.git)

```bash
  pip3 install --upgrade BingImageCreator
```
    
