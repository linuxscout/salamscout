CodepointCharCodes={};
CodepointCharCodes[u"أ"]=u"alif";
CodepointCharCodes[u"ء"]=u"alif";
CodepointCharCodes[u"ئ"]=u"alif";
CodepointCharCodes[u"ا"]=u"alif";
CodepointCharCodes[u"آ"]=u"alif";
CodepointCharCodes[u"ـ"]=u"";
CodepointCharCodes[u"إ"]=u"alif";
CodepointCharCodes[u"ب"]=u"beh";
CodepointCharCodes[u"ت"]=u"teh";
CodepointCharCodes[u"ث"]=u"theh";
CodepointCharCodes[u"ج"]=u"jim"
CodepointCharCodes[u"ح"]=u"hah";
CodepointCharCodes[u"خ"]=u"khah";
CodepointCharCodes[u"د"]=u"del";
CodepointCharCodes[u"ذ"]=u"dhel";
CodepointCharCodes[u"ر"]=u"reh";
CodepointCharCodes[u"ز"]=u"zey";
CodepointCharCodes[u"س"]=u"sin";
CodepointCharCodes[u"ش"]=u"shin";
CodepointCharCodes[u"ص"]=u"sad";
CodepointCharCodes[u"ض"]=u"dad";
CodepointCharCodes[u"ط"]=u"tah";
CodepointCharCodes[u"ظ"]=u"zah";
CodepointCharCodes[u"ع"]=u"ain";
CodepointCharCodes[u"غ"]=u"ghain";
CodepointCharCodes[u"ف"]=u"feh";
CodepointCharCodes[u"ق"]=u"qaf";
CodepointCharCodes[u"ك"]=u"kaf";
CodepointCharCodes[u"ل"]=u"lam";
CodepointCharCodes[u"م"]=u"meem";
CodepointCharCodes[u"ن"]=u"noun";
CodepointCharCodes[u"ه"]=u"heh";
CodepointCharCodes[u"ة"]=u"heh";
CodepointCharCodes[u"و"]=u"waw";
CodepointCharCodes[u"ؤ"]=u"waw";
CodepointCharCodes[u"ي"]=u"yeh";
CodepointCharCodes[u"ى"]=u"yeh";
CodepointCharCodes[u"1"]=u"alif";
CodepointCharCodes[u"2"]=u"beh";
CodepointCharCodes[u"3"]=u"teh";
CodepointCharCodes[u"4"]=u"theh";
CodepointCharCodes[u"5"]=u"jim";
CodepointCharCodes[u"6"]=u"hah";
CodepointCharCodes[u"7"]=u"khah";
CodepointCharCodes[u"8"]=u"del";
CodepointCharCodes[u"9"]=u"dhel";
CodepointCharCodes[u"0"]=u"reh";
CodepointCharCodes[u" "]=u"word";

# tables of choices  for quiz
CodepointCharCodesQuiz={}
CodepointCharCodesQuiz[u"ا"]=u"alif";
CodepointCharCodesQuiz[u"ب"]=u"beh";
CodepointCharCodesQuiz[u"ت"]=u"teh";
CodepointCharCodesQuiz[u"ث"]=u"theh";
CodepointCharCodesQuiz[u"ج"]=u"jim";
CodepointCharCodesQuiz[u"ح"]=u"hah";
CodepointCharCodesQuiz[u"خ"]=u"khah";
CodepointCharCodesQuiz[u"د"]=u"del";
CodepointCharCodesQuiz[u"ذ"]=u"dhel";
CodepointCharCodesQuiz[u"ر"]=u"reh";
CodepointCharCodesQuiz[u"ز"]=u"zey";
CodepointCharCodesQuiz[u"س"]=u"sin";
CodepointCharCodesQuiz[u"ش"]=u"shin";
CodepointCharCodesQuiz[u"ص"]=u"sad";
CodepointCharCodesQuiz[u"ض"]=u"dad";
CodepointCharCodesQuiz[u"ط"]=u"tah";
CodepointCharCodesQuiz[u"ظ"]=u"zah";
CodepointCharCodesQuiz[u"ع"]=u"ain";
CodepointCharCodesQuiz[u"غ"]=u"ghain";
CodepointCharCodesQuiz[u"ف"]=u"feh";
CodepointCharCodesQuiz[u"ق"]=u"qaf";
CodepointCharCodesQuiz[u"ك"]=u"kaf";
CodepointCharCodesQuiz[u"ل"]=u"lam";
CodepointCharCodesQuiz[u"م"]=u"meem";
CodepointCharCodesQuiz[u"ن"]=u"noun";
CodepointCharCodesQuiz[u"هـ"]=u"heh";
CodepointCharCodesQuiz[u"و"]=u"waw";
CodepointCharCodesQuiz[u"ي"]=u"yeh";

def codepoint(text,explicated=False):

    textcoded=u"";
    if explicated:
        path="<img src='images/codepoint/"
    else:
        path="<img src='images/codepoint/imagesquiz/"

    for c in text:
        if CodepointCharCodes.has_key(c):
            textcoded+=path+CodepointCharCodes[c]+".png'>\t"
##            textcoded+=CodepointCharCodes[c];
        else:
            textcoded+=c
    return textcoded;


##
##text=u"السلام الكشفي"
##print code_point(text).encode('utf8');