import os
import os.path as path
import json
from distutils.dir_util import copy_tree, remove_tree
from distutils.file_util import copy_file
from zipfile import ZipFile
from platform import system
import sys

colors = {
    "DONE": '\033[0;30;42m',
    'INFO': '\033[0;30;44m',
    "ERROR": '\033[0;30;41m',
    "WARNING": '\033[0;30;43m',
    "done": '\033[0;32;40m',
    "info": '\033[0;34;40m',
    "error": '\033[0;31;40m',
    "warning": '\033[0;33;40m',
    "normal": '\033[0;37;40m'
}

HELP_TEXT = """
Usage:
  ppx <command> [options]

Commands:
  list                      Lists all available templates in the system.
  add                       Creates a template. Takes folder name as a parameter. Options [--alias].
  get                       Retrieves template to current directory. Options [--name].
  remove                    Deletes a template. Takes template name as a parameter.
  zip                       Zips every template to current directory. Options [--dir].
  help                      Show help for commands.

General Options:
  -v, --version             Show version and exit.
  -h, --help                Show help.
  -d, --dir <path>          Path for output.
  -n, --name <name>         Name of output directory.
  -a, --alias <alias>       Custom name for template.
"""

OS = system()
APPDATA = path.expanduser("~")
ROOT_STORE = "/AppData/Local" if OS == "Windows" else ""
TEMPLATE_FOLDER = "PPX_Custom_Scripts" if OS == "Windows" else ".PPX_Custom_Scripts"

def get_index():
    return json.load(open(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/index.json","r"))

def save_index_file(content):
    json.dump(content,open(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/index.json","w"), indent=4, sort_keys=True)

def check_storage():
    files = os.listdir(f"{APPDATA}{ROOT_STORE}")
    if TEMPLATE_FOLDER not in files:
        os.mkdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}")
        with open(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/index.json","w") as _:
            _.write(json.dumps({}))
            _.close()
        info("\n\n📁 Created Custom Script folder")

def create_custom_script(_dir):
    pname = _dir.split("\\")[-1]
    files = [_ for _ in os.listdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}") if _ != "index.json"]
    if pname in files:
        warning("\n\n⚠️ Template already exists")
        return
    if path.isdir(_dir):
        os.mkdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}")
        copy_tree(_dir,f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}")
        success(f"\n\n✔️ Created template for {pname}")
    elif path.isfile(_dir):
        #os.mkdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname.split('.')[0]}")
        copy_file(_dir,f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}")
        success(f"\n\n✔️ Created template for {pname}")
    else:
        error("Unknown error")

def clone_template(pname, cloner):
    files = [_ for _ in os.listdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}") if _ != "index.json"]
    if len(files) == 0:
        info("No templates installed")
        return
    alias = get_index()
    if pname not in files and pname not in alias.keys():
        error("There appears to be no Template matching that name")
        return
    if pname in alias.keys():
        pname = alias[pname]
    cwd = os.getcwd()
    if path.isdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}"):
        os.mkdir(f"{cwd}/{pname if cloner == '' else cloner}")
        copy_tree(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}",f"{cwd}/{pname if cloner == '' else cloner}")
    elif path.isfile(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}"):
        copy_file(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}",f"{cwd}/{pname if cloner == '' else cloner}")
    success(f"🚀 Happy Coding!")

def remove_template(pname):
    original = pname
    files = os.listdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}")
    alias = get_index()
    if pname not in files and pname not in alias.keys():
        error("There appears to be no Template matching that name")
        return
    if pname in alias.keys():
        pname = alias[pname]
        del alias[original]
    save_index_file(alias)
    if path.isdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}"):
        remove_tree(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}")
    elif path.isfile(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}"):
        os.remove(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{pname}")
    info(f"\n\n✂️ {pname} template deleted successfully")

def list_templates():
    files = [_ for _ in os.listdir(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}") if _ != "index.json"]
    if len(files) == 0:
        info("\n\n💠 No templates installed")
        return
    alias = get_index()
    keys = [_ for _ in alias.keys()]
    if len(keys) > 0:
        values = [alias[_] for _ in alias.keys()]
    for _file in files:
        i = None
        if len(keys) > 0:
            if _file in values:
                i = keys[values.index(_file)]
        print(f"➡️      {_file}{colors['warning'] +' (File)'+colors['normal'] if path.isfile(f'{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}/{_file}') else ''}{' ↔️ ' + colors['done']+'Alias:' + colors['normal'] + ' %s' % i if i != None else ''}")

def zip_templates(p):
    if p != "":
        if not p.endswith("/"):
            p = f"{p}/"
    with ZipFile(f"{p}template.zip", "w") as _zip:
        for root, dirs, files in os.walk(f"{APPDATA}{ROOT_STORE}/{TEMPLATE_FOLDER}"):
            for _ in files:
                _zip.write(path.join(root,_))
        _zip.close()

def verify_consecutive_options(arg,i=None):
    spawn = ["add", "get", "remove"]
    option = ["--dir", "-d", "--alias", "--name"]
    if arg[0] in spawn:
        if len(arg) > 1:
            if arg[1].startswith("-"):
                error("You must not use consecutive commands. Please check 'ppx help' for more information")
                sys.exit(1)
    if i != None:
        if arg[i - 1] in option:
            if i < len(arg):
                if arg[i].startswith("-"):
                    error("You must not use consecutive commands. Please check 'ppx help' for more information")
                    sys.exit(1)

def warning(message):
    print(f"{colors['WARNING']} WARNING {colors['warning']} {message}{colors['normal']}")

def error(message):
    print(f"{colors['ERROR']} ERROR {colors['error']} {message}{colors['normal']}")

def info(message):
    print(f"{colors['INFO']} INFO {colors['info']} {message}{colors['normal']}")

def success(message):
    print(f"{colors['DONE']} DONE {colors['done']} {message}{colors['normal']}")
