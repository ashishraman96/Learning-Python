import urllib2
webUrl = urllib2.urlopen("http://google.co.in")
print "result code: " + str(webUrl.getcode())
data = webUrl.read()
print data
