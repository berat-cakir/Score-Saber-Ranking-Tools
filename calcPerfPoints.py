averageScore = float(input("Enter your expected average performance points per song: "))  # Your expected average performance points for each song
weightDecay = float(input("Enter the weight to consider for each consecutive ranked song (default is 0.965): "))  # Weight to consider for each consecutive ranked song
numberOfPlays = float(input("Enter the number of songs the scores to be calculated on: "))  # Predict for n number of songs

print("\nSong no | Total performance points")
totalScore = 0
for i in range(1, int(numberOfPlays) + 1):
    totalScore += weightDecay**(i - 1) * averageScore
    print(f'{i}. {totalScore:3.2f}pp')
   
print(f'\nYour expected total performance points after playing {int(numberOfPlays)} songs equals {totalScore:3.2f}pp')
input("\nPress ENTER to exit")