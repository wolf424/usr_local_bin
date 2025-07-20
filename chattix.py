# #####################################################
# IMPORT

from openai import OpenAI
import os
import sys
import re
import pyperclip
import argparse
from os.path import exists
import textwrap

# #####################################################
# PARSE COMMAND LINE ARGUMENTS

parser = argparse.ArgumentParser(description='Aide shell par chatGPT.')
parser.add_argument('question', type=str, help='Une question sur le shell linux.')
parser.add_argument('-v', '--verbose', action='store_true', help='Mode verbeux.')
parser.add_argument('-e', '--expert', action='store_true', help='J\'ai un niveau expert')
parser.add_argument('--style', choices=['gitan', 'chat', "grossier","sexy","triste","boomer","technocrate","verlan","louchebem","lacan","audiard"], required=False, help='Style verbal')
args = parser.parse_args()

# Question to chatGPT
question = args.question

# User is expert ? (default : no)
if args.expert:
    niveau="J'ai un niveau expert"
else:
    niveau="J'ai un niveau débutant"

consigne_style=""
if args.style == 'gitan':
    consigne_style = "\nParle moi comme si on était tous les deux des gitans, avec des métaphores en lien avec la culture des gens du voyage."
elif args.style == 'chat':
    consigne_style = "\nImagine que tu es un chat, Pponctue tes phrase par des miaulements et fais des allusions à tes centres d'intérêt de chat."
elif args.style == 'grossier':
    consigne_style = "\nParle moi comme si tu étais un grossier personnage, méprisant et vulgaire. Ponctue tes phrases avec des insultes ou des onomatopées de rôt et de pets."
elif args.style == 'sexy':
    consigne_style = "\nParle moi comme si tu étais une fille qui essaie de me séduire. Complimente moi sur mon physique."
elif args.style == 'triste':
    consigne_style = "\nParle moi comme si tu étais très déprimé, au bout de ta vie. Intercale des phrases pour me dire combien tu vas mal."
elif args.style == 'boomer':
    consigne_style = "\nParle moi comme si tu étais un vieux boomer complètement dépassé par l'informatique et le progrès. Ajoute des phrase pour me dire combien tout était mieux de ton temps."
elif args.style == 'technocrate':
    consigne_style = "\nParle moi dans un langage technocratique, comme si un politique faisait un discours aride meublé avec des phrases creuses. Use de la langue de bois."
elif args.style == 'verlan':
    consigne_style = "\nParle moi en verlan, à la manière d'un jeune des cités dans les années 80. Fais des allusions aux objets à la mode chez les jeunes dans les années 80."
elif args.style == 'louchebem':
    consigne_style = "\nParle moi en louchebem, comme si tu étais un boucher à l'ancienne."
elif args.style == 'lacan':
    consigne_style = "\nParle moi comme si tu étais un vieux psychanalyste lacanien, pédant et imbu de sa personne. Utilise du jargon propre à Lacan. A la fin, demande à l'utilisateur de payer cette séance, de préférence en espèces."
elif args.style == 'audiard':
    consigne_style = "\nImagine que tu es un parain gangster dans un film d'audiard. Tu t'exprime à la manière des tontons flingueurs."

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

columns = os.get_terminal_size().columns
    
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
Réponds à la question (sans l'afficher). Si nécessaire, écris la commande shell à taper, dans une ligne à part, en commençant par le symbole $\n\
Texte simple uniquement, pas de markdown.{}".format(context,niveau,uname,shell,user,pwd,files,question,consigne_style)

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

# Print each line.
for line in answer.splitlines():
    if line.startswith("$ "):
        print(custom_colors.SHELL + line + bcolors.ENDC)
        line = re.sub("^\$ ","",line)
        try:
            pyperclip.copy(line)
        except:
            if args.verbose:
                print (custom_colors.VERBOSE + "Copie vers presse-papier impossible" + bcolors.ENDC)

    else:
        # Wrap this text.
        wrapper = textwrap.TextWrapper(width=columns)
        word_list = wrapper.wrap(text=line)
        for element in word_list:
            print(element)
