import imdb
import random

def getEpisodes(code):

#    ia=imdb.IMDb() # create instance of IMDb

    series=ia.get_movie(code) # find the name of the series corresponding to code
    print('\nSeries: %s\n-------\n'%(series))

    ia.update(series,'episodes') # update instance ia with new information set

    episodes=series.data['episodes'] # get information on the episodes
    episodesList=[]

    for i in episodes.keys():
        print('\nSeason %s\n-------'%(str(i)))
        for j in episodes[i]:
            title=episodes[i][j]['title']
            print('Episode %s: %s'%(str(j),title))
            episodesList.append('S %s,Ep %s: %s'%(str(i),str(j),title))
    print('\n') # ahhhh whitespace

    return(episodesList)


 
### want to have an option to let the user choose the series that the episode will be chosen from

ia=imdb.IMDb() # create instance of IMDb

seriesName=input('Please tell me the name of the series you would like to watch: ')
code=ia.search_movie(seriesName)[0].getID()
episodesList=getEpisodes(code)
epToWatch=random.choice(episodesList)
print('-------\nYou should watch...\n%s\n-------'%(epToWatch))
