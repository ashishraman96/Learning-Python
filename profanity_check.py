import urllib2
def read_text():
    file=open("/home/ashish/python/sample.txt")
    contents = file.read()
    file.close()
    profanity_check(contents)
def profanity_check(query):
    connection = urllib2.urlopen("http://www.wdylike.appspot.com/?q="+query);
    response = connection.read();
    if ( response == 'true'):
        print ("Profanity Alert!!")
    else:
        print ("No curse words found")
read_text()
