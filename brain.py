from fa_console import fa_input
import matplotlib.pyplot as plt
import jdatetime as jdt
import pandas as pd
import random as rd

yeses = [
    "y", "yes", "yeah", "yea", "yeh", "yah", "yuh", "yep", "yip", "yup", "yupp","a","ar",
    "yas", "yass", "yasss", "yess", "yesss", "yeass", "yeahhh", "yessir", "yes sir",
    "yes ma'am", "yes please", "ya", "aye", "ay", "aye aye", "affirmative",
    "ok", "okay", "okey", "okey dokey", "okie", "okie dokie", "okei", "oki",
    "sure", "sure thing", "for sure", "of course", "certainly",
    "absolutely", "definitely", "indeed", "exactly", "correct", "right", "true",
    "agreed", "deal", "bet", "fine", "fine by me", "alright", "aight", "cool",
    "good", "all good", "sounds good", "works for me", "approved", "confirmed",
    "accepted", "affirm", "roger", "roger that", "copy", "copy that", "10-4",
    "understood", "got it", "will do", "no problem", "np",
    "next", "nxt", "next one", "next please", "continue", "continue please",
    "proceed", "go", "go ahead", "go for it", "go on", "keep going", "carry on",
    "let go", "lets go", "let's go", "let's do it", "do it", "come", "come on",
    "why not", "i'm in", "im in", "count me in", "ready", "good to go",
    "areh", "are", "ari", "arey", "areh baba", "are baba", "are dige",
    "bale", "baleh", "bali", "bale chashm", "are chashm",
    "ha", "haa", "hmm ha", "khob", "khoob", "bashe", "basheh", "beshe",
    "doroste", "dorost", "dorooste", "sahih", "ghabole", "ghabul",
    "movafegham", "movafegam", "hale", "halle", "halih","berim","bal","ohom",'uhumm',
    "chashm", "cheshm", "ghorban", "ghorbon", "albate", "hatman", "hatma",
    "hvi", "ys", "آره", "اره", "ار", "ا", "یس", "یه", "بلی", "بله", "هره", "باشه", "بریم", "میام", "اره دارم", "آره دارم", "اوهوم", "اهم", "1", "آ", "آر", "باش", "بل", "بله", "ترو", "درست", "درسته", "صحیح", "صحیحه", "تایید میکنم", "تایید", "بریم"]
continue_prompts = [
    " چیز دیگه ای هم هست عزیزم؟",
    " میخوای بازم ادامه بدیم؟",
    " بریم برای ثبت بعدی؟",
    " میخوای بیشتر بگی؟",
    " چیز دیگه ای هم هست که نگفتی؟",
    " میخوای بازم واسم بگی؟",
    " آماده ای بازم بگی؟",
    " میخوای چیز دیگه ای هم بگی؟",
    " کار دیگه ای هم هست که کردی؟",
    " بازم حرفی داری؟",
    " میخوای بیشتر تعریف کنی؟",
    " ادامه بدیم؟",
    " بازم هست؟",
    " بازم مونده؟",
    " دوست داری بازم بگی؟",
    " امروز بازم کار انجام دادی؟",
    " کار دیگه ای هم کردی امروز؟",
    " کار دیگه هم امروز کردی؟",
    " کار دیگه ای هم انجام دادی؟",
    " ماجرای دیگه ای هم هست؟",
    " بازهم هستی؟",
    " ادامه میدیم؟",
    " بریم برای ادامه؟",
    " میخوای بازهم صحبت کنیم؟"
]
late_back_prompts = [
    ' چه عجب از این ورا!!!',
    ' ببینید کی اینجاست!!',
    ' به به ببین کی اومده!!',
    ' چقدر دیر اومدی دلم تنگ شد!',
    ' بالاخره برگشتی!'
]
welcome_back_prompts = [
    ' خوش برگشتی!',
    ' دلم برات تنگ شده بود!', 
    ' خوحالم که برگشتی!',
    ' ایول. برگشتی!',
    ' خوشحالم دوباره برگشتی!',
    ' اومدی!!!',
    ' برگشتی!!']

early_back_prompts = [
    ' دوباره سلام!',
    ' هه دوباره اومدی!',
    ' خوشحالم که دوباره برگشتی!',
    ' چه زود برگشتی!',
]
vb = [
    ' ... نمیدونم چی بگم. ولی میدونم همه چیز درست میشه...',
    ' ... عیبی نداره اصلا مشکلی نیست منم اصلا ناراحت نشدم :( ...',
    ' ... اوه, عیب نداره خودت خوب میدونی این حال موندگار نیست...',
    ' ... اممم. باشه ولی سخت نگیر مطمئنم همه چیز رو خدا درست میکنه...',
    ' ... اشکالی نداره صبر داشته باش اوکی میشه ... خیلی خوبه که گفتی...',
    ]
b = [
    ' ای بابا. درست میشه مشکلی نیست...',
    ' عیبی نداره اصلا مشکلی نیست منم اصلا ناراحت نشدم :( ...',
    ' اممم. سخت نگیر بابا هیچ خبری نیست...',
    ' هیچی ارزش ناراحتی تو نداره سخت نگیر...',
    ' نگران نباش بابا پس خدا چیکاره ست؟ خودش اوکی میکنه...'
]
g = [
    ' ایول عالیه!!!',
    ' آخ جون منم باهات خوشحال شدم!!',
    ' خیلی عالیه!!',
    ' فوق العاده ست خداروشکر کن!!!',
    ' جدی میگی? این که اوکیی  بی نظیره!!',
    ' ایول این که خوبی معرکه ست!!',
    ' واقعا?? آخجون که خوبی!!'
]
vg = [
    ' پشششمممماممممممم!!!!',
    ' خداروشششککررر!!!!',
    ' ایووللللللللل!!!!',
    ' خداییی?? بی نظیییییییرهه!!',
    ' جدییی??? خیلی خوشحالمممممم!!'
]
n = [
    ' ای بابا, بخند یکم توام... هیچ خبری نیست!',
    ' اههه, ادا در نیار , حالت عالیه دیگه!!',
    ' آها پس خودت خوب میدونی هیچیت نیست مسخره بازی درنیار دیگه!!',
    ' اذیت نکن دیگه . خیلی هم حالت خبه ادا در نیار !!',
    ' خب پس پاشو برو یکم بچرخ نگاه کن چقدر همه چیز قشنگه!!'
]
rd.shuffle(continue_prompts)


def safe_fa_input(inpt=''):
    try:
        inpt = fa_input(inpt)
        return inpt
    except (KeyboardInterrupt, EOFError):
        return ''


def to_late():
    if not data['Date']:
        return None
    today = jdt.datetime.now().date()
    last = jdt.datetime.strptime(data['Date'][-1], "%Y/%m/%d %H:%M").date()
    if today == last:
        return False,False
    return ((today - last).days > 5),True


def count_feelings(grade):
    grade = float(grade)
    if -10 <= grade < -5:
        return 'vb'
    elif -5 <= grade < 0:
        return 'b'
    elif grade == 0:
        return 'n'
    elif 0 < grade < 5:
            return 'g'
    elif 5 <= grade <= 10:
            return 'vg'


def ask(prompt):
    inpt = safe_fa_input(prompt)
    inpt = inpt.strip()
    if inpt.upper() == 'C' or inpt == 'ک' or inpt == 'کنسل' or inpt == 'کنس' or inpt.upper() == 'CANCEL': 
        return None
    return inpt


def intro():
    print('\n c = cancel\n')
    tl = to_late() if file_exist else None
    word = 'امروز'
    if tl is None:
        print(' سلام!!!')
        print(' به جمع ما خوش اومدی!')
    elif tl[0]:
        print(' سلام!!!')
        print(rd.choice(late_back_prompts))
    elif tl[1]:
        word = 'اینبار'
        print(' سلام!')
        print(rd.choice(welcome_back_prompts))
    else:
        word = 'اینبار'
        print(rd.choice(early_back_prompts))
    return word


def get_date_work_grade(word):
    work = ask(f'\n {word} چیکار کردی؟ \n ')
    if work is None:
        return None
    while len(work) < 2:
        print(' یه کم بیشتر توضیح بده ...')
        work = ask(f'\n {word} چیکار کردی؟ \n ')
        if work is None:
            return None
    grade = ask('\nاز 0 تا 10 یعنی حال خوب و 0 تا -10 هم که پایینه!\n اوکی, حالا به حست چه نمره ای میدی؟ ')
    while True:
        if grade is None:
            return None
        try:
            grade = float(grade)
            if -10<= grade <= 10:
                grade = int(grade) if grade.is_integer() else grade
                break
        except ValueError:
            pass
        print(" بی زحمت یه عدد اونم از بین -10 تا 10 انتخاب کن\n نگران نباش! چیزایی که تا الان نوشتی رو نگهشون داشتم . فقط باید یه عدد وارد کنی")
        grade = ask('\n حالا یه نمره به حست بده :  \n ')
    date = jdt.datetime.now().strftime("%Y/%m/%d %H:%M")
    feel = count_feelings(grade)

    if feel == 'vb':
        print(f'\n {grade}{rd.choice(vb)}')
        safe_fa_input('\n هروقت خواستی اینتر کن بریم عزیزم... \n')
    elif feel == 'b':
        print(f'\n {grade},{rd.choice(b)}')
        safe_fa_input('\n هروقت آماده بودی اینتر کن بریم عزیزم... \n')        
    elif feel == 'g':
        print(f'\n {grade}!?{rd.choice(g)}')
        safe_fa_input('\n هروقت خواستی اینتر کن بریم!... \n')
    elif feel == 'vg':
        print(f'\n {grade}!?!!{rd.choice(vg)}')
        safe_fa_input('\n هروقت خواستییی اینتر کننن بریمم!!!!!... \n')
    elif feel == 'n':
        print(f'\n {grade}{rd.choice(n)}')
        safe_fa_input('\n ابنتر کن بریم ادامه عزیزم!! ولی قبلش اول یکم بخند (: ... \n')
    else:
        safe_fa_input('\n چی شد؟ نفهمیدم ولی اینتر کن بریم... \n')
    
    return date, work, grade+10


def new_data(now, work, grade):
    data['Date'].append(now)
    data['Work'].append(work)
    data['Grade'].append(grade)


def run():
    n=0
    nwg = get_date_work_grade(intro())
    while True:
        if nwg is not None:
            new_data(*nwg)
        prmpt = continue_prompts[n]
        nxt = safe_fa_input(f'{prmpt} ')
        if nxt.lower() not in yeses and nxt:
            break
        n+=1
        if n == len(continue_prompts) :
            n=0
        nwg = get_date_work_grade('خب, بگو')


def save():
    pd.DataFrame(data).to_csv('my_did.csv' ,encoding='utf-8-sig', index=False)


def main():
    global data
    global file_exist
    try:
        data = pd.read_csv('my_did.csv', encoding='utf-8-sig').to_dict('list')
        file_exist = True

    except (FileNotFoundError, pd.errors.EmptyDataError):
        file_exist = False
        data = {
            'Date':[],
            'Work':[],
            'Grade':[]
        }

    run()
    save()
    return file_exist
    


def feelings_plot():
    if not data['Date']:
        print('\nهنوز داده ای ثبت نشده مشتی ... وگرنه برات نمودار میاوردم.\n')
        return
    x, y = data['Date'], data['Grade']
    plt.plot(x, y, label='feelings')
    plt.axhline(y=10, ls='--', color='red', label='مرز')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    safe_fa_input()
    plt.bar(x, y)
    plt.axhline(y=10, ls='--', color='red', label='مرز')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
    feelings_plot()
    