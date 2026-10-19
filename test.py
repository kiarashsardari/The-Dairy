
import jdatetime as jdt
import pandas as pd
import random as rd

yeses = [
    "y", "yes", "yeah", "yea", "yeh", "yah", "yuh", "yep", "yip", "yup", "yupp","a","ar",
    "yas", "yass", "yasss", "yess", "yesss", "yeass", "yeahhh", "yessir", "yes sir",
    "yes ma'am", "yes please", "ya", "aye", "ay", "aye aye", "affirmative",
    "ok", "okay", "okey", "okey dokey", "okie", "okie dokie", "okei", "oki",
    "k", "kk", "sure", "sure thing", "for sure", "of course", "certainly",
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
    "hvi", "ys"]
continue_prompts = [
    " Chize dige ie ham anjam dadi, azizam?",
    " Baz ham kari kardi?",
    " Mikhay bazam edame bedim?",
    " Berim baadi?",
    " Mikhay bishtar begi?",
    " Kare dige ie ham kardi ke hanooz nagofti?",
    " Mikhay bishtar begi vasaam?",
    " Amade ie bazam begi?",
    " Mikhay chize dige ie ham begi?",
    " Kar dige ie ham kardi?",
    " Dobare harfi dari, azizam?",
    " Mikhay chiz bishtari ezafe konim?",
    " Edame midim?",
    " Baz ham hast?",
    " Baz ham monde?",
    " Doost dari bazam begi?",
    " Emrooz kar dige ie ham kardi?",
    " Kare dige ie ham kardi?",
    " Kare dige ie ham emrooz kardi?",
    " Kare dige ie ham anjam dadi?",
    " Majara ye dige ie ham hast?",
    " Bazham hast?",
    " Edame bedim?",
    " Berim baraye baadi?",
    " Mikhay baz ham sohbat koni?"
]
late_back_prompts = [
    ' Che ajab az invara!!!',
    ' Bebinid ki injast!!',
    ' Bahbah bebin ki umadeh!!',
    ' Cheghadr dir kardi delam tang shod!',
    ' Balakhareh bargashti!'
]
welcome_back_prompts = [
    ' Khosh bargashti!',
    ' Delam barat tang shodeh bood!', 
    ' Khoshhalam ke bargashti!',
    ' Eival, oomadi!',
    ' Khoshhalam dobareh oomadi!',
    ' Umadi!!!',
    ' Bargashti!!']

early_back_prompts = [
    ' Doobareh!',
    ' Akhjoon dobareh oomadi!',
    ' Khoshhalam ke zood bargashti!',
    ' Che zood bargashti!',
    ' Baz chi avordi?',
    ' Bego bebinam dige chi dari?'
]
vb = [
    ' ... Nemidoonam chi begam. vali negaran nabash hame chiz ok misheh...',
    ' ... Eybi nadareh. asla moshkeli nist...',
    ' ... Oh, negaran nabash khodet ham midooni in haal mondegar nist...',
    ' ... Amm.. bashe vali sakht nagir motmaen am dorost mishe...',
    ' ... Eshkali nadareh hame chiz dorost mishe ... kheyli khoobe ke gofti...',
    ]
b = [
    ' Ey baba, dorost mishe moshkeli nist...',
    ' Amm, sakht nagir baba hich khabari nist...',
    ' Hichi arzash nadareh ke bekhai baash narahat bashi eiyb nadare...',
    ' Negaran nabash baba pas khoda chikare hast? khodesh komak mikoneh...'
]
g = [
    ' Eiyval aliyehh!!!',
    ' Akhjoon manam bahat khoshhal shodam!!',
    ' Kheyli aliye!!',
    ' Fogholade ast!!!',
    ' Jedi migi? binazire!!',
    ' Eiyval in maarekast!!',
    ' Vaghaan?? akhjoooon!!'
]
vg = [
    ' Pashmmaaammmmmmmmmm!!!!',
    ' Khoddaa ro shokrrr!!!!',
    ' Akhjoooooooon!!!!',
    ' Vaghaan?? Binaziiirehhhhhhhhhh!!',
    ' Jediiiii??? kheily khoshhalaamm!!'
]
n = [
    ' Ey baba, bekhand ekam to ham... hich khabari nist!',
    ' eeeeh, ada dar naiar dige, halet aliye digeh!!',
    ' Aha pas hich khabari nisto halet okeyeh!!',
    ' Aziat nakon digeh, kheily ham khoobi fghat khodet nemidooni!!',
    ' Eh, negah kon ta alan in hame kar kardi be khodet negah kon, halet aliye!!',
    ' Khob pas pasho boro yekam becharkh negah kon chegadr hame chiz ghashangeh!!'
]
rd.shuffle(continue_prompts)


def safe_input(inpt):
    try:
        inpt = input(inpt)
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
    inpt = safe_input(prompt)
    inpt = inpt.strip()
    if inpt.upper() == 'C':
        return None
    return inpt


def intro():
    print('\n c = cancel\n')
    tl = to_late() if file_exist else None
    word = 'Emrooz'
    if tl is None:
        print(' Salaam!!!')
        print(' Khosh umadi pishe ma!')
    elif tl[0]:
        print(' Salaam!!!')
        print(rd.choice(late_back_prompts))
    elif tl[1]:
        word = 'Inbar'
        print(' Salaam!!!')
        print(rd.choice(welcome_back_prompts))
    else:
        word = 'Inbar'
        print(rd.choice(early_back_prompts))
    return word


def get_date_work_grade(word):
    work = ask(f'\n {word} chikar kardi? \n ')
    if work is None:
        return None
    while len(work) < 2:
        print(' Bizahmat yekam bishtar sohbat kon, bebakhshid dast man nist raais gofte...')
        work = ask(f'\n {word} chikar kardi? \n ')
        if work is None:
            return None
    

    grade = ask('\nAz 0 ta 10 yaani hale khoob & vali mishe -10 ta 0 ham vared kard!\n OK, hala be heset che nomrei midi?! ')
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
        print(" Bizahmat ye adad, oon ham az -10 ta 10 entekhab kon\n Negaran nabash, chizayee ke alan neveshti ro negah midaram. faghat ye adadi bego!")
        grade = ask('\n Hala ye nomrei be heset bede (az -10 ta 10): \n ')
    date = jdt.datetime.now().strftime("%Y/%m/%d %H:%M")
    feel = count_feelings(grade)

    if feel == 'vb':
        print(f' {grade}{rd.choice(vb)}')
        safe_input('\n harvaght amade boodi enter kon berim, aziz delam... \n')
    elif feel == 'b':
        print(f' {grade},{rd.choice(b)}')
        safe_input('\n harvaght khasti, enter kon berim azizam... \n')
    elif feel == 'g':
        print(f' {grade}!?{rd.choice(g)}')
        safe_input('\n man haminjaamm, harvaght khasti enter kon beriimm!!!!!... \n')
    elif feel == 'vg':
        print(f' {grade}!?!!{rd.choice(vg)}')
        safe_input('\n man haminjaamm,, harvaght khasti enter kon beriimm!!!!!... \n')
    elif feel == 'n':
        print(f'{grade}{rd.choice(n)}')
        safe_input('\n enter ro bezan berim edameh azizam!! vali ghblesh yekam bekhand aval... \n')
    else:
        safe_input('\n chi shod? nfahmidam... vali harvaght amade boodi enter ro bezan ...\n')
    
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
        nxt = safe_input(f'{prmpt} ')
        if nxt.lower() not in yeses and nxt:
            break
        n+=1
        if n == len(continue_prompts) :
            n=0
        nwg = get_date_work_grade('khob, bego')


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


if __name__ == '__main__':
    main()