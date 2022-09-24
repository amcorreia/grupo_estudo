# Encontro #01

## Nomenclatura

| | | exemplo de uso | |
|--|--|--|--|
| <> | comando obrigatorio | mkdir <diretorio> | mdkir grupo_estudo |
| [] | comando opcional| ls [diretorio] | ls, ls grupo_estudo |
| \| | lista de argumento alternativo "ou" | route [add\|del\|list] | route add <rota..>, route del <rota..> |


## Comandos basicos Linux

|||
|--|--|
| [ls](https://man7.org/linux/man-pages/man1/ls.1.html) | Lista diretorios |
| [mkdir](https://man7.org/linux/man-pages/man1/mkdir.1.html) | cria um diretorio |
| [pwd](https://man7.org/linux/man-pages/man1/pwd.1.html) | retorna diretorio atual |
| [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) | altera o diretorio atual |
| [rm](https://man7.org/linux/man-pages/man1/mkdir.1.html) | remove arquivo/diretorio(-r) |
| [rmdir](https://man7.org/linux/man-pages/man1/rmdir.1.html) | remove diretorio vazio |
| [mv](https://man7.org/linux/man-pages/man1/mv.1.html) | move ou renomeia arquivo/diretorio |

## Criar chave SSH
>>> ssh-key -t rsa 4096

Adicionar a chave publica ao Github

## Comandos basicos do Git

>>> git add <arquivos>
Adiciona um arquivo ao repositorio

>>> git add -u [arquivos]
Atualiza um arquivo do repositorio (stage)

>>> git clone <repos>
clone de um repositorio

>>> git rm <arquivo>
Remove um arquivo do repositorio (stage)

>>> git checkout
Atualiza os arquivos na arvore de trabalho (repos), ou altera entre branchs

>>> git commit
Grava alteracoes feitas no repositorio

>>> git diff
Mostra diferencas entre os commits

>>> git log
Mostra os registros de log do commit

## Ler sobre git-flow
https://danielkummer.github.io/git-flow-cheatsheet/

