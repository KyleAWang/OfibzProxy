

class OrderStatus():
    def __init__(self):
        self.orderId = ''
        self.statusId = ''

# <eeval-WorkEffort createdStamp="2016-09-27 00:02:32.0" createdTxStamp="2016-09-27 00:02:30.0" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" workEffortId="_NA_"/>
# <eeval-WorkEffort createdStamp="2016-09-27 00:03:11.0" createdTxStamp="2016-09-27 00:03:09.0" currentStatusId="ROU_ACTIVE" description="PC Assembly" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" quantityToProduce="0.000000" revisionNumber="1" workEffortId="ROUT01" workEffortName="PC assembly" workEffortTypeId="ROUTING"/>
# <eeval-WorkEffort createdStamp="2016-09-27 00:02:46.0" createdTxStamp="2016-09-27 00:02:44.0" currentStatusId="CAL_TENTATIVE" description="General Party" estimatedCompletionDate="2009-06-17 23:00:00.0" estimatedStartDate="2009-06-17 19:00:00.0" lastStatusUpdate="2008-01-01 00:00:00.0" lastUpdatedStamp="2016-09-30 22:19:15.0" lastUpdatedTxStamp="2016-09-30 22:19:14.0" locationDesc="Tom's Banquet Hall" scopeEnumId="WES_PUBLIC" workEffortId="PublicEvent" workEffortName="The general company party june 17" workEffortTypeId="MEETING"/>

class WorkEffort():
    def __init__(self, workEffortTypeId=None, workEffortName=None, workEffortId=None, scopeEnumId=None, locationDesc=None, lastUpdatedTxStamp=None, lastUpdatedStamp=None, lastStatusUpdate=None, estimatedStartDate=None, estimatedCompletionDate=None, description=None, createdStamp=None, createdTxStamp=None, currentStatusId=None ):
        self._workEffortTypeId = workEffortTypeId
        self._workEffortName = workEffortName
        self._workEffortId = workEffortId
        self._scopeEnumId = scopeEnumId
        self._locationDesc = locationDesc
        self._lastUpdatedTxStamp = lastUpdatedTxStamp
        self._lastUpdatedStamp = lastUpdatedStamp
        self._lastStatusUpdate = lastStatusUpdate
        self._estimatedStartDate = estimatedStartDate
        self._estimatedCompletionDate = estimatedCompletionDate
        self._description = description
        self._createdStamp = createdStamp
        self._createdTxStamp = createdTxStamp
        self._currentStatusId = currentStatusId

    @property
    def workEffortTypeId(self):
        return self._workEffortTypeId
    @workEffortTypeId.setter
    def workEffortTypeId(self, workEffortTypeId):
        self._workEffortTypeId = workEffortTypeId

    @property
    def workEffortName(self):
        return self._workEffortName
    @workEffortName.setter
    def workEffortName(self, workEffortName):
        self._workEffortName = workEffortName

    @property
    def workEffortId(self):
        return self._workEffortId
    @workEffortId.setter
    def workEffortId(self, workEffortId):
        self._workEffortId = workEffortId

    @property
    def scopeEnumId(self):
        return self._scopeEnumId
    @scopeEnumId.setter
    def scopeEnumId(self, scopeEnumId):
        self._scopeEnumId = scopeEnumId

    @property
    def locationDesc(self):
        return self._locationDesc
    @locationDesc.setter
    def locationDesc(self, locationDesc):
        self._locationDesc = locationDesc

    @property
    def lastUpdatedTxStamp(self):
        return self._lastUpdatedTxStamp
    @lastUpdatedTxStamp.setter
    def lastUpdatedTxStamp(self, lastUpdatedTxStamp):
        self._lastUpdatedTxStamp = lastUpdatedTxStamp

    @property
    def lastUpdatedStamp(self):
        return self._lastUpdatedStamp
    @lastUpdatedStamp.setter
    def lastUpdatedStamp(self, lastUpdatedStamp):
        self._lastUpdatedStamp = lastUpdatedStamp

    @property
    def lastStatusUpdate(self):
        return self._lastStatusUpdate
    @lastStatusUpdate.setter
    def lastStatusUpdate(self, lastStatusUpdate):
        self._lastStatusUpdate = lastStatusUpdate

    @property
    def estimatedStartDate(self):
        return self._estimatedStartDate
    @estimatedStartDate.setter
    def estimatedStartDate(self, estimatedStartDate):
        self._estimatedStartDate = estimatedStartDate

    @property
    def estimatedCompletionDate(self):
        return self._estimatedCompletionDate
    @estimatedCompletionDate.setter
    def estimatedCompletionDate(self, estimatedCompletionDate):
        self._estimatedCompletionDate = estimatedCompletionDate

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def createdStamp(self):
        return self._createdStamp
    @createdStamp.setter
    def createdStamp(self, createdStamp):
        self._createdStamp = createdStamp

    @property
    def createdTxStamp(self):
        return self._createdTxStamp
    @createdTxStamp.setter
    def createdTxStamp(self, createdTxStamp):
        self._createdTxStamp = createdTxStamp

    @property
    def currentStatusId(self):
        return self._currentStatusId
    @currentStatusId.setter
    def currentStatusId(self, currentStatusId):
        self._currentStatusId = currentStatusId
