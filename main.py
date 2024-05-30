POS = ['ADP', 'NOUN', 'VERB', 'ADJ', 'CONJ', 'DET', 'ADV', 'NUM', 'PRON', 'PRT']
start_probability = {'ADP': 0,
                     'NOUN': 0,
                     'VERB': 0,
                     'ADJ': 0,
                     'CONJ': 0,
                     'DET': 0,
                     'ADV': 0,
                     'NUM': 0,
                     'PRON': 0,
                     'PRT': 0}

df = open("dataset/brown_train.txt", mode="r")
lines = df.readlines()
data = []
count = 0
for i in lines:
    sp = i.split(" ")
    for j in range(len(sp)):
        sp2 = sp[j].split("/")
        if sp2[0] != '\n':
            if sp2[1] in POS:
                if j == 0:
                    start_probability[sp2[1]] += 1
                lower = sp2[0].lower()
                data.append((lower, sp2[1]))


def generateUniqueTags(data):
    unique_tags = []
    for tag in data:
        if tag[1] not in unique_tags:
            unique_tags.append(tag[1])

    return unique_tags


def startProbabilityFunction(start):
    total_start_probability = sum(start.values())
    return {i: start[i] / total_start_probability for i in start_probability.keys()}


def transitionalProbabilityFunction(tags):
    M = {}
    for i in range(len(tags)):
        prev = tags[i - 1][1]
        current = tags[i][1]
        if (prev, current) not in M.keys():
            M[(prev, current)] = 1
        else:
            M[(prev, current)] += 1

    for tag in M.keys():
        current = tag
        total = M[current]
        for tag2 in M.keys():
            if current != tag2 and current[0] == tag2[0]:
                total += M[tag2]
        M[current] = M[current] / total

    return M


def emissionProbabilityFunction(tags):
    emission = {}
    word_counts = {}

    for word, tag in tags:
        word_counts[word] = word_counts.get(word, 0) + 1
        key = (word, tag)
        emission[key] = emission.get(key, 0) + 1
    for (word, tag), count in emission.items():
        emission[(word, tag)] = count / word_counts[word]

    return emission


StartProbability = startProbabilityFunction(start_probability)
EmissionProbability = emissionProbabilityFunction(data)
TransitionProbability = transitionalProbabilityFunction(data)


def viterbiAlgorithm(sentence, emission, transition, start, allTags):
    sentence = sentence.split(" ")
    firstIter = True
    prevProbability = {}
    OUTPUT = ""
    trainOutput = []
    i = 0
    for word in sentence:
        i += 1
        temp = {}
        for tag in allTags:
            maxVal = 0
            maxTag = ()
            current = (word, tag)
            if current in emission.keys():
                if firstIter:
                    emissionValue = emission[current]
                    startValue = start[current[1]]
                    temp[("Start", current[1])] = emissionValue * startValue
                else:
                    currentTag = current[1]
                    for prev in prevProbability.keys():
                        prevTag = prev[1]
                        transitionalValue = transition[(prevTag, currentTag)]
                        emissionValue = emission[current]
                        # print(f"EMISSION of {current} = {emissionValue}")
                        # print(f"PREV{prevTag, current} AND TRANSITIONAL {transitionalValue}")
                        ans = transitionalValue * emissionValue * prevProbability[prev]
                        if ans > maxVal:
                            maxVal = ans
                            maxTag = (prevTag, currentTag)
                    temp[maxTag] = maxVal
                prevProbability = temp

        # print(f"PREV PROB {prevProbability}, WORD = {word}")
        if prevProbability:
            ans = word, max(prevProbability, key=lambda x: prevProbability[x])[1]
            OUTPUT += f"{ans[0]}({ans[1]}) "
            trainOutput.append(ans[1])
        else:
            print(f"{word} not found")

            return False

        firstIter = False


    return OUTPUT

def SecondOrderHMM(emissionProbabilities, transitionProbabilities, startProbabilities, sentence):
    POSans = []
    uniqueTags = generateUniqueTags(data)
    firstTag = True
    prevProbability = {}
    ANS = ""
    totalCount = 0
    temp = {}
    for word in sentence.split(" "):
        totalCount += 1
        word = word.lower()
        maxTag = ()
        maxValue = 0
        for tag in uniqueTags:
            current = (word, tag)
            if current in data:
                if firstTag:
                    startProbability = startProbabilities[tag]
                    emission = emissionProbabilities[current]
                    total = emission * startProbability
                    if total > maxValue:
                        maxValue = total
                        maxTag = (tag, tag)

                elif totalCount == 2:
                    maxValue = 0
                    for previous in prevProbability:
                        tTag = (previous[1][0], current[1])
                        emission = emissionProbabilities[current]
                        transition = transitionProbabilities[tTag]
                        prev = prevProbability[previous]
                        total = emission * transition * prev
                        if total > maxValue:
                            maxValue = total
                            maxTag = tTag
                else:

                    for previous in prevProbability:
                        prev *= prevProbability[previous]
                    tTag = (previous[1][0], current[1])
                    emission = emissionProbabilities[current]
                    transition = transitionProbabilities[tTag]
                    total = emission * transition * prev
                    if total > maxValue:
                        maxValue = total
                        maxTag = tTag

        temp[(current[0], maxTag)] = maxValue

        prevProbability = temp

        ANS += f"{current[0]}({maxTag[1]}) "
        POSans.append(maxTag[1])
        if totalCount >= 2:
            for item in temp:
                temp.pop(item)
                break

        firstTag = False

    return ANS


print(len(EmissionProbability))
sent = input("Input Sentence: ")

allTags = generateUniqueTags(data)

print(viterbiAlgorithm(sent, EmissionProbability, TransitionProbability, StartProbability, allTags))
# print(SecondOrderHMM(EmissionProbability, TransitionProbability, StartProbability, sent))