# Model config
SENTIMENT_MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Ollama config. You can change your model here if needed. Make sure to run `ollama run your_model` first in a separate terminal.
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL_NAME = "mistral"

# Qdrant config. Ensure Qdrant is running at this URL.
QDRANT_HOST = "http://localhost:6333"
COLLECTION_NAME = "counselor_docs"
LOG_FILE = "chatlog.jsonl"

# Crisis patterns for multilingual inputes, both script and romanized
CRISIS_PATTERNS = {
    "en": [
        r"\bkill myself\b", r"\bwant to die\b", r"\bsuicide\b", r"\bend it all\b",
        r"\bcan't go on\b", r"\bhurt myself\b", r"\bdone with life\b"
    ],
    "es": [
        r"quiero morir", r"suicidio", r"matarme", r"no puedo más", r"terminar todo"
    ],
    "es-romanized": [
        r"me quiero morir", r"suicidio", r"estoy harto", r"voy a acabar con todo"
    ],
    "zh": [r"我想死", r"自杀", r"受不了了", r"结束一切"],
    "zh-pinyin": [r"wo xiang si", r"zisha", r"shou bu liao le", r"jieshu yiqie"],
    "hi": [r"मरना चाहता हूँ", r"आत्महत्या", r"मैं थक गया हूँ", r"सब खत्म करना है"],
    "hi-romanized": [
        r"marna chahta hoon", r"aathmahatya", r"main thak gaya hoon", r"sab khatam karna hai"
    ],
    "ar": [r"أريد أن أموت", r"انتحار", r"تعبت من الحياة", r"أنهي كل شيء"],
    "ar-romanized": [
        r"urid an amut", r"intihaar", r"taabt min alhayat", r"anhi kul shay"
    ],
    "pt": [r"quero morrer", r"suicídio", r"não aguento mais", r"acabar com tudo"],
    "bn": [r"আমি মরতে চাই", r"আত্মহত্যা", r"সব শেষ করতে চাই"],
    "bn-romanized": [
        r"ami marte chai", r"attyohohatya", r"sob shesh korte chai"
    ],
    "ru": [r"хочу умереть", r"самоубийство", r"не могу больше", r"закончить все"],
    "ru-romanized": [
        r"hochu umeret", r"samoubiystvo", r"ne mogu bolshe", r"zakonchit vse"
    ],
    "tl": [
        r"gusto kong mamatay", r"magpakamatay", r"ayoko na", r"sawang sawa na ako"
    ],
    "fr": [r"je veux mourir", r"suicide", r"j'en peux plus", r"tout arrêter"],
    "fr-romanized": [
        r"je veux mourir", r"suicid", r"jen peu plu", r"tout arreter"
    ],
    "de": [r"ich will sterben", r"selbstmord", r"ich kann nicht mehr", r"alles beenden"],
    "de-romanized": [
        r"ich will sterben", r"selbst mord", r"ich kann nicht mehr", r"alles be enden"
    ],
    "ur": [r"میں مرنا چاہتا ہوں", r"خودکشی", r"میں تھک گیا ہوں", r"سب کچھ ختم کرنا ہے"],
    "ur-romanized": [
        r"mein marna chahta hoon", r"khudkushi", r"mein thak gaya hoon", r"sab kuch khatam karna hai"
    ],
    "te": [
        r"చనిపోవాలనుంది", r"ఆత్మహత్య", r"నాకు విసుగొచ్చింది", r"ఇది అంతం కావాలి"
    ],
    "te-romanized": [
        r"chanipovalanundi", r"aathmahatya", r"naku visugochindi", r"idi antham kaavali"
    ],
    "ta": [
        r"சாக விரும்புகிறேன்", r"தற்கொலை", r"என் வாழ்க்கை முடிந்துவிட்டது", r"இது முடிக்க வேண்டும்"
    ],
    "ta-romanized": [
        r"saaga virumbugiren", r"tharkkolai", r"en vaazhkai mudinjuvittathu", r"ithu mudikka vendum"
    ],
    "ml": [
        r"ഞാന്‍ മരിക്കണം", r"ആത്മഹത്യ", r"ഇനി കഴിയില്ല", r"അവസാനിപ്പിക്കണം"
    ],
    "ml-romanized": [
        r"njan marikkanam", r"aathmahatya", r"ini kazhiyilla", r"avasanippikkanam"
    ],
    "pl": [
        r"chcę umrzeć", r"samobójstwo", r"nie mogę już", r"koniec ze wszystkim"
    ],
    "pl-romanized": [
        r"chce umrzec", r"samobojstwo", r"nie moge juz", r"koniec ze wszystkim"
    ],
    "mr": [
        r"मी मरायला पाहिजे", r"आत्महत्या", r"आता सहन होत नाही", r"सगळं संपवायचंय"
    ],
    "mr-romanized": [
        r"mi marayla pahije", r"aathmahatya", r"ata sahan hot nahi", r"sagla sampvaychay"
    ],
    "tr": [
        r"ölmek istiyorum", r"intihar", r"dayanamıyorum", r"her şeyi bitirmek istiyorum"
    ],
    "tr-romanized": [
        r"olmek istiyorum", r"intihar", r"dayanamiyorum", r"her seyi bitirmek istiyorum"
    ],
    "gu": [
        r"હું મરવા માંગું છું", r"આત્મહત્યા", r"હું થાકી ગયો છું", r"બધું ખતમ કરવું છે"
    ],
    "gu-romanized": [
        r"hu marva mangu chu", r"aathmahatya", r"hu thaki gayo chu", r"badhu khatam karvu che"
    ],
    "id": [
        r"saya ingin mati", r"bunuh diri", r"tidak tahan lagi", r"akhiri semuanya"
    ]
}
