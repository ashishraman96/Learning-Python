import urllib2
def read_text():
    file=open("/home/ashish/python/sample.txt")
    contents = file.read()
    file.close()
    profanity_check(contents)
def profanity_check(query):
    connection = urllib2.urlopen("http://www.wdylike.appspot.com/?q="+query);
    response = connection.read();
    if 'true' in response:
        print ("Profanity Alert!!")
    elif 'false' in response:
        print ("No curse words found")
    else:
        print ("Could not scan document")
    connection.close()
read_text()
