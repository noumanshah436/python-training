'''

You are given few sentences as a list (Python list of sentences). Take a query string as
an input from the user. You have to pull out the sentences matching this query inputted by
the user in decreasing order of relevance after converting every word in the query and the
sentence to lowercase. Most relevant sentence is the one with the maximum number of matching
words with the query.
Sentences = [“This is good”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:
1.	python is not python snake
2.	python is good
3.	This is good
'''


def matching_words(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")    # strip removes extra spaces in front or rear of string
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # matching_words("This is good", "python is good")
    sentences = ["Perhaps you have wondered how predictable machines ",
                 "like computers can generate randomness.",
                 " In reality, most random numbers used in computer programs",
                 " are pseudo-random, which means ",
                 "they are generated in a predictable fashion ",
                 "are using a mathematical formula. ",
                 "This is fine for many purposes, but it ",
                 "may not be random in the way you expect ",
                 "if you're used to dice rolls and lottery drawings.",
                 "harry is a good bro", "Subscribe to code with harry"]

    query = input("Please enter the query string\n")
    scores = [matching_words(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\" -- ( score = {score}) ")

