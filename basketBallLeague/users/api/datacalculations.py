from operator import itemgetter


class Calculate():
    def calculatePercentile(data):
        length = len(data)
        nintyPercentile = round(length*0.9)
        # inorder to find th players who laid on the 90th percentile based on their average scores
        # players must be sorted by their average score
        sortedList = sorted(data, key=itemgetter('averagescore'))
        players = []
        if length > 0:
            for i in range(nintyPercentile-1, length):
                players.append(sortedList[i])

        return players
