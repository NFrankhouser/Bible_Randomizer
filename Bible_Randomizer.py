import random

print("The King James Bible Book and Chapter Random Selector")
# print("=======================================================================================")
print("---------------------------------------------------------------------------------------")
print("Please select one of the following.")
print("(If you are already planning to go to either the Old or New Testaments.")
print(" Just enter the one you want to go to. Otherwise choose the Both to both as an option.)")
print("Old Testament (O), New Testament (N), or Both (B)")

while True:

    testament = input("Start with: ").upper()
    BibleOptions = ["OLD TESTAMENT", "O", "OLD", "NEW TESTAMENT", "NEW", "N", "BOTH", "B"]
    partBible = ["Old Testament", "New Testament"]
    oldTest = ["Genesis", "Exodus", "Leviticus", "Numbers",
               "Deuteronomy", "Joshua", "Judges", "Ruth",
               "1 Samuel", "2 Samuel", "1 Kings", "2 Kings",
               "1 Chronicles", "2 Chronicles", "Ezra",
               "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
               "Ecclesiastes", "Song of Solomon", "Isaiah",
               "Jeremiah", "Lamentations", "Ezekiel", "Daniel",
               "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
               "Nahum", "Habakkuk", "Zephaniah", "Haggai",
               "Zechariah", "Malachi"]

    tempList = []
    tempList2 = []
    tempList3 = []
    tempList4 = []
    tempList5 = []

    # Old Testament Book Chapters
    Genesis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
               22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
               40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    Exodus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    Leviticus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27]
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
               22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    Deuteronomy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    Joshua = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    Judges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    Ruth = [1, 2, 3, 4]
    Samuel_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    Samuel_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24]
    Kings_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    Kings_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25]
    Chronicles_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    Chronicles_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                    32, 33, 34, 35, 36]
    Ezra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Nehemiah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Esther = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Job = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
           38, 39, 40, 41, 42]
    Psalm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
             38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
             55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
             72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
             90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
             105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
             118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
             131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
             144, 145, 146, 147, 148, 149, 150]
    Proverbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    Ecclesiastes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Song_of_Solomon = [1, 2, 3, 4, 5, 6, 7, 8]
    Isaiah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
              36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
              53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    Jeremiah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    Lamentations = [1, 2, 3, 4, 5]
    Ezekiel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
               39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
    Daniel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    Hosea = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    Joel = [1, 2, 3]
    Amos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Obadiah = [1]
    Jonah = [1, 2, 3, 4]
    Micah = [1, 2, 3, 4, 5, 6, 7]
    Nahum = [1, 2, 3]
    Habakkuk = [1, 2, 3]
    Zephaniah = [1, 2, 3]
    Haggai = [1, 2]
    Zechariah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    Malachi = [1, 2, 3, 4]

    # Old Testament Book Chapters
    Matthew = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28]

    Mark = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    Luke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            22, 23, 24]

    John = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

    Acts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
            22, 23, 24, 25, 26, 27, 28]

    Romans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    Corinthians_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    Corinthians_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    Galatians = [1, 2, 3, 4, 5, 6]

    Ephesians = [1, 2, 3, 4, 5, 6]

    Philippians = [1, 2, 3, 4]

    Colossians = [1, 2, 3, 4]

    Thessalonians_1 = [1, 2, 3, 4, 5]

    Thessalonians_2 = [1, 2, 3]

    Timothy_1 = [1, 2, 3, 4, 5, 6]

    Timothy_2 = [1, 2, 3, 4]

    Titus = [1, 2, 3]

    Philemon = [1]

    Hebrews = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    James = [1, 2, 3, 4, 5]

    Peter_1 = [1, 2, 3, 4, 5]

    Peter_2 = [1, 2, 3]

    John_1 = [1, 2, 3, 4, 5]

    John_2 = [1]

    John_3 = [1]

    Jude = [1]

    Revelation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                  17, 18, 19, 20, 21, 22]

    # If user types in "Old Testament"
    if testament == "OLD TESTAMENT":
        print("Selected: Old Testament")
        bList = []
        for b in oldTest:
            for i in range(40):
                bk = random.choice(oldTest)
            bList.append(bk)
            # print(bList)
            """Returns only one of the most occurring items"""
            most1 = max(bList, key=bList.count)
            # print(most1)
            tempList.append(most1)
            # print(tempList)
            most2 = max(tempList, key=tempList.count)
            # print(most2)
            tempList2.append(most2)
            # print(tempList2)
            most3 = max(tempList2, key=tempList2.count)
            # print(most3)
            tempList3.append(most3)
            # print(tempList3)
            most4 = max(tempList3, key=tempList3.count)
            tempList4.append(most4)
            # print(tempList4)
            most5 = max(tempList4, key=tempList4.count)
            tempList5.append(most5)
        """Prints chosen Book."""
        print("Book: " + tempList5[0])

        """The Below Block is for choosing a Chapter in Genesis."""
        if tempList5[0] == "Genesis":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(51):
                bookChapter = random.choice(Genesis)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Exodus"""
        if tempList5[0] == "Exodus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(41):
                bookChapter = random.choice(Exodus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Leviticus"""
        if tempList5[0] == "Leviticus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(28):
                bookChapter = random.choice(Leviticus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Numbers"""
        if tempList5[0] == "Numbers":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Numbers)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Deuteronomy"""
        if tempList5[0] == "Deuteronomy":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(35):
                bookChapter = random.choice(Deuteronomy)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joshua"""
        if tempList5[0] == "Joshua":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Joshua)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Judges"""
        if tempList5[0] == "Judges":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(22):
                bookChapter = random.choice(Judges)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ruth"""
        if tempList5[0] == "Ruth":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Ruth)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Samuel"""
        if tempList5[0] == "1 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Samuel_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Samuel"""
        if tempList5[0] == "2 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Samuel_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Kings"""
        if tempList5[0] == "1 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(23):
                bookChapter = random.choice(Kings_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Kings"""
        if tempList5[0] == "2 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(26):
                bookChapter = random.choice(Kings_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Chronicles"""
        if tempList5[0] == "1 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(30):
                bookChapter = random.choice(Chronicles_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Chronicles"""
        if tempList5[0] == "2 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Chronicles_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezra"""
        if tempList5[0] == "Ezra":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Ezra)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nehemiah"""
        if tempList5[0] == "Nehemiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(14):
                bookChapter = random.choice(Nehemiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Esther"""
        if tempList5[0] == "Esther":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Esther)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Job"""
        if tempList5[0] == "Job":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(43):
                bookChapter = random.choice(Job)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Psalms"""
        if tempList5[0] == "Psalms":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(151):
                bookChapter = random.choice(Psalm)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Proverbs"""
        if tempList5[0] == "Proverbs":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Proverbs)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ecclesiastes"""
        if tempList5[0] == "Ecclesiastes":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Ecclesiastes)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Song of Solomon"""
        if tempList5[0] == "Song of Solomon":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(9):
                bookChapter = random.choice(Song_of_Solomon)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Isaiah"""
        if tempList5[0] == "Isaiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(67):
                bookChapter = random.choice(Isaiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jeremiah"""
        if tempList5[0] == "Jeremiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(53):
                bookChapter = random.choice(Jeremiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Lamentations"""
        if tempList5[0] == "Lamentations":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(6):
                bookChapter = random.choice(Lamentations)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezekiel"""
        if tempList5[0] == "Ezekiel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(49):
                bookChapter = random.choice(Ezekiel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Daniel"""
        if tempList5[0] == "Daniel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Daniel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Hosea"""
        if tempList5[0] == "Hosea":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Hosea)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joel"""
        if tempList5[0] == "Joel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Joel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Amos"""
        if tempList5[0] == "Amos":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(10):
                bookChapter = random.choice(Amos)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Obadiah"""
        if tempList5[0] == "Obadiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(1):
                bookChapter = random.choice(Obadiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jonah"""
        if tempList5[0] == "Jonah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Jonah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Micah"""
        if tempList5[0] == "Micah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(8):
                bookChapter = random.choice(Micah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nahum"""
        if tempList5[0] == "Nahum":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Nahum)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Habakkuk"""
        if tempList5[0] == "Habakkuk":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Habakkuk)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zephaniah"""
        if tempList5[0] == "Zephaniah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Zephaniah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Haggai"""
        if tempList5[0] == "Haggai":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(3):
                bookChapter = random.choice(Haggai)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zechariah"""
        if tempList5[0] == "Zechariah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Zechariah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Malachi"""
        if tempList5[0] == "Malachi":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Malachi)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

    # If the user types the Letter "O" for Old Testament
    elif testament == "O":
        print("=======================================================================================")
        # print("---------------------------------------------------------------------------------------")
        print("Selected: Old Testament")
        bList = []
        for b in oldTest:
            for i in range(40):
                bk = random.choice(oldTest)
            bList.append(bk)
            # print(bList)
            """Returns only one of the most occurring items"""
            most1 = max(bList, key=bList.count)
            # print(most1)
            tempList.append(most1)
            # print(tempList)
            most2 = max(tempList, key=tempList.count)
            # print(most2)
            tempList2.append(most2)
            # print(tempList2)
            most3 = max(tempList2, key=tempList2.count)
            # print(most3)
            tempList3.append(most3)
            # print(tempList3)
            most4 = max(tempList3, key=tempList3.count)
            tempList4.append(most4)
            # print(tempList4)
            most5 = max(tempList4, key=tempList4.count)
            tempList5.append(most5)
        """Prints chosen Book."""
        print("Book: " + tempList5[0])

        """The Below Block is for choosing a Chapter in Genesis."""
        if tempList5[0] == "Genesis":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(51):
                bookChapter = random.choice(Genesis)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Exodus"""
        if tempList5[0] == "Exodus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(41):
                bookChapter = random.choice(Exodus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Leviticus"""
        if tempList5[0] == "Leviticus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(28):
                bookChapter = random.choice(Leviticus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Numbers"""
        if tempList5[0] == "Numbers":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Numbers)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Deuteronomy"""
        if tempList5[0] == "Deuteronomy":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(35):
                bookChapter = random.choice(Deuteronomy)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joshua"""
        if tempList5[0] == "Joshua":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Joshua)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Judges"""
        if tempList5[0] == "Judges":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(22):
                bookChapter = random.choice(Judges)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ruth"""
        if tempList5[0] == "Ruth":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Ruth)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Samuel"""
        if tempList5[0] == "1 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Samuel_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Samuel"""
        if tempList5[0] == "2 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Samuel_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Kings"""
        if tempList5[0] == "1 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(23):
                bookChapter = random.choice(Kings_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Kings"""
        if tempList5[0] == "2 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(26):
                bookChapter = random.choice(Kings_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Chronicles"""
        if tempList5[0] == "1 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(30):
                bookChapter = random.choice(Chronicles_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Chronicles"""
        if tempList5[0] == "2 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Chronicles_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezra"""
        if tempList5[0] == "Ezra":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Ezra)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nehemiah"""
        if tempList5[0] == "Nehemiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(14):
                bookChapter = random.choice(Nehemiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Esther"""
        if tempList5[0] == "Esther":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Esther)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Job"""
        if tempList5[0] == "Job":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(43):
                bookChapter = random.choice(Job)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Psalms"""
        if tempList5[0] == "Psalms":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(151):
                bookChapter = random.choice(Psalm)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Proverbs"""
        if tempList5[0] == "Proverbs":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Proverbs)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ecclesiastes"""
        if tempList5[0] == "Ecclesiastes":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Ecclesiastes)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Song of Solomon"""
        if tempList5[0] == "Song of Solomon":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(9):
                bookChapter = random.choice(Song_of_Solomon)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Isaiah"""
        if tempList5[0] == "Isaiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(67):
                bookChapter = random.choice(Isaiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jeremiah"""
        if tempList5[0] == "Jeremiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(53):
                bookChapter = random.choice(Jeremiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Lamentations"""
        if tempList5[0] == "Lamentations":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(6):
                bookChapter = random.choice(Lamentations)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezekiel"""
        if tempList5[0] == "Ezekiel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(49):
                bookChapter = random.choice(Ezekiel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Daniel"""
        if tempList5[0] == "Daniel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Daniel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Hosea"""
        if tempList5[0] == "Hosea":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Hosea)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joel"""
        if tempList5[0] == "Joel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Joel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Amos"""
        if tempList5[0] == "Amos":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(10):
                bookChapter = random.choice(Amos)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Obadiah"""
        if tempList5[0] == "Obadiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(1):
                bookChapter = random.choice(Obadiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jonah"""
        if tempList5[0] == "Jonah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Jonah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Micah"""
        if tempList5[0] == "Micah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(8):
                bookChapter = random.choice(Micah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nahum"""
        if tempList5[0] == "Nahum":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Nahum)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Habakkuk"""
        if tempList5[0] == "Habakkuk":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Habakkuk)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zephaniah"""
        if tempList5[0] == "Zephaniah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Zephaniah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Haggai"""
        if tempList5[0] == "Haggai":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(3):
                bookChapter = random.choice(Haggai)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zechariah"""
        if tempList5[0] == "Zechariah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Zechariah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Malachi"""
        if tempList5[0] == "Malachi":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Malachi)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

    # If user types "Old" for Old Testament
    elif testament == "OLD":
        print("Selected: Old Testament")
        bList = []
        for b in oldTest:
            for i in range(40):
                bk = random.choice(oldTest)
            bList.append(bk)
            # print(bList)
            """Returns only one of the most occurring items"""
            most1 = max(bList, key=bList.count)
            # print(most1)
            tempList.append(most1)
            # print(tempList)
            most2 = max(tempList, key=tempList.count)
            # print(most2)
            tempList2.append(most2)
            # print(tempList2)
            most3 = max(tempList2, key=tempList2.count)
            # print(most3)
            tempList3.append(most3)
            # print(tempList3)
            most4 = max(tempList3, key=tempList3.count)
            tempList4.append(most4)
            # print(tempList4)
            most5 = max(tempList4, key=tempList4.count)
            tempList5.append(most5)
        """Prints chosen Book."""
        print("Book: " + tempList5[0])

        """The Below Block is for choosing a Chapter in Genesis."""
        if tempList5[0] == "Genesis":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(51):
                bookChapter = random.choice(Genesis)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Exodus"""
        if tempList5[0] == "Exodus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(41):
                bookChapter = random.choice(Exodus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Leviticus"""
        if tempList5[0] == "Leviticus":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(28):
                bookChapter = random.choice(Leviticus)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Numbers"""
        if tempList5[0] == "Numbers":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Numbers)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Deuteronomy"""
        if tempList5[0] == "Deuteronomy":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(35):
                bookChapter = random.choice(Deuteronomy)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joshua"""
        if tempList5[0] == "Joshua":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Joshua)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Judges"""
        if tempList5[0] == "Judges":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(22):
                bookChapter = random.choice(Judges)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ruth"""
        if tempList5[0] == "Ruth":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Ruth)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Samuel"""
        if tempList5[0] == "1 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Samuel_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Samuel"""
        if tempList5[0] == "2 Samuel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(25):
                bookChapter = random.choice(Samuel_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Kings"""
        if tempList5[0] == "1 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(23):
                bookChapter = random.choice(Kings_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Kings"""
        if tempList5[0] == "2 Kings":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(26):
                bookChapter = random.choice(Kings_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """1 Chronicles"""
        if tempList5[0] == "1 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(30):
                bookChapter = random.choice(Chronicles_1)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """2 Chronicles"""
        if tempList5[0] == "2 Chronicles":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(37):
                bookChapter = random.choice(Chronicles_2)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezra"""
        if tempList5[0] == "Ezra":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Ezra)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nehemiah"""
        if tempList5[0] == "Nehemiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(14):
                bookChapter = random.choice(Nehemiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Esther"""
        if tempList5[0] == "Esther":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(11):
                bookChapter = random.choice(Esther)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Job"""
        if tempList5[0] == "Job":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(43):
                bookChapter = random.choice(Job)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Psalms"""
        if tempList5[0] == "Psalms":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(151):
                bookChapter = random.choice(Psalm)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Proverbs"""
        if tempList5[0] == "Proverbs":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(32):
                bookChapter = random.choice(Proverbs)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ecclesiastes"""
        if tempList5[0] == "Ecclesiastes":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Ecclesiastes)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Song of Solomon"""
        if tempList5[0] == "Song of Solomon":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(9):
                bookChapter = random.choice(Song_of_Solomon)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Isaiah"""
        if tempList5[0] == "Isaiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(67):
                bookChapter = random.choice(Isaiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jeremiah"""
        if tempList5[0] == "Jeremiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(53):
                bookChapter = random.choice(Jeremiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Lamentations"""
        if tempList5[0] == "Lamentations":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(6):
                bookChapter = random.choice(Lamentations)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Ezekiel"""
        if tempList5[0] == "Ezekiel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(49):
                bookChapter = random.choice(Ezekiel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Daniel"""
        if tempList5[0] == "Daniel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(13):
                bookChapter = random.choice(Daniel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Hosea"""
        if tempList5[0] == "Hosea":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Hosea)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Joel"""
        if tempList5[0] == "Joel":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Joel)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Amos"""
        if tempList5[0] == "Amos":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(10):
                bookChapter = random.choice(Amos)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Obadiah"""
        if tempList5[0] == "Obadiah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(1):
                bookChapter = random.choice(Obadiah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Jonah"""
        if tempList5[0] == "Jonah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Jonah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Micah"""
        if tempList5[0] == "Micah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(8):
                bookChapter = random.choice(Micah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Nahum"""
        if tempList5[0] == "Nahum":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Nahum)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Habakkuk"""
        if tempList5[0] == "Habakkuk":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Habakkuk)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zephaniah"""
        if tempList5[0] == "Zephaniah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(4):
                bookChapter = random.choice(Zephaniah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Haggai"""
        if tempList5[0] == "Haggai":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(3):
                bookChapter = random.choice(Haggai)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Zechariah"""
        if tempList5[0] == "Zechariah":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(15):
                bookChapter = random.choice(Zechariah)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

        """Malachi"""
        if tempList5[0] == "Malachi":
            chList = []
            chList2 = []
            chList3 = []
            chList4 = []
            chList5 = []
            chList6 = []
            chList7 = []
            for c in range(5):
                bookChapter = random.choice(Malachi)
                chList.append(bookChapter)
                chM1 = max(chList, key=chList.count)
                chList2.append(chM1)
                chM2 = max(chList2, key=chList2.count)
                chList3.append(chM2)
                chM3 = max(chList3, key=chList3.count)
                chList4.append(chM3)
                chM4 = max(chList4, key=chList4.count)
                chList5.append(chM4)
                chM5 = max(chList5, key=chList5.count)
                chList6.append(chM5)
                chM6 = max(chList6, key=chList6.count)
                chList7.append(chM6)
            print("Chapter: " + str(chList7[0]))

    # If user types "New Testament"
    elif testament == "NEW TESTAMENT":
        print("Selected: New Testament")
    elif testament == "NEW":
        print("Selected: New Testament")
    elif testament == "N":
        print("Selected: New Testament")
    elif testament == "BOTH":
        print("Selected: Old and New Testaments")
    elif testament == "B":
        print("Selected: Old and New Testaments")
        print("----------------------------------------------------------------")

    else:
        print("Please enter a valid option.")

    print("=======================================================================================")
    # if user wants to use again
    use_again = input("Go again? (Y/N): ")
    if use_again != "yes":
        if use_again != "y":
            break
print("Have a nice day.")
