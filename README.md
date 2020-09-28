## Python rep IDCLASS 

Criei esse código com o intuito de ajudar outras pessoas que se encontram na mesma situação que eu.


O código visa ajudar a conectar, importar e processar os dados AFD vindos de um relógio de ponto Control ID IDCLASS.


### entidades
* Session: Classe usada para criar uma session com o REP
	* Session(usuario_rep, senha_rep, host_rep)
* User: Guarda as informações relacionadas aos usuários (empregados)
	* User(data_do_usuario) 
* AFD: Responsável por processar as informações com um código AFD
	* AFD(codigo_afd, objeto_session) 

### funções
* get_afds: retorna as afds a partir da data informada
	* get_afds(objeto_session, dia, mes, ano) **retorna** list(AFD)
* get_users_from_afds: retorna os usuarios existentes na lista de afds fornecida 
	* get_users_from_afds(objeto_session, afds:list(AFD)) **retorna** list(User)
* transform_afds: adiciona a coluna "funcionario" contendo o nome do mesmo a lista de afds (obs: ignora os afds em que os usuarios informados nao estiverem) 
	* transform_afds(afds:list(AFD), users:list(User) **retorna** list(dict)
* to_csv: transforma uma lista em um arquvio csv 
	* to_csv(data: list(any), caminho_arquivo) **retorna** None

### rodar
para rodar o projeto, rode:
    ```
    pip install -r requirements.txt
    ```
    ```
    jupyter notebook
    ```


ou veja: o arquivo **example.py**
    
### Criador
Flávio Vitoriano ->  [github](https://www.github.com/flavioVitoriano)
