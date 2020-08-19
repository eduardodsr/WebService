from zeep import Client

# Forma 1
wsdl = 'http://soapclient.com/xml/soapresponder.wsdl'
client = Client(wsdl)
print(client.service.Method1('Eduardo', 'Rodrigues'))

# Forma 2
client = Client('http://soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1(bstrParam1='Eduardo1', bstrParam2='Rodrigues1')
print(result)

