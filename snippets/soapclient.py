from xml.dom.minidom import Document
import http.client
import xml.etree.ElementTree as ET
from .beans import OrderStatus, WorkEffort

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

# <eeval-WorkEffort createdStamp="2016-09-27 00:02:46.0" createdTxStamp="2016-09-27 00:02:44.0" currentStatusId="CAL_TENTATIVE" description="General Party" estimatedCompletionDate="2009-06-17 23:00:00.0" estimatedStartDate="2009-06-17 19:00:00.0" lastStatusUpdate="2008-01-01 00:00:00.0" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" locationDesc="Tom's Banquet Hall" scopeEnumId="WES_PUBLIC" workEffortId="PublicEvent" workEffortName="The general company party june 17" workEffortTypeId="MEETING"/>
    def getWorkEfforts(self):
        doc = Document()
        root = super().callSoapService(doc, 'getWorkEffortsKS', None)
        workEfforts = [ ]
        for child in root:
            for chia in child:
                for chib in chia:
                    for chic in chib:
                        for chid in chic:
                            for chie in chid:
                                for chif in chie:
                                    workEffort = WorkEffort()
                                    if 'workEffortId' in chif.attrib:
                                        workEffort.workEffortId = chif.attrib['workEffortId']
                                    if 'createdTxStamp' in chif.attrib:
                                        workEffort.createdTxStamp = chif.attrib['createdTxStamp']
                                    if 'currentStatusId' in chif.attrib:
                                        workEffort.currentStatusId = chif.attrib['currentStatusId']
                                    if 'description' in chif.attrib:
                                        workEffort.description = chif.attrib['description']
                                    if 'estimatedCompletionDate' in chif.attrib:
                                        workEffort.estimatedCompletionDate = chif.attrib['estimatedCompletionDate']
                                    if 'estimatedStartDate' in chif.attrib:
                                        workEffort.estimatedStartDate = chif.attrib['estimatedStartDate']
                                    if 'lastStatusUpdate' in chif.attrib:
                                        workEffort.lastStatusUpdate = chif.attrib['lastStatusUpdate']
                                    if 'lastUpdatedStamp' in chif.attrib:
                                        workEffort.lastUpdatedStamp = chif.attrib['lastUpdatedStamp']
                                    if 'lastUpdatedTxStamp' in chif.attrib:
                                        workEffort.lastUpdatedTxStamp = chif.attrib['lastUpdatedTxStamp']
                                    if 'locationDesc' in chif.attrib:
                                        workEffort.locationDesc = chif.attrib['locationDesc']
                                    if 'scopeEnumId' in chif.attrib:
                                        workEffort.scopeEnumId = chif.attrib['scopeEnumId']
                                    if 'workEffortTypeId' in chif.attrib:
                                        workEffort.workEffortTypeId = chif.attrib['workEffortTypeId']
                                    if 'workEffortName' in chif.attrib:
                                        workEffort.workEffortName = chif.attrib['workEffortName']
                                    workEfforts.append(workEffort)

        return workEfforts
