import urllib, httplib, re, urllib2
userAGE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', userAGE)]
sitelist = []
comp = []
def dorker(dork,pages):
    d = urllib.quote(dork)
    p = 1
    m = pages * 10
    while p <= m:
        try:
            search = "http://www.bing.com/search?q=" + d +"&first=" + str(p)
            req = opener.open(search)
            source = req.read()
            sites = re.findall('<h2><a href="http://(.*?)"', source)
            sitelist.extend(sites)
            p += 10
        except urllib2.URLError:
            print ("url error")
            continue
        except urllib2.HTTPError:
            print ("http error")
            continue
        except IOError:
            continue
        except httplib.HTTPException:
            continue
    uniqsites = list(set(sitelist))  
    for line in uniqsites:
        sep = '/'
        build = "http://" + line.split(sep,1)[0]
        comp.append(build)
        print "\t\t" + build
    final1 = list(set(comp))
    l = "bing_search_" + str(len(final1)) + ".txt"
    foo = open(l,"w")
    for ss in final1:
        foo.write(ss + "\n")
    foo.close()
    print "[OK] file saved as " + l
print 'Type dork below:'
dr = raw_input('')
print 'Number of pages to look for:'
numpages = int(raw_input(''))
print '[>] Search in progress ...'
dorker(dr, numpages)
