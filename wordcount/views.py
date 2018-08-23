from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(request):
        return render(request,'home.html',{'hithere':'this is deepsa'})
def about(request):
		return render(request,'about.html')
def count(request):
		ft=request.GET['fulltext']
		wordlist=ft.split()
		print(ft)
		worddictionary={}
		for word in wordlist:
			if word in worddictionary:
				#INCREASE
				worddictionary[word]+=1
			else:
				#add to dictionary
				worddictionary[word]=1
			
		sorted_words=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
		
		return render(request,'count.html',{'fulltext':ft,'count_words':len(wordlist),'worddictionary':sorted_words})