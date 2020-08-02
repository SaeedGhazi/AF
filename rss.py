import feedparser
NewsFeed = feedparser.parse("https://www.tabnak.ir/fa/rss/allnews")
entry = NewsFeed.entries[99]

print (entry.keys())
print (len(NewsFeed.entries))

print (entry.title)
print ("******")
print (entry.published)
print ("******")
print (entry.summary)
print ("------News Link--------")
print (entry.link)






