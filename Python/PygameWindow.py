# Import Necessary Libraries
import pygame# GUI game 

# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400,500))

# Create a loop to run till the game is quit by the user
done = False

while not done:# while true

	# Clear the event queue
	for event in pygame.event.get():# get method that take input
		if event.type == pygame.QUIT:
			pygame.quit()

	# Make the changes visible
	pygame.display.flip()