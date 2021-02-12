# Meme Generator
## Overview
This is meme generator, it combines text with image to create memes.
The aplication can be split in three parts: engine of the application, console app and web app - 
it can be use as a consol app and as web app as well.
It contians its own base of images and quotes, but it also allow user to provide its own.

## Set up
Requirements are save in requirements.txt, so can be install using pip:

```bash
pip install -r requirements.txt
```
PDF parser use pdftotext command application, this could be install on Linux

```bash
sudo apt-get install libpoppler-dev
```

## Description 
This application is spilted into: 
- QuoteEngine - module that handels parsing quotes from various type of files. It contains QuoteModel class to build quotes objects,
abstract IngestorInterface class and its subclasses that handel parsing for various type of files; 
- MemeGenerator - module that generate memes, it contain MemeEngine class that build meme;
- meme.py - this file contains console version of meme generator app;
- app.py - this is web meme generator app based on flask.