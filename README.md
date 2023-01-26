# HashtagTreinamento

###### Controle de estoque
- Criação de uma interface gráfica usando a biblioteca tkinter;
- Conectar e abrir as informações no jupyter notebook, importando duas bibliotecas: mysql_connector e pandas;
- Integração Python + SQL, utilizando o CRUD nas funcionalidades dos botões da janela criada.

###### Automacao de Processo
- Importando várias bases de dados do excel;
- Mesclar 2 tabelas para ficar mais fácil identificar o ID da loja, loja e o que foi vendido;
- Criar uma pasta chamada 'backup', verificar se já não existe e salvar as planilhas lá;
- Calcular o indicador para cada loja;
- Enviar por e-mail de forma automatizada para os gerentes, utizando gmail, o indicador de cada loja e as planilhas ;
- Criar ranking para diretoria;
- Enviar e-mail para diretoria com 2 anexos, ranking do dia e anual.

###### Projeto 2
- Neste projeto foi automatizado um processo de busca de 2 produtos em 2 sites diferentes; 
- Foi definido um preço minímo e máximo e termos banidos para não pegar qualquer item de mesmo nome;
- Com os resultados obtidos criado uma nova tabela com o nome do produto, preço e link;
- Enviar por e-mail de forma automatizada a tebela e o anexo.

###### CEP
Busca de CEP a partir de endereço:
- O usuário digita o UF, Estado e Logadrouro que deseja obter o CEP;
- Através do site <https://viacep.com.br/> a integração é feita pra obter essa informação, aqui é usado a biblioteca requests para facilitar as solitações http;
- Informação obtida no formato json;
- Converter para uma tabela usando o pandas.

###### sistema_cotacao
- Criação de uma interface gráfica usando a biblioteca tkinter;
- Uso do tkcalendar para criar calendários e tkinter.filedialog para selecionar arquivo;
- Ajustar o layout para ter uma boa aparência;
- API de Cotações de Moedas no formato json;
- Uso de funções para pegar a cotação, selecionar arquivo e atualizar cotações.

##### rpa_email
Automatizar a extração de informações de um sistema e envio de um relatório por e-mail
- Utilização da biblioteca pyautogui;
- Criar um alerta para não mexer no computador enquanto o código está rodando;
- Tirar print das imagens dos lugares onde você vai clicar;
- Entrar no sistema;
- Entrar em uma aba específica do sistema onde tem o relatório;
- Exportar o Relatório;
- Pegar o relatório exportado, tratar e pegar as informações que queremos com pandas;
- Preencher/Atualizar informações do sistema.
