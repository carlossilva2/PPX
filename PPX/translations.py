translations = {
    "english": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "unknown_option": "Usage:\n  ppx <command> [options]\n\nNo such option: ${word}",
        "existing_alias": "Alias already present. Please use another alias for this template",
        "created_template": "✔️ Created template for ${word}",
        "custom_folder": "📁 Created Custom Template folder",
        "no_templates": "💠 No templates installed",
        "no_match": "There appears to be no Template matching that name",
        "consecutive_command": "You must not use consecutive commands. Please check 'ppx help' for more information",
        "delete": "✂️ ${word} template deleted successfully",
        "template_exists": "⚠️ Template already exists",
        "no_dir_temp": "You must provide a directory/template",
        "file_not_found": "No such File or Directory",
        "alias_required": "An Alias name must be provided"
    },
    "portuguese": {
        "missing_template": "É necessário o nome do template",
        "missing_directory": "É necessário uma pasta para copiar os ficheiros",
        "i18n_missing_par": "Argumentos em falta para tradução",
        "unknown_option": "Utilização:\n  ppx <comando> [opções]\n\nNão existe esta opção: ${word}",
        "existing_alias": "Este Alias já existe. Por favor utilize outro Alias para este template",
        "created_template": "✔️ Template criado ${word}",
        "custom_folder": "📁 Pasta para Templates criada",
        "no_templates": "💠 Não existe nenhum Template instalado",
        "no_match": "Não foi encontrado nenhum Template com esse nome",
        "consecutive_command": "O uso de comandos sucessivos não é permitido. Usa 'ppx help' para mais informações",
        "delete": "✂️ O Template ${word} foi apagado com sucesso",
        "template_exists": "⚠️ O Template já existe no sistema",
        "no_dir_temp": "Deve indicar uma diretoria/template",
        "file_not_found": "Ficheiro ou diretoria não encontrada",
        "alias_required": "É necessário indicar um Alias para o template"
    },
    "spanish": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "unknown_option": "\n\nUsage:\n  ppx <command> [options]\n\nNo such option: ${word}",
        "existing_alias": "Alias already present. Please use another alias for this template",
        "created_template": "\n\n✔️ Created template for ${word}",
        "custom_folder": "\n\n📁 Created Custom Template folder",
        "no_templates": "\n\n💠 No templates installed",
        "no_match": "There appears to be no Template matching that name",
        "consecutive_command": "You must not use consecutive commands. Please check 'ppx help' for more information",
        "delete": "\n\n✂️ ${word} template deleted successfully",
        "template_exists": "\n\n⚠️ Template already exists"
    },
    "german": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "unknown_option": "\n\nUsage:\n  ppx <command> [options]\n\nNo such option: ${word}",
        "existing_alias": "Alias already present. Please use another alias for this template",
        "created_template": "\n\n✔️ Created template for ${word}",
        "custom_folder": "\n\n📁 Created Custom Template folder",
        "no_templates": "\n\n💠 No templates installed",
        "no_match": "There appears to be no Template matching that name",
        "consecutive_command": "You must not use consecutive commands. Please check 'ppx help' for more information",
        "delete": "\n\n✂️ ${word} template deleted successfully",
        "template_exists": "\n\n⚠️ Template already exists"
    },
    "french": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "unknown_option": "\n\nUsage:\n  ppx <command> [options]\n\nNo such option: ${word}",
        "existing_alias": "Alias already present. Please use another alias for this template",
        "created_template": "\n\n✔️ Created template for ${word}",
        "custom_folder": "\n\n📁 Created Custom Template folder",
        "no_templates": "\n\n💠 No templates installed",
        "no_match": "There appears to be no Template matching that name",
        "consecutive_command": "You must not use consecutive commands. Please check 'ppx help' for more information",
        "delete": "\n\n✂️ ${word} template deleted successfully",
        "template_exists": "\n\n⚠️ Template already exists"
    },
    "italian": {
        "missing_template": "You must provide a template",
        "missing_directory": "An output directory must be provided",
        "i18n_missing_par": "Missing or Extra words required",
        "unknown_option": "\n\nUsage:\n  ppx <command> [options]\n\nNo such option: ${word}",
        "existing_alias": "Alias already present. Please use another alias for this template",
        "created_template": "\n\n✔️ Created template for ${word}",
        "custom_folder": "\n\n📁 Created Custom Template folder",
        "no_templates": "\n\n💠 No templates installed",
        "no_match": "There appears to be no Template matching that name",
        "consecutive_command": "You must not use consecutive commands. Please check 'ppx help' for more information",
        "delete": "\n\n✂️ ${word} template deleted successfully",
        "template_exists": "\n\n⚠️ Template already exists"
    }
}

def get_translation(lang,key):
    if lang in translations.keys():
        if key in translations[lang].keys():
            return translations[lang][key]
    return ""