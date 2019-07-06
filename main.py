#  __    __  ____    __    ____     ___   
# |  |  |  | \   \  /  \  /   /    |__ \  
# |  |__|  |  \   \/    \/   / ______ ) | 
# |   __   |   \            / |______/ /  
# |  |  |  |    \    /\    /        / /_  
# |__|  |__|     \__/  \__/        |____| 
# ---------------------------------------------------------

# Global variables.
# Song's title
Title         = "All the small things"
# Song's album
Album         = "Enema of the State"
# Song's artist
Artist        = "Blink-182"
# Song's record label
Label         = "MCA Records"
# Song'genre
Genre         = "Punk rock"
# Song's duration in minutes
DurationInMin = 2.8
# Album's yaer
Year          = 1999
# Track number in album
TrackNum      = 3

# get song's title
def title():
	return Title

# get song's genre
def genre():
	return Genre

# get song's duration in minutes
def durationInMin():
	return DurationInMin
# returns True if track number is one
def IsFirstTrack():
	return TrackNum == 1

# Print al varliables
print()
print("--------------------------")
print("Title: ", title())
print("--------------------------")
print("Album:         ", Album)
print("Artist:        ", Artist)
print("Label:         ", Label)
print("Genre:         ", genre())
print("DurationInMin: ", durationInMin())
print("Year:          ", Year)
print("Track:         ", TrackNum)
print("Is First Track:", IsFirstTrack())
print("--------------------------")