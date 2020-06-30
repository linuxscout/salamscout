SemaphoreCharCodes={};
SemaphoreCharCodes[u"أ"]=u"alif";
SemaphoreCharCodes[u"ء"]=u"alif";
SemaphoreCharCodes[u"ئ"]=u"alif";
SemaphoreCharCodes[u"ا"]=u"alif";
SemaphoreCharCodes[u"آ"]=u"alif";
SemaphoreCharCodes[u"ـ"]=u"";
SemaphoreCharCodes[u"إ"]=u"alif";
SemaphoreCharCodes[u"ب"]=u"beh";
SemaphoreCharCodes[u"ت"]=u"teh";
SemaphoreCharCodes[u"ث"]=u"theh";
SemaphoreCharCodes[u"ج"]=u"jim"
SemaphoreCharCodes[u"ح"]=u"hah";
SemaphoreCharCodes[u"خ"]=u"khah";
SemaphoreCharCodes[u"د"]=u"del";
SemaphoreCharCodes[u"ذ"]=u"dhel";
SemaphoreCharCodes[u"ر"]=u"reh";
SemaphoreCharCodes[u"ز"]=u"zey";
SemaphoreCharCodes[u"س"]=u"sin";
SemaphoreCharCodes[u"ش"]=u"shin";
SemaphoreCharCodes[u"ص"]=u"sad";
SemaphoreCharCodes[u"ض"]=u"dad";
SemaphoreCharCodes[u"ط"]=u"tah";
SemaphoreCharCodes[u"ظ"]=u"zah";
SemaphoreCharCodes[u"ع"]=u"ain";
SemaphoreCharCodes[u"غ"]=u"ghain";
SemaphoreCharCodes[u"ف"]=u"feh";
SemaphoreCharCodes[u"ق"]=u"qaf";
SemaphoreCharCodes[u"ك"]=u"kaf";
SemaphoreCharCodes[u"ل"]=u"lam";
SemaphoreCharCodes[u"م"]=u"meem";
SemaphoreCharCodes[u"ن"]=u"noun";
SemaphoreCharCodes[u"ه"]=u"heh";
SemaphoreCharCodes[u"ة"]=u"heh";
SemaphoreCharCodes[u"و"]=u"waw";
SemaphoreCharCodes[u"ؤ"]=u"waw";
SemaphoreCharCodes[u"ي"]=u"yeh";
SemaphoreCharCodes[u"ى"]=u"yeh";
SemaphoreCharCodes[u"1"]=u"alif";
SemaphoreCharCodes[u"2"]=u"beh";
SemaphoreCharCodes[u"3"]=u"teh";
SemaphoreCharCodes[u"4"]=u"theh";
SemaphoreCharCodes[u"5"]=u"jim";
SemaphoreCharCodes[u"6"]=u"hah";
SemaphoreCharCodes[u"7"]=u"khah";
SemaphoreCharCodes[u"8"]=u"del";
SemaphoreCharCodes[u"9"]=u"dhel";
SemaphoreCharCodes[u"0"]=u"reh";
SemaphoreCharCodes[u" "]=u"word";

# tables of choices  for quiz
SemaphoreCharCodesQuiz={}
SemaphoreCharCodesQuiz[u"ا"]=u"alif";
SemaphoreCharCodesQuiz[u"ب"]=u"beh";
SemaphoreCharCodesQuiz[u"ت"]=u"teh";
SemaphoreCharCodesQuiz[u"ث"]=u"theh";
SemaphoreCharCodesQuiz[u"ج"]=u"jim";
SemaphoreCharCodesQuiz[u"ح"]=u"hah";
SemaphoreCharCodesQuiz[u"خ"]=u"khah";
SemaphoreCharCodesQuiz[u"د"]=u"del";
SemaphoreCharCodesQuiz[u"ذ"]=u"dhel";
SemaphoreCharCodesQuiz[u"ر"]=u"reh";
SemaphoreCharCodesQuiz[u"ز"]=u"zey";
SemaphoreCharCodesQuiz[u"س"]=u"sin";
SemaphoreCharCodesQuiz[u"ش"]=u"shin";
SemaphoreCharCodesQuiz[u"ص"]=u"sad";
SemaphoreCharCodesQuiz[u"ض"]=u"dad";
SemaphoreCharCodesQuiz[u"ط"]=u"tah";
SemaphoreCharCodesQuiz[u"ظ"]=u"zah";
SemaphoreCharCodesQuiz[u"ع"]=u"ain";
SemaphoreCharCodesQuiz[u"غ"]=u"ghain";
SemaphoreCharCodesQuiz[u"ف"]=u"feh";
SemaphoreCharCodesQuiz[u"ق"]=u"qaf";
SemaphoreCharCodesQuiz[u"ك"]=u"kaf";
SemaphoreCharCodesQuiz[u"ل"]=u"lam";
SemaphoreCharCodesQuiz[u"م"]=u"meem";
SemaphoreCharCodesQuiz[u"ن"]=u"noun";
SemaphoreCharCodesQuiz[u"هـ"]=u"heh";
SemaphoreCharCodesQuiz[u"و"]=u"waw";
SemaphoreCharCodesQuiz[u"ي"]=u"yeh";

def semaphore(text,explicated=False):

    textcoded=u"";
    if explicated:
        path="<img src='images/semaphore/"
    else:
        path="<img src='images/semaphore/imagesquiz/"

    for c in text:
        if SemaphoreCharCodes.has_key(c):
            textcoded+=path+SemaphoreCharCodes[c]+".png'>\t"
##            textcoded+=SemaphoreCharCodes[c];
        else:
            textcoded+=c
##    textcoded+="</body></html>"
    return textcoded;
##
##text=u"السلام الكشفي"
##print semaphore(text,True).encode('utf8');