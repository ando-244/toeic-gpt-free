# patterns_part1.py
# Part1の問題パターン集だけをまとめたモジュール

# === Part1 用の問題パターン集 ===
PART1_PATTERNS = [
    # --- A2 level 30patterns (easy) ---
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
