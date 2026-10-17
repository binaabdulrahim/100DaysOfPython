"""Jokes and riddles written for each kind of product, so the bubble matches
what's on screen (a perfume gets perfume jokes, a mascara gets mascara riddles).

Each entry is (setup/question, punchline/answer). If a type runs out, the
product falls back to its category ("makeup", "skincare", "hair"), then to the
general lists in jokes.py.
"""

THEMED = {
    # ---------- fragrance ----------
    "fragrance": {
        "jokes": [
            ("Why does perfume get invited to every party?", "It always makes a great first impression."),
            ("What did the perfume say on its first date?", "I hope I leave a lasting impression."),
            ("Why did the perfume get so many compliments?", "It was simply irresistible."),
            ("What's a perfume's favourite kind of music?", "Anything with good notes."),
            ("Why did the perfume bottle go back to school?", "To work on its top notes."),
            ("Why is perfume so good at keeping secrets?", "It never makes a scene, just a scent."),
            ("How do perfumes find their way home?", "They follow their nose."),
        ],
        "riddles": [
            ("What do you smell but never see, and wear but never touch?", "Perfume."),
            ("I have top notes, heart notes and base notes, but I'm not a song. What am I?", "A perfume."),
            ("I'm a cloud you can wear, and you spray me on your wrist. What am I?", "A fragrance."),
            ("You can't see me, but people remember me after you've left the room. What am I?", "Your perfume."),
            ("I'm dabbed on wrists and behind ears. What am I?", "Perfume."),
            ("I live in a glass bottle on your dresser and follow you all day. What am I?", "Your signature scent."),
            ("One spritz of me and you smell like a holiday. What am I?", "A fragrance."),
        ],
    },
    # ---------- nails ----------
    "nails": {
        "jokes": [
            ("Why did the nail polish get promoted?", "It always nailed it."),
            ("Why did the manicure need a day off?", "It had too many chips on its shoulder."),
            ("What's a nail polish's favourite dance?", "The top coat shuffle."),
            ("Why do nail polishes make great friends?", "They always stick with you."),
            ("What did the nail file say to the nail?", "Let's smooth things over."),
            ("Why did the nail polish win the award?", "It really knew how to make a statement."),
        ],
        "riddles": [
            ("I come in a bottle, I'm painted on, and I dry on your fingertips. What am I?", "Nail polish."),
            ("I have a brush in my cap but I never touch hair. What am I?", "Nail polish."),
            ("I'm ten little canvases that get painted every week. What am I?", "Your nails."),
            ("Blow on me, wave me around, but don't touch me for ten minutes. What am I?", "Wet nail polish."),
            ("I make chips disappear, but I'm not hungry. What am I?", "A fresh manicure."),
            ("I'm a tiny bottle with a big colour inside. Where do I end up?", "On your nails."),
        ],
    },
    "top_coat": {
        "jokes": [("Why was the top coat so confident?", "It knew how to seal the deal.")],
        "riddles": [("I'm the last coat on, and I keep your colour shiny. What am I?", "A top coat.")],
    },
    # ---------- makeup ----------
    "mascara": {
        "jokes": [
            ("Why did the mascara break up with the eyeliner?", "It wanted more volume in its life."),
            ("Why did the eyelashes go to the gym?", "To build some volume."),
            ("What did one eyelash say to the other?", "Stick together, mascara's coming."),
            ("Why was the mascara so dramatic?", "It just loved making a long story longer."),
        ],
        "riddles": [
            ("I have a brush but no hair of my own, and I make lashes look long. What am I?", "Mascara."),
            ("I'm a wand, but I don't do magic tricks. I just make lashes longer. What am I?", "Mascara."),
            ("I add length and volume, but I'm not a novel. What am I?", "Mascara."),
            ("You swipe me upward and your eyes look wide awake. What am I?", "Mascara."),
        ],
    },
    "brow": {
        "jokes": [
            ("What's a brow's favourite exercise?", "Raises."),
            ("Why are brows so good at debates?", "They always raise good points."),
        ],
        "riddles": [
            ("I sit above your eyes and say everything without a word. What am I?", "Your eyebrows."),
            ("I'm brushed up every morning, but I'm not a toothbrush. What am I?", "Your brows."),
        ],
    },
    "lips": {
        "jokes": [
            ("Why are lips so good at keeping secrets?", "They're always sealed."),
            ("What did the lip product say to dry lips?", "Don't worry, I've got you covered."),
            ("Why do lip products get so many compliments?", "They always know how to make a pout."),
            ("Why did the lips go on holiday?", "They needed some time to gloss over things."),
            ("Why are lips always so polite?", "They never forget to say please and thank you."),
        ],
        "riddles": [
            ("I'm swiped on in seconds and make your smile pop. Where do I go?", "On your lips."),
            ("I'm a little colour and a lot of comfort for your pout. What am I?", "A lip product."),
            ("I keep your lips soft and give them a hint of colour. What am I?", "A tinted lip product."),
            ("I live in your bag and come out every time your lips feel dry. What am I?", "Your lip favourite."),
            ("What gets kissed every day but never complains?", "Your lips."),
        ],
    },
    "lipstick": {
        "jokes": [
            ("Why did the lipstick break up with the mirror?", "It needed space to reflect."),
            ("Why don't lipsticks ever get lost?", "They always know where to make their mark."),
        ],
        "riddles": [
            ("I have a cap but no head, I come in many shades, and I love a kiss. What am I?", "Lipstick!"),
            ("I leave my mark on coffee cups. What am I?", "Lipstick."),
        ],
    },
    "blush": {
        "jokes": [
            ("Why did the blush go to the party?", "To get a little cheeky."),
            ("What did the blush say to the cheek?", "You make me feel all rosy."),
            ("Why is blush so easy to talk to?", "It always brings out your best side."),
        ],
        "riddles": [
            ("I make you look like you just came in from the cold, without the cold. What am I?", "Blush."),
            ("A few taps of me and your cheeks look rosy. What am I?", "Blush."),
            ("I'm the pink in your cheeks that didn't come from embarrassment. What am I?", "Blush."),
        ],
    },
    "bronzer": {
        "jokes": [
            ("Why did the bronzer get invited to the beach?", "It brought the warmth."),
            ("Why is bronzer always so relaxed?", "It's on a permanent holiday."),
        ],
        "riddles": [
            ("I give you a sun-kissed look with no sun at all. What am I?", "Bronzer."),
            ("I'm a summer tan that comes in a compact. What am I?", "Bronzer."),
        ],
    },
    "highlighter": {
        "jokes": [
            ("Why did the highlighter win the talent show?", "It really knew how to shine."),
            ("Why is a luminizer always so cheerful?", "It looks on the bright side."),
        ],
        "riddles": [
            ("Tap me on your cheekbones and I catch the light. What am I?", "Highlighter."),
            ("I'm a little glow you can carry in your bag. What am I?", "A highlighter."),
        ],
    },
    "concealer": {
        "jokes": [
            ("What did the concealer say at the meeting?", "Let's cover the basics."),
            ("Why is concealer such a good friend?", "It always covers for you."),
        ],
        "riddles": [
            ("I hide spots and dark circles, but I'm not a magician. What am I?", "Concealer."),
            ("I'm dabbed under your eyes after a late night. What am I?", "Concealer."),
        ],
    },
    "foundation": {
        "jokes": [
            ("Why did the foundation stay calm in an argument?", "It knew how to keep things even."),
            ("Why did the skin tint never worry?", "It knew everything would even out."),
            ("Why is foundation so dependable?", "It's the base of every good look."),
        ],
        "riddles": [
            ("I'm the canvas before the masterpiece. What am I?", "Foundation."),
            ("I even everything out, but I'm not a referee. What am I?", "Foundation."),
            ("I make skin look like skin, only smoother. What am I?", "Your base."),
        ],
    },
    "powder": {
        "jokes": [
            ("What did the powder say to the shine?", "You've been set."),
            ("Why is powder so calm?", "It knows how to keep things matte-r of fact."),
        ],
        "riddles": [
            ("I fight shine without saying a word. What am I?", "Powder."),
            ("I'm soft, I'm loose and I come with a puff. What am I?", "Powder."),
        ],
    },
    "setting_spray": {
        "jokes": [
            ("Why did the setting spray never panic?", "It always kept everything in place."),
            ("Why did the makeup stay for the whole party?", "Its setting spray was perfect."),
        ],
        "riddles": [
            ("Mist me over your makeup and it stays put all day. What am I?", "Setting spray."),
            ("I'm the last step that keeps the rest in place. What am I?", "Setting spray."),
        ],
    },
    "makeup": {
        "jokes": [
            ("Why did the makeup bag go to therapy?", "It was carrying too much."),
            ("Why was the makeup sponge so relaxed?", "It just soaked everything in."),
            ("Why did the eyeshadow palette go to school?", "To brush up on its colours."),
        ],
        "riddles": [
            ("I come in a bag, I live on your face, and I wash off at night. What am I?", "Makeup."),
            ("I have many brushes but never paint a wall. What am I?", "A makeup kit."),
        ],
    },
    # ---------- skincare ----------
    "sunscreen": {
        "jokes": [
            ("What did the sunscreen say to the sun?", "Not today."),
            ("Why is sunscreen such a good friend?", "It always has your back, and your face."),
        ],
        "riddles": [
            ("I protect you every day, but you can't see me once I'm on. What am I?", "Sunscreen."),
            ("I have a number on my label and the sun is scared of it. What am I?", "SPF."),
        ],
    },
    "patch": {
        "jokes": [
            ("Why did the pimple patch get a medal?", "It always covered for its friends."),
            ("Why do pimple patches work the night shift?", "They do their best work while you sleep."),
        ],
        "riddles": [
            ("You dot me on spots overnight and peel me off in the morning. What am I?", "A pimple patch."),
            ("I'm a tiny sticker that takes care of big problems. What am I?", "A pimple patch."),
        ],
    },
    "cleanser": {
        "jokes": [
            ("What did the cleanser say to the dirt?", "It's not you, it's me. Actually, it's you."),
            ("Why did the cleansing balm melt?", "It saw the makeup and couldn't resist."),
            ("Why is cleanser so good at goodbyes?", "It takes everything off your face."),
        ],
        "riddles": [
            ("I melt the day off your face. What am I?", "A cleanser."),
            ("I take your makeup off without any scrubbing. What am I?", "A cleanser."),
            ("I'm the first step of every routine. What am I?", "Cleansing."),
        ],
    },
    "toner": {
        "jokes": [
            ("Why did the toner quit its job?", "It wanted a fresh start."),
            ("What did the toner say to the pores?", "Let's tighten things up."),
            ("Why is toner so refreshing to be around?", "It always resets the mood."),
        ],
        "riddles": [
            ("I come after cleansing and get your skin ready for the rest. What am I?", "Toner."),
            ("I look like water, but your skin knows I'm more. What am I?", "Toner."),
            ("Pat me in with your hands or a cotton pad. What am I?", "Toner."),
        ],
    },
    "serum": {
        "jokes": [
            ("What did the serum say to the wrinkle?", "Smooth move."),
            ("Why did the serum go to school?", "To become more concentrated."),
            ("Why are serums so good at advice?", "They get straight to the point, a few drops at a time."),
            ("Why did the serum get the lead role?", "It had real star quality in every drop."),
        ],
        "riddles": [
            ("I come with a dropper, and a few drops of me go a long way. What am I?", "A serum."),
            ("I'm small, mighty and go on before your moisturiser. What am I?", "Serum."),
            ("I'm sold by the drop, but I'm worth my weight in glow. What am I?", "A serum."),
            ("I'm thinner than cream and stronger than water. What am I?", "A serum."),
        ],
    },
    "moisturizer": {
        "jokes": [
            ("Why did the moisturizer go to therapy?", "It had too many dry spells."),
            ("What did the moisturizer say to dry skin?", "Drink up, it's on me."),
            ("Why do moisturizers make great friends?", "They're always there when things get rough."),
            ("What's a moisturizer's favourite weather?", "A little dewy."),
            ("Why did the face cream get a standing ovation?", "It left everyone feeling smooth."),
            ("Why is cream so popular?", "It always makes people feel soft."),
        ],
        "riddles": [
            ("I make thirsty skin happy, morning and night. What am I?", "Moisturiser."),
            ("I'm smoothed on morning and night, and I lock the water in. What am I?", "A moisturiser."),
            ("Your skin drinks me, but I'm not water. What am I?", "Face cream."),
            ("I'm soft, I'm rich and I sit on your bathroom shelf. What am I?", "A cream."),
            ("I turn tight, dry skin into soft, comfy skin. What am I?", "Moisturiser."),
            ("I'm the last step before bed and the first step of a good morning. What am I?", "Moisturiser."),
        ],
    },
    "skincare": {
        "jokes": [
            ("Why was the face mask so relaxed?", "It knew how to unwind for 15 minutes."),
            ("What do you call a dinosaur with great skin?", "A glow-saurus."),
        ],
        "riddles": [
            ("What do you wash, tone and moisturise every single day?", "Your face!"),
            ("I'm a routine, but I'm not a workout. What am I?", "Skincare."),
        ],
    },
    # ---------- hair ----------
    "shampoo": {
        "jokes": [
            ("Why was the shampoo so calm?", "It knew how to lather, rinse, repeat."),
            ("Why was the shampoo bottle so wise?", "It had been through a lot of heads."),
            ("Why did the shampoo get a promotion?", "It always came out on top."),
            ("Why don't shampoos ever hold a grudge?", "They wash it all away."),
        ],
        "riddles": [
            ("I get bubbly every time I get wet. What am I?", "Shampoo."),
            ("Lather, rinse, repeat: that's my whole job. What am I?", "Shampoo."),
            ("I'm the first step of wash day. What am I?", "Shampoo."),
            ("I foam up on your head and wash the week away. What am I?", "Shampoo."),
        ],
    },
    "hair_oil": {
        "jokes": [
            ("Why don't hair oils ever argue?", "They just smooth things over."),
            ("What did the hair oil say to frizz?", "Not on my watch."),
            ("Why does hair serum get invited to every party?", "It makes everything look sleek."),
        ],
        "riddles": [
            ("A little of me turns frizz into shine. What am I?", "Shine in a bottle."),
            ("Your ends love me, and frizz is scared of me. What am I?", "A frizz fighter."),
            ("I tame flyaways and add gloss, all from a small bottle. What am I?", "Hair shine in a bottle."),
        ],
    },
    "hair_dryer": {
        "jokes": [
            ("Why did the hair dryer get a raise?", "It always blew everyone away."),
            ("Why is the blow dryer so popular?", "It's full of hot air, in the best way."),
        ],
        "riddles": [
            ("I'm hot air with a handle. What am I?", "A hair dryer."),
            ("I'm loud, I'm warm and I turn wet hair into a blowout. What am I?", "A blow dryer."),
        ],
    },
    "hair_brush": {
        "jokes": [
            ("What did the brush say to the tangled hair?", "Let's work through this together."),
            ("Why did the hairbrush go to the party alone?", "It didn't want any tangles."),
        ],
        "riddles": [
            ("I have bristles, a handle, and I'm best friends with your hair. What am I?", "A hairbrush."),
            ("I get to the root of the problem and leave no knot behind. What am I?", "A detangling brush."),
        ],
    },
    "hair": {
        "jokes": [
            ("Why do bad hair days never last?", "Good products always get to the root of it."),
            ("Why was the hair so confident?", "It had great body."),
            ("Why did the hair go to the party?", "It wanted to let its hair down."),
            ("Why are hair products so supportive?", "They always have your back, and your roots."),
        ],
        "riddles": [
            ("I can be big, sleek or wavy, depending on what you put on me. What am I?", "Your hair."),
            ("I'm on your head every day and I love a good wash day. What am I?", "Your hair."),
            ("I'm sprayed, scrunched and styled, then washed and started over. What am I?", "Your hair."),
            ("I go from frizzy to glossy with the right bottle. What am I?", "Your hair."),
        ],
    },
}

# Types that fall back to a category before the general lists
PARENT = {
    "mascara": "makeup", "brow": "makeup", "lips": "makeup", "lipstick": "makeup", "blush": "makeup",
    "bronzer": "makeup", "highlighter": "makeup", "concealer": "makeup", "foundation": "makeup",
    "powder": "makeup", "setting_spray": "makeup", "top_coat": "nails",
    "sunscreen": "skincare", "patch": "skincare", "cleanser": "skincare", "toner": "skincare",
    "serum": "skincare", "moisturizer": "skincare",
    "shampoo": "hair", "hair_oil": "hair", "hair_dryer": "hair", "hair_brush": "hair",
}

# File-name codes used by the sketch pipeline, e.g. 2026-10-17_1900_frg-dorsay-vanilla-affair
CODES = {"frg": "fragrance", "nai": "nails", "mua": "makeup", "mub": "makeup",
         "ska": "skincare", "skb": "skincare", "hra": "hair", "hrb": "hair"}

# Keyword rules per category, checked in order against the product name
RULES = {
    "fragrance": [("fragrance", ["perfume", "parfum", "edp", "edt", "cologne", "fragrance", "eau-de",
                                 "body-mist", "perfume-mist", "hair-body-mist"])],
    "nails": [
        ("top_coat", ["top-coat", "topcoat"]),
        ("nails", ["nail", "vernis", "polish", "lacquer", "quickcoat", "manucurist"]),
    ],
    "makeup": [
        ("mascara", ["mascara", "lash"]),
        ("brow", ["brow"]),
        ("lipstick", ["lipstick", "matte-revolution"]),
        ("lips", ["lip-", "gloss-bomb"]),
        ("blush", ["blush", "cheek", "cloud-paint", "miracle-balm", "flush"]),
        ("bronzer", ["bronzer"]),
        ("highlighter", ["luminizer", "highlighter", "glow-drops"]),
        ("concealer", ["concealer"]),
        ("foundation", ["foundation", "skin-tint", "tint-stick", "filter", "skin-tech"]),
        ("powder", ["powder"]),
        ("setting_spray", ["setting", "fixing-spray"]),
    ],
    "skincare": [
        ("sunscreen", ["spf", "sunscreen", "sun-"]),
        ("patch", ["patch"]),
        ("cleanser", ["cleans", "micellar", "face-wash"]),
        ("toner", ["toner"]),
        ("serum", ["serum", "essence", "ampoule", "dew-drops"]),
        ("moisturizer", ["cream", "moistur", "balm", "lotion", "butter", "mask"]),
    ],
    "hair": [
        ("hair_dryer", ["dryer", "flexstyle", "airsmooth", "airwrap", "blow"]),
        ("hair_brush", ["brush", "tangle-teezer", "mason-pearson", "comb"]),
        ("shampoo", ["shampoo"]),
        ("hair_oil", ["oil", "elixir", "serum", "anti-frizz", "drops"]),
    ],
}
