# POO2
Repositório para as atividades referentes ao trabalho da disciplina de POO2


### 1. COMPONENTES

André Altivo: Andrehdx@gmail.com  <br>
Ewerson Vieira: ewersonv@gmail.com <br>
Jadson Pereira: jadsonpereira121@gmail.com <br>
Marcos de Paula: cardepaula@gmail.com <br>

### 2. INTRODUÇÃO E MOTIVAÇAO



### 3. MINI-MUNDO

<inserir o mini mundo>

### 4. TECNOLOGIAS UTILIZADAS <br>

Mockup: Mockplus <br>
Gerenciamento de projeto e controle de versão: GitHub <br>
Modelagem do banco de dados: brModelo <br>
Banco de dados: Sqlite <br>
Software: desenvolvido em Python, utilizando pyCharm e o framework Django. <br>


### 5. PMC <br> 
https://docs.google.com/drawings/d/1a-0lQvwfUCVxYfxCVV7p6tyMoTpmQ2pI3AYdvLzMa3k/edit

### 6. DIÁRIO DE BORDO <br>
[Diário de bordo](https://docs.google.com/document/d/1jsbV87FM1IgDgYg8sVrKC3exxmWTPYckfMhe58PNbCs/edit)

### 7. PROTÓTIPO <br>
[Mockup](https://drive.google.com/drive/folders/1Q0q1J942u3t1DoPic3Kgb_pzQReLMcU0)

### 8. Kanban <br>
[Tarefas](https://github.com/ewersonv/POO2/projects/1)

### 9. Modelo conceitual <br>
<Inserir >

### 10. Requisitos <br>
#### Requisitos Não Funcionais
| Identificador | Descrição | Categoria | Escopo |
|--|--|--|--|
|RNF001| O aplicativo deverá funcionar em aparelhos mobile Android e IOS |Portabilidade|Funcionalidade|
|RNF002| É necessária conexão com a internet para a funcionalidade do aplicativo |Estabilidade|Sistema|
|RNF003| O Sistema precisa reconhecer se a pessoa é fisica ou juridica, pois possuem autorizações diferentes |Autorização|Sistema|
|RNF004| O Candidato, caso pessoa física, poderá conectar com contas como Linkedin e Freelancer para poder informar trabalhos anteriores |Interoperabilidade|Funcionalidade|
|RNF005| O sistema exigirá aos usuários apenas detalhes técnicos como experiência e outros empregos|Proteção contra erros do usuário|Sistema|
|RNF006| O sistema pode ser atualizado com novas profissões |Modificabilidade|Funcionalidade|
|RNF007| O sistema armazena matchs, conversas e criações de vagas em banco de dado |Analisabilidade|Sistema|
|RNF008| O sistema consulta o CPF e o CNPJ do cadastrado para validar o cadastro |Autenticação|Sistema|
  
### 11. Diagrama de Classes <br>
![alt text](https://raw.githubusercontent.com/ewersonv/POO2/master/arquivos/JobTinder.png)

### 12. Iniciando o servidor

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
