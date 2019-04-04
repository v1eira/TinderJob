# POO2
Repositório para as atividades referentes ao trabalho da disciplina de POO2


### 1. COMPONENTES

Ewerson Vieira: ewersonv@gmail.com <br>
Jadson Pereira: jadsonpereira121@gmail.com <br>
André Altivo: Andrehdx@gmail.com  <br>
Marcos de Paula: cardepaula@gmail.com <br>

### 2. INTRODUÇÃO E MOTIVAÇAO



### 3. MINI-MUNDO

<inserir o mini mundo>

### 4. TECNOLOGIAS UTILIZADAS <br>

Mockup: Balsamiq <br>
Gerenciamento de projeto e controle de versão: GitHub <br>
Modelagem do banco de dados: brModelo <br>
Banco de dados: Sqlite <br>
Software: desenvolvido em Python, utilizando pyCharm e o framework Django. <br>


### 5. MPC <br> 
https://docs.google.com/drawings/d/1a-0lQvwfUCVxYfxCVV7p6tyMoTpmQ2pI3AYdvLzMa3k/edit

### 6. DIÁRIO DE BORDO <br>
https://docs.google.com/document/d/1jsbV87FM1IgDgYg8sVrKC3exxmWTPYckfMhe58PNbCs/edit

### 7. PROTÓTIPO <br>
https://drive.google.com/drive/folders/1Q0q1J942u3t1DoPic3Kgb_pzQReLMcU0

### 8. Kanban <br>
https://github.com/ewersonv/POO2/projects/1

### 9. Modelo conceitual <br>
<Inserir >
  
### 10. Diagrama de Classes <br>
<Inserir >

### 11. Iniciando o servidor

#### Preparando o ambiente
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
#### Instalandos as dependências
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
#### Rodando o servidor
Coloque o arquivo *.env* em *django/jobTinder* e de o comando seguinte para rodar o servidor.
```bash
(venv) ~$  python manage.py runserver
```
Se tudo estiver certo, no enderoço `http://localhost:8000/` ou `http://127.0.0.1:8000` aparecerá a página padrão do **django**


### Referencias

[Django Girls](https://tutorial.djangogirls.org/pt/)
