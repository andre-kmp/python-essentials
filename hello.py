#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente, 
o programa exibe a mensagem correspondente.

Observações iniciais:

O curso Python Essentials está sendo ministrado em Linux e eu
uso Windows. Por isso, algumas adaptações precisaram ser feitas.
Todos os meus códigos terão que rodar em Windows.

Como usar:

Importe a biblioteca locale
Tenha a variável LANG devidamente configurada. Exemplo:
    
    import locale
    LANG =  locale.getdefaultlocale()[0]

Execução:

	python3 hello.py
	ou
	hello.py
"""
__version__ = "0.0.1"
__author__ = "André Klaic"
__license__ = "Unlicense"

import locale

current_language = locale.getdefaultlocale()[0]

msg = "Hello, World!"


if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "en_US":
	msg = "Hello, World!"
else
    msg = ":( Please wait until we are ready for your system :("



print(msg)