import feedparser
NewsFeed = feedparser.parse("https://www.tabnak.ir/fa/rss/2")
dim = len(NewsFeed)

entry = NewsFeed.entries[dim -1]

print (entry.title)
print ("******")
print (entry.published)
print ("******")
print (entry.summary)
print ("------News Link--------")
print (entry.link)






