import os
import os.path as path
import sys
import json
from .utils import *
from .internationalization import i18n

__version__ = "0.1.1"

def main():
    check_storage()
    args = sys.argv[1:]
    if len(args) == 0:
        print(HELP_TEXT)
        sys.exit(1)
    if args[0] == "add":
        verify_consecutive_options(args)
        if len(args) == 1:
            error(i18n("no_dir_temp"))
            sys.exit(1)
        if args[1] != ".":
            _list = os.listdir()
            if args[1] not in _list:
                error(i18n("file_not_found"))
                sys.exit(1)
        _dir = os.getcwd() if args[1] == "." else f"{os.getcwd()}\\{args[1]}"
        pname = os.getcwd().split("\\")[-1] if args[1] == "." else args[1]
        if "--alias" in args or "-a" in args:
            i = args.index("--alias") + 1 if "--alias" in args else args.index("-a") + 1
            verify_consecutive_options(args,i)
            _file = get_index()
            if i < len(args):
                name = args[i]
                if name not in _file.keys():
                    _file[name] = pname
                    save_index_file(_file)
                else:
                    error(i18n("existing_alias"))
                    sys.exit(1)
            else:
                error(i18n("alias_required"))
                sys.exit(1)
        create_custom_script(_dir)
    elif args[0] == "get":
        verify_consecutive_options(args)
        if len(args) == 1:
            error(i18n("missing_template"))
            sys.exit(1)
        template = args[1]
        n = None
        if "--name" in args or "-n" in args:
            i = args.index("--name") + 1 if "--name" in args else args.index("-n") + 1
            verify_consecutive_options(args,i=i)
            n = args[i]
        clone_template(template, "" if n == None else n)
    elif args[0] == "help" or args[0] == "-h" or args[0] == "--help":
        print(HELP_TEXT)
    elif args[0] == "list":
        list_templates()
    elif args[0] == "remove":
        verify_consecutive_options(args)
        if len(args) == 1:
            error(i18n("missing_template"))
            sys.exit(1)
        template = args[1]
        remove_template(template)
    elif args[0] == "-v" or args[0] == "--version":
        print(__version__)
    elif args[0] == "zip" or args[0] == "-z":
        p = ""
        if "--dir" in args:
            i = args.index("--dir") + 1
            if i < len(args):
                p = args[i]
            else:
                error(i18n("missing_directory"))
                sys.exit(1)
        if "-d" in args:
            i = args.index("--dir") + 1
            if i < len(args):
                p = args[i]
            else:
                error(i18n("missing_directory"))
                sys.exit(1)
        zip_templates(p)
    elif args[0] == "settings":
        open_settings()
    else:
        warning(i18n("unknown_option",args[0]))

if __name__ == "__main__":
    main()