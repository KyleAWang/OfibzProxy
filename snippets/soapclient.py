from xml.dom.minidom import Document
import http.client
import xml.etree.ElementTree as ET
from .beans import OrderStatus


class SoapClient():
    def test_soap_client(self, orderId):
        OFBIZ_WEBSERVICE_URL = 'http://localhost:8080/webtools/control/SOAPService'

        ###### Create the minidom document ######

        orderStatus = OrderStatus()
        print('soapClient', 'orderId:', orderId)
        if orderId:
            print('soapClient', 'orderId:', orderId)
            doc = Document()
            soapenv = doc.createElement("soapenv:Envelope")
            doc.appendChild(soapenv)
            soapenv.setAttribute("xmlns:soapenv", "http://schemas.xmlsoap.org/soap/envelope/")
            soapenv.setAttribute("xmlns:ser", 'http://ofbiz.apache.org/service/')

            header = doc.createElement("soapenv:Header")
            soapenv.appendChild(header)

            body = doc.createElement("soapenv:Body")
            soapenv.appendChild(body)

            updateScrumRevision = doc.createElement("ser:getOrderStatus")
            body.appendChild(updateScrumRevision)

            mapMap = doc.createElement("map-Map")
            updateScrumRevision.appendChild(mapMap)

            mapEntry = doc.createElement("ser:map-Entry")
            mapKey = doc.createElement("ser:map-Key")
            stdString = doc.createElement("ser:std-String")
            stdString.setAttribute("value", "orderId")
            mapKey.appendChild(stdString)
            mapEntry.appendChild(mapKey)
            mapValue = doc.createElement("ser:map-Value")
            stdString = doc.createElement("ser:std-String")
            stdString.setAttribute("value", orderId)
            mapValue.appendChild(stdString)
            mapEntry.appendChild(mapValue)
            mapMap.appendChild(mapEntry)

            soapMessage = doc.toprettyxml(indent="  ")

            #######  Call Webservice #######
            # Send request
            webservice = http.client.HTTPConnection('localhost:8080', timeout=10)
            webservice.putrequest("POST", OFBIZ_WEBSERVICE_URL)
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



# class OrderStatus():
#     def __index__(self):