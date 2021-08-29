repeat = True

while repeat:

    averageScore = float(str(input("Enter your expected average performance points per song: ")).replace(",", "."))  # Your expected average performance points for each song
    numberOfPlays = float(str(input("Enter the number of songs the scores to be calculated on: ")).replace(",", "."))  # Predict for n number of songs
    if str(input("Do you want to use the standard weight (0.965) for each consecutive ranked song? (Y/N): ")).upper() == "N":
        weightDecay = float(str(input("Enter the weight to consider for each consecutive ranked song (default is 0.965): ")).replace(",", "."))  # Weight to consider for each consecutive ranked song
    else:
        weightDecay = 0.965

    print("\nSong no | Cumulated performance points")
    totalScore = 0
    for i in range(1, int(numberOfPlays) + 1):
        totalScore += weightDecay**(i - 1) * averageScore
        print(f"{i}. {totalScore:3.2f}pp")
    
    print(f"\nYour expected total performance points after playing {int(numberOfPlays)} songs equals {totalScore:3.2f}pp ({averageScore:3.2f}pp on average) with a weight decay of {weightDecay}")
    if str(input("\nPress ENTER to exit or R to start over: ")).upper() != "R":
        repeat = False
    else:
        print()