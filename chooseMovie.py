import json

def filterGenre(movieList,genre):

    '''find the movie options for the chosen genre from inside movieList'''

    outList=[]
    for m in movieList:
        if m['genre']==genre:
            outList.append(m['title'])
    if len(outList)==0:
      raise ValueError('There are no movies in that genre')

    return(outList)

def getMovieDetails(movieList,movie): # issue::: what if user does not capitalise in the right way -- need to modify the initial dictionary itself to simplify but look at this later
  '''not perfect but a first attempt'''
  for m in movieList:
    if m['title']==movie: # if the movie title in the list matches that selected
      outString=''
      for k in m.keys():
        outString+='%s: %s\n'%(k,m[k])
    else:
      next
  return(outString)


with open('movies.json','r') as f: # import all the movie options
  movies=json.load(f) # store movies in list of dictionaries

g=[m['genre'] for m in movies] # get a list of genres
uniqueGenres=list(set(g)) # get unique list of genres

genre=input('What genre of movie would you like?  The options are %s\n'%(uniqueGenres))
genre=(genre.lower()).capitalize() # make sure only first letter is capitalized
print('\nYou have chosen %s\n'%(genre))

try:
  idx=uniqueGenres.index(genre)
except:
  print('That is not one of the options\nPlease enter a different genre:\n')
  gotit=False
  while gotit==False:
    newGenre=input('The options are %s\n'%(uniqueGenres))
    if newGenre in uniqueGenres:
      gotit=True
      genre=newGenre
      break
    else:
      print('Try again...')

genreMovies=filterGenre(movies,genre)
print('\nMovies in that genre: \n')
for x in genreMovies:
    print(x)
print('\n')

movieSelection=input('Please choose one of these films to get more information on it: ')
print('\n')
print(getMovieDetails(movies,movieSelection))
