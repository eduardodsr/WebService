# WebService

[![](https://img.shields.io/badge/made_by-eduardodsr-green)](https://github.com/eduardods/)
![GitHub repo size](https://img.shields.io/github/repo-size/eduardodsr/WebService)
![GitHub top language](https://img.shields.io/github/languages/top/eduardodsr/WebService)
![GitHub language count](https://img.shields.io/github/languages/count/eduardodsr/WebService)
![Visitor](https://visitor-badge.glitch.me/badge?page_id=eduardodsr.WebService
 
 ## Fundamentos de Arquitetura de Sistemas 
 
 ### Projeto WebService - Soap Client - Python Zeep
  
 <p align="center">
   <img src=https://docs.python-zeep.org/en/master/_static/zeep-logo.png?raw=true" alt="imagem" width="200px" />
 </p>
 
<strong>Webservices</strong> são soluções adotadas para integração entre sistemas distintos. Através de sua comunicação é possível que diferentes aplicações se comuniquem de forma transparente, independente da tecnologia utilizada. Existem diversos sistemas antigos que possuem integração com outros mais atuais, tudo isso através de um webservice.

Muitos destes webservices trabalham com XML (linguagem de marcação para padronizar a comunicação dos dados através de um padrão) e os protocolos HTTP/HTTPS (para o transporte dos dados). Especificamente com o protocolo SOAP (Simple Object Access Protocol). Geralmente é feito o uso de um WSDL (Web Service Definition Language), se trata de um documento disponível onde contém todas as especificações do Webservice, entre elas:
- Descrição do serviço.
- Especificações de acesso.
- Operações e métodos disponíveis.

 ### WebService - Atividades | Tarefa Prática
 
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
 
  
 ### XML 
 
```xml 
<definitions xmlns:tns="http://www.SoapClient.com/xml/SoapResponder.wsdl" xmlns:xsd1="http://www.SoapClient.com/xml/SoapResponder.xsd" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns="http://schemas.xmlsoap.org/wsdl/" name="SoapResponder" targetNamespace="http://www.SoapClient.com/xml/SoapResponder.wsdl">
<types>
<schema xmlns="http://www.w3.org/1999/XMLSchema" targetNamespace="http://www.SoapClient.com/xml/SoapResponder.xsd"> </schema>
</types>
<message name="Method1">
<part name="bstrParam1" type="xsd:string"/>
<part name="bstrParam2" type="xsd:string"/>
</message>
<message name="Method1Response">
<part name="bstrReturn" type="xsd:string"/>
</message>
<portType name="SoapResponderPortType">
<operation name="Method1" parameterOrder="bstrparam1 bstrparam2 return">
<input message="tns:Method1"/>
<output message="tns:Method1Response"/>
</operation>
</portType>
<binding name="SoapResponderBinding" type="tns:SoapResponderPortType">
<soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
<operation name="Method1">
<soap:operation soapAction="http://www.SoapClient.com/SoapObject"/>
<input>
<soap:body use="encoded" namespace="http://www.SoapClient.com/xml/SoapResponder.xsd" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</input>
<output>
<soap:body use="encoded" namespace="http://www.SoapClient.com/xml/SoapResponder.xsd" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</output>
</operation>
</binding>
<service name="SoapResponder">
<documentation>A SOAP service that echoes input parameters in the response</documentation>
<port name="SoapResponderPortType" binding="tns:SoapResponderBinding">
<soap:address location="http://www.soapclient.com/xml/soapresponder.wsdl"/>
</port>
</service>
</definitions>
``` 
 
  ``` link XML:  ``` http://soapclient.com/xml/soapresponder.wsdl
  

### Resultado Final da Tarefa Prática:

![](https://github.com/eduardodsr/WebService/blob/master/python/SoapUI.png?raw=true)

![](https://github.com/eduardodsr/WebService/blob/master/python/soap.py.png?raw=true)



### Links utilizados na tarefa prática de WebServices

``` link: ```  http://soapclient.com/xml/soapresponder.wsdl 

``` link: ```  https://github.com/mvantellingen/python-zeep

``` link: ```  https://www.soapui.org

``` link: ```  https://docs.python-zeep.org/en/master/

``` link: ```  https://pip.pypa.io/en/stable/installing/
