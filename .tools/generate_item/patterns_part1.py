# patterns_part1.py
# Part1の問題パターン集だけをまとめたモジュール

# === Part1 用の問題パターン集 ===
PART1_PATTERNS = [
    # --- A2 level 100patterns (easy) ---
    # 1: correct = A (A2)
    {
        "level": "A2",
        "query": "kitchen woman making breakfast",
        "statements": [
            "A woman is cooking eggs in a frying pan on a stove.",
            "A man is repairing a bicycle outside a house.",
            "Some children are swimming in an outdoor pool.",
            "Passengers are getting on a train at a platform.",
        ],
        "answer": "A",
        "rationale": "The picture shows a woman cooking breakfast in a kitchen. The other choices describe outdoor or travel scenes."
    },

    # 2: correct = B (A2)
    {
        "level": "A2",
        "query": "bus stop people waiting umbrellas",
        "statements": [
            "A man is typing on a laptop at a desk.",
            "Several people are standing under umbrellas at a bus stop.",
            "Two workers are carrying boxes in a warehouse.",
            "A cook is taking bread out of an oven.",
        ],
        "answer": "B",
        "rationale": "The scene is at a bus stop where people are waiting with umbrellas. The other statements describe work indoors."
    },

    # 3: correct = C (A2)
    {
        "level": "A2",
        "query": "park bench elderly couple resting",
        "statements": [
            "A waiter is serving food at a restaurant.",
            "A woman is choosing fruit in a supermarket aisle.",
            "An elderly couple is sitting together on a bench in a park.",
            "A student is writing on a whiteboard in a classroom.",
        ],
        "answer": "C",
        "rationale": "The correct description is the older couple resting on a bench in a park. The other options show indoor activities."
    },

    # 4: correct = D (A2)
    {
        "level": "A2",
        "query": "train interior passengers reading",
        "statements": [
            "A chef is chopping vegetables on a cutting board.",
            "A woman is sweeping the floor in a living room.",
            "A boy is kicking a ball on a soccer field.",
            "Several passengers are sitting on a train and reading books.",
        ],
        "answer": "D",
        "rationale": "The picture is inside a train with passengers reading. The other sentences describe very different locations."
    },

    # 5: correct = A (A2)
    {
        "level": "A2",
        "query": "coffee shop barista preparing drink",
        "statements": [
            "A barista is pouring milk into a cup behind a counter.",
            "A nurse is talking to a patient in a hospital room.",
            "A group of people is listening to music at a concert.",
            "A man is mowing the grass in a yard.",
        ],
        "answer": "A",
        "rationale": "The scene shows a barista making a drink at a coffee shop counter. The other choices are hospital, concert, or yard scenes."
    },

    # 6: correct = B (A2)
    {
        "level": "A2",
        "query": "supermarket aisle woman pushing cart",
        "statements": [
            "A mechanic is looking under the hood of a car.",
            "A woman is pushing a shopping cart down a supermarket aisle.",
            "A child is painting at a small table.",
            "A man is raking leaves in a park.",
        ],
        "answer": "B",
        "rationale": "The picture is inside a supermarket with a shopper and a cart. The other sentences describe different tasks."
    },

    # 7: correct = C (A2)
    {
        "level": "A2",
        "query": "office desk man on phone",
        "statements": [
            "A woman is walking a dog along a sidewalk.",
            "Some workers are painting a wall outside a building.",
            "A man is talking on the phone while sitting at an office desk.",
            "A group of students is eating lunch at a cafeteria table.",
        ],
        "answer": "C",
        "rationale": "The correct sentence shows an office worker on the phone at his desk. The other choices are outdoor or school scenes."
    },

    # 8: correct = D (A2)
    {
        "level": "A2",
        "query": "kitchen family eating dinner table",
        "statements": [
            "A cashier is handing a receipt to a customer.",
            "A driver is filling a car with gasoline.",
            "A woman is folding clothes on a sofa.",
            "A family is having a meal together at a kitchen table.",
        ],
        "answer": "D",
        "rationale": "The picture shows family members eating at a table in a kitchen. The other options show different activities."
    },

    # 9: correct = A (A2)
    {
        "level": "A2",
        "query": "street crosswalk people crossing",
        "statements": [
            "Several pedestrians are walking across a crosswalk at an intersection.",
            "A man is trimming plants in a greenhouse.",
            "Children are playing with blocks in a classroom.",
            "A singer is standing on a stage with a microphone.",
        ],
        "answer": "A",
        "rationale": "The correct statement is people crossing the street at a crosswalk. The other sentences do not match an intersection scene."
    },

    # 10: correct = B (A2)
    {
        "level": "A2",
        "query": "living room sofa family watching tv",
        "statements": [
            "A woman is standing in front of a shelf of books in a library.",
            "A family is sitting on a sofa and watching television in a living room.",
            "A man is cleaning windows on the outside of a building.",
            "Some workers are unloading boxes from a truck.",
        ],
        "answer": "B",
        "rationale": "The scene takes place in a living room with a family watching TV. The other statements show library, outdoor cleaning, or delivery work."
    },

    # 11: correct = C (A2)
    {
        "level": "A2",
        "query": "restaurant table couple reading menu",
        "statements": [
            "A clerk is printing a receipt at a counter.",
            "A boy is riding a bicycle along a path.",
            "A couple is sitting at a restaurant table and looking at menus.",
            "A woman is watering flowers on a balcony.",
        ],
        "answer": "C",
        "rationale": "Only the third sentence describes diners reading menus at a table. The others are unrelated actions."
    },

    # 12: correct = D (A2)
    {
        "level": "A2",
        "query": "classroom teacher pointing board",
        "statements": [
            "A woman is choosing vegetables at an outdoor market.",
            "A man is tying his shoes near a bench.",
            "A worker is painting a fence outside a house.",
            "A teacher is pointing at something written on a board in a classroom.",
        ],
        "answer": "D",
        "rationale": "The picture is inside a classroom with a teacher pointing at the board. The other statements describe outdoor activities."
    },

    # 13: correct = A (A2)
    {
        "level": "A2",
        "query": "kitchen man washing dishes sink",
        "statements": [
            "A man is washing dishes in a sink filled with soapy water.",
            "Two cyclists are riding along a country road.",
            "Passengers are standing in a crowded train car.",
            "A woman is paying for groceries at a register.",
        ],
        "answer": "A",
        "rationale": "The scene shows someone doing dishes at a kitchen sink. The other choices show transportation or shopping."
    },

    # 14: correct = B (A2)
    {
        "level": "A2",
        "query": "office meeting small group table",
        "statements": [
            "A cook is slicing bread on a cutting board.",
            "Several people are sitting around a small table having a meeting.",
            "A child is feeding pigeons in a square.",
            "A tourist is taking a picture of a statue.",
        ],
        "answer": "B",
        "rationale": "The correct sentence describes coworkers in a small meeting. The other choices describe unrelated scenes."
    },

    # 15: correct = C (A2)
    {
        "level": "A2",
        "query": "kitchen woman opening refrigerator",
        "statements": [
            "A man is reading a magazine on a park bench.",
            "Some workers are standing on a ladder near a ceiling light.",
            "A woman is opening the door of a refrigerator in a kitchen.",
            "A bus driver is greeting a passenger at the front door of a bus.",
        ],
        "answer": "C",
        "rationale": "Only the third sentence talks about a woman opening a refrigerator. The others show different locations."
    },

    # 16: correct = D (A2)
    {
        "level": "A2",
        "query": "playground children on swings",
        "statements": [
            "A man is putting files into a cabinet.",
            "Two women are looking at clothes in a store.",
            "A waiter is clearing plates from a table.",
            "Children are sitting on swings at a playground.",
        ],
        "answer": "D",
        "rationale": "The scene shows children using swings outdoors. The other statements involve office work, shopping, or restaurant service."
    },

    # 17: correct = A (A2)
    {
        "level": "A2",
        "query": "kitchen man cutting vegetables board",
        "statements": [
            "A man is cutting vegetables on a board beside a sink.",
            "A group of people is dancing on a stage.",
            "Shoppers are walking through a mall corridor.",
            "A woman is waiting at a train platform.",
        ],
        "answer": "A",
        "rationale": "The correct choice is the man preparing food in a kitchen. The others describe public or travel settings."
    },

    # 18: correct = B (A2)
    {
        "level": "A2",
        "query": "library woman reading at table",
        "statements": [
            "A driver is checking the engine of a car.",
            "A woman is sitting alone at a table reading a book in a library.",
            "A cook is washing vegetables in a sink.",
            "Workers are fixing a roof on a house.",
        ],
        "answer": "B",
        "rationale": "The scene is clearly inside a library with a reader at a table. The other sentences show other types of work."
    },

    # 19: correct = C (A2)
    {
        "level": "A2",
        "query": "kitchen child helping bake cookies",
        "statements": [
            "A man is repairing a computer monitor on a desk.",
            "Some people are jogging along a riverside path.",
            "A child is standing on a stool and helping an adult bake cookies.",
            "A woman is selling tickets at a theater window.",
        ],
        "answer": "C",
        "rationale": "Only the third sentence describes a child helping with baking in a kitchen. The other options show different activities."
    },

    # 20: correct = D (A2)
    {
        "level": "A2",
        "query": "office printer man collecting pages",
        "statements": [
            "A woman is sitting in the backseat of a taxi.",
            "A couple is looking at a menu outside a restaurant.",
            "A gardener is using a hose to water flowers.",
            "A man is picking up printed pages from a machine in an office.",
        ],
        "answer": "D",
        "rationale": "The correct description is an office worker collecting pages from a printer. The others are unrelated places."
    },

    # 21: correct = A (A2)
    {
        "level": "A2",
        "query": "kitchen woman washing vegetables in sink",
        "statements": [
            "A woman is rinsing vegetables under running water in a kitchen sink.",
            "A man is locking a bicycle to a rack.",
            "A child is standing at a bus stop with a backpack.",
            "A group of people is looking at paintings on a wall.",
        ],
        "answer": "A",
        "rationale": "The image shows someone washing vegetables at a sink. The other statements mention bicycles, buses, or art."
    },

    # 22: correct = B (A2)
    {
        "level": "A2",
        "query": "cafe outdoor tables people chatting",
        "statements": [
            "A doctor is writing notes on a chart.",
            "People are sitting at small tables outside a café and talking.",
            "A worker is painting lines on a road.",
            "A woman is closing a window in an office.",
        ],
        "answer": "B",
        "rationale": "The correct description matches an outdoor café scene. The other options show medical, road, or office settings."
    },

    # 23: correct = C (A2)
    {
        "level": "A2",
        "query": "bedroom woman making bed",
        "statements": [
            "A man is lifting a suitcase onto a shelf on a train.",
            "Two men are shaking hands across a desk.",
            "A woman is straightening a blanket on a bed in a bedroom.",
            "A child is drawing pictures on a chalkboard.",
        ],
        "answer": "C",
        "rationale": "The picture shows a woman making a bed in a bedroom. The other choices show business, travel, or school scenes."
    },

    # 24: correct = D (A2)
    {
        "level": "A2",
        "query": "grocery checkout man paying cashier",
        "statements": [
            "A boy is climbing stairs in a building.",
            "A woman is watering plants on a window ledge.",
            "A musician is playing a piano on stage.",
            "A man is handing money to a cashier at a grocery checkout.",
        ],
        "answer": "D",
        "rationale": "The correct sentence describes a customer paying at a supermarket checkout. The others are unrelated actions."
    },

    # 25: correct = A (A2)
    {
        "level": "A2",
        "query": "kitchen couple drinking coffee at counter",
        "statements": [
            "A couple is standing at a kitchen counter drinking coffee together.",
            "A man is sweeping leaves off a sidewalk.",
            "Some tourists are looking at a map on a street corner.",
            "A girl is tying her shoelaces on a bench.",
        ],
        "answer": "A",
        "rationale": "The image is of a couple having coffee in a kitchen. The other statements describe outdoor scenes."
    },

    # 26: correct = B (A2)
    {
        "level": "A2",
        "query": "classroom students using tablets",
        "statements": [
            "A woman is buying a ticket from a vending machine.",
            "Students are sitting at desks and using tablet computers in a classroom.",
            "A man is repairing a fence in a yard.",
            "A runner is stretching beside a track.",
        ],
        "answer": "B",
        "rationale": "Only the second sentence talks about students using tablets in class. The others refer to very different environments."
    },

    # 27: correct = C (A2)
    {
        "level": "A2",
        "query": "kitchen woman taking tray from oven",
        "statements": [
            "A driver is looking into a rearview mirror.",
            "A shopper is weighing fruit on a scale.",
            "A woman is removing a tray from an oven while wearing oven gloves.",
            "A child is climbing on playground equipment.",
        ],
        "answer": "C",
        "rationale": "The picture shows someone taking a tray out of an oven with gloves. The other options describe unrelated activities."
    },

    # 28: correct = D (A2)
    {
        "level": "A2",
        "query": "office reception woman talking to visitor",
        "statements": [
            "A man is taking money from an ATM machine.",
            "A child is feeding ducks at a pond.",
            "A worker is stacking boxes on a shelf.",
            "A receptionist is speaking with a visitor at a front desk.",
        ],
        "answer": "D",
        "rationale": "The correct sentence describes a receptionist and a visitor at an office desk. The others are not reception scenes."
    },

    # 29: correct = A (A2)
    {
        "level": "A2",
        "query": "street market woman choosing flowers",
        "statements": [
            "A woman is selecting flowers from a stand at an outdoor market.",
            "A man is ironing a shirt on an ironing board.",
            "A boy is washing his hands in a bathroom sink.",
            "A group of people is sitting in a meeting room.",
        ],
        "answer": "A",
        "rationale": "The correct choice is a woman picking flowers at a street stall. The others show indoor tasks or meetings."
    },

    # 30: correct = B (A2)
    {
        "level": "A2",
        "query": "bus interior woman holding handrail",
        "statements": [
            "A cook is stirring sauce in a pan.",
            "A woman is standing on a bus and holding onto a handrail.",
            "A man is hanging clothes on a line outside.",
            "Some children are playing on a carpet with toys.",
        ],
        "answer": "B",
        "rationale": "The scene is inside a bus with a passenger holding a handrail. The other statements describe cooking, laundry, or play."
    },
    # === A2 Part1 Patterns (31-50 revised) ===
    {
        "level": "A2",
        "query": "woman holding smartphone living room sofa casual",
        "statements": [
            "A woman is holding a smartphone.",
            "A man is typing on a computer.",
            "The woman is cooking dinner.",
            "The sofa is empty."
        ],
        "answer": "A",
        "rationale": "The picture shows a woman holding a smartphone while sitting on the sofa."
    },
    {
        "level": "A2",
        "query": "man drinking coffee office desk laptop morning",
        "statements": [
            "A man is sleeping on the floor.",
            "The man is drinking coffee at his desk.",
            "A woman is using a whiteboard.",
            "The desk is full of vegetables."
        ],
        "answer": "B",
        "rationale": "The man is drinking coffee at his desk."
    },
    {
        "level": "A2",
        "query": "two people walking park sunny trees path",
        "statements": [
            "Two people are running a race indoors.",
            "Two people are sitting on a bench.",
            "Two people are walking in the park.",
            "A car is parked next to them."
        ],
        "answer": "C",
        "rationale": "Two people are walking outside in the park."
    },
    {
        "level": "A2",
        "query": "woman reading book bed pillow lamp night",
        "statements": [
            "The woman is dancing on a stage.",
            "She is washing dishes in the kitchen.",
            "A woman is reading a book in bed.",
            "The room is a busy office."
        ],
        "answer": "C",
        "rationale": "The woman is reading a book while lying in bed."
    },
    {
        "level": "A2",
        "query": "man riding bicycle city street daytime helmet",
        "statements": [
            "A man is driving a bus.",
            "The street is covered with heavy snow.",
            "He is walking his dog.",
            "A man is riding a bicycle on a city street."
        ],
        "answer": "D",
        "rationale": "A man is cycling on a city street."
    },
    {
        "level": "A2",
        "query": "woman shopping supermarket groceries cart aisle",
        "statements": [
            "The woman is sitting in a restaurant.",
            "The cart is full of toys.",
            "She is cleaning the floor.",
            "A woman is pushing a shopping cart."
        ],
        "answer": "D",
        "rationale": "The woman is walking with a shopping cart in the supermarket aisle."
    },
    {
        "level": "A2",
        "query": "man waiting bus stop checking watch evening street",
        "statements": [
            "The man is swimming in a pool.",
            "He is repairing a car engine.",
            "The man is sitting inside a bus.",
            "A man is waiting at a bus stop."
        ],
        "answer": "D",
        "rationale": "The man is standing and waiting for a bus."
    },
    {
        "level": "A2",
        "query": "woman cutting vegetables kitchen counter cooking",
        "statements": [
            "She is working at a computer.",
            "A family is eating dinner.",
            "The kitchen is empty.",
            "A woman is cutting vegetables."
        ],
        "answer": "D",
        "rationale": "The woman is preparing food by cutting vegetables."
    },
    {
        "level": "A2",
        "query": "man talking phone office chair notebook pen",
        "statements": [
            "A woman is writing a report.",
            "The man is talking on the phone.",
            "The man is cooking pasta.",
            "He is reading a newspaper outside."
        ],
        "answer": "B",
        "rationale": "The man is using his phone while seated in the office."
    },
    {
        "level": "A2",
        "query": "woman cleaning window cloth spray bottle home",
        "statements": [
            "She is lying on a beach.",
            "The woman is driving a car.",
            "A woman is cleaning a window.",
            "A dog is sleeping on the bed."
        ],
        "answer": "C",
        "rationale": "The woman is using a cloth and spray to clean the window."
    },
    {
        "level": "A2",
        "query": "two people eating lunch cafe table food drinks",
        "statements": [
            "They are fixing a bicycle.",
            "Two people are eating lunch at a cafe.",
            "A person is sleeping on a bench.",
            "They are painting a wall together."
        ],
        "answer": "B",
        "rationale": "The picture shows two people sharing a meal at a cafe."
    },
    {
        "level": "A2",
        "query": "man watering plants garden morning sunshine",
        "statements": [
            "A woman is playing the piano.",
            "A man is watering the plants.",
            "The plants are dying in the snow.",
            "He is driving a tractor."
        ],
        "answer": "B",
        "rationale": "The man is watering plants in the garden."
    },
    {
        "level": "A2",
        "query": "woman holding umbrella rainy street crosswalk",
        "statements": [
            "A woman is sunbathing.",
            "She is walking in the desert.",
            "The street is covered in snow.",
            "A woman is holding an umbrella."
        ],
        "answer": "D",
        "rationale": "It is raining and the woman is holding an umbrella."
    },
    {
        "level": "A2",
        "query": "man reading newspaper bench park daylight",
        "statements": [
            "The bench is empty.",
            "A woman is cutting grass.",
            "A man is riding a horse.",
            "A man is reading a newspaper."
        ],
        "answer": "D",
        "rationale": "The man is sitting on a bench and reading."
    },
    {
        "level": "A2",
        "query": "woman using laptop cafe cup coffee table",
        "statements": [
            "She is sleeping in bed.",
            "A woman is using a laptop at a cafe.",
            "The woman is cooking soup.",
            "She is running on a track."
        ],
        "answer": "B",
        "rationale": "The woman is working on a laptop with coffee nearby."
    },
    {
        "level": "A2",
        "query": "man brushing teeth bathroom mirror morning",
        "statements": [
            "He is shouting at a crowd.",
            "The man is brushing his teeth.",
            "The man is cutting his hair.",
            "He is sleeping on a bench."
        ],
        "answer": "B",
        "rationale": "The man is brushing his teeth in front of a mirror."
    },
    {
        "level": "A2",
        "query": "woman folding clothes laundry room baskets",
        "statements": [
            "A woman is folding clothes.",
            "She is swimming in a pool.",
            "The clothes are burning in a fire.",
            "She is driving a car."
        ],
        "answer": "A",
        "rationale": "The woman is folding clean laundry in the room."
    },
    {
        "level": "A2",
        "query": "man cooking frying pan stove kitchen apron",
        "statements": [
            "The man is fixing a bicycle wheel.",
            "A man is cooking on the stove.",
            "He is watching TV on a couch.",
            "He is checking tickets at a station."
        ],
        "answer": "B",
        "rationale": "A man is preparing food on a frying pan."
    },
    {
        "level": "A2",
        "query": "family walking dog neighborhood houses afternoon",
        "statements": [
            "A man is flying an airplane.",
            "A woman is working in a hospital.",
            "A family is walking their dog.",
            "The dog is sleeping inside a house."
        ],
        "answer": "C",
        "rationale": "A family is outdoors walking a dog."
    },
    {
        "level": "A2",
        "query": "woman listening music headphones park trees relaxing",
        "statements": [
            "The headphones are on the table.",
            "She is speaking to a large audience.",
            "A woman is listening to music with headphones.",
            "She is writing on the whiteboard."
        ],
        "answer": "C",
        "rationale": "The woman is wearing headphones and listening to something."
    },
    # === A2 Part1 Patterns (51–70 revised answers distributed) ===
    {
        "level": "A2",
        "query": "man washing car driveway hose sponge outdoor",
        "statements": [
            "The man is flying a kite.",
            "A woman is cutting paper.",
            "The car is parked inside a garage.",
            "A man is washing a car."
        ],
        "answer": "D",
        "rationale": "The man is cleaning the car using a sponge and water outside."
    },
    {
        "level": "A2",
        "query": "woman painting wall roller ladder indoor renovation",
        "statements": [
            "The woman is reading a picture book.",
            "She is lying in a hammock outside.",
            "A woman is painting a wall with a roller.",
            "She is cooking in the kitchen."
        ],
        "answer": "C",
        "rationale": "The woman is painting a wall as part of home renovation."
    },
    {
        "level": "A2",
        "query": "two people assembling furniture living room tools instruction",
        "statements": [
            "They are jogging in the park.",
            "Two people are assembling furniture.",
            "They are sleeping on the sofa.",
            "Two people are playing a board game."
        ],
        "answer": "B",
        "rationale": "The two people are building furniture using tools and an instruction sheet."
    },
    {
        "level": "A2",
        "query": "woman walking dog forest path morning",
        "statements": [
            "A woman is teaching a class.",
            "She is driving a motorcycle.",
            "A woman is walking a dog in the forest.",
            "She is shopping at a market."
        ],
        "answer": "C",
        "rationale": "The picture shows a woman walking her dog on a forest path."
    },
    {
        "level": "A2",
        "query": "man taking photo camera city bridge sightseeing",
        "statements": [
            "A man is taking a picture with a camera.",
            "A man is talking on the phone.",
            "He is fixing a bike.",
            "The man is cutting vegetables."
        ],
        "answer": "A",
        "rationale": "The man is holding a camera and taking a photo near a bridge."
    },
    {
        "level": "A2",
        "query": "couple eating ice cream outdoor bench sunny",
        "statements": [
            "They are fixing a broken computer.",
            "A couple is eating ice cream outside.",
            "The people are in a concert hall.",
            "A family is swimming in a pool."
        ],
        "answer": "B",
        "rationale": "The couple is enjoying ice cream together outdoors."
    },
    {
        "level": "A2",
        "query": "woman making sandwich kitchen bread cheese lunch",
        "statements": [
            "She is polishing her shoes.",
            "A woman is singing on a stage.",
            "She is watering flowers.",
            "A woman is making a sandwich."
        ],
        "answer": "D",
        "rationale": "The woman is preparing a sandwich for lunch."
    },
    {
        "level": "A2",
        "query": "man tying shoelaces park running shoes morning exercise",
        "statements": [
            "The man is painting in an art studio.",
            "He is tying his shoelaces.",
            "He is cleaning dishes in the sink.",
            "He is brushing the dog."
        ],
        "answer": "B",
        "rationale": "The man is sitting down and tying his shoelaces before exercising."
    },
    {
        "level": "A2",
        "query": "woman feeding cat pet bowl home kitchen floor",
        "statements": [
            "The woman is driving a truck.",
            "The woman is feeding a cat.",
            "She is checking luggage at the airport.",
            "She is playing tennis outside."
        ],
        "answer": "B",
        "rationale": "The woman is placing food in a bowl for her cat."
    },
    {
        "level": "A2",
        "query": "man sweeping porch broom house entrance evening",
        "statements": [
            "The man is eating spaghetti.",
            "The man is sweeping the porch.",
            "He is sleeping next to a fire.",
            "The man is surfing in the ocean."
        ],
        "answer": "B",
        "rationale": "The man is cleaning the house entrance with a broom."
    },
    {
        "level": "A2",
        "query": "woman packing suitcase bedroom travel clothes luggage",
        "statements": [
            "A woman is lifting weights at a gym.",
            "She is washing vegetables.",
            "The woman is packing a suitcase.",
            "She is playing with a cat on the floor."
        ],
        "answer": "C",
        "rationale": "The woman is preparing clothes and packing her suitcase."
    },
    {
        "level": "A2",
        "query": "man buying ticket vending machine station public transport",
        "statements": [
            "The man is swinging on a playground.",
            "He is painting a wall.",
            "The man is baking bread.",
            "He is buying a ticket from a machine."
        ],
        "answer": "D",
        "rationale": "The man is using a vending machine to purchase a ticket."
    },
    {
        "level": "A2",
        "query": "woman stretching yoga mat living room home exercise",
        "statements": [
            "The woman is swimming across a lake.",
            "A woman is stretching on a yoga mat.",
            "She is repairing a fence outside.",
            "She is serving food to guests."
        ],
        "answer": "B",
        "rationale": "The woman is exercising and stretching on a yoga mat."
    },
    {
        "level": "A2",
        "query": "man carrying grocery bags front door house shopping",
        "statements": [
            "The man is tying a boat to a dock.",
            "The man is carrying grocery bags.",
            "He is cooking fish on a campfire.",
            "The man is painting his face for a show."
        ],
        "answer": "B",
        "rationale": "The man is returning home with full grocery bags."
    },
    {
        "level": "A2",
        "query": "woman planting flowers backyard soil gardening gloves",
        "statements": [
            "A woman is planting flowers in the backyard.",
            "The woman is driving a small tractor.",
            "She is studying at a desk.",
            "She is watching a live concert."
        ],
        "answer": "A",
        "rationale": "The woman is gardening and placing flowers in the soil."
    },
    {
        "level": "A2",
        "query": "man washing hands bathroom sink soap hygiene",
        "statements": [
            "He is dancing in the living room.",
            "The man is reading a map outside.",
            "The man is washing his hands.",
            "He is petting a horse."
        ],
        "answer": "C",
        "rationale": "The man is washing his hands with soap in the bathroom."
    },
    {
        "level": "A2",
        "query": "woman sewing clothes needles fabric home craft",
        "statements": [
            "She is climbing a tall tree.",
            "A woman is sewing clothes.",
            "The woman is taking out the trash.",
            "She is using a vacuum cleaner."
        ],
        "answer": "B",
        "rationale": "The woman is sewing fabric with a needle."
    },
    {
        "level": "A2",
        "query": "man changing light bulb ladder ceiling repair home",
        "statements": [
            "He is fishing at a river.",
            "The man is eating cake at a party.",
            "He is snowboarding down a hill.",
            "The man is changing a light bulb."
        ],
        "answer": "D",
        "rationale": "The man is standing on a ladder to replace a light bulb."
    },
    {
        "level": "A2",
        "query": "woman hanging clothes clothesline backyard laundry drying",
        "statements": [
            "A woman is hanging clothes outside.",
            "She is typing on a computer keyboard.",
            "She is fishing on a boat.",
            "She is making a speech onstage."
        ],
        "answer": "A",
        "rationale": "The woman is placing wet laundry onto a clothesline to dry."
    },
    {
        "level": "A2",
        "query": "man sitting firepit roasting marshmallow camping chair night outdoor",
        "statements": [
            "He is answering phones in an office.",
            "The man is washing a car at a gas station.",
            "The man is roasting a marshmallow at a firepit.",
            "He is sleeping on a long flight."
        ],
        "answer": "C",
        "rationale": "The man is sitting outdoors and roasting a marshmallow by the fire."
    },
    # === A2 Part1 Patterns (71–90) ===
    {
        "level": "A2",
        "query": "man ironing shirt ironing board laundry home",
        "statements": [
            "The man is ironing a shirt.",
            "He is swimming in a pool.",
            "The man is eating at a restaurant.",
            "He is playing basketball."
        ],
        "answer": "A",
        "rationale": "The man is using an iron on a shirt at home."
    },
    {
        "level": "A2",
        "query": "woman washing lettuce kitchen sink preparing salad",
        "statements": [
            "A woman is washing lettuce.",
            "She is driving a scooter.",
            "She is painting a landscape outdoors.",
            "She is working on a farm."
        ],
        "answer": "A",
        "rationale": "The woman is washing vegetables in a sink to make a meal."
    },
    {
        "level": "A2",
        "query": "man taking out trash garbage bag front yard evening",
        "statements": [
            "The man is taking out the trash.",
            "The man is skiing down a hill.",
            "He is selling fruit at a market.",
            "He is washing dishes."
        ],
        "answer": "A",
        "rationale": "The man is holding a garbage bag outside the house."
    },
    {
        "level": "A2",
        "query": "woman feeding baby bottle living room sofa daytime",
        "statements": [
            "The woman is bathing a baby.",
            "A woman is feeding a baby with a bottle.",
            "The woman is jogging in the park.",
            "She is repairing a bicycle."
        ],
        "answer": "B",
        "rationale": "The woman is sitting on the sofa and feeding a baby."
    },
    {
        "level": "A2",
        "query": "man reading instructions assembling toy table tools",
        "statements": [
            "The man is reading instructions while building a toy.",
            "The man is napping on the couch.",
            "He is cutting grass outside.",
            "He is working as a cashier."
        ],
        "answer": "A",
        "rationale": "The man is assembling a toy using tools and a manual."
    },
    {
        "level": "A2",
        "query": "woman pouring juice dining table breakfast glasses",
        "statements": [
            "A woman is pouring juice.",
            "The woman is singing karaoke.",
            "She is lifting heavy boxes.",
            "She is working at a construction site."
        ],
        "answer": "A",
        "rationale": "The woman is filling glasses with juice at the table."
    },
    {
        "level": "A2",
        "query": "man organizing books bookshelf living room cleaning",
        "statements": [
            "The man is organizing books on a shelf.",
            "The man is climbing a tall tower.",
            "He is fencing with a sword.",
            "He is dancing in a studio."
        ],
        "answer": "A",
        "rationale": "The man is tidying the books on the shelf."
    },
    {
        "level": "A2",
        "query": "woman knitting scarf yarn needles couch cozy",
        "statements": [
            "The woman is knitting a scarf.",
            "The woman is washing a car.",
            "She is directing traffic.",
            "She is skateboarding in a park."
        ],
        "answer": "A",
        "rationale": "The woman is using knitting needles and yarn on the couch."
    },
    {
        "level": "A2",
        "query": "man grilling food barbecue backyard picnic",
        "statements": [
            "A man is grilling food outside.",
            "The man is preparing pizza in a bakery.",
            "He is fishing from a boat.",
            "He is watching a movie on TV."
        ],
        "answer": "A",
        "rationale": "The man is cooking food on a grill in the backyard."
    },
    {
        "level": "A2",
        "query": "woman washing car windshield sponge water driveway",
        "statements": [
            "A woman is washing the windshield of a car.",
            "She is sitting in a classroom.",
            "The woman is flying an airplane.",
            "She is running a clothing shop."
        ],
        "answer": "A",
        "rationale": "She is standing outside and cleaning the front of her car."
    },
    {
        "level": "A2",
        "query": "man buying bread bakery counter cashier morning",
        "statements": [
            "The man is buying bread at a bakery.",
            "The man is mowing a lawn.",
            "He is camping in the mountains.",
            "He is working as a dentist."
        ],
        "answer": "A",
        "rationale": "The man is at a bakery counter selecting bread."
    },
    {
        "level": "A2",
        "query": "woman mopping floor kitchen bucket cleaning",
        "statements": [
            "The woman is playing volleyball.",
            "The woman is mopping the floor.",
            "She is wrapping gifts for a party.",
            "She is taking photos of birds."
        ],
        "answer": "B",
        "rationale": "She is cleaning the floor using a mop and bucket."
    },
    {
        "level": "A2",
        "query": "man cooking soup stirring pot stove apron",
        "statements": [
            "The man is stirring soup on the stove.",
            "The man is sewing clothes.",
            "He is swimming with dolphins.",
            "He is cutting wood in a forest."
        ],
        "answer": "A",
        "rationale": "The man is preparing food on the stove."
    },
    {
        "level": "A2",
        "query": "woman fixing hair looking mirror bathroom getting ready",
        "statements": [
            "The woman is fixing her hair in front of a mirror.",
            "The woman is painting a sunset picture.",
            "She is hiking up a steep hill.",
            "She is feeding ducks at the lake."
        ],
        "answer": "A",
        "rationale": "The woman is adjusting her hair while looking in the mirror."
    },
    {
        "level": "A2",
        "query": "man wrapping gift present ribbon table celebration",
        "statements": [
            "The man is playing the violin.",
            "He is fixing a broken car.",
            "The man is wrapping a gift.",
            "He is washing windows."
        ],
        "answer": "C",
        "rationale": "The man is wrapping a present using ribbon and paper."
    },
    {
        "level": "A2",
        "query": "woman cutting fruit kitchen knife breakfast bowl",
        "statements": [
            "She is repairing a phone screen.",
            "She is cutting fruit in the kitchen.",
            "A woman is flying a drone.",
            "She is watering indoor plants."
        ],
        "answer": "B",
        "rationale": "The woman is slicing fruit into a bowl."
    },
    {
        "level": "A2",
        "query": "man petting dog living room sofa friendship",
        "statements": [
            "The man is petting a dog.",
            "The man is juggling balls.",
            "He is giving a speech on a stage.",
            "He is analyzing data on a laptop."
        ],
        "answer": "A",
        "rationale": "The man is gently petting his dog next to the sofa."
    },
    {
        "level": "A2",
        "query": "woman refilling bird feeder backyard birds nature",
        "statements": [
            "The woman is refilling a bird feeder.",
            "She is skiing through snow.",
            "She is playing drums in a band.",
            "She is washing her car at a gas station."
        ],
        "answer": "A",
        "rationale": "The woman is adding food to a bird feeder outside."
    },
    {
        "level": "A2",
        "query": "man pouring milk cereal breakfast table morning",
        "statements": [
            "A man is pouring milk into a bowl of cereal.",
            "The man is fixing a ceiling lamp.",
            "He is painting a large fence.",
            "He is skateboarding at a park."
        ],
        "answer": "A",
        "rationale": "The man is having breakfast and adding milk to cereal."
    },
    {
        "level": "A2",
        "query": "woman playing board game table family fun weekend",
        "statements": [
            "The woman is playing a board game.",
            "The woman is lifting furniture.",
            "She is jogging near a river.",
            "She is organizing files in an office."
        ],
        "answer": "A",
        "rationale": "The woman is engaged in a board game at the table."
    },
    # === A2 Part1 Patterns (91–100 FINAL balanced answers) ===
    {
        "level": "A2",
        "query": "woman typing keyboard office desk coffee notebook work",
        "statements": [
            "She is talking to customers at a store counter.",
            "The woman is typing on a keyboard at her desk.",
            "She is handing out leaflets on the street.",
            "The woman is drinking water on a sofa."
        ],
        "answer": "B",
        "rationale": "The woman is working at her desk and typing on a keyboard."
    },
    {
        "level": "A2",
        "query": "man talking phone office papers folders business call",
        "statements": [
            "The man is jogging outdoors.",
            "He is repairing a bicycle tire.",
            "The man is talking on the phone in the office.",
            "He is cooking dinner in a kitchen."
        ],
        "answer": "C",
        "rationale": "The man is holding a phone to his ear while working at his desk."
    },
    {
        "level": "A2",
        "query": "woman writing notes meeting table documents pens",
        "statements": [
            "She is driving a truck on a highway.",
            "The woman is writing notes during a meeting.",
            "The woman is washing a car.",
            "She is watering flowers in a garden."
        ],
        "answer": "B",
        "rationale": "She is sitting at the meeting table and taking notes."
    },
    {
        "level": "A2",
        "query": "man using photocopier office hallway machine documents",
        "statements": [
            "The man is painting a large wall.",
            "He is sweeping leaves outside.",
            "The man is using a photocopier.",
            "He is playing a guitar on stage."
        ],
        "answer": "C",
        "rationale": "The man is standing by the machine and making copies of documents."
    },
    {
        "level": "A2",
        "query": "woman checking calendar planner workspace schedule",
        "statements": [
            "The woman is climbing a mountain.",
            "The woman is checking a calendar in her planner.",
            "The woman is running a marathon race.",
            "The woman is taking a bath at home."
        ],
        "answer": "B",
        "rationale": "She is reviewing her schedule with a planner open on the desk."
    },
    {
        "level": "A2",
        "query": "group teammates discussing project office table laptops",
        "statements": [
            "The team is exercising in a gym.",
            "The group is taking photos with a celebrity.",
            "The team is discussing a project at a table.",
            "They are resting on a bus."
        ],
        "answer": "C",
        "rationale": "Several people are gathered at a desk discussing work."
    },
    {
        "level": "A2",
        "query": "man drinking coffee break lounge office sofa relaxing",
        "statements": [
            "The man is receiving a medical injection.",
            "He is swimming at a beach.",
            "He is doing laundry at home.",
            "The man is drinking coffee on a sofa during a break."
        ],
        "answer": "D",
        "rationale": "He is relaxing and having coffee in the office lounge."
    },
    {
        "level": "A2",
        "query": "woman using calculator bills budget finance papers",
        "statements": [
            "The woman is lifting heavy furniture.",
            "She is delivering food to tables.",
            "The woman is using a calculator and checking papers.",
            "She is ice skating outdoors."
        ],
        "answer": "C",
        "rationale": "She is working with bills and a calculator at her desk."
    },
    {
        "level": "A2",
        "query": "man presenting chart conference room screen pointer",
        "statements": [
            "The man is fixing a motorcycle.",
            "He is cutting vegetables in a kitchen.",
            "He is presenting a chart in a conference room.",
            "He is throwing a baseball."
        ],
        "answer": "C",
        "rationale": "The man is pointing to a screen and explaining business data."
    },
    {
        "level": "A2",
        "query": "woman handing documents coworker office collaboration",
        "statements": [
            "The woman is combing a dog's fur.",
            "The woman is flying a helicopter.",
            "The woman is handing documents to a coworker.",
            "She is selling vegetables at a market."
        ],
        "answer": "C",
        "rationale": "She is passing papers to someone at the office."
    },
    {
        "level": "A2",
        "query": "man stamping papers reception desk visitor counter",
        "statements": [
            "He is dancing on a stage.",
            "The man is stamping papers at a reception desk.",
            "The man is shaving in a bathroom.",
            "The man is snorkeling underwater."
        ],
        "answer": "B",
        "rationale": "He is working behind a counter with documents in front of him."
    },
    {
        "level": "A2",
        "query": "woman opening laptop cafe working remote coffee shop",
        "statements": [
            "The woman is skiing down a hill.",
            "She is doing yoga in a gym.",
            "She is sweeping a warehouse floor.",
            "The woman is opening a laptop at a cafe."
        ],
        "answer": "D",
        "rationale": "She is beginning work by opening her laptop near a drink."
    },
    {
        "level": "A2",
        "query": "man writing on whiteboard brainstorming office ideas",
        "statements": [
            "The man is karate training.",
            "The man is writing ideas on a whiteboard.",
            "He is drilling a hole in wood.",
            "He is playing a board game with kids."
        ],
        "answer": "B",
        "rationale": "He is standing near a whiteboard and writing for discussion."
    },
    {
        "level": "A2",
        "query": "woman arranging folders office shelf organizing files",
        "statements": [
            "The woman is arranging folders on a shelf.",
            "The woman is climbing a wall with ropes.",
            "She is playing a computer game.",
            "She is planting trees in a field."
        ],
        "answer": "A",
        "rationale": "She is organizing office files neatly on the shelf."
    },
    {
        "level": "A2",
        "query": "man signing contract paper pen handshake business",
        "statements": [
            "He is delivering a speech in a stadium.",
            "The man is signing a contract.",
            "He is repairing a broken lamp.",
            "He is feeding chickens on a farm."
        ],
        "answer": "B",
        "rationale": "The man is holding a pen and writing on an official document."
    },
    {
        "level": "A2",
        "query": "woman checking name tag visitor lobby corporate company",
        "statements": [
            "The woman is checking a name tag in a lobby.",
            "She is washing the windows of a house.",
            "She is hiking through a forest.",
            "The woman is fishing at a lake."
        ],
        "answer": "A",
        "rationale": "She is verifying her visitor name tag in the corporate lobby."
    },
    {
        "level": "A2",
        "query": "man sorting mail envelopes office cubicle desk",
        "statements": [
            "The man is taking a nap in bed.",
            "A man is sorting envelopes and mail.",
            "He is playing tennis on a court.",
            "The man is raking leaves outside."
        ],
        "answer": "B",
        "rationale": "The man is separating envelopes and papers at his desk."
    },
    {
        "level": "A2",
        "query": "woman pointing laptop screen coworker teamwork office",
        "statements": [
            "She is singing into a microphone on stage.",
            "The woman is pointing at something on a laptop screen.",
            "She is watering flowers on the balcony.",
            "She is riding a surfboard."
        ],
        "answer": "B",
        "rationale": "She is showing information on the screen to a coworker."
    },
    {
        "level": "A2",
        "query": "man carrying box storage room archive shelf office",
        "statements": [
            "The man is carrying a box into a storage room.",
            "He is practicing golf on a field.",
            "The man is painting a mountain landscape.",
            "The man is operating a forklift outdoors."
        ],
        "answer": "A",
        "rationale": "The man is holding a box and heading toward the archive shelves."
    },
    {
        "level": "A2",
        "query": "woman drinking tea break office lounge relaxing",
        "statements": [
            "The woman is drinking tea during a break.",
            "The woman is washing her car.",
            "She is swimming in the sea.",
            "The woman is digging holes in a garden."
        ],
        "answer": "A",
        "rationale": "She is relaxing with a cup of tea in the office lounge."
    },

    # --- B1 level 100patterns (standard) ---
    # 1: correct = A
    {
        "level": "B1",
        "query": "office desk laptop coffee",
        "statements": [
            "A laptop is open on the desk.",
            "Some people are standing in a line.",
            "A car is parked on the street.",
            "The room is decorated for a party.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: A laptop is open on the desk. The other options describe different situations that do not match the picture.",
    },
    # 2: correct = A
    {
        "level": "B1",
        "query": "meeting room whiteboard coworkers",
        "statements": [
            "Several people are sitting around a table.",
            "A woman is standing at a bus stop.",
            "Boxes are stacked in a warehouse.",
            "A man is walking a dog in the park.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: several people are sitting around a table in a meeting room. The other options describe unrelated places and activities.",
    },
    # 3: correct = A
    {
        "level": "B1",
        "query": "city street crosswalk people",
        "statements": [
            "People are crossing the street at a crosswalk.",
            "A chef is cooking in a kitchen.",
            "A man is using a copy machine.",
            "Desks are arranged in a classroom.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: people are crossing the street at a crosswalk. The other options mention indoor scenes that do not match the picture.",
    },
    # 4: correct = A
    {
        "level": "B1",
        "query": "airport departure board passengers",
        "statements": [
            "Passengers are looking at an information board.",
            "A gardener is planting flowers.",
            "A truck is being loaded with furniture.",
            "Some books are stacked on a shelf.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: passengers are looking at a departure or information board at an airport. The other options describe different locations and actions.",
    },
    # 5: correct = A
    {
        "level": "B1",
        "query": "warehouse worker forklift boxes",
        "statements": [
            "A worker is moving boxes with a forklift.",
            "A group is eating in a restaurant.",
            "A train is arriving at the station.",
            "A musician is playing on a stage.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: a worker is moving boxes with a forklift in a warehouse. The other options show unrelated situations.",
    },
    # 6: correct = B
    {
        "level": "B1",
        "query": "conference speaker audience presentation",
        "statements": [
            "A man is cooking in a small kitchen.",
            "A presenter is speaking in front of an audience.",
            "Children are playing in a park.",
            "A woman is cleaning a window.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes the scene in the photo: a presenter is speaking in front of an audience at a conference. The other options describe completely different activities.",
    },
    # 7: correct = C
    {
        "level": "B1",
        "query": "supermarket aisle shopping cart",
        "statements": [
            "A man is repairing a bicycle.",
            "People are seated in a movie theater.",
            "A woman is pushing a cart down a store aisle.",
            "A waiter is carrying a tray of food.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes the scene in the photo: a woman is pushing a shopping cart down a supermarket aisle. The other options show unrelated locations.",
    },
    # 8: correct = D
    {
        "level": "B1",
        "query": "train station platform commuters",
        "statements": [
            "A woman is typing on a laptop at a cafe.",
            "Children are drawing on a chalkboard.",
            "A chef is preparing dishes in a kitchen.",
            "People are waiting for a train on a platform.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes the scene in the photo: people are waiting for a train on a platform at a station. The other options show indoor scenes in different places.",
    },
    # 9: correct = A
    {
        "level": "B1",
        "query": "restaurant table waiter menu",
        "statements": [
            "A waiter is taking an order at a table.",
            "A mechanic is working under a car.",
            "An artist is painting in a studio.",
            "A man is jogging in the park.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: a waiter is taking an order at a restaurant table. The other options refer to unrelated jobs and locations.",
    },
    # 10: correct = B
    {
        "level": "B1",
        "query": "classroom students teacher projector",
        "statements": [
            "A woman is shopping at an outdoor market.",
            "Students are listening to a teacher at the front of the room.",
            "Workers are unloading boxes from a truck.",
            "A man is playing the guitar on a stage.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes the scene in the photo: students are listening to a teacher in a classroom. The other options describe different activities outside a classroom.",
    },
    # 11: correct = C
    {
        "level": "B1",
        "query": "construction site workers crane",
        "statements": [
            "Tourists are sitting on a tour bus.",
            "Office workers are talking in a meeting.",
            "Workers are wearing helmets at a construction site.",
            "A woman is swimming in a pool.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes the scene in the photo: workers wearing helmets at a construction site. The other options describe unrelated environments.",
    },
    # 12: correct = D
    {
        "level": "B1",
        "query": "cafe barista counter customers",
        "statements": [
            "A delivery driver is unloading packages.",
            "A doctor is examining a patient.",
            "Shoppers are walking through a mall.",
            "A barista is serving drinks at a counter.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes the scene in the photo: a barista is serving drinks at a café counter. The other options show different professions and places.",
    },
    # 13: correct = A
    {
        "level": "B1",
        "query": "subway train passengers seats",
        "statements": [
            "People are sitting and standing inside a subway train.",
            "A group of people is standing around a barbecue grill.",
            "A woman is arranging flowers in a vase.",
            "A man is painting a wall with a roller.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: passengers sitting and standing inside a subway train. The other options describe unrelated activities.",
    },
    # 14: correct = B
    {
        "level": "B1",
        "query": "hospital hallway doctor nurse",
        "statements": [
            "Parents are watching children on a playground.",
            "A doctor and a nurse are walking down a corridor.",
            "People are checking out at a supermarket register.",
            "A cyclist is riding along a country road.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes the scene in the photo: a doctor and a nurse walking down a hospital corridor. The other options refer to very different scenes.",
    },
    # 15: correct = C
    {
        "level": "B1",
        "query": "library bookshelves reading study",
        "statements": [
            "A chef is cooking in a busy kitchen.",
            "People are exercising in a fitness class.",
            "People are reading at tables between bookshelves.",
            "Travelers are waiting at a boarding gate.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes the scene in the photo: people are reading at tables between bookshelves in a library. The other options show different locations and activities.",
    },
    # 16: correct = D
    {
        "level": "B1",
        "query": "parking lot cars security guard",
        "statements": [
            "A woman is speaking on the phone at her desk.",
            "Children are playing soccer on a field.",
            "A man is choosing fruit in a grocery store.",
            "A security guard is walking through a parking lot.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes the scene in the photo: a security guard walking through a parking lot. The other options describe unrelated scenes.",
    },
    # 17: correct = A
    {
        "level": "B1",
        "query": "kitchen home cooking family",
        "statements": [
            "A woman is cutting vegetables on a kitchen counter.",
            "Tourists are taking pictures in front of a monument.",
            "Workers are sitting around a table in a meeting.",
            "A man is repairing a car in a garage.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: a woman preparing food at a kitchen counter. The other options show different places and actions.",
    },
    # 18: correct = B
    {
        "level": "B1",
        "query": "gym treadmill exercise people",
        "statements": [
            "A woman is reading a book on a sofa.",
            "People are running on treadmills at a gym.",
            "A cashier is scanning items at a register.",
            "A man is painting a landscape outdoors.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes the scene in the photo: people running on treadmills in a gym. The other options show unrelated activities.",
    },
    # 19: correct = C
    {
        "level": "B1",
        "query": "museum gallery painting visitors",
        "statements": [
            "A woman is giving a presentation in an office.",
            "A man is washing a car in a driveway.",
            "Visitors are looking at paintings on the wall.",
            "A family is eating at a dining table.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes the scene in the photo: visitors viewing paintings in a museum gallery. The other options describe different settings.",
    },
    # 20: correct = D
    {
        "level": "B1",
        "query": "hotel lobby receptionist luggage",
        "statements": [
            "A cook is preparing food over a stove.",
            "A woman is folding clothes in a laundry room.",
            "A man is speaking to an audience in a theater.",
            "Guests are standing with luggage near a reception desk.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes the scene in the photo: guests with luggage near a reception desk in a hotel lobby. The other options show different scenes.",
    },
    # 21: correct = A
    {
        "level": "B1",
        "query": "bus stop commuters morning",
        "statements": [
            "People are waiting beside a bus stop sign.",
            "A worker is fixing wires on a ladder.",
            "A woman is cooking in a restaurant kitchen.",
            "Shoppers are paying at a checkout counter.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: people waiting beside a bus stop sign. The other options describe unrelated activities.",
    },
    # 22: correct = B
    {
        "level": "B1",
        "query": "open-plan office coworkers collaboration",
        "statements": [
            "Passengers are standing in a crowded train.",
            "Employees are working together at desks in an open office.",
            "Children are climbing on playground equipment.",
            "A woman is watering plants on a balcony.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes the scene in the photo: employees working together at desks in an open-plan office. The other choices show very different places.",
    },
    # 23: correct = C
    {
        "level": "B1",
        "query": "farm field tractor sunset",
        "statements": [
            "A man is speaking into a microphone at a podium.",
            "People are walking along a city sidewalk.",
            "A tractor is moving across a field at sunset.",
            "A woman is choosing clothes in a store.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes the scene in the photo: a tractor moving across a field at sunset on a farm. The other options present unrelated urban or indoor scenes.",
    },
    # 24: correct = D
    {
        "level": "B1",
        "query": "beach umbrellas vacation people",
        "statements": [
            "A man is driving a truck on a highway.",
            "A woman is typing on a keyboard at her desk.",
            "Shoppers are looking at products on shelves.",
            "People are relaxing under umbrellas on a beach.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes the scene in the photo: people relaxing under umbrellas on a beach. The other options describe different environments.",
    },
    # 25: correct = A
    {
        "level": "B1",
        "query": "city night streetlights traffic",
        "statements": [
            "Cars are driving along a city street at night.",
            "A teacher is handing out papers in a classroom.",
            "A gardener is trimming bushes in a yard.",
            "Shoppers are standing at an outdoor market stall.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes the scene in the photo: cars driving along a city street at night under streetlights. The other options show unrelated scenes in different places.",
    },
    # 26: correct = A
    {
        "level": "B1",
        "query": "office cubicle computer phone",
        "statements": [
            "A woman is talking on the phone at her desk.",
            "A chef is preparing food in a busy kitchen.",
            "Children are lining up outside a classroom.",
            "A man is unloading boxes from a truck."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an office scene where a woman is talking on the phone at her desk. The other options show different locations and activities that do not match the picture."
    },
    # 27: correct = B
    {
        "level": "B1",
        "query": "street market stalls shoppers",
        "statements": [
            "A man is washing a car in a driveway.",
            "People are buying food at outdoor market stalls.",
            "A doctor is speaking with a patient.",
            "A cyclist is resting on a bench."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes shoppers buying food at outdoor stalls in a street market. The other options show unrelated situations such as a driveway, a clinic, or a park."
    },
    # 28: correct = C
    {
        "level": "B1",
        "query": "airport check-in counter travelers",
        "statements": [
            "A teacher is writing on a whiteboard.",
            "A waiter is taking an order outside.",
            "Passengers are checking in at an airport counter.",
            "A farmer is feeding animals in a barn."
        ],
        "answer": "C",
        "rationale": "Option C correctly shows passengers checking in at an airport counter. The other options refer to a classroom, a restaurant terrace, and a barn, which do not fit an airport setting."
    },
    # 29: correct = D
    {
        "level": "B1",
        "query": "city square fountain tourists",
        "statements": [
            "A nurse is taking a patient’s temperature.",
            "A mechanic is working under a car.",
            "An artist is painting in a studio.",
            "Tourists are taking photos near a fountain."
        ],
        "answer": "D",
        "rationale": "Option D correctly describes tourists taking photos by a fountain in a city square. The other options show indoor work scenes that do not match the outdoor tourist location."
    },
    # 30: correct = A
    {
        "level": "B1",
        "query": "factory assembly line workers",
        "statements": [
            "Workers are standing along an assembly line.",
            "A student is reading alone in a classroom.",
            "A family is eating dinner at home.",
            "A man is fishing on a lake."
        ],
        "answer": "A",
        "rationale": "Option A correctly shows workers standing by an assembly line in a factory. The other options describe home or leisure activities that are unrelated to a factory floor."
    },
    # 31: correct = B
    {
        "level": "B1",
        "query": "suburban house front yard evening",
        "statements": [
            "A group of people is waiting at a bus stop.",
            "A man is watering plants in front of a house.",
            "Shoppers are riding an escalator in a mall.",
            "Office workers are sitting in a meeting room."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes a man watering plants in the front yard of a house. The other options show very different locations such as a bus stop, a mall, or a meeting room."
    },
    # 32: correct = C
    {
        "level": "B1",
        "query": "university campus students walking",
        "statements": [
            "A pilot is sitting in the cockpit of an airplane.",
            "A cashier is scanning items at a checkout.",
            "Students are walking between buildings on a campus.",
            "A child is playing with a toy car on the floor."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes students walking between buildings on a university campus. The other options show unrelated workplaces or a child playing indoors."
    },
    # 33: correct = D
    {
        "level": "B1",
        "query": "harbor boats dock sunrise",
        "statements": [
            "A dentist is examining a patient’s teeth.",
            "Two runners are competing in a race.",
            "People are shopping for clothes in a store.",
            "Boats are tied to a dock in a harbor."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows boats tied to a dock in a harbor. The other options describe indoor scenes or sporting events that do not match the harbor setting."
    },
    # 34: correct = A
    {
        "level": "B1",
        "query": "train interior passengers luggage",
        "statements": [
            "Passengers are sitting with luggage inside a train.",
            "A cook is chopping vegetables in a kitchen.",
            "A scientist is giving a lecture in an auditorium.",
            "A boy is flying a kite in a field."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes passengers seated with luggage inside a train carriage. The other options show completely different places such as a kitchen, an auditorium, or a field."
    },
    # 35: correct = B
    {
        "level": "B1",
        "query": "shopping mall escalator people",
        "statements": [
            "A lifeguard is watching swimmers at a pool.",
            "Shoppers are riding up an escalator.",
            "A farmer is driving a truck through a field.",
            "Students are taking a test in a classroom."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows shoppers riding an escalator in a shopping mall. The other options describe situations at a pool, on a farm, or in a classroom."
    },
    # 36: correct = C
    {
        "level": "B1",
        "query": "kitchen restaurant chef plating",
        "statements": [
            "A woman is cleaning a window.",
            "A musician is tuning a guitar onstage.",
            "A chef is arranging food on plates.",
            "A man is filling his car with gasoline."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a restaurant kitchen where a chef is plating dishes. The other options show unrelated activities like cleaning, tuning an instrument, or pumping gas."
    },
    # 37: correct = D
    {
        "level": "B1",
        "query": "office reception area waiting chairs",
        "statements": [
            "A child is painting at an easel.",
            "A cyclist is riding down a mountain trail.",
            "A fisherman is standing in a river.",
            "Several people are sitting in chairs in a reception area."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows several people seated in an office reception area. The other options describe outdoor leisure activities that do not match a reception space."
    },
    # 38: correct = A
    {
        "level": "B1",
        "query": "street cafe outdoor tables customers",
        "statements": [
            "People are eating at tables outside a café.",
            "A mail carrier is walking up some stairs.",
            "A doctor is writing in a medical chart.",
            "A construction worker is climbing a ladder."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes customers eating at outdoor tables at a café. The other options show different jobs in other locations."
    },
    # 39: correct = B
    {
        "level": "B1",
        "query": "office meeting video conference screen",
        "statements": [
            "A man is jogging along a beach at sunset.",
            "Coworkers are watching colleagues on a video screen.",
            "A woman is buying a ticket at a machine.",
            "A child is sliding down a playground slide."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows coworkers watching colleagues on a video conference screen. The other options depict very different activities and settings."
    },
    # 40: correct = C
    {
        "level": "B1",
        "query": "warehouse shelves inventory worker",
        "statements": [
            "A woman is playing the piano on a stage.",
            "A barber is cutting a customer’s hair.",
            "A worker is checking items on warehouse shelves.",
            "A group is hiking up a rocky hill."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a worker inspecting items on warehouse shelves. The other options show unrelated professions and outdoor activities."
    },
    # 41: correct = D
    {
        "level": "B1",
        "query": "city bus interior commuters morning",
        "statements": [
            "A chef is stirring a pot on a stove.",
            "A pilot is speaking with an airport staff member.",
            "Two children are building a snowman.",
            "Passengers are sitting and standing inside a city bus."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows commuters seated and standing inside a city bus. The other options describe activities in a kitchen, an airport, or snowy outdoors."
    },
    # 42: correct = A
    {
        "level": "B1",
        "query": "museum dinosaur skeleton visitors",
        "statements": [
            "Visitors are looking up at a dinosaur skeleton.",
            "A man is talking on a mobile phone in an office.",
            "A woman is jogging on a treadmill.",
            "A baker is placing bread into an oven."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes visitors viewing a dinosaur skeleton in a museum. The other options show ordinary work or exercise scenes that do not fit a museum."
    },
    # 43: correct = B
    {
        "level": "B1",
        "query": "airport security checkpoint line",
        "statements": [
            "A gardener is trimming a hedge.",
            "Passengers are waiting in line at a security checkpoint.",
            "A mechanic is changing a tire.",
            "Students are eating lunch outdoors."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows passengers waiting in line at an airport security checkpoint. The other options describe unrelated places like a garden, a garage, or a schoolyard."
    },
    # 44: correct = C
    {
        "level": "B1",
        "query": "classroom science lab students experiment",
        "statements": [
            "A woman is serving drinks at a bar.",
            "A family is checking into a hotel.",
            "Students are wearing goggles and doing an experiment.",
            "An artist is sketching in a notebook."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes students in a science lab wearing goggles and doing an experiment. The other options refer to a bar, a hotel, or an artist at work."
    },
    # 45: correct = D
    {
        "level": "B1",
        "query": "train platform rainy day umbrellas",
        "statements": [
            "A nurse is pushing a wheelchair down a hallway.",
            "A pilot is boarding an airplane.",
            "A child is blowing out candles on a cake.",
            "People holding umbrellas are waiting on a platform."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows people with umbrellas waiting on a train platform on a rainy day. The other options describe different indoor events and locations."
    },
    # 46: correct = A
    {
        "level": "B1",
        "query": "office open laptop notebook glasses",
        "statements": [
            "An open laptop and a notebook are on a desk.",
            "A group of tourists is walking up some stairs.",
            "A chef is placing plates on a counter.",
            "A runner is stretching near a track."
        ],
        "answer": "A",
        "rationale": "Option A correctly shows an office desk with an open laptop and a notebook. The other options describe people engaged in unrelated activities elsewhere."
    },
    # 47: correct = B
    {
        "level": "B1",
        "query": "coffee shop barista making drink",
        "statements": [
            "A man is reading a newspaper on a train.",
            "A barista is preparing a drink with an espresso machine.",
            "Children are playing on a swing set.",
            "A doctor is speaking at a conference."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes a barista preparing a drink with an espresso machine in a coffee shop. The other options show different places and activities."
    },
    # 48: correct = C
    {
        "level": "B1",
        "query": "city crosswalk traffic lights pedestrians",
        "statements": [
            "A teacher is helping a student at a desk.",
            "A janitor is cleaning a restroom.",
            "Pedestrians are crossing at a crosswalk with traffic lights.",
            "A farmer is picking fruit from a tree."
        ],
        "answer": "C",
        "rationale": "Option C correctly shows pedestrians crossing at a city crosswalk controlled by traffic lights. The other options are indoor or rural scenes unrelated to a city intersection."
    },
    # 49: correct = D
    {
        "level": "B1",
        "query": "restaurant kitchen waiters plates",
        "statements": [
            "A woman is choosing flowers at a shop.",
            "A man is typing on a computer keyboard.",
            "A child is riding a scooter on a sidewalk.",
            "Waiters are carrying plates out of a kitchen."
        ],
        "answer": "D",
        "rationale": "Option D correctly describes waiters carrying plates out of a restaurant kitchen. The other options show completely different activities in other locations."
    },
    # 50: correct = A
    {
        "level": "B1",
        "query": "construction crane city building site",
        "statements": [
            "A crane is lifting materials at a building site.",
            "A doctor is checking a patient’s blood pressure.",
            "People are sitting around a dinner table at home.",
            "Shoppers are paying at a supermarket register."
        ],
        "answer": "A",
        "rationale": "Option A correctly shows a crane lifting materials at a city construction site. The other options describe indoor settings that do not match a building site."
    },
    # 51: correct = B
    {
        "level": "B1",
        "query": "park bench lunchtime office workers",
        "statements": [
            "A musician is playing drums in a studio.",
            "Office workers are eating lunch on a park bench.",
            "A diver is swimming under water.",
            "A clerk is putting files into a cabinet."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes office workers sitting on a park bench having lunch. The other options show unrelated scenes in a studio, underwater, or in an office."
    },
    # 52: correct = C
    {
        "level": "B1",
        "query": "street festival lanterns crowd night",
        "statements": [
            "A nurse is washing her hands at a sink.",
            "A man is sitting alone in an empty theater.",
            "People are walking under lanterns at a night festival.",
            "A gardener is planting trees in a yard."
        ],
        "answer": "C",
        "rationale": "Option C correctly shows people walking under lanterns at a night festival. The other options describe indoor or daytime scenes unrelated to a street festival."
    },
    # 53: correct = D
    {
        "level": "B1",
        "query": "shopping street souvenir shops tourists",
        "statements": [
            "A student is writing in a notebook at a desk.",
            "A carpenter is cutting wood with a saw.",
            "An athlete is lifting weights in a gym.",
            "Tourists are browsing goods on a shopping street."
        ],
        "answer": "D",
        "rationale": "Option D correctly describes tourists browsing goods on a shopping street with souvenir shops. The other options show study, construction, or training scenes."
    },
    # 54: correct = A
    {
        "level": "B1",
        "query": "meeting room projector presentation slide",
        "statements": [
            "A presenter is pointing at a slide on a screen.",
            "A security guard is standing at a gate.",
            "A chef is baking bread in an oven.",
            "A woman is pushing a stroller down a sidewalk."
        ],
        "answer": "A",
        "rationale": "Option A correctly shows a presenter pointing at a slide projected on a screen in a meeting room. The other options describe different roles and locations."
    },
    # 55: correct = B
    {
        "level": "B1",
        "query": "subway station ticket gate commuters",
        "statements": [
            "A child is drawing with crayons on paper.",
            "Passengers are passing through ticket gates.",
            "A swimmer is diving into a pool.",
            "A farmer is feeding chickens in a yard."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes commuters passing through ticket gates in a subway station. The other options show unrelated activities in other environments."
    },
    # 56: correct = C
    {
        "level": "B1",
        "query": "office break room fridge microwave coworkers",
        "statements": [
            "A mechanic is opening the hood of a car.",
            "A woman is giving a speech at a podium.",
            "Employees are standing and talking in a break room.",
            "A dancer is performing onstage."
        ],
        "answer": "C",
        "rationale": "Option C correctly shows coworkers standing and talking together in an office break room. The other options take place in very different settings."
    },
    # 57: correct = D
    {
        "level": "B1",
        "query": "downtown intersection cars buses",
        "statements": [
            "A doctor is sitting at a desk with a patient file.",
            "A man is trimming a tree with a ladder.",
            "A child is playing with building blocks.",
            "Cars and buses are waiting at a busy intersection."
        ],
        "answer": "D",
        "rationale": "Option D correctly describes cars and buses waiting at a busy downtown intersection. The other options refer to indoor work or home activities."
    },
    # 58: correct = A
    {
        "level": "B1",
        "query": "hotel hallway room doors carpet",
        "statements": [
            "A long hallway with room doors is shown.",
            "A group of students is playing basketball.",
            "A mechanic is changing a car tire.",
            "A singer is performing in front of a microphone."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes a long hotel hallway lined with room doors. The other options show unrelated activities that do not match the interior corridor."
    },
    # 59: correct = B
    {
        "level": "B1",
        "query": "office printer copier area employee",
        "statements": [
            "A waiter is setting tables in a restaurant.",
            "An employee is standing next to a large printer.",
            "A surfer is walking toward the ocean.",
            "A nurse is holding a clipboard in a hospital room."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows an employee standing beside a large office printer or copier. The other options take place in a restaurant, on a beach, or in a hospital."
    },
    # 60: correct = C
    {
        "level": "B1",
        "query": "university lecture hall students listening",
        "statements": [
            "A family is sitting on a sofa watching TV.",
            "A baker is decorating a cake.",
            "Students are seated in a large lecture hall.",
            "A child is jumping rope in a playground."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes students seated in a large university lecture hall. The other options show home, work, or playground scenes."
    },
    # 61: correct = D
    {
        "level": "B1",
        "query": "parking garage cars levels ramp",
        "statements": [
            "A chef is slicing bread on a cutting board.",
            "A teacher is handing out assignments.",
            "A man is fishing from a small boat.",
            "Cars are parked inside a multi-level garage."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows cars parked in a multi-level parking garage. The other options are unrelated scenes involving teaching, cooking, or fishing."
    },
    # 62: correct = A
    {
        "level": "B1",
        "query": "train dining car tables passengers",
        "statements": [
            "Passengers are eating at tables on a train.",
            "A dentist is adjusting a patient’s chair.",
            "A gardener is raking leaves into a pile.",
            "A runner is tying his shoes before a race."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes passengers eating at tables in a train dining car. The other options occur in a clinic, a yard, or at a running track."
    },
    # 63: correct = B
    {
        "level": "B1",
        "query": "office window city view desk",
        "statements": [
            "A bus driver is talking to a passenger.",
            "A desk is placed by a window with a city view.",
            "Children are running across a field.",
            "An orchestra is performing on a stage."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows an office desk positioned by a window overlooking the city. The other options show a bus, a field, or a concert hall."
    },
    # 64: correct = C
    {
        "level": "B1",
        "query": "street food truck customers queue",
        "statements": [
            "A woman is typing on a laptop in bed.",
            "An engineer is inspecting a machine.",
            "People are lining up in front of a food truck.",
            "A boy is kicking a soccer ball."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes customers standing in a line in front of a street food truck. The other options show unrelated indoor or sports scenes."
    },
    # 65: correct = D
    {
        "level": "B1",
        "query": "airport baggage claim carousel passengers",
        "statements": [
            "A barista is wiping a counter in a café.",
            "A child is stacking blocks on a table.",
            "A doctor is reading an X-ray image.",
            "Passengers are waiting around a baggage carousel."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows passengers standing around a baggage carousel at an airport. The other options describe entirely different locations and activities."
    },
    # 66: correct = A
    {
        "level": "B1",
        "query": "office shared workspace laptops",
        "statements": [
            "Several people are working on laptops at a shared table.",
            "A woman is crossing a river on stepping stones.",
            "A chef is tasting soup with a spoon.",
            "A cyclist is repairing a flat tire."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes several people working on laptops at a shared workspace table. The other options are unrelated outdoor or kitchen scenes."
    },
    # 67: correct = B
    {
        "level": "B1",
        "query": "cafe reading corner armchairs books",
        "statements": [
            "A pilot is standing beside an airplane.",
            "People are sitting in armchairs reading books.",
            "A child is playing with a toy train.",
            "A construction worker is wearing a hard hat."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows people sitting in comfortable armchairs reading books in a café-style reading corner. The other options show unrelated people and places."
    },
    # 68: correct = C
    {
        "level": "B1",
        "query": "tram stop city center passengers waiting",
        "statements": [
            "A woman is cooking soup on a stove.",
            "A cleaner is mopping a floor.",
            "People are waiting at a tram stop in the city center.",
            "A teacher is speaking to a parent."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes people waiting at a tram stop in the city center. The other options describe indoor activities that do not match a public transport stop."
    },
    # 69: correct = D
    {
        "level": "B1",
        "query": "conference registration desk name tags",
        "statements": [
            "A swimmer is standing on the edge of a pool.",
            "A tourist is taking a picture of a mountain.",
            "A baker is putting bread on a shelf.",
            "People are checking in at a conference registration desk."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows people checking in at a conference registration desk where name tags are likely prepared. The other options are unrelated outdoor or shop scenes."
    },
    # 70: correct = A
    {
        "level": "B1",
        "query": "office phone conference speaker device",
        "statements": [
            "A small speakerphone is on the meeting table.",
            "A woman is shopping for vegetables at a market.",
            "A boy is riding a bicycle on a sidewalk.",
            "A mechanic is lying under a car."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes a meeting table with a small conference speakerphone. The other options show people in very different places and activities."
    },
    # 71: correct = B
    {
        "level": "B1",
        "query": "food court tables trays diners",
        "statements": [
            "A driver is filling a car with fuel at a gas station.",
            "People are eating at tables in a food court.",
            "A scientist is writing formulas on a board.",
            "A gardener is watering flowers in a park."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows people eating at tables in a shopping mall food court. The other options refer to gas stations, laboratories, or parks."
    },
    # 72: correct = C
    {
        "level": "B1",
        "query": "office corridor glass walls people walking",
        "statements": [
            "A woman is holding a baby in her arms.",
            "A man is washing dishes in a sink.",
            "People are walking down a corridor with glass walls.",
            "A child is coloring in a picture book."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes people walking along an office corridor with glass walls. The other options show home or family scenes that do not match an office hallway."
    },
    # 73: correct = D
    {
        "level": "B1",
        "query": "railway station ticket machines travelers",
        "statements": [
            "A musician is performing in a subway tunnel.",
            "A chef is washing vegetables in a sink.",
            "A nurse is arranging medicine on a cart.",
            "People are standing in front of ticket machines at a station."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows travelers standing in front of ticket machines at a railway station. The other options describe unrelated jobs and locations."
    },
    # 74: correct = A
    {
        "level": "B1",
        "query": "office cafeteria salad bar employees",
        "statements": [
            "Employees are choosing food at a salad bar.",
            "A runner is drinking water at a fountain.",
            "A student is sleeping at a desk.",
            "A mechanic is closing the hood of a car."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes employees selecting food at a salad bar in an office cafeteria. The other options are different places and activities."
    },
    # 75: correct = B
    {
        "level": "B1",
        "query": "city park jogging path morning",
        "statements": [
            "A dentist is talking to a patient in a clinic.",
            "People are jogging along a path in a park.",
            "A chef is flipping food in a pan.",
            "A shopper is paying for groceries."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows people jogging along a path in a park, likely in the morning. The other options refer to work scenes in a clinic, kitchen, or store."
    },
    # 76: correct = C
    {
        "level": "B1",
        "query": "roof terrace office workers break",
        "statements": [
            "A driver is washing a bus at a depot.",
            "A teacher is erasing writing from a board.",
            "People are relaxing on chairs on a rooftop terrace.",
            "A child is rolling a ball across the floor."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes people relaxing on chairs on a rooftop terrace during a break. The other options show completely different activities and places."
    },
    # 77: correct = D
    {
        "level": "B1",
        "query": "harbor ferry terminal passengers boarding",
        "statements": [
            "A woman is folding clothes on a bed.",
            "A gardener is planting flowers along a path.",
            "A nurse is checking a monitor near a bed.",
            "Passengers are walking onto a ferry at a terminal."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows passengers boarding a ferry at a harbor terminal. The other options describe indoor or garden scenes unrelated to a ferry."
    },
    # 78: correct = A
    {
        "level": "B1",
        "query": "office document scanner paperwork",
        "statements": [
            "A stack of papers is being scanned by a machine.",
            "A boy is throwing a ball to a friend.",
            "A woman is brushing a dog’s fur.",
            "A chef is carrying a tray of desserts."
        ],
        "answer": "A",
        "rationale": "Option A correctly shows a stack of documents being scanned by an office machine. The other options describe unrelated personal or kitchen activities."
    },
    # 79: correct = B
    {
        "level": "B1",
        "query": "suburban train crossing barrier road",
        "statements": [
            "A pharmacist is handing medicine to a customer.",
            "A train is passing a road with lowered barriers.",
            "A librarian is arranging books on a shelf.",
            "A dancer is stretching on the floor."
        ],
        "answer": "B",
        "rationale": "Option B correctly describes a train passing through a crossing where the barriers are down. The other options show different jobs indoors."
    },
    # 80: correct = C
    {
        "level": "B1",
        "query": "town square clock tower pedestrians",
        "statements": [
            "A baker is kneading dough on a table.",
            "A crew is filming a scene with cameras.",
            "People are walking near a clock tower in a town square.",
            "A child is playing a video game at home."
        ],
        "answer": "C",
        "rationale": "Option C correctly shows people walking near a clock tower in a town square. The other options describe baking, filming, or playing at home."
    },
    # 81: correct = D
    {
        "level": "B1",
        "query": "bus interior night dim lights passengers",
        "statements": [
            "A cook is grilling meat on a barbecue.",
            "A student is answering a question in class.",
            "A mechanic is opening a toolbox.",
            "Passengers are sitting quietly on a dimly lit bus."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows passengers sitting quietly on a dimly lit bus at night. The other options describe unrelated daytime or indoor activities."
    },
    # 82: correct = A
    {
        "level": "B1",
        "query": "office filing cabinets documents",
        "statements": [
            "A woman is pulling a folder from a filing cabinet.",
            "A runner is jumping over a hurdle.",
            "A baker is selling bread at a counter.",
            "A man is locking a bicycle to a rack."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an office worker taking a folder from a filing cabinet. The other options show sports, sales, or outdoor scenes."
    },
    # 83: correct = B
    {
        "level": "B1",
        "query": "subway entrance stairs commuters",
        "statements": [
            "A teacher is sitting at a piano with a student.",
            "People are going down stairs into a subway entrance.",
            "A doctor is washing hands at a sink.",
            "A family is playing a board game at a table."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows commuters going down stairs into a subway entrance. The other options take place in a music room, a clinic, or a home."
    },
    # 84: correct = C
    {
        "level": "B1",
        "query": "office desk dual monitors coding",
        "statements": [
            "A nurse is talking to a patient’s family.",
            "A chef is pouring sauce onto a plate.",
            "A person is working at a desk with two computer monitors.",
            "A child is building a tower with blocks."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes someone working at a desk with dual computer monitors in an office. The other options describe unrelated professions or play."
    },
    # 85: correct = D
    {
        "level": "B1",
        "query": "city tram interior passengers seated",
        "statements": [
            "A mechanic is looking under the hood of a truck.",
            "A woman is cleaning the windows of a house.",
            "A teacher is reading a book aloud to children.",
            "Passengers are seated inside a city tram."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows passengers seated inside a city tram. The other options show domestic or work scenes not related to public transport."
    },
    # 86: correct = A
    {
        "level": "B1",
        "query": "airport gate waiting area chairs",
        "statements": [
            "Travelers are sitting in rows of chairs at an airport gate.",
            "A gardener is trimming a small tree.",
            "A man is pushing a wheelbarrow full of bricks.",
            "A shopper is comparing prices on two products."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes travelers sitting in rows of chairs at an airport gate. The other options depict gardening, construction, or shopping activities."
    },
    # 87: correct = B
    {
        "level": "B1",
        "query": "city river bridge pedestrians sunset",
        "statements": [
            "A child is painting pictures at a kitchen table.",
            "People are walking across a bridge over a river at sunset.",
            "A chef is placing dishes on a shelf.",
            "A nurse is writing on a clipboard."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows people walking across a bridge over a river at sunset in a city. The other options are indoor work or home scenes."
    },
    # 88: correct = C
    {
        "level": "B1",
        "query": "office supply room shelves boxes",
        "statements": [
            "A singer is performing into a microphone.",
            "A cyclist is racing on a road.",
            "Shelves filled with office supplies line the walls.",
            "A family is sitting around a campfire."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes an office supply room with shelves full of supplies. The other options show performances, sports, or camping scenes."
    },
    # 89: correct = D
    {
        "level": "B1",
        "query": "shopping mall information desk map",
        "statements": [
            "A child is feeding pigeons in a plaza.",
            "A teacher is correcting papers at a desk.",
            "A mechanic is using a wrench on a wheel.",
            "A shopper is asking for directions at an information desk."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows a shopper asking for directions at a mall information desk. The other options depict unrelated outdoor or work situations."
    },
    # 90: correct = A
    {
        "level": "B1",
        "query": "office boardroom empty chairs",
        "statements": [
            "An empty meeting room is set up with chairs around a table.",
            "A boy is throwing stones into a lake.",
            "A cook is frosting a cake.",
            "A gardener is digging a hole in the ground."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an empty boardroom prepared for a meeting, with chairs around a table. The other options show outdoor or kitchen scenes."
    },
    # 91: correct = B
    {
        "level": "B1",
        "query": "city bike rack bicycles parked",
        "statements": [
            "A doctor is talking on the phone in a hallway.",
            "Several bicycles are locked to a bike rack on the sidewalk.",
            "A chef is writing a menu on a board.",
            "A clerk is counting coins at a counter."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows several bicycles locked to a bike rack on a city sidewalk. The other options show indoor work scenes unrelated to bicycles."
    },
    # 92: correct = C
    {
        "level": "B1",
        "query": "office lobby revolving door people entering",
        "statements": [
            "A child is crouching beside a dog.",
            "A woman is washing dishes in a sink.",
            "People are walking through a revolving door into a building.",
            "A man is tying a rope around a package."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes people entering a building through a revolving door in an office lobby. The other options show unrelated domestic or outdoor activities."
    },
    # 93: correct = D
    {
        "level": "B1",
        "query": "train sleeper cabin bunk beds",
        "statements": [
            "A group of students is standing at a bus stop.",
            "A nurse is pushing a medicine cart down a hall.",
            "A baker is opening the door of an oven.",
            "Bunk beds are arranged in a small train compartment."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows bunk beds arranged in a small sleeper cabin on a train. The other options describe a bus stop, hospital, or bakery."
    },
    # 94: correct = A
    {
        "level": "B1",
        "query": "office desk calendar pen smartphone",
        "statements": [
            "A desk has a calendar, a pen, and a smartphone on it.",
            "A waiter is carrying drinks on a tray.",
            "A child is drawing on the floor with chalk.",
            "A runner is crossing a finish line with arms raised."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an office desk with a calendar, pen, and smartphone on it. The other options show unrelated activities involving people."
    },
    # 95: correct = B
    {
        "level": "B1",
        "query": "city sidewalk cafe umbrellas pedestrians",
        "statements": [
            "A pilot is walking through an airport terminal.",
            "People are passing a sidewalk café with open umbrellas.",
            "A teacher is handing a book to a student.",
            "A mechanic is wiping grease from his hands."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows pedestrians passing a sidewalk café with open umbrellas. The other options depict indoor professional scenes."
    },
    # 96: correct = C
    {
        "level": "B1",
        "query": "office mailroom packages sorting",
        "statements": [
            "A boy is putting on a backpack near a door.",
            "A woman is sweeping leaves off a sidewalk.",
            "An employee is sorting packages in a mailroom.",
            "A chef is peeling potatoes at a counter."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes an employee sorting packages in an office mailroom. The other options are domestic or street scenes unrelated to a mailroom."
    },
    # 97: correct = D
    {
        "level": "B1",
        "query": "tram stop shelter timetable commuters",
        "statements": [
            "A child is spinning on a playground ride.",
            "A farmer is driving a tractor across a field.",
            "A singer is practicing with a band.",
            "People are standing under a shelter reading a tram timetable."
        ],
        "answer": "D",
        "rationale": "Option D correctly shows commuters standing under a shelter and reading a tram timetable. The other options describe unrelated farm, music, or playground scenes."
    },
    # 98: correct = A
    {
        "level": "B1",
        "query": "office desk paperwork coffee mug",
        "statements": [
            "Papers and a coffee mug are scattered on a desk.",
            "A cyclist is riding along a country road.",
            "A doctor is listening to a patient’s chest.",
            "A child is splashing in a puddle."
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an office desk covered with paperwork and a coffee mug. The other options show outdoor or medical situations."
    },
    # 99: correct = B
    {
        "level": "B1",
        "query": "airport arrivals board families greeting",
        "statements": [
            "A construction worker is carrying wooden boards.",
            "People are greeting arriving passengers near an information board.",
            "A scientist is holding a test tube in a lab.",
            "A waiter is wiping crumbs off a table."
        ],
        "answer": "B",
        "rationale": "Option B correctly shows people greeting arriving passengers near an arrivals or information board at the airport. The other options depict unrelated jobs."
    },
    # 100: correct = C
    {
        "level": "B1",
        "query": "office night overtime single worker",
        "statements": [
            "A bus driver is waving at people on the street.",
            "A shop clerk is closing a rolling door.",
            "A lone worker is sitting at a desk in a dark office.",
            "A gardener is watering plants in bright sunlight."
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a single worker sitting at a desk in a dark office, suggesting overtime at night. The other options show very different outdoor or shop scenes."
    },

    # --- B2 level 30patterns (more challenging) ---
    # 1: correct = A (B2)
    {
        "level": "B2",
        "query": "office video conference multiple screens",
        "statements": [
            "Coworkers are taking part in a video conference on several large screens.",
            "A chef is arranging desserts in a display case.",
            "Travelers are waiting in line at a ticket counter.",
            "Students are standing around a lab table.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an office scene where coworkers are engaged in a multi-screen video conference. The other options show food service, travel, or classroom situations."
    },
    # 2: correct = B (B2)
    {
        "level": "B2",
        "query": "rooftop garden office workers informal meeting",
        "statements": [
            "A technician is repairing cables inside a server room.",
            "Office workers are discussing something in a rooftop garden.",
            "Passengers are lining up at a bus stop.",
            "A family is unpacking boxes in a living room.",
        ],
        "answer": "B",
        "rationale": "Option B correctly shows office workers having an informal meeting in a rooftop garden. The other options depict a server room, public transport, or a home interior."
    },
    # 3: correct = C (B2)
    {
        "level": "B2",
        "query": "control room monitors operators headsets",
        "statements": [
            "A doctor is talking with a patient in an examination room.",
            "Shoppers are looking at fruit in an outdoor market.",
            "Operators are watching several monitors while wearing headsets.",
            "Tourists are walking across a small bridge in a park.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a control room where operators observe multiple screens with headsets on. The other options show completely different settings."
    },
    # 4: correct = D (B2)
    {
        "level": "B2",
        "query": "design studio creative team sketches laptops",
        "statements": [
            "A gardener is collecting leaves with a rake.",
            "A mechanic is tightening bolts on a wheel.",
            "A conductor is standing in front of an orchestra.",
            "Designers are reviewing sketches and working on laptops at a large table.",
        ],
        "answer": "D",
        "rationale": "Option D correctly shows a creative team in a design studio reviewing sketches and using laptops. The other options describe outdoor work, repair work, or musical performance."
    },
    # 5: correct = A (B2)
    {
        "level": "B2",
        "query": "airport business lounge laptops refreshments",
        "statements": [
            "Passengers are sitting in a quiet lounge using laptops and drinking refreshments.",
            "A waiter is carrying plates across a busy dining room.",
            "A nurse is taking a patient’s blood pressure.",
            "Joggers are stretching beside a running track.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes business travelers in an airport lounge using laptops and having drinks. The other options show a restaurant, a clinic, or an outdoor sports facility."
    },
    # 6: correct = B (B2)
    {
        "level": "B2",
        "query": "manufacturing plant safety vests assembly line",
        "statements": [
            "A chef is decorating a cake with frosting.",
            "Workers wearing safety vests are standing along an automated assembly line.",
            "A teacher is handing a book to a student.",
            "A musician is tuning a guitar on stage.",
        ],
        "answer": "B",
        "rationale": "Option B correctly shows factory workers in safety vests positioned along an assembly line. The other options present unrelated indoor scenes in different professions."
    },
    # 7: correct = C (B2)
    {
        "level": "B2",
        "query": "research lab microscopes scientists safety goggles",
        "statements": [
            "Commuters are crossing a busy street under traffic lights.",
            "A receptionist is answering a phone at a front desk.",
            "Scientists wearing safety goggles are working with microscopes on a bench.",
            "A family is taking photos in front of a fountain.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a research lab where scientists in goggles are using microscopes. The other options focus on traffic, reception work, or sightseeing."
    },
    # 8: correct = D (B2)
    {
        "level": "B2",
        "query": "logistics warehouse conveyor belts scanning devices",
        "statements": [
            "A barista is pouring coffee into a cup.",
            "A speaker is writing notes on a whiteboard.",
            "Tourists are examining a city map on a wall.",
            "Workers are loading boxes onto conveyor belts and using handheld scanners.",
        ],
        "answer": "D",
        "rationale": "Option D correctly shows a logistics warehouse with conveyor belts and scanning devices. The other options show a café, an office presentation, or tourism."
    },
    # 9: correct = A (B2)
    {
        "level": "B2",
        "query": "conference hall simultaneous interpretation booths",
        "statements": [
            "Interpreters are sitting inside glass booths overlooking a conference hall.",
            "Cyclists are racing around a track outdoors.",
            "A chef is chopping vegetables on a cutting board.",
            "Students are lined up at a cafeteria counter.",
        ],
        "answer": "A",
        "rationale": "Option A correctly depicts simultaneous interpreters in glass booths facing a conference hall. The other options involve sports, cooking, or school dining areas."
    },
    # 10: correct = B (B2)
    {
        "level": "B2",
        "query": "hotel conference reception check-in counters badges",
        "statements": [
            "A mechanic is changing a tire inside a garage.",
            "Attendees are receiving name badges at a conference check-in counter in a hotel lobby.",
            "Children are building sandcastles on a beach.",
            "A librarian is shelving books in a quiet aisle.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes event attendees checking in and getting badges at a hotel conference desk. The other options describe very different locations."
    },
    # 11: correct = C (B2)
    {
        "level": "B2",
        "query": "call center open floor headsets computer monitors",
        "statements": [
            "A dentist is talking to a patient in a chair.",
            "A gardener is trimming bushes along a path.",
            "Agents wearing headsets are seated in rows at computer monitors.",
            "A chef is sliding a tray into an oven.",
        ],
        "answer": "C",
        "rationale": "Option C correctly shows a call center with agents wearing headsets at computer stations. The other options show medical, gardening, or kitchen activities."
    },
    # 12: correct = D (B2)
    {
        "level": "B2",
        "query": "business school lecture case study discussion",
        "statements": [
            "A pilot is walking across the airport apron toward an aircraft.",
            "A cashier is scanning items for a customer.",
            "A family is waiting for a bus at a shelter.",
            "Students in suits are discussing a case study around a horseshoe-shaped table.",
        ],
        "answer": "D",
        "rationale": "Option D correctly depicts business students in a case-study style classroom. The other options relate to aviation, retail, or public transport."
    },
    # 13: correct = A (B2)
    {
        "level": "B2",
        "query": "open office stand up meeting whiteboard sticky notes",
        "statements": [
            "Team members are standing around a whiteboard covered with sticky notes.",
            "A passenger is looking out the window of a train.",
            "A waiter is polishing glasses behind a counter.",
            "A nurse is adjusting a monitor next to a bed.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes an agile stand-up meeting with sticky notes on a whiteboard. The other options refer to travel, hospitality, or healthcare."
    },
    # 14: correct = B (B2)
    {
        "level": "B2",
        "query": "airport control tower controllers radar screens",
        "statements": [
            "A tour guide is speaking to a group outside a museum.",
            "Air traffic controllers are monitoring radar screens inside a control tower.",
            "Office workers are eating lunch in a cafeteria.",
            "Shoppers are choosing fruit at an indoor market.",
        ],
        "answer": "B",
        "rationale": "Option B correctly shows air traffic controllers watching radar displays in a tower. The other options show unrelated activities."
    },
    # 15: correct = C (B2)
    {
        "level": "B2",
        "query": "pharmacy consultation desk pharmacist customer prescription",
        "statements": [
            "A bus driver is checking the side mirror before leaving a stop.",
            "A group of tourists is boarding a sightseeing boat.",
            "A pharmacist is reviewing a prescription with a customer at a counter.",
            "Office workers are waiting at an elevator bank.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a pharmacist consulting with a customer about a prescription. The other statements describe transportation or office waiting areas."
    },
    # 16: correct = D (B2)
    {
        "level": "B2",
        "query": "television studio news anchor cameras crew",
        "statements": [
            "A teacher is writing equations on a classroom board.",
            "Joggers are running along a path beside a river.",
            "A receptionist is handing a visitor a pen to sign in.",
            "A news anchor is sitting at a desk while cameras and crew are positioned around the studio.",
        ],
        "answer": "D",
        "rationale": "Option D correctly depicts a TV news studio with an anchor surrounded by cameras and staff. The other choices describe unrelated scenes."
    },
    # 17: correct = A (B2)
    {
        "level": "B2",
        "query": "airport business traveler security tray laptop",
        "statements": [
            "A traveler is placing a laptop and shoes into a security tray at an airport checkpoint.",
            "A chef is stirring soup in a large pot.",
            "A gardener is planting flowers beside a walkway.",
            "Children are lining up to enter a classroom.",
        ],
        "answer": "A",
        "rationale": "Option A correctly shows a traveler preparing items for an airport security screening. The other statements involve cooking, gardening, or school."
    },
    # 18: correct = B (B2)
    {
        "level": "B2",
        "query": "corporate cafeteria self service salad bar cashless payment",
        "statements": [
            "A librarian is helping a child choose a picture book.",
            "Employees are serving themselves at a salad bar and paying at a cashless terminal.",
            "A mechanic is reaching for a tool on a workbench.",
            "A group of hikers is walking along a forest trail.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes a modern corporate cafeteria with self-service food and cashless payment. The other options show different environments."
    },
    # 19: correct = C (B2)
    {
        "level": "B2",
        "query": "flexible workspace hot desk lockers personal items",
        "statements": [
            "A flight attendant is closing an overhead compartment.",
            "A farmer is guiding cattle through a gate.",
            "Workers are taking laptops from lockers in a hot-desking area.",
            "Children are playing a board game on the floor.",
        ],
        "answer": "C",
        "rationale": "Option C correctly shows employees retrieving laptops from lockers in a flexible workspace. The other statements involve unrelated jobs or leisure activities."
    },
    # 20: correct = D (B2)
    {
        "level": "B2",
        "query": "co working space phone booths remote calls",
        "statements": [
            "A waiter is arranging cutlery on dining tables.",
            "A construction worker is operating a small excavator.",
            "A nurse is wheeling a cart along a corridor.",
            "Several people are using small phone booths for private calls in a co-working space.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes private phone booths inside a co-working space. The other options show restaurant, construction, or hospital scenes."
    },
    # 21: correct = A (B2)
    {
        "level": "B2",
        "query": "urban rooftop solar panels maintenance crew",
        "statements": [
            "Workers in safety harnesses are inspecting solar panels on a rooftop.",
            "A cashier is handing change to a customer at a register.",
            "A violinist is performing on a concert stage.",
            "A child is stacking blocks beside a sofa.",
        ],
        "answer": "A",
        "rationale": "Option A correctly shows a maintenance crew checking solar panels on the roof of a building. The other options depict indoor service, performance, or play."
    },
    # 22: correct = B (B2)
    {
        "level": "B2",
        "query": "airport lounge charging stations mobile devices",
        "statements": [
            "A doctor is looking at an X-ray on a lightbox.",
            "Travelers are sitting near a row of outlets while charging mobile devices.",
            "A teacher is collecting homework from students.",
            "A gardener is watering small trees in large pots.",
        ],
        "answer": "B",
        "rationale": "Option B correctly describes passengers using charging stations in an airport lounge. The other options describe hospital, school, or gardening scenes."
    },
    # 23: correct = C (B2)
    {
        "level": "B2",
        "query": "corporate training room laptops name tents instructor",
        "statements": [
            "A waiter is setting out menus on patio tables.",
            "A bus driver is adjusting the rearview mirror.",
            "Participants with laptops and name tents are listening to an instructor at the front of the room.",
            "A swimmer is standing at the edge of a pool.",
        ],
        "answer": "C",
        "rationale": "Option C correctly shows a corporate training session with laptops and name cards on the tables. The other options describe transportation, dining, or sports."
    },
    # 24: correct = D (B2)
    {
        "level": "B2",
        "query": "international terminal check in kiosks self service",
        "statements": [
            "A scientist is pouring liquid into a test tube.",
            "A child is drawing pictures on a sidewalk with chalk.",
            "Office workers are gathered around a printer.",
            "Passengers are using self-service kiosks in an international terminal.",
        ],
        "answer": "D",
        "rationale": "Option D correctly describes travelers checking in at self-service kiosks at an airport terminal. The other options show laboratory, street, or office scenes."
    },
    # 25: correct = A (B2)
    {
        "level": "B2",
        "query": "modern library study pods glass partitions",
        "statements": [
            "Students are working individually in small study pods separated by glass walls.",
            "A pilot is checking instruments inside a cockpit.",
            "A chef is sprinkling herbs over a pan.",
            "Shoppers are comparing prices in a grocery aisle.",
        ],
        "answer": "A",
        "rationale": "Option A correctly depicts a modern library with glass-enclosed study pods. The other options relate to aviation, cooking, or shopping."
    },
    # 26: correct = B (B2)
    {
        "level": "B2",
        "query": "open office standing desks adjustable monitors",
        "statements": [
            "A child is playing with a toy train on a carpet.",
            "Employees are working at standing desks with adjustable monitors.",
            "A gardener is trimming hedges along a fence.",
            "A musician is rehearsing with a band in a studio.",
        ],
        "answer": "B",
        "rationale": "Option B correctly shows an office with height-adjustable standing desks. The other options involve play, gardening, or music rehearsal."
    },
    # 27: correct = C (B2)
    {
        "level": "B2",
        "query": "project war room wall charts sticky notes",
        "statements": [
            "A nurse is taking supplies from a cabinet.",
            "A commuter is reading a newspaper on a train.",
            "A team is standing in front of a wall covered with charts and sticky notes.",
            "A family is sharing a meal at a dining table.",
        ],
        "answer": "C",
        "rationale": "Option C correctly describes a project war room where charts and sticky notes cover the wall. The other scenes are unrelated."
    },
    # 28: correct = D (B2)
    {
        "level": "B2",
        "query": "harbor container terminal cranes stacked cargo",
        "statements": [
            "A receptionist is opening a drawer in a front desk.",
            "A teacher is reading a story to young children.",
            "A cook is wiping a cutting board with a cloth.",
            "Tall cranes are standing over stacks of containers at a harbor terminal.",
        ],
        "answer": "D",
        "rationale": "Option D correctly shows a container terminal with cranes and stacked cargo. The other options show office, school, or kitchen environments."
    },
    # 29: correct = A (B2)
    {
        "level": "B2",
        "query": "high speed train business class laptop briefcase",
        "statements": [
            "A passenger in business class is working on a laptop beside a briefcase.",
            "A cashier is arranging coins in a register drawer.",
            "A gardener is digging holes for small shrubs.",
            "A child is playing with blocks on a living room floor.",
        ],
        "answer": "A",
        "rationale": "Option A correctly describes a business traveler working on a laptop in a high-speed train’s business class car. The other options show unrelated activities."
    },
    # 30: correct = B (B2)
    {
        "level": "B2",
        "query": "corporate lobby digital directory touch screen",
        "statements": [
            "A chef is tasting soup with a spoon near a stove.",
            "A visitor is using a touch-screen directory in a corporate lobby.",
            "A nurse is closing the curtain around a hospital bed.",
            "A cyclist is waiting at a traffic light.",
        ],
        "answer": "B",
        "rationale": "Option B correctly shows a visitor operating a digital building directory in a lobby. The other options involve kitchen, medical, or street scenes."
    },
    # === Part1 B2 Patterns (31–50) ===
    {
        "level": "B2",
        "query": "businesswoman reviewing quarterly report analyzing bar chart office desk laptop",
        "statements": [
            "The woman is analyzing a bar chart in a quarterly report.",
            "The woman is giving money to a street musician.",
            "She is photographing tourists in a crowded plaza.",
            "She is organizing a flower bouquet."
        ],
        "answer": "A",
        "rationale": "She is looking down at the report while examining a printed bar chart at her desk."
    },
    {
        "level": "B2",
        "query": "team planning marketing strategy meeting whiteboard sticky notes brainstorming session",
        "statements": [
            "The team is cheering for a sports match at a stadium.",
            "The team is brainstorming a marketing strategy using sticky notes on a whiteboard.",
            "The group is performing a dance routine on stage.",
            "The team is lining up to enter a concert hall."
        ],
        "answer": "B",
        "rationale": "The group is actively contributing ideas in front of a whiteboard covered with notes."
    },
    {
        "level": "B2",
        "query": "coworker assisting colleague laptop troubleshooting software issue support help",
        "statements": [
            "A coworker is assisting a colleague with a software issue on a laptop.",
            "The colleague is handing out snacks during a party.",
            "They are watering plants in the greenhouse.",
            "They are attaching price tags to clothes in a shop."
        ],
        "answer": "A",
        "rationale": "One person is pointing at the screen while helping another resolve a problem."
    },
    {
        "level": "B2",
        "query": "manager conducting performance review employee taking notes formal evaluation office",
        "statements": [
            "The manager is conducting a performance review while the employee takes notes.",
            "The employee is trying on different outfits in a store dressing room.",
            "The manager is serving dinner to guests.",
            "The two people are playing card games in a café."
        ],
        "answer": "A",
        "rationale": "They are seated across a desk in a formal evaluation setting, documents open."
    },
    {
        "level": "B2",
        "query": "businessman giving presentation sales forecast digital projector conference room audience focused",
        "statements": [
            "The businessman is giving a presentation on a sales forecast.",
            "The man is tightening bolts on heavy machinery.",
            "He is cooking breakfast on a camping stove.",
            "He is filming a music video in the street."
        ],
        "answer": "A",
        "rationale": "He is pointing at projected figures while speaking to seated listeners."
    },
    {
        "level": "B2",
        "query": "employee scanning printed contract multifunction copier scanning document digital archive",
        "statements": [
            "The employee is scanning a contract using a multifunction copier.",
            "The employee is fishing on a wooden pier.",
            "The employee is repairing a washing machine.",
            "The employee is trimming trees in a field."
        ],
        "answer": "A",
        "rationale": "She is digitizing a document for archiving using office equipment."
    },
    {
        "level": "B2",
        "query": "woman moderating panel discussion speaking microphone conference hall audience",
        "statements": [
            "The woman is moderating a panel discussion.",
            "The woman is repairing a bicycle tire.",
            "She is cleaning windows inside a restaurant.",
            "She is participating in a yoga retreat."
        ],
        "answer": "A",
        "rationale": "She is holding a microphone and guiding speakers through the agenda."
    },
    {
        "level": "B2",
        "query": "businessman reviewing contract fine print signing legal agreement negotiation",
        "statements": [
            "The businessman is signing a legal agreement after reviewing the fine print.",
            "The businessman is arranging marine equipment on a fishing boat.",
            "The businessman is feeding a horse on a ranch.",
            "The businessman is dusting a framed painting."
        ],
        "answer": "A",
        "rationale": "He is using a pen to finalize a contract document."
    },
    {
        "level": "B2",
        "query": "team participating hybrid meeting some in room others via video call large screen",
        "statements": [
            "The team is participating in a hybrid meeting with remote members on a screen.",
            "The members are distributing sports uniforms for a game.",
            "The workers are sweeping debris at a construction site.",
            "The group is practicing choral singing."
        ],
        "answer": "A",
        "rationale": "On-site participants and remote callers are interacting simultaneously."
    },
    {
        "level": "B2",
        "query": "employee preparing shipping labels packaging material warehouse desk barcode printer",
        "statements": [
            "The employee is preparing shipping labels at a packing desk.",
            "The employee is arranging flowers for a wedding ceremony.",
            "The employee is preparing a meal in a restaurant kitchen.",
            "The employee is administering medical treatment to a patient."
        ],
        "answer": "A",
        "rationale": "She is generating labels using a barcode printer among boxes and packaging."
    },
    {
        "level": "B2",
        "query": "woman analyzing financial dashboard multiple graphs laptop trend performance data driven",
        "statements": [
            "The woman is analyzing performance graphs on a dashboard.",
            "The woman is cutting lumber with power tools.",
            "The woman is painting a mural on a brick wall.",
            "The woman is scanning library books through a checkout machine."
        ],
        "answer": "A",
        "rationale": "She is studying various digital charts on her laptop display."
    },
    {
        "level": "B2",
        "query": "man coordinating video conference headphones speaking remote team agenda",
        "statements": [
            "The man is coordinating a video conference while speaking through a headset.",
            "The man is repairing plumbing under the sink.",
            "He is feeding birds on a balcony.",
            "He is teaching a child how to ride a bike."
        ],
        "answer": "A",
        "rationale": "He is wearing headphones, supervising a meeting, and speaking to participants."
    },
    {
        "level": "B2",
        "query": "colleagues celebrating project milestone clinking glasses office lounge informal",
        "statements": [
            "The colleagues are celebrating a project milestone and clinking glasses.",
            "The colleagues are training animals at a wildlife center.",
            "They are supervising children playing in a sandbox.",
            "They are staging a theater performance."
        ],
        "answer": "A",
        "rationale": "The group is making a toast in recognition of their project success."
    },
    {
        "level": "B2",
        "query": "employee assisting customer front desk explaining registration form reception counter",
        "statements": [
            "The employee is assisting a customer at the reception desk.",
            "The employee is cooking at a barbecue party.",
            "The employee is tuning a guitar before a concert.",
            "The employee is kayaking on a lake."
        ],
        "answer": "A",
        "rationale": "The employee is pointing at a form while talking politely across the counter."
    },
    {
        "level": "B2",
        "query": "man replacing toner cartridge office printer maintenance troubleshooting printing",
        "statements": [
            "The man is replacing a toner cartridge in a printer.",
            "The man is surfing in the ocean waves.",
            "The man is fixing a motorcycle engine.",
            "The man is searching shelves in a grocery store."
        ],
        "answer": "A",
        "rationale": "He is opening the printer panel and inserting a new cartridge."
    },
    {
        "level": "B2",
        "query": "woman giving product demo handheld device trade show booth technology expo visitors watching",
        "statements": [
            "The woman is giving a product demonstration at a trade show booth.",
            "The woman is arranging pastries in a bakery display.",
            "She is taking part in a school graduation parade.",
            "She is guiding a canoe on a river."
        ],
        "answer": "A",
        "rationale": "She is explaining the features of a device to event attendees."
    },
    {
        "level": "B2",
        "query": "man checking flight itinerary boarding pass smartphone departure gate airport travel",
        "statements": [
            "The man is checking his flight itinerary on his phone at the gate.",
            "The man is climbing a ladder to paint a tall building.",
            "The man is shoveling snow on his driveway.",
            "The man is performing as a DJ at a nightclub."
        ],
        "answer": "A",
        "rationale": "He is comparing his boarding pass with the flight information on screen."
    },
    {
        "level": "B2",
        "query": "woman negotiating contract terms pointing clause printed document legal discussion office",
        "statements": [
            "The woman is negotiating contract terms while pointing at a clause in the document.",
            "The woman is trimming hair in a beauty salon.",
            "She is playing a violin in a concert orchestra.",
            "She is sculpting a statue from clay."
        ],
        "answer": "A",
        "rationale": "She is emphasizing wording in the contract during a discussion."
    },
    {
        "level": "B2",
        "query": "coworkers comparing two prototypes evaluating features product testing discussion",
        "statements": [
            "The coworkers are evaluating features of two prototypes.",
            "The coworkers are handing out samples of food to pedestrians.",
            "They are polishing antique furniture.",
            "They are installing solar panels on a roof."
        ],
        "answer": "A",
        "rationale": "Both are holding different models and examining differences."
    },
    {
        "level": "B2",
        "query": "employee examining shipment invoice warehouse inventory management clipboard",
        "statements": [
            "The employee is examining a shipment invoice with inventory.",
            "The employee is planting vegetables in a greenhouse.",
            "The employee is hiking through a forest canyon.",
            "The employee is inspecting a horse stable."
        ],
        "answer": "A",
        "rationale": "He is reviewing quantities and numbers on a clipboard next to stacked boxes."
    },
    # === Part1 B2 Patterns (51–70 corrected answer distribution) ===
    {
        "level": "B2",
        "query": "colleagues reviewing gantt chart project schedule digital tablet planning timeline",
        "statements": [
            "They are distributing flyers on the street.",
            "The colleagues are reviewing a project schedule on a tablet.",
            "They are watching a live concert from the audience.",
            "They are washing vegetables at a kitchen sink."
        ],
        "answer": "B",
        "rationale": "Both are leaning toward a shared tablet showing a timeline chart."
    },
    {
        "level": "B2",
        "query": "manager facilitating remote workshop flip chart markers breakout groups hybrid learning",
        "statements": [
            "The manager is braiding a child's hair.",
            "The manager is carving a wooden sculpture.",
            "The manager is facilitating a remote workshop.",
            "She is piloting a small airplane."
        ],
        "answer": "C",
        "rationale": "She is annotating a flip chart while coordinating virtual participants."
    },
    {
        "level": "B2",
        "query": "employee proofreading proposal printed document highlighting revision notes",
        "statements": [
            "The employee is proofreading a proposal with revision notes.",
            "The employee is kayaking in the ocean.",
            "The employee is cleaning fish at a market.",
            "The employee is rearranging furniture in a moving truck."
        ],
        "answer": "A",
        "rationale": "He is marking sections of a printed document with a highlighter."
    },
    {
        "level": "B2",
        "query": "businesswoman giving elevator pitch small group networking event confident presentation",
        "statements": [
            "She is stretching before a morning run.",
            "The businesswoman is presenting a short pitch to a small group.",
            "She is doing laundry in her apartment.",
            "She is frosting a cake in a bakery kitchen."
        ],
        "answer": "B",
        "rationale": "She is speaking confidently while others listen attentively."
    },
    {
        "level": "B2",
        "query": "team preparing slide deck last minute adjustments projector connection cables tech check",
        "statements": [
            "They are repairing a damaged wooden fence.",
            "They are connecting display cables and preparing a presentation.",
            "They are registering guests at a wedding ceremony.",
            "They are preparing musical instruments for a street performance."
        ],
        "answer": "B",
        "rationale": "They are clustered around a laptop while connecting display cables."
    },
    {
        "level": "B2",
        "query": "coworker labeling prototype components test batch product quality inspection verification",
        "statements": [
            "He is collecting seashells on the beach.",
            "He is planting seedlings in a greenhouse.",
            "The coworker is labeling prototype components for quality inspection.",
            "He is cleaning windows on a high-rise building."
        ],
        "answer": "C",
        "rationale": "He is applying temporary labels to small hardware pieces on the desk."
    },
    {
        "level": "B2",
        "query": "remote worker comparing two spreadsheets dual monitors analytics budget revenue forecast",
        "statements": [
            "She is analyzing rows of figures across two monitors.",
            "She is feeding animals at a petting zoo.",
            "She is distributing tickets at an amusement park gate.",
            "She is organizing toys in a child's bedroom."
        ],
        "answer": "A",
        "rationale": "She is comparing spreadsheets across both screens."
    },
    {
        "level": "B2",
        "query": "team member taking minutes during meeting recording action items notebook pen",
        "statements": [
            "The team member is recording action items in a notebook.",
            "The team member is performing magic tricks at a party.",
            "The team member is grooming a horse in a stable.",
            "The team member is flying a drone over a forest."
        ],
        "answer": "A",
        "rationale": "He is writing meeting minutes while listening to others speak."
    },
    {
        "level": "B2",
        "query": "employee preparing invoice spreadsheet supplier items pricing accounting admin task",
        "statements": [
            "The employee is sculpting a statue outdoors.",
            "The employee is preparing an invoice in a spreadsheet.",
            "The employee is conducting an orchestra.",
            "The employee is washing a pet in a bathtub."
        ],
        "answer": "B",
        "rationale": "She is entering pricing data line by line at her computer."
    },
    {
        "level": "B2",
        "query": "businessman comparing printed portfolios meeting a client coffee shop negotiation",
        "statements": [
            "He is trimming bushes in a backyard.",
            "The businessman is comparing portfolios with a client.",
            "He is vacuuming the carpet of his living room.",
            "He is applying stickers to a laptop."
        ],
        "answer": "B",
        "rationale": "Two binders and printed pages are spread across the café table during discussion."
    },
    {
        "level": "B2",
        "query": "person training guide dog obedience commands outdoor park responsible handling",
        "statements": [
            "A person is packing gifts into boxes for shipment.",
            "A person is training a guide dog using obedience commands.",
            "A person is lighting candles on a birthday cake.",
            "A person is handing out drinks to sports fans."
        ],
        "answer": "B",
        "rationale": "The individual is reinforcing controlled guidance movements with the dog."
    },
    {
        "level": "B2",
        "query": "couple practicing partner yoga core balance synchronization indoor fitness stretch",
        "statements": [
            "The couple is directing traffic on a busy road.",
            "The couple is repairing a jammed door lock.",
            "The couple is practicing partner yoga for balance.",
            "The couple is replacing tires on a truck."
        ],
        "answer": "C",
        "rationale": "They are coordinating movement while holding mirrored poses."
    },
    {
        "level": "B2",
        "query": "family organizing garage belongings sorting boxes donating unused items cleanup",
        "statements": [
            "A family is organizing their garage and sorting items for donation.",
            "The family is painting a large mural together.",
            "The family is selling vegetables at a farmers market.",
            "The family is putting up stage lighting for a concert."
        ],
        "answer": "A",
        "rationale": "They are dividing boxes into keep and donate piles."
    },
    {
        "level": "B2",
        "query": "cyclist adjusting derailleur fine tuning gears workshop tools maintenance",
        "statements": [
            "The cyclist is competing in a stadium sprint.",
            "The cyclist is adjusting the gears on the bicycle.",
            "The cyclist is shopping at a department store.",
            "The cyclist is taking tickets at a movie theater."
        ],
        "answer": "B",
        "rationale": "He is fine-tuning the derailleur using tools."
    },
    {
        "level": "B2",
        "query": "photographer using reflector natural light outdoor portrait creative lighting",
        "statements": [
            "The photographer is positioning a reflector for natural light.",
            "The photographer is tuning a drum set.",
            "The photographer is knitting scarves for charity.",
            "The photographer is writing a novel at a desk."
        ],
        "answer": "A",
        "rationale": "She is using a reflective board to direct sunlight toward the subject."
    },
    {
        "level": "B2",
        "query": "teacher holding science model explaining concept classroom attentive students",
        "statements": [
            "The teacher is hanging holiday decorations at home.",
            "The teacher is guiding a canoe down a river.",
            "The teacher is explaining a concept using a science model.",
            "The teacher is trimming hedges in a park."
        ],
        "answer": "C",
        "rationale": "She is showing the structure object while the class watches."
    },
    {
        "level": "B2",
        "query": "friends organizing board game pieces strategy meeting living room gathering",
        "statements": [
            "The friends are roasting a pig at a beach party.",
            "The friends are mixing cement at a construction site.",
            "The friends are marching in a parade.",
            "The friends are setting up pieces for a strategy board game."
        ],
        "answer": "D",
        "rationale": "They are discussing rule sheets while placing tokens on the board."
    },
    {
        "level": "B2",
        "query": "chef arranging ingredients garnish final plating high end restaurant attention detail",
        "statements": [
            "The chef is shopping for clothes at a mall.",
            "The chef is arranging ingredients carefully to finish a plate.",
            "The chef is repairing a broken boat motor.",
            "The chef is playing arcade games in a game center."
        ],
        "answer": "B",
        "rationale": "Tweezers and garnish elements are being placed delicately on the dish."
    },
    {
        "level": "B2",
        "query": "hiker checking navigation app comparing elevation route topographic map trail",
        "statements": [
            "The hiker is repairing earrings in a jewelry shop.",
            "The hiker is sorting fresh produce for sale.",
            "The hiker is checking an elevation route on a navigation app.",
            "The hiker is drawing portraits in a studio."
        ],
        "answer": "C",
        "rationale": "He is comparing altitude markers and trail lines on the smartphone."
    },
    {
        "level": "B2",
        "query": "artist selecting precise paintbrush fine detail canvas studio natural light creative",
        "statements": [
            "The artist is reading bedtime stories to children.",
            "The artist is pouring concrete to build a staircase.",
            "The artist is selecting a fine paintbrush for detailed work.",
            "The artist is polishing silverware for a banquet."
        ],
        "answer": "C",
        "rationale": "She is choosing a slim brush while examining a canvas under natural light."
    },
    # === Part1 B2 Patterns (71–85 corrected answer distribution) ===
    {
        "level": "B2",
        "query": "colleague reviewing compliance checklist pen pointing document legal requirement verification",
        "statements": [
            "The colleague is sharpening a kitchen knife before cooking.",
            "The colleague is feeding birds in a public park.",
            "The colleague is pointing to a checklist to verify compliance items.",
            "The colleague is decorating a wedding cake."
        ],
        "answer": "C",
        "rationale": "The document contains marked rule items that the colleague is confirming carefully."
    },
    {
        "level": "B2",
        "query": "business team analyzing user survey feedback trend sticky notes insight grouping office wall",
        "statements": [
            "They are repairing the roof of a house.",
            "They are assembling a tent for camping.",
            "They are scrubbing floors in a warehouse.",
            "The team is grouping survey insights on sticky notes."
        ],
        "answer": "D",
        "rationale": "The team is identifying patterns and trends by clustering the notes on the wall."
    },
    {
        "level": "B2",
        "query": "employee logging customer request crm system typing follow up ticket desktop",
        "statements": [
            "The employee is logging a customer request in a CRM system.",
            "The employee is stirring soup in a restaurant kitchen.",
            "The employee is sweeping leaves in a garden.",
            "The employee is waxing a surfboard on the beach."
        ],
        "answer": "A",
        "rationale": "The employee is typing follow-up notes into customer records."
    },
    {
        "level": "B2",
        "query": "coworkers analyzing heat map product dashboard metrics digital workspace",
        "statements": [
            "They are washing their personal cars in a driveway.",
            "They are singing karaoke on stage.",
            "They are analyzing a heat map on a dashboard.",
            "They are driving a tractor through a farm field."
        ],
        "answer": "C",
        "rationale": "Multiple hotspots and activity regions on the heat map are being discussed."
    },
    {
        "level": "B2",
        "query": "business analyst comparing kpi targets quarterly board charts glass meeting room",
        "statements": [
            "The analyst is grooming a dog in a backyard.",
            "The analyst is arranging flowers in a bouquet shop.",
            "The analyst is comparing KPI targets against quarterly results.",
            "The analyst is inspecting jewelry at a pawnshop counter."
        ],
        "answer": "C",
        "rationale": "He is referencing printed charts and numbers during the review."
    },
    {
        "level": "B2",
        "query": "coworker onboarding training new employee screen sharing software demo corporate workplace",
        "statements": [
            "The coworker is organizing suitcases for a family vacation.",
            "The coworker is fixing a flat tire on the road.",
            "The coworker is giving a tour of a museum exhibition.",
            "The coworker is coaching a new employee via software demo."
        ],
        "answer": "D",
        "rationale": "Screen sharing shows key features of a business system for the new hire."
    },
    {
        "level": "B2",
        "query": "project leader updating risk matrix probability impact status presentation decision board",
        "statements": [
            "The leader is handing out candy to trick-or-treaters.",
            "The leader is frying vegetables on a stove.",
            "The leader is updating a risk matrix for a project review.",
            "The leader is designing costumes for a theater production."
        ],
        "answer": "C",
        "rationale": "He is modifying the probability and impact indicators visible on the chart."
    },
    {
        "level": "B2",
        "query": "employee conducting product usability test recording participant reaction notes camera tripod",
        "statements": [
            "The employee is recording reactions during a usability test.",
            "The employee is hiking up a snowy mountain.",
            "The employee is sanding wood in a workshop.",
            "The employee is supervising children at a water park."
        ],
        "answer": "A",
        "rationale": "He is documenting feedback while the user interacts with the product."
    },
    {
        "level": "B2",
        "query": "remote colleagues co editing shared document comments suggestions cloud collaboration",
        "statements": [
            "The colleagues are washing dishes in a restaurant kitchen.",
            "The colleagues are ice-skating on a frozen pond.",
            "The colleagues are co-editing a shared document with comments.",
            "The colleagues are hammering nails into wooden beams."
        ],
        "answer": "C",
        "rationale": "Edits and suggestions are visible in the collaboration interface."
    },

    # ── 非ビジネス ──

    {
        "level": "B2",
        "query": "friends repairing vintage motorcycle adjusting bolts testing engine garage weekend hobby",
        "statements": [
            "The friends are adjusting bolts on a vintage motorcycle.",
            "The friends are organizing a puppet show for children.",
            "The friends are rehearsing dance moves in a studio.",
            "The friends are making banners for a fundraiser."
        ],
        "answer": "A",
        "rationale": "Tools and parts are spread across the floor as they fix the engine."
    },
    {
        "level": "B2",
        "query": "woman composing song arranging sheet music digital piano creative session",
        "statements": [
            "The woman is washing windows on a tall building.",
            "The woman is preparing medical supplies for surgery.",
            "The woman is arranging sheet music while composing a song.",
            "The woman is repairing garden sprinklers."
        ],
        "answer": "C",
        "rationale": "She is marking chords on the score beside the digital piano."
    },
    {
        "level": "B2",
        "query": "man training for rock climbing securing harness chalk checking route indoor climbing gym",
        "statements": [
            "The man is grilling steaks for a party.",
            "The man is checking the climbing route while securing his harness.",
            "The man is folding laundry after washing.",
            "The man is making pottery on a spinning wheel."
        ],
        "answer": "B",
        "rationale": "He is applying chalk and visually inspecting holds before climbing."
    },
    {
        "level": "B2",
        "query": "family preparing camping gear assembling tent poles tarps campsite teamwork nature",
        "statements": [
            "The family is carving pumpkins for a festival.",
            "The family is distributing product samples to shoppers.",
            "The family is assembling tent poles at a campsite.",
            "The family is repairing bicycles for a fundraiser."
        ],
        "answer": "C",
        "rationale": "They are building the tent frame together while preparing outdoor gear."
    },
    {
        "level": "B2",
        "query": "artist adjusting studio lights portrait shoot light angle softbox diffusion photography workspace",
        "statements": [
            "The artist is selling snacks at a theater concession stand.",
            "The artist is supervising children at a beach daycare.",
            "The artist is adjusting studio lights for a portrait shoot.",
            "The artist is trimming hedges for landscaping work."
        ],
        "answer": "C",
        "rationale": "They are fine-tuning the lighting angle and diffuser placement for the subject."
    },
    # === Part1 B2 Patterns (86–100) ===
    {
        "level": "B2",
        "query": "business team reviewing budget allocation pie chart touchscreen monitor financial planning",
        "statements": [
            "They are slicing fruit to serve at a picnic.",
            "They are reviewing a pie chart on a touchscreen monitor.",
            "They are practicing musical instruments on stage.",
            "They are setting up decorations for a birthday party."
        ],
        "answer": "B",
        "rationale": "Team members are gathered around a screen displaying segmented budget proportions."
    },
    {
        "level": "B2",
        "query": "coworker presenting user journey map printed infographic product design workshop",
        "statements": [
            "The coworker is repairing a flat bicycle tire.",
            "The coworker is presenting a user journey map to the group.",
            "The coworker is installing a ceiling fan at home.",
            "The coworker is sanding wooden furniture."
        ],
        "answer": "B",
        "rationale": "She is pointing at key transition moments on the printed journey illustration."
    },
    {
        "level": "B2",
        "query": "employee calibrating barcode scanner testing device inventory logistics storage facility",
        "statements": [
            "The employee is calibrating a barcode scanner.",
            "The employee is swimming in a community pool.",
            "The employee is roasting vegetables in an oven.",
            "The employee is polishing a brass instrument."
        ],
        "answer": "A",
        "rationale": "He is testing scan accuracy while boxes and storage racks surround him."
    },
    {
        "level": "B2",
        "query": "manager facilitating roadmap alignment session post it notes quarterly milestones leadership",
        "statements": [
            "The manager is facilitating a roadmap alignment discussion.",
            "The manager is watering houseplants on a balcony.",
            "The manager is carving pumpkins for a festival.",
            "The manager is checking car tire pressure at a gas station."
        ],
        "answer": "A",
        "rationale": "She is pointing at milestones and guiding the team through each delivery target."
    },
    {
        "level": "B2",
        "query": "analyst verifying procurement receipts cross checking vendor codes spreadsheet accounting",
        "statements": [
            "The analyst is frosting cookies for a bake sale.",
            "The analyst is checking receipts against vendor codes.",
            "The analyst is releasing birds from a cage.",
            "The analyst is gluing paper figures for arts and crafts."
        ],
        "answer": "B",
        "rationale": "He is matching receipt numbers to supplier details in a spreadsheet."
    },
    {
        "level": "B2",
        "query": "businesswoman leading webinar virtual whiteboard annotations remote participants training session",
        "statements": [
            "She is cooking soup at a restaurant stove.",
            "She is leading a webinar using a virtual whiteboard.",
            "She is loading gardening soil into wheelbarrows.",
            "She is repairing a broken guitar string."
        ],
        "answer": "B",
        "rationale": "She is writing annotations on a shared digital board while participants follow remotely."
    },
    {
        "level": "B2",
        "query": "team conducting customer interview recording notes handheld mic audio log insights",
        "statements": [
            "They are interviewing a customer and recording notes.",
            "They are folding laundry together.",
            "They are playing arcade games at a mall.",
            "They are shipping pumpkins for a seasonal market."
        ],
        "answer": "A",
        "rationale": "One team member holds the microphone while another captures qualitative insights."
    },
    {
        "level": "B2",
        "query": "consultant explaining performance dashboard metrics to client office presentation",
        "statements": [
            "The consultant is trimming hedges in a garden.",
            "The consultant is reviewing performance metrics with a client.",
            "The consultant is distributing food at a soup kitchen.",
            "The consultant is jogging down a suburban street."
        ],
        "answer": "B",
        "rationale": "Both are focused on the dashboard while the consultant points to indicators."
    },
    {
        "level": "B2",
        "query": "coworkers printing shipping manifests packing orders fulfillment center barcode labels trays",
        "statements": [
            "The coworkers are printing shipping manifests and packing orders.",
            "The coworkers are lifting weights at a fitness gym.",
            "The coworkers are skating down a city street.",
            "The coworkers are conducting an orchestra rehearsal."
        ],
        "answer": "A",
        "rationale": "They are printing labels and placing merchandise into trays for dispatch."
    },
    {
        "level": "B2",
        "query": "project coordinator tracking sprint backlog kanban board stand up meeting sticky notes software dev",
        "statements": [
            "The coordinator is evaluating vegetables at a street market.",
            "The coordinator is leading a stand-up at a kanban board.",
            "The coordinator is cleaning a bicycle chain.",
            "The coordinator is coaching a child to swim."
        ],
        "answer": "B",
        "rationale": "She stands beside a wall filled with sticky notes while discussing sprint progress."
    },
    {
        "level": "B2",
        "query": "man restoring vintage radio soldering wires testing audio receiver electronics hobby workshop",
        "statements": [
            "The man is hiking steep trails in the mountains.",
            "The man is grilling appetizers for a neighborhood party.",
            "The man is soldering wires in a vintage radio.",
            "The man is shoveling snow in his driveway."
        ],
        "answer": "C",
        "rationale": "He is adjusting components inside the casing using a soldering tool."
    },
    {
        "level": "B2",
        "query": "woman painting ceramic plate detailed patterns tiny brush glazing artistic craft studio",
        "statements": [
            "The woman is applying glaze with a fine brush to a ceramic plate.",
            "The woman is stocking merchandise on grocery shelves.",
            "The woman is helping children cross a busy intersection.",
            "The woman is washing a car with a sponge."
        ],
        "answer": "A",
        "rationale": "She is carefully applying detailed patterns as part of decorative glazing."
    },
    {
        "level": "B2",
        "query": "friends assembling model train layout miniature town tracks controller collaborative hobby",
        "statements": [
            "The friends are putting together a model train layout.",
            "The friends are performing repairs on a fishing boat.",
            "The friends are handing out posters at a marathon.",
            "The friends are serving drinks at a music festival."
        ],
        "answer": "A",
        "rationale": "Tracks, scenery pieces, and wiring are being arranged on a table."
    },
    {
        "level": "B2",
        "query": "hiker checking hydration pack trail map compass high altitude preparation",
        "statements": [
            "The hiker is welding metal bars together.",
            "The hiker is washing dishes in a kitchen.",
            "The hiker is checking a hydration pack and studying a trail map.",
            "The hiker is taking photographs at a wedding ceremony."
        ],
        "answer": "C",
        "rationale": "He is matching map details with direction and equipment before starting the hike."
    },
    {
        "level": "B2",
        "query": "family repairing remote control car checking battery wheels gears fun weekend activity living room",
        "statements": [
            "The family is cleaning windows in the living room.",
            "The family is checking the battery and wheels of a remote-control car.",
            "The family is teaching a dog to fetch objects.",
            "The family is preparing salad ingredients on the kitchen counter."
        ],
        "answer": "B",
        "rationale": "They are kneeling around the toy car while tightening small screws and verifying power."
    }

]

def _auto_topic_from_query(query: str, max_words: int = 3) -> list[str]:
    #"""
    #Part1のquery（例: 'office desk laptop coffee'）から
    #先頭の単語を max_words 個だけ抜き出して topic にする簡易ヘルパー。
    #例: 'office desk laptop coffee' → ["office", "desk", "laptop"]
    #"""
    if not isinstance(query, str):
        return ["photo"]
    # スペース区切りで単語に分割
    words = [w for w in query.split() if w]
    if not words:
        return ["photo"]
    return words[:max_words]


# すべてのパターンに topic を付与（既にtopicがある場合は尊重）
for p in PART1_PATTERNS:
    if "topic" not in p:
        q = p.get("query", "")
        p["topic"] = _auto_topic_from_query(q)
