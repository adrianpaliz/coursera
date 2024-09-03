# Exercise: Classes and object exploration
# Class definition of Audio
class Audio:
    # Constrauctor for Audio
    def __init__(self, seconds):
        print('---------Inside class A---------')
        self.seconds = seconds
    print('Print inside Audio.')
    # Definition of local method progress()
    def progress(self):
        seconds = self.seconds + 1
        return seconds

print(dir(Audio))
print('Instantiating Audio...')
# Instantiating object audio over class Audio
audio = Audio(1)
# Calling method progress() over object of class Audio
print(audio.progress())

# Class definition of Video
class Video:
    # Constructor for Video
    def __init__(self, minutes):
        print('---------Inside class B---------')
        self.minutes = minutes
    # Calling method progress() over object of class Audio
    # This prints the address of the object instead of the contents
    print(audio.progress())
    frames = 5
    print(frames)
    print(audio)

print('Instantiating Video...')
# Instantiating object audio over class Video
video = Video(audio)
print(audio)

