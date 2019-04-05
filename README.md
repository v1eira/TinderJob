# POO2
Repositório para as atividades referentes ao trabalho da disciplina de POO2


### 1. COMPONENTES

André Altivo: Andrehdx@gmail.com  <br>
Ewerson Vieira: ewersonv@gmail.com <br>
Jadson Pereira: jadsonpereira121@gmail.com <br>
Marcos de Paula: cardepaula@gmail.com <br>

### 2. INTRODUÇÃO E MOTIVAÇAO
Hoje, no Brasil, existem [12,7 milhões de desempregados](https://g1.globo.com/economia/noticia/2019/02/27/desemprego-sobe-para-12-em-janeiro-diz-ibge.ghtml). É verdade que o mercado para profissionais de TI segue aquecido apesar desse número alarmante de desempregados em nossa sociedade. Porém, nota-se a falta de um canal unificado, para divulgação de vagas de emprego, por parte das empresas, e procura de vagas de emprego, por parte dos profissionais.

Usualmente, empresas divulgam suas vagas em seus sites, grupos em redes sociais ou em plataformas terceirizadas de vagas de emprego. No modelo atual, as empresas cadastram suas vagas nessas plataformas e os profissionais procuram por elas, geralmente tendo que assinar a plataforma em questão para ter acesso à mais informações sobre as vagas e a empresa.

Analisando esse cenário, tivemos a ideia de criar uma plataforma que facilitasse esse acesso às vagas, por parte dos candidatos, e à profissionais qualificados por parte das empresas. A ideia é que em nossa plataforma, com apenas alguns cliques, tanto empresas quanto candidatos, possam encontrar sua parte correspondente com facilidade, afetando até mesmo a forma como os profissionais de RH dessas empresas se comunicam com novos talentos e os recrutam.

Com isso, pretendemos ser a principal plataforma na busca e divulgação de vagas de emprego. Num primeiro momento focando apenas em vagas para profissionais de TI, mas podendo expandir o escopo para outras profissões, chegando até mesmo a ser uma plataforma universal para procura e divulgação de qualquer tipo de vaga de emprego.


### 3. MINI-MUNDO
Observando as formas que as empresas, nos dias de hoje, divulgam suas vagas de emprego e como os profissionais de TI procuram estas vagas, pensamos na criação de uma plataforma que pudesse unificar, facilitar e agilizar esse processo tanto para as empresas quanto para os profissionais.

Na plataforma em questão os profissionais de TI realizam seus cadastros e informam os conhecimentos que possuem. Eles podem procurar vagas, candidatando-se à elas ou não, alterar seus dados e enviar mensagens para as empresas que gostaram de seus perfis. As empresas, por sua vez, podem criar novas vagas de emprego, informando os requisitos necessários para preencher a vaga, alterar e deletar vagas, procurar profissionais de acordo com a vaga em questão, aceitando-os ou não, alterar seus dados e enviar mensagens para os candidatos que foram aceitos para suas vagas.

Para um profissional enviar mensagem para uma empresa ou o contrário, é necessário que o profissional tenha se candidatado à vaga da empresa e que a empresa tenha aceitado o perfil do profissional.

Para o profissional é importante que apareçam apenas vagas que sejam compatíveis com seus conhecimentos. Para as empresas o importante é que apareçam apenas candidatos que preencham os requisitos necessários para suas vagas, de acordo com a porcentagem de compatibilidade estipulada pela mesma.

### 4. TECNOLOGIAS UTILIZADAS <br>

Mockup: Mockplus <br>
Gerenciamento de projeto e controle de versão: GitHub <br>
Modelagem do banco de dados: brModelo <br>
Banco de dados: Sqlite <br>
Software: desenvolvido em Python, utilizando pyCharm e o framework Django. <br>


### 5. PMC <br> 
[PMC](https://docs.google.com/drawings/d/1a-0lQvwfUCVxYfxCVV7p6tyMoTpmQ2pI3AYdvLzMa3k/edit)

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

#### Regras de Negócio
| TIPO | Descrição |
|--|--|
|Restrições| A vaga de emprego só aparece para o candidato quando tiver 50% de compatibilidade entre os requisitos  da vaga e as informações do candidato. <br><br> Vagas são ofertadas de acordo com a região selecionada pelo candidato. <br><br> Vagas desativadas só ficarão armazenadas no banco de dados por 6 meses.|
|Ativadores de Ação| Se ambos os pares aceitarem o match, o chat é criado. <br><br> Se o match for desfeito por um dos pares, o chat é deletado. <br><br> A empresa, caso a vaga seja preenchida, pode desativar a vaga. |
|Inferências| Se a empresa tiver muitas requisições de match, será considerada empresa Popular. |
  
### 11. Diagrama de Classes <br>
![alt text](https://github.com/ewersonv/POO2/blob/master/arquivos/diagramas/JobTinder.jpg)

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
