#!/home/alexandra/.venvs/MyEnv/bin/python

# #####################################################
# IMPORT

from openai import OpenAI
import os
import sys
import re
import pyperclip
import argparse
from os.path import exists

# #####################################################
# PARSE COMMAND LINE ARGUMENTS

parser = argparse.ArgumentParser(description='Aide shell par chatGPT.')
parser.add_argument('question', type=str, help='Une question sur le shell linux.')
parser.add_argument('-v', '--verbose', action='store_true', help='Mode verbeux.')
parser.add_argument('-e', '--expert', action='store_true', help='J\'ai un niveau expert.')
args = parser.parse_args()

# Question to chatGPT
question = args.question

# User is expert ? (default : no)
if args.expert:
    niveau="J'ai un niveau expert"
else:
    niveau="J'ai un niveau débutant"


# #####################################################
# CONST

# Colors
class bcolors:
    T_BLACK = '\033[90m'
    T_RED = '\033[91m'
    T_GREEN = '\033[92m'
    T_YELLOW = '\033[93m'
    T_BLUE = '\033[94m'
    T_PURPLE = '\033[95m'
    T_CYAN = '\033[96m'
    T_WHITE = '\033[97m'
    B_BLACK = '\033[40m'
    B_RED = '\033[41m'
    B_GREEN = '\033[42m'
    B_YELLOW = '\033[43m'
    B_BLUE = '\033[44m'
    B_PURPLE = '\033[45m'
    B_CYAN = '\033[46m'
    B_WHITE = '\033[47m'
    S_NORMAL = '\033[0m'
    S_BOLD = '\033[1m'
    S_LIGHT = '\033[2m'
    S_ITALIC = '\033[3m'
    S_UNDERLINE = '\033[4m'
    S_BLINK = '\033[5m'
    ENDC = '\033[0m'

# Custom colors
class custom_colors:
    STANDARD = bcolors.ENDC
    VERBOSETITLE = bcolors.T_GREEN + bcolors.S_LIGHT + bcolors.S_ITALIC + bcolors.S_UNDERLINE
    VERBOSE = bcolors.ENDC + bcolors.T_GREEN + bcolors.S_LIGHT + bcolors.S_ITALIC
    READFILE = bcolors.T_RED + bcolors.S_LIGHT + bcolors.S_ITALIC
    SHELL = bcolors.T_WHITE + bcolors.S_BOLD
    

# GPT settings
GPT_ROLE = "Tu es un sysadmin linux, professeur d'informatique et excellent pédagogue. Tu me tutoies"

# #####################################################
# GET CONTEXT

uname = os.uname()
shell = os.environ['SHELL']
home = os.environ['HOME']
user = os.getlogin()
pwd = os.getcwd()
files = os.listdir(pwd)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if args.verbose:
    print (custom_colors.VERBOSETITLE + "uname :" + custom_colors.VERBOSE + " {}".format(uname) + bcolors.ENDC)
    print (custom_colors.VERBOSETITLE + "shell :" + custom_colors.VERBOSE + " {}".format(shell) + bcolors.ENDC)
    print (custom_colors.VERBOSETITLE + "home :" + custom_colors.VERBOSE + " {}".format(home) + bcolors.ENDC)
    print (custom_colors.VERBOSETITLE + "user :" + custom_colors.VERBOSE + " {}".format(user) + bcolors.ENDC)
    print (custom_colors.VERBOSETITLE + "pwd :" + custom_colors.VERBOSE + " {}".format(pwd) + bcolors.ENDC)
    print (custom_colors.VERBOSETITLE + "files :" + custom_colors.VERBOSE + " {}".format(files) + bcolors.ENDC)

# #####################################################
# 

def config_file_needed (question, fname):
    prompt = "Ma question est : \"{}\"\n\
    Le contenu de mon fichier {} peut-il contribuer à améliorer ta réponse ?\n\
    Réponds simplement par oui ou non".format(question, fname)
    
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system",
             "content": GPT_ROLE},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 1000,  # Maximum output length
        temperature = 1)  # Temperature rate of determinism (0 = highly deterministic, 2 = random)
    
    # Extracting the Models Answer
    answer = response.choices[0].message.content
    return re.search('oui', answer, re.IGNORECASE)

# #####################################################
# évaluation du contexte nécessaire

context = "# Voici le contexte\n"

config_fnames = ["/etc/fstab", "/etc/hosts", "/etc/resolv.conf", "/etc/passwd", "/etc/group", "{}/.bashrc".format(home), "{}/.bash_aliases".format(home)]

for fname in config_fnames:
    if exists(fname):
        if config_file_needed (question, fname):
            print(custom_colors.READFILE + "Je consulte {}\n".format(fname) + bcolors.ENDC)
            context = "{}\n# Contenu de mon fichier {}\n".format(context,fname)
            with open(fname) as f:
                context = context + f.read()
    
# #####################################################
# prompt contextualisé

prompt = "Je vais te poser une question au sujet de mon environnement linux.\n\
{}\n\
J'ai un niveau {}\n\
Un uname -a me donne ceci : {}\n\
Mon shell est : {}\n\
Je suis l'utilisateur : {}\n\
Mon répertoire courant est : {}\n\
Il contient les fichiers suivants : {}\n\
Voici ma question: \"{}\"\n\
Réponds à la question (sans l'afficher). Si nécessaire, écris la commande shell à taper en commençant la ligne par le symbole $\n\
Texte simple uniquement, pas de markdown.".format(context,niveau,uname,shell,user,pwd,files,question)

if args.verbose:
    print (custom_colors.VERBOSE + "# PROMPT :\n{}\n".format(prompt) + bcolors.ENDC)

response = client.chat.completions.create(
  model = "gpt-4o",
  messages = [
        {"role": "system",
         "content": GPT_ROLE},
        {"role": "user", "content": prompt}
    ],
  max_tokens = 1000,  # Maximum output length
  temperature = 1)  # Temperature rate of determinism (0 = highly deterministic, 2 = random)

# Extracting the Models Answer
answer = response.choices[0].message.content

for line in answer.splitlines():
    if line.startswith("$ "):
        print(custom_colors.SHELL + line + bcolors.ENDC)
        line = re.sub("^\$ ","",line)
        pyperclip.copy(line)
    else:
        print(line)
