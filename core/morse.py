MorseCharCodes={};

# tables of choices  for quiz
MorseCharCodesQuiz={}


MorseCharCodes[u"أ"]=u". _";
MorseCharCodes[u"ء"]=u". _";
MorseCharCodes[u"ئ"]=u". _";
MorseCharCodes[u"ا"]=u". _";
MorseCharCodes[u"آ"]=u". _";
MorseCharCodes[u"ـ"]=u"";
MorseCharCodes[u"إ"]=u". _";
MorseCharCodes[u"ب"]=u"_ . . .";
MorseCharCodes[u"ت"]=u"_";
MorseCharCodes[u"ث"]=u"_ . _ .";
MorseCharCodes[u"ج"]=u". _ _ _";
MorseCharCodes[u"ح"]=u". . . .";
MorseCharCodes[u"خ"]=u"_ _ _";
MorseCharCodes[u"د"]=u"_ . .";
MorseCharCodes[u"ذ"]=u"_ _ . .";
MorseCharCodes[u"ر"]=u". _ .";
MorseCharCodes[u"ز"]=u"_ _ _ .";
MorseCharCodes[u"س"]=u". . .";
MorseCharCodes[u"ش"]=u"_ _ _ _";
MorseCharCodes[u"ص"]=u"_ . . _";
MorseCharCodes[u"ض"]=u". . . _";
MorseCharCodes[u"ط"]=u". . _";
MorseCharCodes[u"ظ"]=u"_ . _ _";
MorseCharCodes[u"ع"]=u". _ . _";
MorseCharCodes[u"غ"]=u"_ _ .";
MorseCharCodes[u"ف"]=u". . _ .";
MorseCharCodes[u"ق"]=u"_ _ . _";
MorseCharCodes[u"ك"]=u"_ . _";
MorseCharCodes[u"ل"]=u". _ . .";
MorseCharCodes[u"م"]=u"_ _";
MorseCharCodes[u"ن"]=u"_ .";
MorseCharCodes[u"ه"]=u". ._ . .";
MorseCharCodes[u"ة"]=u". ._ . .";
MorseCharCodes[u"و"]=u". _ _";
MorseCharCodes[u"ؤ"]=u". _ _";
MorseCharCodes[u"ي"]=u". .";
MorseCharCodes[u"ى"]=u". .";
MorseCharCodes[u"1"]=u". _ _ _ _";
MorseCharCodes[u"2"]=u". . _ _ _";
MorseCharCodes[u"3"]=u". . . _ _";
MorseCharCodes[u"4"]=u". . . . _";
MorseCharCodes[u"5"]=u". . . . .";
MorseCharCodes[u"6"]=u"_ . . . .";
MorseCharCodes[u"7"]=u"_ _ . . .";
MorseCharCodes[u"8"]=u"_ _ _ . .";
MorseCharCodes[u"9"]=u"_ _ _ _ .";
MorseCharCodes[u"0"]=u"_ _ _ _ _";

# tables of choices  for quiz
MorseCharCodesQuiz[u"أ"]=u". _";
MorseCharCodesQuiz[u"ب"]=u"_ . . .";
MorseCharCodesQuiz[u"ت"]=u"_";
MorseCharCodesQuiz[u"ث"]=u"_ . _ .";
MorseCharCodesQuiz[u"ج"]=u". _ _ _";
MorseCharCodesQuiz[u"ح"]=u". . . .";
MorseCharCodesQuiz[u"خ"]=u"_ _ _";
MorseCharCodesQuiz[u"د"]=u"_ . .";
MorseCharCodesQuiz[u"ذ"]=u"_ _ . .";
MorseCharCodesQuiz[u"ر"]=u". _ .";
MorseCharCodesQuiz[u"ز"]=u"_ _ _ .";
MorseCharCodesQuiz[u"س"]=u". . .";
MorseCharCodesQuiz[u"ش"]=u"_ _ _ _";
MorseCharCodesQuiz[u"ص"]=u"_ . . _";
MorseCharCodesQuiz[u"ض"]=u". . . _";
MorseCharCodesQuiz[u"ط"]=u". . _";
MorseCharCodesQuiz[u"ظ"]=u"_ . _ _";
MorseCharCodesQuiz[u"ع"]=u". _ . _";
MorseCharCodesQuiz[u"غ"]=u"_ _ .";
MorseCharCodesQuiz[u"ف"]=u". . _ .";
MorseCharCodesQuiz[u"ق"]=u"_ _ . _";
MorseCharCodesQuiz[u"ك"]=u"_ . _";
MorseCharCodesQuiz[u"ل"]=u". _ . .";
MorseCharCodesQuiz[u"م"]=u"_ _";
MorseCharCodesQuiz[u"ن"]=u"_ .";
MorseCharCodesQuiz[u"ه"]=u". ._ . .";
MorseCharCodesQuiz[u"و"]=u". _ _";
MorseCharCodesQuiz[u"ي"]=u". .";
MorseCharCodesQuiz[u"1"]=u". _ _ _ _";
MorseCharCodesQuiz[u"2"]=u". . _ _ _";
MorseCharCodesQuiz[u"3"]=u". . . _ _";
MorseCharCodesQuiz[u"4"]=u". . . . _";
MorseCharCodesQuiz[u"5"]=u". . . . .";
MorseCharCodesQuiz[u"6"]=u"_ . . . .";
MorseCharCodesQuiz[u"7"]=u"_ _ . . .";
MorseCharCodesQuiz[u"8"]=u"_ _ _ . .";
MorseCharCodesQuiz[u"9"]=u"_ _ _ _ .";
MorseCharCodesQuiz[u"0"]=u"_ _ _ _ _";

def morse(text,explicated=False):
    textcoded=u"";
    for c in text:
        if MorseCharCodes.has_key(c):
            if explicated:
                textcoded+="("+c+")"
            textcoded+=MorseCharCodes[c]+"\t"
        else:
            textcoded+=c
    return textcoded;
##
##text=u"السلام الكشفي"
##print morse(text,True).encode('utf8');

##
##for c in MorseCharCodesQuiz.keys():
##    m=MorseCharCodesQuiz[c];
##    print "<tr>"
##    print "<td>"+c+"</td>"+"<td>"+m+"</td>"
##    print "</tr>"


