'When answering prompts correctFile(), nameDate(), honorStatement(), and videoLink(), Yes or No are the only accepted responses'

def computeGrade():
    if (correctFile()) == False:
        return 0
    if (nameDate()) == False:
        return 0
    if (honorStatement()) == False:
        return 0
    if (videoLink()) == False:
        return 0
    score = ((getCorrectScore()) + (getHygieneScore()) + (getEleganceScore()) + (getDiscussionScore()))
    res = score - (score * (getLateScore()) * 0.01)
    return res
    
def correctFile():
    """The only acceptable answers are Yes and No, other respones won't be recognized"""
    file = input('Did the student submit a single uncompressed file?')
    if file == 'Yes':
        return True 
    elif file == 'No':
        return False

def nameDate():
    """The only acceptable answers are Yes and No, other respones won't be recognized"""
    name = input('Did the student include their name and date?')
    if name == 'Yes':
        return True
    elif name == 'No':
        return False

def honorStatement():
    """The only acceptable answers are Yes and No, other respones won't be recognized"""    
    honor = input('Did the student include an honor statement?')
    if honor == 'Yes':
        return True
    elif honor == 'No':
        return False

def videoLink():
    """The only acceptable answers are Yes and No, other respones won't be recognized"""
    video = input('Did the student submit a video link?')
    if video == 'Yes':
        return True
    elif video == 'No':
        return False

def getCorrectScore():
    """Enter any numeric value between 0 and 10"""
    correct = eval(input('Out of 10 points, how would you evaluate the correctness of the score?'))
    return correct

def getEleganceScore():
    """Enter any numeric value between 0 and 10"""
    elegance = eval(input('Out of 10 points, how would you evaluate the elegance of the score?'))
    return elegance

def getHygieneScore():
    """Enter any numeric value between 0 and 10"""
    hygiene = eval(input('Out of 10 points, how would you evaluate the hygiene of the score?'))
    return hygiene

def getDiscussionScore():
    """Enter any numeric value between 0 and 10"""
    discussion = eval(input('Out of 10 points, how would you evaluate the discussion of the video?'))
    return discussion

def getLateScore():
    """Ener how many hours the assignment was late, 0 should be entered for on time assignments"""
    late = int(input('How many hours was the assignment late?'))
    return late
