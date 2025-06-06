const knownProducts = [
  {
    name: "Pearl Millets",
    synonyms: [
      "pearl millets", "bajra", "sajja", "सज्जा", "बाजरा", "పెర్ల్ మిల్లెట్స్", "సజ్జ",
      "perl millets", "pearl millet", "sajje", "sajji", "sajji ginjalu", "bajre", "bajara"
    ]
  },
  {
    name: "Red Dhal",
    synonyms: [
      "red dhal", "lal dal", "ఎర్ర పప్పు", "लाल दाल", "red dal", "errapappu", "erra pappu", "lal daal", "red lentil", "masoor dal", "masur dal"
    ]
  },
  {
    name: "Pesara",
    synonyms: [
      "pesara", "moong", "పెసర", "मूंग दाल", "moong dal", "mung dal", "pesarappu", "pesara pappu", "mung", "moog", "pesaru"
    ]
  },
  {
    name: "Little Foxtail",
    synonyms: [
      "little foxtail", "samalu", "సామలు", "छोटा कोदो", "little millet", "samai", "samalu ginjalu", "little fox tail", "samalu pindi"
    ]
  },
  {
    name: "Kudo",
    synonyms: [
      "kudo", "arikelu", "अरिका", "అరికెలు", "kodo millet", "arika", "kodon", "kodon millet"
    ]
  },
  {
    name: "Foxtail Millets",
    synonyms: [
      "foxtail millets", "korralu", "कोर्रलु", "కొర్రలు", "foxtail millet", "korra", "korra ginjalu", "korralu pindi", "kangni"
    ]
  },
  {
    name: "Chana Dhal",
    synonyms: [
      "chana dhal", "sanagapappu", "चना दाल", "శనగ పప్పు", "chana dal", "sanaga pappu", "bengal gram", "chanadal", "chana", "chanadal", "sanaga"
    ]
  },
  {
    name: "Browntop",
    synonyms: [
      "browntop", "andukorralu", "అందుకొర్రలు", "ब्राउनटॉप", "browntop millet", "andukorra", "brown top", "brown top millet"
    ]
  },
  {
    name: "Bay of Bengal Sanaga",
    synonyms: [
      "bay of bengal sanaga", "bay sanaga", "బే సనగ", "बे संगा", "bay sanaga pappu", "bay sanagapappu", "bay sanaga dal"
    ]
  },
  {
    name: "Barnyard",
    synonyms: [
      "barnyard", "udalu", "ఉడలు", "बारनयार्ड", "barnyard millet", "udalu ginjalu", "sawa", "sawa millet", "jhangora"
    ]
  },
  {
    name: "Basmati",
    synonyms: [
      "basmati", "బాస్మతి", "बासमती", "basmati rice", "basmathi", "basamati", "basumathi", "basumati"
    ]
  },
  {
    name: "Brown Rice",
    synonyms: [
      "brown rice", "బ్రౌన్ రైస్", "ब्राउन राइस", "brownrice", "brown rise", "brown ric", "pacha biyyam"
    ]
  },
  {
    name: "Rice",
    synonyms: [
      "rice", "annam", "चावल", "అన్నం", "arisi", "biyyam", "chaaval", "chawal", "rize", "raice"
    ]
  },
  {
    name: "Raw Rice",
    synonyms: [
      "raw rice", "vadlu", "వద్లు", "कच्चा चावल", "rawrice", "kacha chawal", "raw rize", "raw rise", "vadlu biyyam"
    ]
  },
  {
    name: "Beets",
    synonyms: [
      "beets", "beetroot", "బీట్‌రూట్", "चुकंदर", "beet", "beetroots", "chukandar", "beet rot", "beet root"
    ]
  },
  {
    name: "Brinjal",
    synonyms: [
      "brinjal", "vankaya", "వంకాయ", "बैंगन", "eggplant", "baingan", "vangaya", "vangai", "brinjal eggplant"
    ]
  },
  {
    name: "Gutti Vankaya",
    synonyms: [
      "gutti vankaya", "stuffed brinjal", "గుత్తివంకాయ", "भरवां बैंगन", "guthi vankaya", "stuffed eggplant", "guttivankaya"
    ]
  },
  {
    name: "Carrot",
    synonyms: [
      "carrot", "కారెట్", "गाजर", "gajar", "carrots", "keret", "carot", "kerret"
    ]
  },
  {
    name: "Dondakaya",
    synonyms: [
      "dondakaya", "tindora", "దొండకాయ", "कुंदरू", "ivy gourd", "kundru", "dondakai", "donkaya", "kovakka"
    ]
  },
  {
    name: "Gongura",
    synonyms: [
      "gongura", "गोंगुरा", "గోంగూరా", "sorrel", "gongura leaves", "gongura aaku", "gonguraa", "gongura leaf", "pitwaa"
    ]
  },
  {
    name: "Green Chilly",
    synonyms: [
      "green chilly", "green chili", "pachi mirchi", "పచ్చి మిర్చి", "पचि मिर्ची", "हरी मिर्च", "mirchi", "green mirchi", "hari mirch", "pachimirchi", "chili", "chilly", "mirch"
    ]
  },
  {
    name: "Kakarikaya",
    synonyms: [
      "kakarikaya", "bitter gourd", "కాకరకాయ", "करेला", "karela", "kakarakai", "bitterguard", "pavakkai"
    ]
  },
  {
    name: "Kothimira",
    synonyms: [
      "kothimira", "dhaniya", "ధనియాల", "धनिया", "coriander", "coriander leaves", "cilantro", "kothmir", "kotmir", "kotthamalli", "kottimeera", "kotimeera", "dhaniya patta"
    ]
  },
  {
    name: "Lady Finger",
    synonyms: [
      "lady finger", "bendakaya", "బెండకాయ", "भिंडी", "okra", "bendi", "bhindi", "bendakai", "bendakayi", "ladies finger", "ladyfinger"
    ]
  },
  {
    name: "Onion",
    synonyms: [
      "onion", "ullipaya", "ఉల్లిపాయ", "प्याज", "pyaz", "ulli", "ulipaya", "oniyan", "onyan", "oniyin", "oniun", "oniion", "oniyin", "kanda", "erulli"
    ]
  },
  {
    name: "Potato",
    synonyms: [
      "potato", "bangaladumpa", "బంగాళాదుంప", "आलू", "aloo", "alu", "batata", "potatoe", "patato", "poteto"
    ]
  },
  {
    name: "Tomato",
    synonyms: [
      "tomato", "tamata", "టమాట", "टमाटर", "tamato", "tommato", "tommoto", "tameto", "thakkali", "takali", "tomatto"
    ]
  }
];