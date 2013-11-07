import httplib2
h = httplib2.Http(".cache")
resp, content = h.request("http://example.org/", "GET")
print 'resp:', resp
print 'content', content