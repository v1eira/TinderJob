# POO2
Repositório para as atividades referentes ao trabalho da disciplina de POO2

# Iniciando o servidor

## Preparando o ambiente
Entre no diretorio *./django*.
```bash
$ cd ./django
```
Crie um [virtualenv](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais), para encapsular o projeto e não instalar os pacotes globalmente.

```bash
$ python3 -m venv venv
```
Ative o virtualenv.
```bash
$ source venv/bin/activate
ou
$ . venv/bin/activat
```
## Instalandos as dependências
Primeiro, garanta que o pip instalado esteja na ultima versão
```bash
(venv) ~$ python3 -m pip install --upgrade pip
```
Depois instale as dependências
```bash
(venv) ~$ sudo pip install -r requirements.txt
```
OBS: Para desativar o *virtualenv*:
```bash
(venv) ~$ deactivate
```
## Rodando o servidor
Coloque o arquivo *.env* em *django/jobTinder* e de o comando seguinte para rodar o servidor.
```bash
(venv) ~$  python manage.py runserver
```
Se tudo estiver certo, no enderoço `http://localhost:8000/` ou `http://127.0.0.1:8000` aparecerá a página padrão do **django**


# Referencias

[Django Girls](https://tutorial.djangogirls.org/pt/)
