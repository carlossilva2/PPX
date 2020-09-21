translations = {
    "english": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "test": "Hello ${word}, I am ${word}"
    },
    "portuguese": {
        "missing_template": "É necessário o nome do template",
        "missing_directory": "É necessário uma pasta para copiar os ficheiros",
        "i18n_missing_par": "Argumentos em falta para tradução",
        "test": "Olá ${word}, eu sou o ${word}"
    },
    "spanish": {
        "missing_template": "",
        "missing_directory": "",
        "i18n_missing_par": "",
        "test": "Hello ${word}, I am ${word}"
    }
}

def get_translation(lang,key):
    #TODO: add verification
    return translations[lang][key]