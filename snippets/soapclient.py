from xml.dom.minidom import Document
import http.client
import xml.etree.ElementTree as ET
from .beans import OrderStatus

class abstractSoapClient():
    def callSoapService(self, doc, serviceName, params):
        soapenv = doc.createElement("soapenv:Envelope")
        doc.appendChild(soapenv)
        soapenv.setAttribute("xmlns:soapenv", "http://schemas.xmlsoap.org/soap/envelope/")
        soapenv.setAttribute("xmlns:ser", 'http://ofbiz.apache.org/service/')

        header = doc.createElement("soapenv:Header")
        soapenv.appendChild(header)

        body = doc.createElement("soapenv:Body")
        soapenv.appendChild(body)

        updateScrumRevision = doc.createElement("ser:" + serviceName)
        body.appendChild(updateScrumRevision)

        mapMap = doc.createElement("map-Map")
        updateScrumRevision.appendChild(mapMap)

        if params != None:
            for key, value in params.items():
                mapEntry = doc.createElement("ser:map-Entry")
                mapKey = doc.createElement("ser:map-Key")
                stdString = doc.createElement("ser:std-String")
                stdString.setAttribute("value", key)
                mapKey.appendChild(stdString)
                mapEntry.appendChild(mapKey)
                mapValue = doc.createElement("ser:map-Value")
                stdString = doc.createElement("ser:std-String")
                stdString.setAttribute("value", value)
                mapValue.appendChild(stdString)
                mapEntry.appendChild(mapValue)
                mapMap.appendChild(mapEntry)

        soapMessage = doc.toprettyxml(indent="  ")

        #######  Call Webservice #######
        # Send request
        webservice = http.client.HTTPConnection('localhost:8080', timeout=10)
        webservice.putrequest("POST", SoapClient.OFBIZ_WEBSERVICE_URL)
        webservice.putheader("Host", 'localhost')
        webservice.putheader("User-Agent", "Python post")
        webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(soapMessage))
        webservice.putheader("SOAPAction", "\"\"")
        webservice.endheaders()
        webservice.send(soapMessage.encode())

        #Get response
        respnose = webservice.getresponse()
        rspxml = respnose.read()
        # print(rspxml)
        # tree = ET.parse(respnose.read().decode())
        # root = tree.getroot()
        webservice.close()


        root = ET.fromstring(rspxml.decode())
        return  root


class SoapClient(abstractSoapClient):
    OFBIZ_WEBSERVICE_URL = 'http://localhost:8080/webtools/control/SOAPService'
    def getOrderStatus(self, orderId):
        ###### Create the minidom document ######

        orderStatus = OrderStatus()
        print('soapClient', 'orderId:', orderId)
        if orderId:
            doc = Document()
            params = {
                'orderId': orderId
            }
            root = super().callSoapService(doc, 'getOrderStatus', params)

            orderStatus.orderId = orderId
            for child in root:
                for chia in child:
                    for chib in chia:
                        for chic in chib:
                            for chid in chic:
                                for chie in chid:
                                    orderStatus.statusId = chie.attrib['value']
        else:
            orderStatus = None
        return orderStatus

    def getWorkEfforts(self):
        doc = Document()
        root = super().callSoapService(doc, 'getWorkEffortsKS', None)
        for child in root:
            for chia in child:
                for chib in chia:
                    for chic in chib:
                        print(1, chic)
                        for chid in chic:
                            print(2, chid)
                            for chie in chid:
                                print(3, chie)
                                for chif in chie:
                                    print(4, chif)
                                    print(chif.attrib['createdStamp'])
        # print(root)
