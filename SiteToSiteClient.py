class SiteToSiteClient(object):

    def __init__(self, config):
        self.config = config
        self.compress = config.get('compress') or False
        self.commsTimeout = config.get('timeout') or 0
        self.portIdentifier = config.get('portId')
        self.portName = config.get('portName')
        self.ssl = config.get('ssl')
        self.clusterURLs = config.get('urls')
        self.readTimeout = self.commsTimeout
        self.cachedContentsExpirationMillis = config.get('cache_expiration')
        self.proxy = config.get('proxy')
        self.localAddress = config.get('local_address')
        self.penalizationNanos = config.get('penalize_period')

    def createSiteToSiteRestApiClient(self):
        pass

    def getActiveClusterUrl(self):
        pass

    def getClusterUrls(self):
        pass

    def getInputPortIdentifier(self, portname):
        pass

    def getOutputPortIdentifier(self, portname):
        pass

    def getPortIdentifier(self, portname, direction):
        pass

    def getSiteToSiteHttpPort(self):
        pass

    def getSiteToSitePort(self):
        pass

    def isSecure(self):
        pass

    def isWebInterfaceSecure(self):
        filter(lambda url: url.startsWith('https'), self.clusterURLs)

    def __refreshRemoteInfo(self):
        pass

    def __getPortIdentifier(self, portname, portdict):
        pass
