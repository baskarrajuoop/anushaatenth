import os
import pyttsx3
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
#nltk.download()

data1=['name','hi','hey','hello','heyy','hii','nice','meet']
data2=['yes','sure','ok','okie','yass','yess','yas','yeah','ya','yea','ye']
data3=['no','nope','sorry','never','not now','not','bye','quit']

'''
def hf(str):
    words5=word_tokenize(str)
    x=1
    while x>0:
        for w5 in words5:
            if w5 in data2:
                x=-5
                continue
            elif w5 in data3:
                u6=input("do you want any other books to be recommended in some other genre of fiction?")
                words6=word_tokenize(u6)
                y=1
                while y>0:
                    for w6 in words6:
                        if w6 in data2:
                            x=-5
                            j=-5
                            y=-5
                            i+=1
                            continue
                        elif w6 in data3:
                            import cv2 
                            im1=cv2.imread(r"panda4.jpg")
                            cv2.imshow("Bye", im1)
                            cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            print("Bye")
                            exit()
                        else:
                            print("Do text smthg relevant or more easily understandable")
                            str1=input()
                            words6=word_tokenize(str1)
                            y+=1
                            continue
            else:
                print("Do text smthg relevant or more easily understandable")
                str1=input()
                words5=word_tokenize(str1)
                x+=1
                continue
    return'''


def yesorno(str):
    str=input()
    words2=word_tokenize(str)
    i=5
    while i>=5:
        for w2 in words2:
            if w2 in data2:
                print("Great!Let's get started")
                i=0
                break
            elif w2 in data3:
                print("maybe next time then...Byee")
                import cv2 
                im1=cv2.imread(r"panda4.jpg")
                cv2.imshow("Bye", im1)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                exit()
            elif w2 not in data2 and w2 not in data3:
                print("Do text smthg relevant or more easily understandable")
                str1=input()
                words2=word_tokenize(str1)
                i=i+1
            break
            
    return


print("Hi! I am Book Panda! What is your name?")
# initialize Text-to-speech engine
engine = pyttsx3.init()
#setting new voice rate
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)
#changing voices
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# converting this text to speech and playing it
text = "Hi! I am Book Panda. What is your name?"
engine.say(text)
engine.runAndWait()
u1=input()
stopWords = set(stopwords.words('english'))
sent=sent_tokenize(u1)
for w2 in sent:
    words1 = word_tokenize(w2)
    wordsFiltered = []
    for w1 in words1:
        if w1 not in stopWords and w1 not in data1:
            wordsFiltered.append(w1)
us1=wordsFiltered[0]
print("Nice to meet you",us1,"! I am a book recommending chatbot")
print("I recommend books to the user based on their interests.\nWill you let me help you?")
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
text = "Nice to meet you",us1,"! I am a book recommending chatbot. I recommend books to the user based on their interests. Will you let me help you?"
engine.say(text)
engine.runAndWait()
u2=input()
yesorno(u2)
i=1
while i>0:
    print("Select a genre from the genre list by typing the index number")
    f = open("C:\\Users\\gayathribaskar\\Desktop\\lists\\genrefile.txt","r")
    print(f.read())
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    text = "Select a genre from the genre list by typing the index number"
    engine.say(text)
    engine.runAndWait()
    u3=input()
    if u3=="1":
        j=1
        while j>0:
            print("")
            print("Here's a list of good historical fiction  books  by various authors,")
            data = [[1, 'The Wednesday Wars   ', 'Gary D. Schmidt'],
            [2, 'The Fountains Of Silence', 'Ruta Sepetys'],
            [3, 'Salt To The Sea        ', '     Ruta Sepetys'],
            [4,'Allies                 ', '             Alan Gratz']]
            print ("{:<10} {:<50} {:<30} ".format('S.no','Book name','Author name'))
            for v in data:
                s_no, book_name, author_name = v
                print ("{:<10} {:<27} {:<30}".format(s_no, book_name, author_name ))
            print("")
            print("Type the index no. to get more information about a particular book.")
            print("If you're not interseted in any of these books press 0")
            engine = pyttsx3.init()
            rate = engine.getProperty("rate")
            engine.setProperty("rate", 150)
            voices = engine.getProperty("voices")
            engine.setProperty("voice", voices[1].id)
            text = "Here's a list of good historical fiction  books  by various authors. Type the index no. to get more information about a particular book. If you're not interseted in any of these books press 0"
            engine.say(text)
            engine.runAndWait()
            u4=input()
            if u4=="1":
                print("")
                f = open("C:\\Users\\gayathribaskar\\Desktop\\hf\\hfdesc.txt","r")
                sep=f.read(447)
                print(sep)
                print("press any key to continue")
                engine = pyttsx3.init()
                rate = engine.getProperty("rate")
                engine.setProperty("rate", 150)
                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[1].id)
                text = "Press any key to continue"
                engine.say(text)
                engine.runAndWait()
                import cv2 
                im1=cv2.imread(r"hf1.png")
                cv2.imshow("hf1", im1)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print("Hope this was helpful!! Do you want more info on any of the other books?")
                engine = pyttsx3.init()
                rate = engine.getProperty("rate")
                engine.setProperty("rate", 150)
                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[1].id)
                text = "Hope this was helpful!! Do you want more info on any of the other books?"
                engine.say(text)
                engine.runAndWait()
                u5=input()
                words5=word_tokenize(u5)
                x=1
                while x>0:
                    for w5 in words5:
                        if w5 in data2:
                            x=-5
                            continue
                        elif w5 in data3:
                            u6=input("do you want any other books to be recommended in some other genre of fiction?")
                            words6=word_tokenize(u6)
                            y=1
                            while y>0:
                                for w6 in words6:
                                    if w6 in data2:
                                        x=-5
                                        j=-5
                                        y=-5
                                        i+=1
                                        continue
                                    elif w6 in data3:
                                        import cv2 
                                        im1=cv2.imread(r"panda4.jpg")
                                        cv2.imshow("Bye", im1)
                                        cv2.waitKey(0)
                                        cv2.destroyAllWindows()
                                        print("Bye")
                                        exit()
                                    else:
                                        print("Do text smthg relevant or more easily understandable")
                                        str1=input()
                                        words6=word_tokenize(str1)
                                        y+=1
                                    continue
                        else:
                            print("Do text smthg relevant or more easily understandable")
                            str1=input()
                            words5=word_tokenize(str1)
                            x+=1
                        continue










