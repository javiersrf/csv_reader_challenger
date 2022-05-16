# csv_reader_challenger

This project is a python challenger for backend job opportunity

The project contains a django api (with a basic web view) that can read a txt file (as dados.txt example) and
somiplify the dada inside to adequate in database (sqlite3) formater.
- File in the correct formater is attached in repository
- To start tha application, use the bash file 'run.sh': 'bash run.sh', it will start the migration and docker-compose
- The application is set tu port 65501 but can be change in docker-compose file

The Challenge command (portuguese and english):
<pt-br>
Você recebeu um arquivo de texto com os dados de vendas da empresa. Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload de arquivos, normalize os dados e armazene-os no banco de dados.

Sua aplicação web DEVE:

Aceitar (via formulário) o upload de arquivos text, com dados separados por TAB. A primeira linha do arquivo tem o nome das colunas. Você pode assumir que as colunas estarão sempre nesta ordem e sempre haverá uma linha de cabeçalho. Um arquivo de exemplo chamado 'dados.txt' está incluído neste repositório.
Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional.
Exibir todos os registros importados, bem como a receita bruta total dos registros contidos no arquivo enviado após o upload + parser.
A aplicação deve ser escrita obrigatoriamente em: Python 3.7+ ou PHP 7+ (dependendo da vaga que está se candidatando), utilizando qualquer framework de preferência.
Executar via Docker ou Docker Compose.
Utilizar apenas linguagens e bibliotecas livres ou gratuitas.
Ter testes de model e controller automatizados.
Ter uma boa aparência e ser fácil de usar.
    
<en-US>
You have received a text file with the company's sales data. We need to create a way for this data to be imported into a database.

Your task is to create a web interface that accepts file uploads, normalizes the data and stores it in the database.

Your web application MUST:

Accept (via form) the upload of text files, with data separated by TAB. The first line of the file has the column names. You can assume the columns will always be in this order and there will always be a header row. An example file called 'data.txt' is included in this repository.
Interpret ("parse") the received file, normalize the data, and correctly save the information in a relational database.
View all imported records as well as the total gross revenue of records contained in the uploaded file after upload + parser.
The application must be written in: Python 3.7+ or PHP 7+ (depending on the position you are applying for), using any framework you prefer.
Run via Docker or Docker Compose.
Use only free or free languages ​​and libraries.
Have automated model and controller tests.
Look good and be easy to use.
