# import random
# import math


# def rollDie():
#     return random.choice([1, 2, 3, 4, 5, 6])


# def checkPascal(numTrials):
#     numWins = 0
#     for i in range(numTrials):
#         for j in range(24):
#             d1 = rollDie()
#             d2 = rollDie()
#             if d1 == 6 and d2 == 6:
#                 numWins += 1
#                 break
#     print("Probability of winning = ", numWins / numTrials)


# checkPascal(1000000)

import random
import math


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0

    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpLosses += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break

    def passResults(self):
        return (self.passWins, self.passLosses)

    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)


def stdDev(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def crapsSim(handsPerGame, numGames):
    games = []

    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)

    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses) / float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses) / float(handsPerGame))

    meanROI = str(round((100 * sum(pROIPerGame) / numGames), 4)) + "%"
    sigma = str(round(100 * stdDev(pROIPerGame), 4)) + "%"
    print("Pass:", "Mean ROI =", meanROI, "Std. Dev. =", sigma)
    meanROI = str(round((100 * sum(dpROIPerGame) / numGames), 4)) + "%"
    sigma = str(round(100 * stdDev(dpROIPerGame), 4)) + "%"
    print("Don't pass:", "Mean ROI =", meanROI, "Std Dev =", sigma)


crapsSim(20, 10)
