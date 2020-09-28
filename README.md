## Python rep IDCLASS 

Criei esse código com o intuito de ajudar outras pessoas que se encontram na mesma situação que eu.


O código visa ajudar a conectar, importar e processar os dados AFD vindos de um relógio de ponto Control ID IDCLASS.

Atualmente, tenho apenas um exemplo em um notebook jupyter, mas logo disponibilizarei uma biblioteca.

### classes
* Session: Classe usada para criar uma session com o REP
	* Session(usuario_rep, senha_rep, host_rep)
* User: Guarda as informações relacionadas aos usuários (empregados)
	* User(data_do_usuario) 
* AFD: Responsável por processar as informações com um código AFD
	* AFD(codigo_afd, objeto_session) 

### rodar
para rodar o projeto, rode:
    ```
    pip install -r requirements.txt
    ```
    ```
    jupyter notebook
    ``` 
    
### Criador
Flávio Vitoriano ->  [github](https://www.github.com/flavioVitoriano)
