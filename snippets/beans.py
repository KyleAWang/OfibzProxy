

class OrderStatus():
    def __init__(self):
        self.orderId = ''
        self.statusId = ''

# <eeval-WorkEffort createdStamp="2016-09-27 00:02:32.0" createdTxStamp="2016-09-27 00:02:30.0" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" workEffortId="_NA_"/>
# <eeval-WorkEffort createdStamp="2016-09-27 00:03:11.0" createdTxStamp="2016-09-27 00:03:09.0" currentStatusId="ROU_ACTIVE" description="PC Assembly" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" quantityToProduce="0.000000" revisionNumber="1" workEffortId="ROUT01" workEffortName="PC assembly" workEffortTypeId="ROUTING"/>
# <eeval-WorkEffort createdStamp="2016-09-27 00:02:46.0" createdTxStamp="2016-09-27 00:02:44.0" currentStatusId="CAL_TENTATIVE" description="General Party" estimatedCompletionDate="2009-06-17 23:00:00.0" estimatedStartDate="2009-06-17 19:00:00.0" lastStatusUpdate="2008-01-01 00:00:00.0" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" locationDesc="Tom's Banquet Hall" scopeEnumId="WES_PUBLIC" workEffortId="PublicEvent" workEffortName="The general company party june 17" workEffortTypeId="MEETING"/>

class WorkEffort():
    @property
    def workEffortTypeId(self):
        return self.workEffortTypeId
    @workEffortTypeId.setter
    def workEffortTypeId(self, workEffortTypeId):
        self.workEffortTypeId = workEffortTypeId

    @property
    def workEffortName(self):
        return self.workEffortName
    @workEffortName.setter
    def workEffortName(self, workEffortName):
        self.workEffortName = workEffortName

    @property
    def workEffortId(self):
        return self.workEffortId
    @workEffortId.setter
    def workEffortId(self, workEffortId):
        self.workEffortId = workEffortId

    @property
    def scopeEnumId(self):
        return self.scopeEnumId
    @scopeEnumId.setter
    def scopeEnumId(self, scopeEnumId):
        self.scopeEnumId = scopeEnumId

    @property
    def locationDesc(self):
        return self.locationDesc
    @locationDesc.setter
    def locationDesc(self, locationDesc):
        self.locationDesc = locationDesc

    @property
    def lastUpdatedTxStamp(self):
        return self.lastUpdatedTxStamp
    @lastUpdatedTxStamp.setter
    def lastUpdatedTxStamp(self, lastUpdatedTxStamp):
        self.lastUpdatedTxStamp = lastUpdatedTxStamp

    @property
    def lastUpdatedStamp(self):
        return self.lastUpdatedStamp
    @lastUpdatedStamp.setter
    def lastUpdatedStamp(self, lastUpdatedStamp):
        self.lastUpdatedStamp = lastUpdatedStamp

    @property
    def lastStatusUpdate(self):
        return self.lastStatusUpdate
    @lastStatusUpdate.setter
    def lastStatusUpdate(self, lastStatusUpdate):
        self.lastStatusUpdate = lastStatusUpdate

    @property
    def estimatedStartDate(self):
        return self.estimatedStartDate
    @estimatedStartDate.setter
    def estimatedStartDate(self, estimatedStartDate):
        self.estimatedStartDate = estimatedStartDate

    @property
    def estimatedCompletionDate(self):
        return self.estimatedCompletionDate
    @estimatedCompletionDate.setter
    def estimatedCompletionDate(self, estimatedCompletionDate):
        self.estimatedCompletionDate = estimatedCompletionDate

    @property
    def description(self):
        return self.description
    @description.setter
    def description(self, description):
        self.description = description

    @property
    def createdStamp(self):
        return self.createdStamp
    @createdStamp.setter
    def createdStamp(self, createdStamp):
        self.createdStamp = createdStamp

    @property
    def createdTxStamp(self):
        return self.createdTxStamp
    @createdTxStamp.setter
    def createdTxStamp(self, createdTxStamp):
        self.createdTxStamp = createdTxStamp

    @property
    def currentStatusId(self):
        return self.currentStatusId
    @currentStatusId.setter
    def currentStatusId(self, currentStatusId):
        self.currentStatusId = currentStatusId
