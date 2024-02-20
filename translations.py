english_to_genz = {

    'win': 'w',
    'loss': 'l',

    'politically': 'woke',
    'political': 'woke',

    'makeup':'glowup',
    'makeover': 'glowup',
    'improved': 'glowup',
    'improvement': 'glowup',

    'guys': 'chat',
    'suspicious':'sus',

    'fan':'stan',
    'supporter':'stan',

    'friend': 'bro',
    'sister': 'bro',
    'brother': 'bro',
    'friends': 'bros',
    'sisters': 'bros',
    'brothers': 'bros',
    'group': 'squad',
    'team': 'squad',
    
    'lying': 'capping',
    'lie': 'cap',
    'liar': 'capper',
    'crazy': 'wild',
    
    'better': 'hits different',
    'great': 'hits different',
    'greater': 'hits diffrent',
    'good': 'slaps',
    'delicious': 'bussin',
    'tasty': 'bussin',
    'new': 'fresh',

    'thing': 'shit',
    'things': 'shit',
    'stuff': 'shit',
    'hell': 'ohio',

    'perform': 'slay',
    'do': 'slay',
    'doing':'slaying', 
    'gaving off': 'giving',

    'confident': 'sigma',
    'brave': 'sigma',
    'courageous': 'sigma',
    'attractive': 'sigma',
    'masculine': 'chad',
    'muscular': 'chad',
    'strong': 'chad',
    'fighter':'chad',
    'manly':'chad',

    'goal': 'assignment',
    'money': 'guap',
    'wealth': 'guap',
    'wealthy': 'guapy',
    'rich': 'guapy',

    '5': 'mid',
    'mediocre':'mid',
    'ugly':'mid',
    'so-so':'mid',
    'soso': 'mid',

    'ruined': 'butchered',
    'ruin': 'butcher',
    'kill': 'knock',
    'killed': 'knocked',
    'insult': 'roast',
    'burned': 'roasted',
    'burnt': 'roasted',


    'surprised':'shook',
    'amazed': 'shook',

    'nope': 'nah',
    'not': 'naur',
    
    'yes': 'yas',
    'my': 'ma',
    'hey': 'yo',
    'about': 'bout',
    'letting': 'lettin',
    'create': 'cook',
    'make': 'cook',
    'creating':'cooking',
    'making': 'cooking',
    'made': 'cooked',
    'created': 'cooked',
    # 'do': 'cook',
    # 'doing': 'cooking',


    'genius': 'big brain',
    'intelligent': 'big brain',
    'stupid': 'goofy',
    'weirdo':'NPC',
    'weird':'NPC',


    'confuse':'gaslight',
    'confusing': 'gaslighting',
    'manipulate': 'gaslight',
    'manipulating': 'gaslighting',

    'sex': 'hook up',
    'slept': 'hooked up',
    'romance': 'hook up',
    'kiss': 'hook-up',
    'secretly': 'lowkey',
    'husband': 'zaddy',
    'boyfriend': 'daddy',
    'wife': 'mommy',
    'girlfriend': 'mommy',
    
    'ass': 'gyatt',
    'butt': 'gyatt',
    'bootie': 'gyatt',
    "booty": 'gyatt',


    'romantic': 'rizzler',
    'charismatic': 'rizzler',
    'charisma': 'rizz',
    
}

# genz_to_english= {v: k for k, v in english_to_genz.items()}

# def invertDictionary(d):
#     myDict = {}
#     for i in d:
#         value = d.get(i)
#         english_to_genz.setdefault(value,[]).append(i)   
#     return english_to_genz

# basically the above code but its faster i think

genz_to_english=  {value: [key for key, val in english_to_genz.items() if val == value] for value in english_to_genz.values()}
