import locale
from .translations import get_translation
from .utils import info, success, error, warning
import sys

__trigger = "${word}"

locales = {
    "default": "english",
    "english": [
        "en_gb",
        "en_us",
        "en_ca"
    ],
    "portuguese": [
        "pt_pt",
        "pt_br",
    ],
    "spanish": [
        "es_es",
        "es_mx",
        "es_ve"
    ]
}

current_locale = locale.getdefaultlocale()[0].lower()
language = None
for _ in locales.keys():
    if current_locale in locales[_]:
        language = _
        break
if language == None:
    language = locales['default']

def i18n(invoque, *args):
    original = get_translation(language,invoque).split(" ")
    _replacers = len(args)
    original_indexes = [i for i,w in enumerate(original) if __trigger in w]
    if _replacers != len(original_indexes):
        info(get_translation(language, "i18n_missing_par"))
        sys.exit(1)
    if len(original_indexes) > 0:
        l = 0
        for i in original_indexes:
            original[i] = original[i].replace(__trigger,args[l])
            l += 1
    return " ".join(original)