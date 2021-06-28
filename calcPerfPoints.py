averageScore = 250  # Your expected average performance points for each play
weightDecay = 0.965  # Weight to consider for each consecutive ranked play
numberOfPlays = 100  # Predict for n number of plays

totalScore = 0
for i in range(1, numberOfPlays + 1):
    totalScore += weightDecay**(i - 1) * averageScore
    print(f'{i}. {totalScore:3.2f}pp')