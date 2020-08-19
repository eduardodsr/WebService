# WebService
 
 ### Backend Developer Carrefour - Fundamentos de Arquitetura de Sistemas 
 
 ### Projeto WebService - Soap Client - Python Zeep
 
Webservices são soluções adotadas para integração entre sistemas distintos. Através de sua comunicação é possível que diferentes aplicações se comuniquem de forma transparente, independente da tecnologia utilizada. Existem diversos sistemas antigos que possuem integração com outros mais atuais, tudo isso através de um webservice.

Muitos destes webservices trabalham com XML (linguagem de marcação para padronizar a comunicação dos dados através de um padrão) e os protocolos HTTP/HTTPS (para o transporte dos dados). Especificamente com o protocolo SOAP (Simple Object Access Protocol). Geralmente é feito o uso de um WSDL (Web Service Definition Language), se trata de um documento disponível onde contém todas as especificações do Webservice, entre elas:
- Descrição do serviço.
- Especificações de acesso.
- Operações e métodos disponíveis.

 ### Tarefa Prática
 
 1. Realizar teste com o SOAP Client, http://soapclient.com/xml/soapresponder.wsdl

 2. Instalar o software SOAP UI na versão Open Source, https://www.soapui.org
 
 3. Importar o endereço do SOAP Client (http://soapclient.com/xml/soapresponder.wsdl) no Sofware SOAP UI
 
 4. SOAP - New Open Project - Initial WSDL : http://soapclient.com/xml/soapresponder.wsdl
 
 5. Analisar no arquivo.wsdl, as propriedades SoapResponderBinding e Method1
 
 6. Fazer um request e verificar se comunicou com sucesso.
 
 7. Analisar a biblioteca Zeep: Python SOAP client
 
 8. Importar a biblioteca Zeep e fazer a instalação com get-pip.py 
 
 9. Executar os comandos no terminal de importação e instalação do Python SOAP client
 
 10. Criar uma pasta WebServices, com dois arquivos: soap.py e rest.py
 
 11. No arquivo soap.py realizar um teste passando meu nome e sobrenome e executar o comando no terminal, python soap.py
 
 12. Os parametros passados (nome e sobrenome) devem ser retornados na consulta do terminal.
 

### Resultado Final da Tarefa Prática:

![](https://github.com/eduardodsr/WebService/blob/master/python/SoapUI.png?raw=true)

![](https://github.com/eduardodsr/WebService/blob/master/python/soap.py.png?raw=true)



### Links utilizados na tarefa prática de WebServices

``` link: ```  http://soapclient.com/xml/soapresponder.wsdl 

``` link: ```  https://github.com/mvantellingen/python-zeep

``` link: ```  https://www.soapui.org

``` link: ```  https://docs.python-zeep.org/en/master/

``` link: ```  https://pip.pypa.io/en/stable/installing/
