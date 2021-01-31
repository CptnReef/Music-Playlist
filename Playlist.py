from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    print("=" * 90)
    
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

    print("song added to playlist")

    print("=" * 90)


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    print("=" * 90)

    current_song = 0
    select_song = self.__first_song

    while select_song != None:
      if select_song.set_next_song(title) == title:
        return current_song
      current_song += 1
      select_song = select_song.get_next_song()

    print("=" * 90)

    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    select_song = self.__first_song
    
    if select_song.get_title() == title:
      self.__first_song = select_song.get_next_song()
      return
    
    while select_song != None:
      if select_song.get_next_song() == None:
        break
      elif select_song.get_next_song().get_next_song() == title:
        select_song.set_next_song.remove(select_song.get_next_song().get_next_song())
        break
      else:
        select_song = select_song.get_next_song()
    

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    print("=" * 90)

    count_songs = 0
    current_song = self.__first_song

    while current_song != None:
      count_songs += 1
      current_song = current_song.get_next_song()

    print("=" * 90)

    return count_songs


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    print("=" * 90)
        
    lst = 0
    song_file = self.__first_song
    while song_file != None:
      lst += 1
      print(f"# {lst}. {song_file}")
      song_file = song_file.get_next_song()

    print("=" * 90)
