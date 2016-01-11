# -*- coding: utf-8 -*-
from scrapy.dupefilter import RFPDupeFilter

class URLFilter(RFPDupeFilter):
    def request_fingerprint(self, request):
        print '11111111111'
        pass
    
    def request_seen(self, request):
        print '22222222222'
        return False
#         fp = self.__getid(request.url)
#         if fp in self.fingerprints:
#             return True
#         self.fingerprints.add(fp)
#         if self.file:
#             self.file.write(fp + os.linesep)
