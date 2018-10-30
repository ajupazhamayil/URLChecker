def nmberOfSbStrigs(rl,sb):
   temp = [i for i in range(len(rl)) if rl.startswith(sb, i)]
   return len(temp)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


domain = ['com']
sbdomain = ['blogs']
url = raw_input("Enter a URL\n")

print "length of url is ", len(url)
#give inpt as any thing like ., /, _ or whatever yo want
for i in ['.','_','https']:
   print i,"s are ",nmberOfSbStrigs(url,i)
print "# of domains ",intersection(url.split('.'),domain)
print "# of subdomains ",intersection(url.split('.'),sbdomain)
