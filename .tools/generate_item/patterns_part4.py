# patterns_part4.py
# Part4の問題パターン集だけをまとめたモジュール

# === Part4 用アナウンス／トークパターン集 ===
PART4_PATTERNS = [
    # --- A2 level 30patterns (easy) ---
    # 1. スーパーの朝の案内
    {
        "level": "A2",
        "topic": ["supermarket", "morning announcement"],
        "script": (
            "Good morning, shoppers. "
            "Our store has just opened for the day. "
            "Fresh bread is now ready in the bakery corner, and all milk products are ten percent off this morning. "
            "Please take a basket at the entrance and enjoy your shopping with us."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main purpose of the announcement?",
                "choices": {
                    "A": "To welcome customers and share today’s specials.",
                    "B": "To ask customers to leave the store.",
                    "C": "To explain the return policy.",
                    "D": "To advertise a new branch opening."
                },
                "answer": "A",
                "rationale": "It greets shoppers and mentions today’s offers."
            },
            {
                "stem": "(audio) What item is on sale this morning?",
                "choices": {
                    "A": "Coffee beans.",
                    "B": "Milk products.",
                    "C": "Frozen food.",
                    "D": "Cleaning supplies."
                },
                "answer": "B",
                "rationale": "Milk products are ten percent off."
            },
            {
                "stem": "(audio) What are customers asked to take at the entrance?",
                "choices": {
                    "A": "A discount coupon.",
                    "B": "A shopping cart from outside.",
                    "C": "A basket.",
                    "D": "A store map."
                },
                "answer": "C",
                "rationale": "They are told to take a basket."
            },
        ],
    },

    # 2. 小学校の遠足のお知らせ
    {
        "level": "A2",
        "topic": ["school", "field trip"],
        "script": (
            "Students, this is a message about our field trip next Tuesday. "
            "We will visit the city zoo and have lunch in the park. "
            "Please bring a packed lunch, a drink, and a hat. "
            "Do not forget to give the permission form to your homeroom teacher."
        ),
        "questions": [
            {
                "stem": "(audio) Where will the students go on the trip?",
                "choices": {
                    "A": "To a science museum.",
                    "B": "To the city zoo.",
                    "C": "To a swimming pool.",
                    "D": "To the beach."
                },
                "answer": "B",
                "rationale": "The announcement says they will visit the city zoo."
            },
            {
                "stem": "(audio) What should students bring for lunch?",
                "choices": {
                    "A": "Only money for food.",
                    "B": "Snacks from the school shop.",
                    "C": "A packed lunch and a drink.",
                    "D": "Lunch boxes for other students."
                },
                "answer": "C",
                "rationale": "They must bring a packed lunch and a drink."
            },
            {
                "stem": "(audio) What form must be given to the teacher?",
                "choices": {
                    "A": "A health check form.",
                    "B": "A club registration form.",
                    "C": "A permission form.",
                    "D": "A library application form."
                },
                "answer": "D" if False else "C",  # 正解: C
                "rationale": "They need to hand in the permission form."
            },
        ],
    },

    # 3. 図書館のマナー案内
    {
        "level": "A2",
        "topic": ["library", "rules"],
        "script": (
            "Welcome to the town library. "
            "Please speak quietly while you are inside the building. "
            "Food and drinks are not allowed in the reading area. "
            "Before you leave, return all books to the front desk or to the book return box near the door."
        ),
        "questions": [
            {
                "stem": "(audio) What is the speaker mainly talking about?",
                "choices": {
                    "A": "Library closing times.",
                    "B": "Rules for using the library.",
                    "C": "New books in the library.",
                    "D": "How to join a reading club."
                },
                "answer": "B",
                "rationale": "The announcement explains basic library rules."
            },
            {
                "stem": "(audio) What is NOT allowed in the reading area?",
                "choices": {
                    "A": "Using a notebook.",
                    "B": "Talking with friends.",
                    "C": "Eating and drinking.",
                    "D": "Using the internet."
                },
                "answer": "C",
                "rationale": "Food and drinks are not allowed."
            },
            {
                "stem": "(audio) Where can visitors return their books?",
                "choices": {
                    "A": "Only to the children’s corner.",
                    "B": "To the front desk or the box near the door.",
                    "C": "To the city office.",
                    "D": "To the school library."
                },
                "answer": "B",
                "rationale": "They can return books at the desk or in the return box."
            },
        ],
    },

    # 4. バス停での案内
    {
        "level": "A2",
        "topic": ["bus", "stop announcement"],
        "script": (
            "This is a message for passengers waiting at Central Bus Stop. "
            "The next bus to Lakeside Park will arrive in about ten minutes. "
            "Please line up behind the yellow line and have your bus card or exact change ready. "
            "Thank you for waiting."
        ),
        "questions": [
            {
                "stem": "(audio) Who is this announcement for?",
                "choices": {
                    "A": "Passengers on the train.",
                    "B": "Drivers in the parking lot.",
                    "C": "Passengers at the bus stop.",
                    "D": "Visitors in the museum."
                },
                "answer": "C",
                "rationale": "It is for people at Central Bus Stop."
            },
            {
                "stem": "(audio) When will the bus to Lakeside Park arrive?",
                "choices": {
                    "A": "In about ten minutes.",
                    "B": "Right now.",
                    "C": "In about one hour.",
                    "D": "Tomorrow morning."
                },
                "answer": "A",
                "rationale": "The bus will arrive in around ten minutes."
            },
            {
                "stem": "(audio) What are passengers asked to prepare?",
                "choices": {
                    "A": "An umbrella and a coat.",
                    "B": "Passports for inspection.",
                    "C": "Their bus card or exact change.",
                    "D": "A printed ticket from the office."
                },
                "answer": "C",
                "rationale": "They should have a card or exact money ready."
            },
        ],
    },

    # 5. カフェの閉店前アナウンス
    {
        "level": "A2",
        "topic": ["cafe", "closing soon"],
        "script": (
            "Good evening. "
            "This is a notice from Sunny Café. "
            "We will close in twenty minutes. "
            "If you would like to order something else, please do so now. "
            "The last order for drinks is in ten minutes. "
            "Thank you for spending time with us today."
        ),
        "questions": [
            {
                "stem": "(audio) When will the café close?",
                "choices": {
                    "A": "In ten minutes.",
                    "B": "In twenty minutes.",
                    "C": "In thirty minutes.",
                    "D": "In one hour."
                },
                "answer": "B",
                "rationale": "The café will close in twenty minutes."
            },
            {
                "stem": "(audio) By when must customers order their final drinks?",
                "choices": {
                    "A": "In five minutes.",
                    "B": "In ten minutes.",
                    "C": "In twenty minutes.",
                    "D": "Right after closing."
                },
                "answer": "B",
                "rationale": "The last drink order is in ten minutes."
            },
            {
                "stem": "(audio) What is the tone of the announcement?",
                "choices": {
                    "A": "Thankful and polite.",
                    "B": "Angry and upset.",
                    "C": "Confused and worried.",
                    "D": "Excited and loud."
                },
                "answer": "A",
                "rationale": "The speaker thanks customers in a polite way."
            },
        ],
    },

    # 6. 公園の落とし物案内
    {
        "level": "A2",
        "topic": ["park", "lost item"],
        "script": (
            "Attention, visitors. "
            "A small blue backpack has been found near the playground. "
            "If you think it may belong to you or your child, please come to the park office next to the main gate. "
            "A staff member will help you there."
        ),
        "questions": [
            {
                "stem": "(audio) What has been found in the park?",
                "choices": {
                    "A": "A pair of glasses.",
                    "B": "A blue backpack.",
                    "C": "A red umbrella.",
                    "D": "A mobile phone."
                },
                "answer": "B",
                "rationale": "The announcement mentions a small blue backpack."
            },
            {
                "stem": "(audio) Where is the park office?",
                "choices": {
                    "A": "Behind the playground.",
                    "B": "Next to the main gate.",
                    "C": "Across from the parking lot.",
                    "D": "On the second floor of a building."
                },
                "answer": "B",
                "rationale": "It is next to the main gate."
            },
            {
                "stem": "(audio) Who will help the owner of the backpack?",
                "choices": {
                    "A": "Another visitor.",
                    "B": "A police officer.",
                    "C": "A park staff member.",
                    "D": "The bus driver."
                },
                "answer": "C",
                "rationale": "A staff member will help at the office."
            },
        ],
    },

    # 7. 駅での天候による遅れ
    {
        "level": "A2",
        "topic": ["train", "delay"],
        "script": (
            "Attention, passengers. "
            "Because of heavy rain, the next local train on Line 2 will be about five minutes late. "
            "We are sorry for the delay. "
            "Please wait on the platform and stand behind the white line until the train stops."
        ),
        "questions": [
            {
                "stem": "(audio) Why is the train delayed?",
                "choices": {
                    "A": "Because of a festival.",
                    "B": "Because of heavy rain.",
                    "C": "Because of a driver change.",
                    "D": "Because of a holiday schedule."
                },
                "answer": "B",
                "rationale": "Heavy rain is causing the delay."
            },
            {
                "stem": "(audio) How late will the train be?",
                "choices": {
                    "A": "About five minutes.",
                    "B": "About fifteen minutes.",
                    "C": "About thirty minutes.",
                    "D": "About one hour."
                },
                "answer": "A",
                "rationale": "The train will be about five minutes late."
            },
            {
                "stem": "(audio) What are passengers told to do?",
                "choices": {
                    "A": "Wait inside the train.",
                    "B": "Leave the station and return later.",
                    "C": "Wait on the platform behind the white line.",
                    "D": "Move to another platform right away."
                },
                "answer": "C",
                "rationale": "They should stay behind the safety line."
            },
        ],
    },

    # 8. 病院の受付案内
    {
        "level": "A2",
        "topic": ["clinic", "reception"],
        "script": (
            "Welcome to Sunny Clinic. "
            "If this is your first visit, please fill out a simple form at the reception desk. "
            "Then, take a seat in the waiting area until a nurse calls your name. "
            "Patients with a cold or a fever, please wear a mask while you wait."
        ),
        "questions": [
            {
                "stem": "(audio) What should first-time visitors do first?",
                "choices": {
                    "A": "Go directly to the doctor.",
                    "B": "Sit in the waiting area only.",
                    "C": "Fill out a form at reception.",
                    "D": "Call the clinic later."
                },
                "answer": "C",
                "rationale": "New patients must complete a form."
            },
            {
                "stem": "(audio) When can patients see the nurse?",
                "choices": {
                    "A": "When their name is called.",
                    "B": "Exactly at nine o’clock.",
                    "C": "Only after lunch time.",
                    "D": "Only on weekends."
                },
                "answer": "A",
                "rationale": "They wait until a nurse calls their name."
            },
            {
                "stem": "(audio) What are people with a cold asked to do?",
                "choices": {
                    "A": "Stand near a window.",
                    "B": "Wear a mask in the waiting area.",
                    "C": "Wait outside the building.",
                    "D": "Go to another clinic."
                },
                "answer": "B",
                "rationale": "They are asked to wear a mask."
            },
        ],
    },

    # 9. ジムの初心者クラス案内
    {
        "level": "A2",
        "topic": ["gym", "beginner class"],
        "script": (
            "Hello, members. "
            "Tonight we will have a beginner exercise class in Studio B from seven to eight p.m. "
            "This class is slow and easy, so it is good for people who are new to the gym. "
            "Please bring a towel and a bottle of water if you join."
        ),
        "questions": [
            {
                "stem": "(audio) Who is the class mainly for?",
                "choices": {
                    "A": "Experienced runners.",
                    "B": "People new to the gym.",
                    "C": "Children under ten.",
                    "D": "Professional athletes."
                },
                "answer": "B",
                "rationale": "It is a slow and easy beginner class."
            },
            {
                "stem": "(audio) Where will the class take place?",
                "choices": {
                    "A": "In Studio A.",
                    "B": "In the swimming pool.",
                    "C": "In Studio B.",
                    "D": "On the rooftop."
                },
                "answer": "C",
                "rationale": "The class is in Studio B."
            },
            {
                "stem": "(audio) What should participants bring?",
                "choices": {
                    "A": "Only indoor shoes.",
                    "B": "A towel and water.",
                    "C": "Their own stereo.",
                    "D": "Cooking tools."
                },
                "answer": "B",
                "rationale": "They are asked to bring a towel and water."
            },
        ],
    },

    # 10. オフィスの来客受付
    {
        "level": "A2",
        "topic": ["office", "visitor"],
        "script": (
            "Welcome to River Tower Office Building. "
            "All visitors must sign in at the front desk and wear a visitor badge. "
            "Please wait in the lobby seats until your host comes to meet you. "
            "When you leave, return your badge to the desk."
        ),
        "questions": [
            {
                "stem": "(audio) What must visitors do when they arrive?",
                "choices": {
                    "A": "Go directly to the top floor.",
                    "B": "Sign in at the front desk.",
                    "C": "Use the staff entrance.",
                    "D": "Wait outside the building."
                },
                "answer": "B",
                "rationale": "Visitors need to sign in at reception."
            },
            {
                "stem": "(audio) What should visitors wear?",
                "choices": {
                    "A": "A company uniform.",
                    "B": "A safety helmet.",
                    "C": "A visitor badge.",
                    "D": "A special name tag from home."
                },
                "answer": "C",
                "rationale": "They must wear a visitor badge."
            },
            {
                "stem": "(audio) What are visitors asked to do before leaving?",
                "choices": {
                    "A": "Pay a small fee.",
                    "B": "Take a survey online.",
                    "C": "Return the badge to the desk.",
                    "D": "Check the weather forecast."
                },
                "answer": "C",
                "rationale": "They must return the visitor badge."
            },
        ],
    },

    # 11. 住宅街の清掃活動
    {
        "level": "A2",
        "topic": ["neighborhood", "cleaning"],
        "script": (
            "Good evening, residents. "
            "This Sunday morning, we will have a neighborhood clean-up. "
            "We will meet at nine o’clock in front of the community center. "
            "Gloves and garbage bags will be prepared, but please bring your own drink. "
            "We hope many of you can join."
        ),
        "questions": [
            {
                "stem": "(audio) What event will take place on Sunday?",
                "choices": {
                    "A": "A sports competition.",
                    "B": "A neighborhood clean-up.",
                    "C": "A fireworks show.",
                    "D": "A music concert."
                },
                "answer": "B",
                "rationale": "It is a clean-up activity in the neighborhood."
            },
            {
                "stem": "(audio) What items will be prepared by organizers?",
                "choices": {
                    "A": "Lunch boxes for everyone.",
                    "B": "Chairs and tables.",
                    "C": "Gloves and garbage bags.",
                    "D": "Umbrellas and coats."
                },
                "answer": "C",
                "rationale": "Gloves and garbage bags will be ready."
            },
            {
                "stem": "(audio) What should residents bring themselves?",
                "choices": {
                    "A": "Their own drink.",
                    "B": "Large tools.",
                    "C": "Pets and children.",
                    "D": "Old clothes to sell."
                },
                "answer": "A",
                "rationale": "They are asked to bring a drink."
            },
        ],
    },

    # 12. 幼稚園の迎え時間
    {
        "level": "A2",
        "topic": ["kindergarten", "pickup time"],
        "script": (
            "Parents, this is a reminder from Rainbow Kindergarten. "
            "Today we will finish thirty minutes earlier because of a teachers’ meeting. "
            "Please come to pick up your children by three p.m. "
            "If you will be late, call the office as soon as possible."
        ),
        "questions": [
            {
                "stem": "(audio) Why will the kindergarten finish early today?",
                "choices": {
                    "A": "Because of a sports day.",
                    "B": "Because of a teachers’ meeting.",
                    "C": "Because of heavy snow.",
                    "D": "Because of construction work."
                },
                "answer": "B",
                "rationale": "There is a teachers’ meeting."
            },
            {
                "stem": "(audio) By what time should parents pick up their children?",
                "choices": {
                    "A": "By two thirty p.m.",
                    "B": "By three p.m.",
                    "C": "By four p.m.",
                    "D": "By five p.m."
                },
                "answer": "B",
                "rationale": "Parents should come by three p.m."
            },
            {
                "stem": "(audio) What should parents do if they will be late?",
                "choices": {
                    "A": "Send a letter the next day.",
                    "B": "Ask another parent silently.",
                    "C": "Call the office as soon as possible.",
                    "D": "Come without saying anything."
                },
                "answer": "C",
                "rationale": "They are asked to call the office."
            },
        ],
    },

    # 13. ペットショップからの案内
    {
        "level": "A2",
        "topic": ["pet shop", "event"],
        "script": (
            "Welcome to Happy Paws Pet Shop. "
            "This Saturday afternoon, we will have a free dog brushing lesson in front of the store. "
            "Anyone who has a small dog can join. "
            "Please bring your own brush if you have one. "
            "For more information, ask a staff member."
        ),
        "questions": [
            {
                "stem": "(audio) What special event will the pet shop hold?",
                "choices": {
                    "A": "A pet photo contest.",
                    "B": "A free dog brushing lesson.",
                    "C": "A cat adoption day.",
                    "D": "A bird training show."
                },
                "answer": "B",
                "rationale": "The event is a dog brushing lesson."
            },
            {
                "stem": "(audio) Who can join the event?",
                "choices": {
                    "A": "People who have small dogs.",
                    "B": "Only children under ten.",
                    "C": "Only store staff.",
                    "D": "Only people without pets."
                },
                "answer": "A",
                "rationale": "Anyone with a small dog can join."
            },
            {
                "stem": "(audio) What are participants asked to bring if possible?",
                "choices": {
                    "A": "A bag of food.",
                    "B": "A water bowl.",
                    "C": "Their own brush.",
                    "D": "A large cage."
                },
                "answer": "C",
                "rationale": "They should bring their own brush if they have one."
            },
        ],
    },

    # 14. 市民プールの注意
    {
        "level": "A2",
        "topic": ["pool", "rules"],
        "script": (
            "Welcome to the city swimming pool. "
            "Before entering the water, please take a shower and do some light stretching. "
            "Running around the pool is dangerous, so always walk. "
            "Children must stay with an adult at all times."
        ),
        "questions": [
            {
                "stem": "(audio) What should visitors do before entering the pool?",
                "choices": {
                    "A": "Eat a big meal.",
                    "B": "Take a shower and stretch.",
                    "C": "Run around the pool.",
                    "D": "Turn off the lights."
                },
                "answer": "B",
                "rationale": "They are told to shower and stretch."
            },
            {
                "stem": "(audio) What activity is said to be dangerous?",
                "choices": {
                    "A": "Walking slowly.",
                    "B": "Swimming in the deep end.",
                    "C": "Running around the pool.",
                    "D": "Using a towel."
                },
                "answer": "C",
                "rationale": "Running is called dangerous."
            },
            {
                "stem": "(audio) What is required for children?",
                "choices": {
                    "A": "They must swim alone.",
                    "B": "They must stay with an adult.",
                    "C": "They must wait in the car.",
                    "D": "They must bring their own life guard."
                },
                "answer": "B",
                "rationale": "Children must always be with an adult."
            },
        ],
    },

    # 15. レストランのランチタイム案内
    {
        "level": "A2",
        "topic": ["restaurant", "lunch time"],
        "script": (
            "Thank you for coming to Garden Lunch Restaurant. "
            "Our lunch menu is available from eleven thirty a.m. to two p.m. "
            "All lunch sets include a small salad and a drink. "
            "Please place your order at the counter first and then take any free seat."
        ),
        "questions": [
            {
                "stem": "(audio) What time does the lunch menu end?",
                "choices": {
                    "A": "At noon.",
                    "B": "At one p.m.",
                    "C": "At two p.m.",
                    "D": "At three p.m."
                },
                "answer": "C",
                "rationale": "Lunch is served until two p.m."
            },
            {
                "stem": "(audio) What is included with every lunch set?",
                "choices": {
                    "A": "A soup and dessert.",
                    "B": "A salad and a drink.",
                    "C": "Two main dishes.",
                    "D": "A free lunch box."
                },
                "answer": "B",
                "rationale": "Each set has a small salad and a drink."
            },
            {
                "stem": "(audio) What should customers do before sitting down?",
                "choices": {
                    "A": "Reserve a table online.",
                    "B": "Wait for staff to choose a seat.",
                    "C": "Order at the counter.",
                    "D": "Pay after eating."
                },
                "answer": "C",
                "rationale": "They must order at the counter first."
            },
        ],
    },

    # 16. コインランドリーの案内
    {
        "level": "A2",
        "topic": ["laundromat", "usage"],
        "script": (
            "Welcome to Clean Spin Laundromat. "
            "To use a washing machine, first put in your clothes and then add detergent. "
            "Next, insert coins and press the start button. "
            "Please do not leave your laundry in the machines after it finishes."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of place is being described?",
                "choices": {
                    "A": "A book store.",
                    "B": "A laundromat.",
                    "C": "A movie theater.",
                    "D": "A bus station."
                },
                "answer": "B",
                "rationale": "The announcement talks about washing machines and coins."
            },
            {
                "stem": "(audio) What should customers do after inserting coins?",
                "choices": {
                    "A": "Turn off the power.",
                    "B": "Call the staff.",
                    "C": "Press the start button.",
                    "D": "Remove the detergent."
                },
                "answer": "C",
                "rationale": "They must press the start button to begin."
            },
            {
                "stem": "(audio) What are customers asked NOT to do?",
                "choices": {
                    "A": "Use the machines at night.",
                    "B": "Talk to other people.",
                    "C": "Leave laundry in machines after it finishes.",
                    "D": "Wash more than once a day."
                },
                "answer": "C",
                "rationale": "They should not leave laundry in the machines."
            },
        ],
    },

    # 17. コンビニのコピー機案内
    {
        "level": "A2",
        "topic": ["convenience store", "copy machine"],
        "script": (
            "Thank you for using Green Corner Convenience Store. "
            "Our copy machine is next to the drink cooler. "
            "You can make black-and-white copies and color copies there. "
            "If you need help, please press the call button and a staff member will come."
        ),
        "questions": [
            {
                "stem": "(audio) Where is the copy machine located?",
                "choices": {
                    "A": "Behind the cash register.",
                    "B": "Next to the drink cooler.",
                    "C": "In front of the store.",
                    "D": "Inside the storage room."
                },
                "answer": "B",
                "rationale": "It is next to the drink cooler."
            },
            {
                "stem": "(audio) What kind of copies can customers make?",
                "choices": {
                    "A": "Only color copies.",
                    "B": "Only black-and-white copies.",
                    "C": "Black-and-white and color copies.",
                    "D": "Only photo prints."
                },
                "answer": "C",
                "rationale": "Both black-and-white and color copies are possible."
            },
            {
                "stem": "(audio) How can customers ask for help?",
                "choices": {
                    "A": "By calling the manager on the phone.",
                    "B": "By pressing the call button.",
                    "C": "By writing on a form.",
                    "D": "By sending an e-mail."
                },
                "answer": "B",
                "rationale": "They should press the call button."
            },
        ],
    },

    # 18. 中学校の昼休みの注意
    {
        "level": "A2",
        "topic": ["school", "lunch break"],
        "script": (
            "Students, please listen. "
            "During lunch break, you may eat in the classroom or in the cafeteria. "
            "Running in the hallways is not allowed. "
            "After you finish eating, please throw away your trash and return your tray."
        ),
        "questions": [
            {
                "stem": "(audio) Where can students eat lunch?",
                "choices": {
                    "A": "Only outside.",
                    "B": "In the classroom or cafeteria.",
                    "C": "Only in the gym.",
                    "D": "Only at home."
                },
                "answer": "B",
                "rationale": "They can eat in either place."
            },
            {
                "stem": "(audio) What is NOT allowed during lunch break?",
                "choices": {
                    "A": "Talking with friends.",
                    "B": "Walking slowly.",
                    "C": "Running in the hallways.",
                    "D": "Sitting in the classroom."
                },
                "answer": "C",
                "rationale": "Running in the hallways is not allowed."
            },
            {
                "stem": "(audio) What should students do after eating?",
                "choices": {
                    "A": "Leave their tray on the table.",
                    "B": "Take a nap in the classroom.",
                    "C": "Throw away trash and return the tray.",
                    "D": "Go home right away."
                },
                "answer": "C",
                "rationale": "They should clean up by throwing trash away and returning the tray."
            },
        ],
    },

    # 19. シェアオフィスの利用ルール
    {
        "level": "A2",
        "topic": ["shared office", "rules"],
        "script": (
            "Welcome to Bright Desk Shared Office. "
            "Please keep your voice low when you talk on the phone. "
            "If you want to have a long meeting, use the small meeting room. "
            "Drinks with lids are allowed, but food is not permitted at the desks."
        ),
        "questions": [
            {
                "stem": "(audio) What is the speaker explaining?",
                "choices": {
                    "A": "How to pay the rent.",
                    "B": "Rules for using the shared office.",
                    "C": "The Wi-Fi password.",
                    "D": "Parking directions."
                },
                "answer": "B",
                "rationale": "It explains office use rules."
            },
            {
                "stem": "(audio) Where should users have long meetings?",
                "choices": {
                    "A": "At the main desks.",
                    "B": "In the hallway.",
                    "C": "In the small meeting room.",
                    "D": "At a nearby café."
                },
                "answer": "C",
                "rationale": "Long meetings belong in the meeting room."
            },
            {
                "stem": "(audio) What is said about drinks and food?",
                "choices": {
                    "A": "No drinks or food are allowed.",
                    "B": "Drinks and food are free.",
                    "C": "Only food is allowed at the desks.",
                    "D": "Drinks with lids are allowed but food is not."
                },
                "answer": "D",
                "rationale": "Drinks with lids are okay; food is not."
            },
        ],
    },

    # 20. マンションのゴミ出しルール
    {
        "level": "A2",
        "topic": ["apartment", "trash rules"],
        "script": (
            "Dear residents, this is a notice from the apartment manager. "
            "Burnable trash is collected on Monday and Thursday mornings. "
            "Please put your trash bags in the garbage area before eight a.m. on those days. "
            "Do not leave bags in the hallway."
        ),
        "questions": [
            {
                "stem": "(audio) When is burnable trash collected?",
                "choices": {
                    "A": "On Monday and Thursday.",
                    "B": "On Wednesday and Friday.",
                    "C": "Only on weekends.",
                    "D": "Every night."
                },
                "answer": "A",
                "rationale": "Burnable trash is collected twice a week on those days."
            },
            {
                "stem": "(audio) Where should residents place trash bags?",
                "choices": {
                    "A": "In front of their doors.",
                    "B": "In the parking lot.",
                    "C": "In the garbage area.",
                    "D": "On the stairs."
                },
                "answer": "C",
                "rationale": "Bags must be put in the garbage area."
            },
            {
                "stem": "(audio) What are residents told NOT to do?",
                "choices": {
                    "A": "Use clear trash bags.",
                    "B": "Take the elevator in the morning.",
                    "C": "Leave trash bags in the hallway.",
                    "D": "Talk to the apartment manager."
                },
                "answer": "C",
                "rationale": "They must not leave bags in the hallway."
            },
        ],
    },

    # 21. 自転車店の点検サービス
    {
        "level": "A2",
        "topic": ["bicycle shop", "check-up"],
        "script": (
            "Welcome to Sunny Wheels Bicycle Shop. "
            "Every Wednesday, we offer a free safety check for your bicycle. "
            "We look at the brakes, tires, and lights. "
            "If you are interested, please bring your bicycle to the back service area."
        ),
        "questions": [
            {
                "stem": "(audio) What special service is offered on Wednesdays?",
                "choices": {
                    "A": "A free helmet.",
                    "B": "A free safety check.",
                    "C": "A free repair for all parts.",
                    "D": "Free bicycle rental."
                },
                "answer": "B",
                "rationale": "They offer a free safety check."
            },
            {
                "stem": "(audio) Which parts are checked?",
                "choices": {
                    "A": "Only the bell.",
                    "B": "Only the chain.",
                    "C": "The brakes, tires, and lights.",
                    "D": "The seat and basket only."
                },
                "answer": "C",
                "rationale": "Brakes, tires, and lights are checked."
            },
            {
                "stem": "(audio) Where should customers bring their bicycles?",
                "choices": {
                    "A": "To the front entrance.",
                    "B": "To the back service area.",
                    "C": "To the parking garage.",
                    "D": "To the supermarket next door."
                },
                "answer": "B",
                "rationale": "They must go to the back service area."
            },
        ],
    },

    # 22. 小さな映画会の案内
    {
        "level": "A2",
        "topic": ["community center", "movie night"],
        "script": (
            "Good afternoon. "
            "This Friday evening, we will show a family movie at the community center hall. "
            "The movie starts at six thirty p.m., and entrance is free. "
            "You may bring a light snack, but please keep the hall clean."
        ),
        "questions": [
            {
                "stem": "(audio) What event will happen on Friday evening?",
                "choices": {
                    "A": "A sports game.",
                    "B": "A family movie showing.",
                    "C": "An English class.",
                    "D": "A cooking lesson."
                },
                "answer": "B",
                "rationale": "They will show a family movie."
            },
            {
                "stem": "(audio) How much does it cost to enter?",
                "choices": {
                    "A": "There is no charge.",
                    "B": "500 yen per person.",
                    "C": "1,000 yen per family.",
                    "D": "The price changes every week."
                },
                "answer": "A",
                "rationale": "Entrance is free."
            },
            {
                "stem": "(audio) What are visitors asked to do regarding snacks?",
                "choices": {
                    "A": "Buy snacks at the door.",
                    "B": "Bring a full dinner.",
                    "C": "Not eat anything at all.",
                    "D": "Keep the hall clean if they bring snacks."
                },
                "answer": "D",
                "rationale": "They may bring a snack but must keep the hall clean."
            },
        ],
    },

    # 23. 本屋の読み聞かせ会
    {
        "level": "A2",
        "topic": ["bookstore", "story time"],
        "script": (
            "Welcome to Sunrise Bookstore. "
            "On Saturday morning, we will have a story time for children in the kids’ corner. "
            "It begins at eleven a.m. and lasts about thirty minutes. "
            "Parents can sit with their children and listen together."
        ),
        "questions": [
            {
                "stem": "(audio) What special activity will the bookstore offer?",
                "choices": {
                    "A": "A writing class for adults.",
                    "B": "A story time for children.",
                    "C": "A book-signing event.",
                    "D": "A language exam."
                },
                "answer": "B",
                "rationale": "It is a story time event."
            },
            {
                "stem": "(audio) How long will the story time last?",
                "choices": {
                    "A": "About ten minutes.",
                    "B": "About thirty minutes.",
                    "C": "About one hour.",
                    "D": "About two hours."
                },
                "answer": "B",
                "rationale": "It lasts about thirty minutes."
            },
            {
                "stem": "(audio) What can parents do during the event?",
                "choices": {
                    "A": "Leave their children at the door.",
                    "B": "Sit with their children and listen.",
                    "C": "Work in the office upstairs.",
                    "D": "Return books to the library."
                },
                "answer": "B",
                "rationale": "Parents may sit with their children and listen."
            },
        ],
    },

    # 24. コワーキングスペースのWi-Fi案内
    {
        "level": "A2",
        "topic": ["coworking", "Wi-Fi"],
        "script": (
            "Hello and welcome to River Space Coworking. "
            "Free Wi-Fi is available in all areas. "
            "The network name and password are written on the white board near the entrance. "
            "Please do not share the password outside this space."
        ),
        "questions": [
            {
                "stem": "(audio) What service is free at the coworking space?",
                "choices": {
                    "A": "Printing in color.",
                    "B": "Coffee and tea.",
                    "C": "Wi-Fi access.",
                    "D": "Locker rental."
                },
                "answer": "C",
                "rationale": "Free Wi-Fi is available."
            },
            {
                "stem": "(audio) Where can users find the network information?",
                "choices": {
                    "A": "On the floor.",
                    "B": "On the white board near the entrance.",
                    "C": "Only on the website.",
                    "D": "On each desk."
                },
                "answer": "B",
                "rationale": "Network name and password are on the white board."
            },
            {
                "stem": "(audio) What are users asked not to do with the password?",
                "choices": {
                    "A": "Write it in their notebook.",
                    "B": "Use it on their devices.",
                    "C": "Share it outside the space.",
                    "D": "Change it every day."
                },
                "answer": "C",
                "rationale": "They should not share the password outside."
            },
        ],
    },

    # 25. 市営駐車場の夜間閉鎖
    {
        "level": "A2",
        "topic": ["parking", "closing"],
        "script": (
            "This is a notice from Riverside City Parking. "
            "The parking lot will close at ten p.m. tonight. "
            "If your car is still inside after that time, you cannot take it out until tomorrow morning. "
            "Please move your car before closing time."
        ),
        "questions": [
            {
                "stem": "(audio) What is announced about the parking lot?",
                "choices": {
                    "A": "It will open all night.",
                    "B": "It will close at ten p.m.",
                    "C": "It is free today.",
                    "D": "It will move to another street."
                },
                "answer": "B",
                "rationale": "The parking lot closes at ten p.m."
            },
            {
                "stem": "(audio) What happens if a car stays after closing?",
                "choices": {
                    "A": "It will be washed for free.",
                    "B": "It will be moved to the road.",
                    "C": "It cannot be taken out until morning.",
                    "D": "It will be given a free ticket."
                },
                "answer": "C",
                "rationale": "Cars cannot leave until the next morning."
            },
            {
                "stem": "(audio) What are drivers asked to do?",
                "choices": {
                    "A": "Pay more money after ten p.m.",
                    "B": "Move their cars before closing time.",
                    "C": "Call the police about their cars.",
                    "D": "Leave their keys at the office."
                },
                "answer": "B",
                "rationale": "Drivers should move cars before ten p.m."
            },
        ],
    },

    # 26. 市民センターの英会話サロン
    {
        "level": "A2",
        "topic": ["community center", "English conversation"],
        "script": (
            "Thank you for calling Hilltop Community Center. "
            "Every Tuesday evening, we hold a simple English conversation salon for adults. "
            "It starts at seven p.m. and no reservation is needed. "
            "Please come to Room 3 on the second floor if you are interested."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of activity is held on Tuesday evenings?",
                "choices": {
                    "A": "A cooking class.",
                    "B": "An English conversation salon.",
                    "C": "A music lesson.",
                    "D": "A movie club."
                },
                "answer": "B",
                "rationale": "It is a simple English conversation salon."
            },
            {
                "stem": "(audio) What time does the salon begin?",
                "choices": {
                    "A": "At six p.m.",
                    "B": "At seven p.m.",
                    "C": "At eight p.m.",
                    "D": "At nine p.m."
                },
                "answer": "B",
                "rationale": "It begins at seven p.m."
            },
            {
                "stem": "(audio) What is said about reservations?",
                "choices": {
                    "A": "They are required one week in advance.",
                    "B": "They are required by e-mail.",
                    "C": "No reservation is needed.",
                    "D": "Only teachers can reserve seats."
                },
                "answer": "C",
                "rationale": "People can join without a reservation."
            },
        ],
    },

    # 27. 町内会の防災訓練
    {
        "level": "A2",
        "topic": ["neighborhood", "disaster drill"],
        "script": (
            "Residents of Green Hill, this is a notice about our disaster drill. "
            "Next Sunday at ten a.m., we will practice how to move to the emergency shelter. "
            "Please meet in front of the small park. "
            "Bring comfortable shoes and a hat if the weather is sunny."
        ),
        "questions": [
            {
                "stem": "(audio) What will residents practice next Sunday?",
                "choices": {
                    "A": "How to drive cars.",
                    "B": "How to move to the emergency shelter.",
                    "C": "How to fix broken windows.",
                    "D": "How to cook for a party."
                },
                "answer": "B",
                "rationale": "They will practice going to the emergency shelter."
            },
            {
                "stem": "(audio) Where should residents meet?",
                "choices": {
                    "A": "Inside the school gym.",
                    "B": "In front of the small park.",
                    "C": "At the bus stop.",
                    "D": "In the city hall lobby."
                },
                "answer": "B",
                "rationale": "They will gather in front of the park."
            },
            {
                "stem": "(audio) What items are suggested if it is sunny?",
                "choices": {
                    "A": "A camera and umbrella.",
                    "B": "Formal clothes and shoes.",
                    "C": "Comfortable shoes and a hat.",
                    "D": "Books and notebooks."
                },
                "answer": "C",
                "rationale": "Comfortable shoes and a hat are recommended."
            },
        ],
    },

    # 28. スポーツクラブの無料体験デー
    {
        "level": "A2",
        "topic": ["sports club", "free trial"],
        "script": (
            "Dear neighbors, this Saturday is free trial day at Blue Sky Sports Club. "
            "You can use the gym and the pool without paying. "
            "Please bring indoor shoes, a towel, and your own drink. "
            "Children under twelve must come with an adult."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about this Saturday at the sports club?",
                "choices": {
                    "A": "There will be a big competition.",
                    "B": "Only members can enter.",
                    "C": "It is a free trial day.",
                    "D": "The club will be closed."
                },
                "answer": "C",
                "rationale": "People can use the club for free."
            },
            {
                "stem": "(audio) Which facilities can visitors use?",
                "choices": {
                    "A": "Only the tennis courts.",
                    "B": "The gym and the pool.",
                    "C": "Only the restaurant.",
                    "D": "Only the parking lot."
                },
                "answer": "B",
                "rationale": "The gym and pool are available."
            },
            {
                "stem": "(audio) What is required for children under twelve?",
                "choices": {
                    "A": "They must come alone.",
                    "B": "They must bring homework.",
                    "C": "They must come with an adult.",
                    "D": "They must pay a special fee."
                },
                "answer": "C",
                "rationale": "Children under twelve must be with an adult."
            },
        ],
    },

    # 29. 市バスの運賃支払い方法
    {
        "level": "A2",
        "topic": ["city bus", "fare"],
        "script": (
            "This is a guide for city bus passengers. "
            "You can pay the fare with a bus card or with cash. "
            "If you pay with cash, please put coins or bills into the box next to the driver. "
            "Change is not given, so prepare the exact fare before you get on."
        ),
        "questions": [
            {
                "stem": "(audio) What is the announcement explaining?",
                "choices": {
                    "A": "Bus routes.",
                    "B": "How to pay the bus fare.",
                    "C": "Lost and found rules.",
                    "D": "Night bus schedules."
                },
                "answer": "B",
                "rationale": "It explains fare payment methods."
            },
            {
                "stem": "(audio) Where should passengers put cash?",
                "choices": {
                    "A": "On the seat next to them.",
                    "B": "In the box next to the driver.",
                    "C": "At the back of the bus.",
                    "D": "On the ticket machine outside."
                },
                "answer": "B",
                "rationale": "Cash goes into the box next to the driver."
            },
            {
                "stem": "(audio) What is said about change?",
                "choices": {
                    "A": "Change is always given.",
                    "B": "Change is only given at night.",
                    "C": "Change is not given.",
                    "D": "Change is sent by mail."
                },
                "answer": "C",
                "rationale": "Passengers must prepare the exact fare."
            },
        ],
    },

    # 30. 図書館の子どもコーナー利用案内
    {
        "level": "A2",
        "topic": ["library", "children area"],
        "script": (
            "Welcome to the children’s area of the city library. "
            "This space is for children and their families. "
            "Please keep bags and toys away from the walkways. "
            "After you finish reading, return books to the low shelves or give them to a librarian."
        ),
        "questions": [
            {
                "stem": "(audio) Who is the children’s area mainly for?",
                "choices": {
                    "A": "Office workers.",
                    "B": "Tour groups.",
                    "C": "Children and their families.",
                    "D": "Only librarians."
                },
                "answer": "C",
                "rationale": "It is a space for children and families."
            },
            {
                "stem": "(audio) Where should bags and toys NOT be placed?",
                "choices": {
                    "A": "On the low shelves.",
                    "B": "Behind the desk.",
                    "C": "In the walkways.",
                    "D": "Near the windows."
                },
                "answer": "C",
                "rationale": "They must be kept away from the walkways."
            },
            {
                "stem": "(audio) What should visitors do after reading books?",
                "choices": {
                    "A": "Hide them under the chairs.",
                    "B": "Take them home without checking out.",
                    "C": "Return them to the low shelves or to a librarian.",
                    "D": "Leave them anywhere on the floor."
                },
                "answer": "C",
                "rationale": "Books should go back to the shelves or to staff."
            },
        ],
    },

    # --- B1 level 100patterns (standard) ---
    # 1. 飛行機搭乗の案内
    {
        "level": "B1",
        "topic": ["airport", "delay"],
        "script": (
            "Good afternoon, passengers. "
            "This is an announcement for all travelers waiting for Flight 102 to Seattle. "
            "Due to heavy fog, the departure will be delayed for about thirty minutes. "
            "Please remain near Gate 12 and listen for further updates. "
            "We apologize for the inconvenience and thank you for your patience."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main purpose of the announcement?",
                "choices": {
                    "A": "To advertise a new flight route.",
                    "B": "To report a flight delay.",
                    "C": "To ask passengers to change seats.",
                    "D": "To cancel a flight."
                },
                "answer": "B",
                "rationale": "The speaker explains that the departure will be delayed."
            },
            {
                "stem": "(audio) What is causing the delay?",
                "choices": {
                    "A": "Mechanical problems.",
                    "B": "Heavy fog.",
                    "C": "A baggage issue.",
                    "D": "A crew change."
                },
                "answer": "B",
                "rationale": "The announcement mentions heavy fog as the reason."
            },
            {
                "stem": "(audio) What are passengers asked to do?",
                "choices": {
                    "A": "Go to another gate.",
                    "B": "Return to the check-in counter.",
                    "C": "Remain near Gate 12.",
                    "D": "Board the plane immediately."
                },
                "answer": "C",
                "rationale": "They are told to remain near Gate 12 and listen for updates."
            },
        ],
    },
    # 2. 会社の案内
    {
        "level": "B1",
        "topic": ["company", "orientation"],
        "script": (
            "Welcome to Greenfield Electronics. "
            "The orientation for new employees will begin at nine o’clock in Conference Room A. "
            "Please bring the documents you received at the reception desk. "
            "After the orientation, your supervisors will guide you to your departments. "
            "If you have any questions, feel free to ask our staff members."
        ),
        "questions": [
            {
                "stem": "(audio) Who is this announcement mainly for?",
                "choices": {
                    "A": "Company shareholders.",
                    "B": "Sales representatives.",
                    "C": "New employees.",
                    "D": "Delivery drivers."
                },
                "answer": "C",
                "rationale": "It mentions an orientation for new employees."
            },
            {
                "stem": "(audio) What are listeners asked to bring?",
                "choices": {
                    "A": "Their identification cards.",
                    "B": "The documents from reception.",
                    "C": "A laptop computer.",
                    "D": "Product samples."
                },
                "answer": "B",
                "rationale": "They are asked to bring the documents received at the reception desk."
            },
            {
                "stem": "(audio) What will happen after the orientation?",
                "choices": {
                    "A": "A factory tour will be held.",
                    "B": "Employees will have lunch.",
                    "C": "Supervisors will take them to their departments.",
                    "D": "A test will be given."
                },
                "answer": "C",
                "rationale": "Supervisors will guide them to their departments."
            },
        ],
    },
    # 3. 朝のラジオ
    {
        "level": "B1",
        "topic": ["radio", "event"],
        "script": (
            "You’re listening to City Morning Radio. "
            "This Saturday, the annual River Park Festival will be held from ten a.m. to five p.m. "
            "There will be live music, food trucks, and games for children. "
            "Admission is free, but parking spaces are limited, so we recommend using public transportation. "
            "For more details, visit our station’s website."
        ),
        "questions": [
            {
                "stem": "(audio) What is being announced?",
                "choices": {
                    "A": "A new radio program.",
                    "B": "A local festival.",
                    "C": "A charity concert.",
                    "D": "A store opening."
                },
                "answer": "B",
                "rationale": "It describes the annual River Park Festival."
            },
            {
                "stem": "(audio) What is said about admission?",
                "choices": {
                    "A": "It is free.",
                    "B": "It includes a free meal.",
                    "C": "It is only for children.",
                    "D": "It must be reserved in advance."
                },
                "answer": "A",
                "rationale": "The announcement says admission is free."
            },
            {
                "stem": "(audio) Why are listeners encouraged to use public transportation?",
                "choices": {
                    "A": "Parking is expensive.",
                    "B": "The roads will be closed.",
                    "C": "Parking spaces are limited.",
                    "D": "Buses are free on weekends."
                },
                "answer": "C",
                "rationale": "Because parking spaces are limited."
            },
        ],
    },

    # 4. 図書館の案内
    {
        "level": "B1",
        "topic": ["library", "notice"],
        "script": (
            "Attention, library visitors. "
            "The second-floor reading room will close at six p.m. today for maintenance. "
            "Please borrow or return any materials before that time. "
            "The first-floor study area will remain open until the usual closing time. "
            "We appreciate your understanding and cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) Why will the second-floor reading room close early?",
                "choices": {
                    "A": "For a special event.",
                    "B": "For maintenance.",
                    "C": "Because of bad weather.",
                    "D": "Because of a power failure."
                },
                "answer": "B",
                "rationale": "The room will close for maintenance."
            },
            {
                "stem": "(audio) By what time should visitors borrow or return materials?",
                "choices": {
                    "A": "By five p.m.",
                    "B": "By six p.m.",
                    "C": "By seven p.m.",
                    "D": "By eight p.m."
                },
                "answer": "B",
                "rationale": "They are asked to do so before six p.m."
            },
            {
                "stem": "(audio) What is said about the first-floor study area?",
                "choices": {
                    "A": "It will also close at six p.m.",
                    "B": "It will be closed all day.",
                    "C": "It will remain open as usual.",
                    "D": "It is only for staff members."
                },
                "answer": "C",
                "rationale": "The first-floor study area will stay open until the usual closing time."
            },
        ],
    },

    # 5. スーパーマーケットのセール
    {
        "level": "B1",
        "topic": ["supermarket", "sale"],
        "script": (
            "Good morning, shoppers. "
            "Today only, our supermarket is offering a special discount on fresh fruits and vegetables. "
            "You can save up to thirty percent on selected items marked with red labels. "
            "We also have free samples near the entrance of the produce section. "
            "Please enjoy your shopping and thank you for coming."
        ),
        "questions": [
            {
                "stem": "(audio) What is being offered today?",
                "choices": {
                    "A": "Free parking.",
                    "B": "Discounts on fresh produce.",
                    "C": "Cheaper household appliances.",
                    "D": "A free delivery service."
                },
                "answer": "B",
                "rationale": "Special discounts apply to fresh fruits and vegetables."
            },
            {
                "stem": "(audio) How can customers find the discounted items?",
                "choices": {
                    "A": "They are marked with red labels.",
                    "B": "They are in a separate building.",
                    "C": "They are only available online.",
                    "D": "They are behind the service counter."
                },
                "answer": "A",
                "rationale": "Discounted items are marked with red labels."
            },
            {
                "stem": "(audio) Where are the free samples located?",
                "choices": {
                    "A": "At the customer service desk.",
                    "B": "Near the exit doors.",
                    "C": "Next to the bakery.",
                    "D": "Near the entrance of the produce section."
                },
                "answer": "D",
                "rationale": "Free samples are near the produce section entrance."
            },
        ],
    },

    # 6. オフィスビルの防災訓練
    {
        "level": "B1",
        "topic": ["office building", "drill"],
        "script": (
            "Attention all employees. "
            "A fire drill will be conducted at two p.m. this afternoon. "
            "When you hear the alarm, please leave the building calmly using the nearest emergency exit. "
            "Do not use the elevators during the drill. "
            "Your cooperation is important for everyone’s safety."
        ),
        "questions": [
            {
                "stem": "(audio) What event is being announced?",
                "choices": {
                    "A": "A company party.",
                    "B": "A fire drill.",
                    "C": "An equipment inspection.",
                    "D": "A staff meeting."
                },
                "answer": "B",
                "rationale": "The announcement is about a fire drill."
            },
            {
                "stem": "(audio) What should employees do when they hear the alarm?",
                "choices": {
                    "A": "Wait at their desks.",
                    "B": "Use the elevator.",
                    "C": "Leave the building calmly.",
                    "D": "Call the security office."
                },
                "answer": "C",
                "rationale": "They are told to leave the building calmly."
            },
            {
                "stem": "(audio) What are employees told NOT to use?",
                "choices": {
                    "A": "The stairs.",
                    "B": "The side entrance.",
                    "C": "The parking lot.",
                    "D": "The elevators."
                },
                "answer": "D",
                "rationale": "They are instructed not to use the elevators."
            },
        ],
    },

    # 7. バス路線の変更
    {
        "level": "B1",
        "topic": ["bus", "route change"],
        "script": (
            "This is an announcement from the City Bus Company. "
            "Starting next Monday, the timetable and route for Bus Number 25 will change. "
            "The bus will no longer stop at Central Park Station. "
            "Instead, it will stop at Riverside Plaza. "
            "Please check the updated schedule on our website or at bus stops."
        ),
        "questions": [
            {
                "stem": "(audio) What will change about Bus Number 25?",
                "choices": {
                    "A": "Its driver.",
                    "B": "Its color.",
                    "C": "Its timetable and route.",
                    "D": "Its ticket price."
                },
                "answer": "C",
                "rationale": "Both the timetable and route will change."
            },
            {
                "stem": "(audio) Where will the bus no longer stop?",
                "choices": {
                    "A": "Riverside Plaza.",
                    "B": "Central Park Station.",
                    "C": "The airport terminal.",
                    "D": "The city hall."
                },
                "answer": "B",
                "rationale": "The bus will no longer stop at Central Park Station."
            },
            {
                "stem": "(audio) Where can passengers find the new schedule?",
                "choices": {
                    "A": "Only at the city hall.",
                    "B": "At the airport counter.",
                    "C": "On the website or at bus stops.",
                    "D": "In local newspapers only."
                },
                "answer": "C",
                "rationale": "They are told to check the website or bus stops."
            },
        ],
    },

    # 8. 美術館の特別展
    {
        "level": "B1",
        "topic": ["museum", "special exhibition"],
        "script": (
            "Welcome to the City Art Museum. "
            "From this Friday, we will hold a special exhibition of modern photography. "
            "The exhibition will run for three weeks and is located in Gallery 2 on the third floor. "
            "Audio guides are available in three languages at the entrance. "
            "We hope you enjoy your visit."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of exhibition will be held?",
                "choices": {
                    "A": "Traditional paintings.",
                    "B": "Modern photography.",
                    "C": "Historical sculptures.",
                    "D": "Children’s drawings."
                },
                "answer": "B",
                "rationale": "It is a special exhibition of modern photography."
            },
            {
                "stem": "(audio) Where is the exhibition located?",
                "choices": {
                    "A": "On the first floor.",
                    "B": "In Gallery 1.",
                    "C": "In Gallery 2 on the third floor.",
                    "D": "In the basement hall."
                },
                "answer": "C",
                "rationale": "It is in Gallery 2 on the third floor."
            },
            {
                "stem": "(audio) What extra service is mentioned?",
                "choices": {
                    "A": "Free parking.",
                    "B": "Guided tours by artists.",
                    "C": "Audio guides in three languages.",
                    "D": "Discounted tickets on weekends."
                },
                "answer": "C",
                "rationale": "Audio guides are available in three languages."
            },
        ],
    },

    # 9. ジムの会員向け案内
    {
        "level": "B1",
        "topic": ["gym", "membership"],
        "script": (
            "Dear gym members, "
            "please note that the fitness center will be closed next Tuesday for equipment inspection. "
            "All group exercise classes on that day will be canceled. "
            "Your membership will be extended by one day automatically. "
            "Thank you for your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) Why will the fitness center be closed?",
                "choices": {
                    "A": "For staff training.",
                    "B": "For equipment inspection.",
                    "C": "For building renovation.",
                    "D": "For a private event."
                },
                "answer": "B",
                "rationale": "It will close for equipment inspection."
            },
            {
                "stem": "(audio) What will happen to group exercise classes on that day?",
                "choices": {
                    "A": "They will be held as usual.",
                    "B": "They will be held online.",
                    "C": "They will be postponed to next week.",
                    "D": "They will be canceled."
                },
                "answer": "D",
                "rationale": "All group classes on that day will be canceled."
            },
            {
                "stem": "(audio) What happens to the members’ contracts?",
                "choices": {
                    "A": "They will not change.",
                    "B": "They will be shortened.",
                    "C": "They will be extended by one day.",
                    "D": "They will be canceled."
                },
                "answer": "C",
                "rationale": "Membership is automatically extended by one day."
            },
        ],
    },

    # 10. カフェの新メニュー紹介
    {
        "level": "B1",
        "topic": ["cafe", "new menu"],
        "script": (
            "Thank you for visiting Starleaf Café. "
            "We are happy to introduce our new seasonal drinks, including iced matcha latte and citrus herb tea. "
            "These items are available only until the end of next month. "
            "Customers who order a seasonal drink will receive a small cookie for free. "
            "Please try them while they last."
        ),
        "questions": [
            {
                "stem": "(audio) What is being introduced?",
                "choices": {
                    "A": "A new breakfast menu.",
                    "B": "Seasonal drinks.",
                    "C": "A catering service.",
                    "D": "A loyalty card program."
                },
                "answer": "B",
                "rationale": "The café introduces new seasonal drinks."
            },
            {
                "stem": "(audio) Until when are the new items available?",
                "choices": {
                    "A": "Until this weekend.",
                    "B": "Until the end of this month.",
                    "C": "Until the end of next month.",
                    "D": "Until the end of the year."
                },
                "answer": "C",
                "rationale": "They are available until the end of next month."
            },
            {
                "stem": "(audio) What benefit do customers get with a seasonal drink?",
                "choices": {
                    "A": "A discount coupon.",
                    "B": "A free drink refill.",
                    "C": "A free small cookie.",
                    "D": "A larger size."
                },
                "answer": "C",
                "rationale": "Customers receive a small cookie for free."
            },
        ],
    },

    # 11. オンラインセミナー案内
    {
        "level": "B1",
        "topic": ["webinar", "registration"],
        "script": (
            "Thank you for your interest in our online seminar on time management. "
            "The seminar will be held next Thursday from seven to eight thirty p.m. "
            "Participation is free, but advance registration is required. "
            "Please visit our website and fill out the registration form by Tuesday. "
            "A link to join the seminar will be sent to your e-mail address."
        ),
        "questions": [
            {
                "stem": "(audio) What is the topic of the seminar?",
                "choices": {
                    "A": "Customer service skills.",
                    "B": "Time management.",
                    "C": "Business writing.",
                    "D": "Public speaking."
                },
                "answer": "B",
                "rationale": "The seminar focuses on time management."
            },
            {
                "stem": "(audio) What must participants do before attending?",
                "choices": {
                    "A": "Pay a fee at the bank.",
                    "B": "Visit the office in person.",
                    "C": "Register on the website.",
                    "D": "Send a fax to the organizer."
                },
                "answer": "C",
                "rationale": "They must complete an online registration form."
            },
            {
                "stem": "(audio) How will participants receive the seminar link?",
                "choices": {
                    "A": "By text message.",
                    "B": "By regular mail.",
                    "C": "By e-mail.",
                    "D": "By phone call."
                },
                "answer": "C",
                "rationale": "The link will be sent to their e-mail address."
            },
        ],
    },

    # 12. ホテルの朝食案内
    {
        "level": "B1",
        "topic": ["hotel", "breakfast"],
        "script": (
            "Good evening, guests. "
            "We would like to inform you about our breakfast service. "
            "A buffet breakfast is served on the second floor restaurant from six thirty to ten a.m. "
            "Guests who have breakfast included in their plan can enter by showing their room key. "
            "If it is not included, you can still enjoy breakfast for an additional fee at the counter."
        ),
        "questions": [
            {
                "stem": "(audio) Where is the breakfast served?",
                "choices": {
                    "A": "In the lobby.",
                    "B": "On the second floor restaurant.",
                    "C": "On the rooftop terrace.",
                    "D": "In the guest rooms only."
                },
                "answer": "B",
                "rationale": "Breakfast is served in the second floor restaurant."
            },
            {
                "stem": "(audio) How can guests with breakfast included enter?",
                "choices": {
                    "A": "By signing a form.",
                    "B": "By paying at the counter.",
                    "C": "By showing their room key.",
                    "D": "By making a reservation."
                },
                "answer": "C",
                "rationale": "They only need to show their room key."
            },
            {
                "stem": "(audio) What can guests without breakfast included do?",
                "choices": {
                    "A": "They cannot use the restaurant.",
                    "B": "They must cook in their room.",
                    "C": "They can pay an extra fee at the counter.",
                    "D": "They must eat before six thirty."
                },
                "answer": "C",
                "rationale": "They can still eat by paying an additional fee."
            },
        ],
    },

    # 13. ショッピングモールの閉店時間
    {
        "level": "B1",
        "topic": ["shopping mall", "closing time"],
        "script": (
            "Attention, shoppers. "
            "Our shopping mall will close in thirty minutes. "
            "Please make your final purchases and proceed to the checkouts. "
            "The main entrance on the first floor will remain open until closing time. "
            "Thank you for shopping with us and have a safe trip home."
        ),
        "questions": [
            {
                "stem": "(audio) When will the mall close?",
                "choices": {
                    "A": "In ten minutes.",
                    "B": "In twenty minutes.",
                    "C": "In thirty minutes.",
                    "D": "In one hour."
                },
                "answer": "C",
                "rationale": "The announcement says the mall will close in thirty minutes."
            },
            {
                "stem": "(audio) What are customers asked to do?",
                "choices": {
                    "A": "Return all items.",
                    "B": "Go to the information desk.",
                    "C": "Move to the parking area.",
                    "D": "Finish shopping and go to the checkouts."
                },
                "answer": "D",
                "rationale": "They should make final purchases and proceed to checkouts."
            },
            {
                "stem": "(audio) What is said about the main entrance?",
                "choices": {
                    "A": "It is already closed.",
                    "B": "It will stay open until closing time.",
                    "C": "It is only for staff members.",
                    "D": "It will be moved to the second floor."
                },
                "answer": "B",
                "rationale": "The main entrance remains open until closing time."
            },
        ],
    },

    # 14. 公民館の講座案内
    {
        "level": "B1",
        "topic": ["community center", "class"],
        "script": (
            "This is an announcement from the Riverside Community Center. "
            "We will start a new evening class in basic computer skills next month. "
            "The class will be held every Wednesday from seven to eight thirty p.m. "
            "The fee for the entire course is three thousand yen. "
            "If you are interested, please sign up at the reception desk."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of class will start next month?",
                "choices": {
                    "A": "Basic computer skills.",
                    "B": "Foreign language conversation.",
                    "C": "Cooking for beginners.",
                    "D": "Yoga and stretching."
                },
                "answer": "A",
                "rationale": "The class teaches basic computer skills."
            },
            {
                "stem": "(audio) How often will the class be held?",
                "choices": {
                    "A": "Every day.",
                    "B": "Every Monday.",
                    "C": "Every Wednesday evening.",
                    "D": "Every weekend."
                },
                "answer": "C",
                "rationale": "It takes place every Wednesday evening."
            },
            {
                "stem": "(audio) What should interested people do?",
                "choices": {
                    "A": "Call the city office.",
                    "B": "Send an e-mail to the teacher.",
                    "C": "Visit the website.",
                    "D": "Sign up at the reception desk."
                },
                "answer": "D",
                "rationale": "They are told to sign up at the reception desk."
            },
        ],
    },

    # 15. オンラインショップからの発送案内
    {
        "level": "B1",
        "topic": ["online shop", "shipping"],
        "script": (
            "Thank you for shopping with BlueSky Online Store. "
            "Your order has been shipped and is expected to arrive within three business days. "
            "You can track your package using the number sent to your e-mail. "
            "If you are not at home, the delivery company will leave a notice. "
            "Please contact them directly to arrange redelivery if necessary."
        ),
        "questions": [
            {
                "stem": "(audio) What is the purpose of this message?",
                "choices": {
                    "A": "To confirm payment.",
                    "B": "To announce a sale.",
                    "C": "To inform the customer about shipping.",
                    "D": "To cancel an order."
                },
                "answer": "C",
                "rationale": "It explains that the order has been shipped."
            },
            {
                "stem": "(audio) How can the customer check the delivery status?",
                "choices": {
                    "A": "By visiting the store.",
                    "B": "By using the tracking number.",
                    "C": "By calling the post office.",
                    "D": "By asking a neighbor."
                },
                "answer": "B",
                "rationale": "They can track the package using the number in the e-mail."
            },
            {
                "stem": "(audio) What happens if the customer is not at home?",
                "choices": {
                    "A": "The package will be left at the door.",
                    "B": "The order will be returned immediately.",
                    "C": "The delivery company will leave a notice.",
                    "D": "The customer will be charged extra."
                },
                "answer": "C",
                "rationale": "A notice will be left so the customer can arrange redelivery."
            },
        ],
    },
    
    # 16. 期末試験の案内
    {
        "level": "B1",
        "topic": ["school", "final exam"],
        "script": (
            "Students, may I have your attention, please. "
            "Final exams will begin next Monday and continue for three days. "
            "All students must bring their student ID cards to every exam. "
            "Please check the detailed schedule on the bulletin board outside the teachers’ room. "
            "If you have any questions, ask your homeroom teacher."
        ),
        "questions": [
            {
                "stem": "(audio) What is this announcement about?",
                "choices": {
                    "A": "A school festival.",
                    "B": "Final exams.",
                    "C": "A class trip.",
                    "D": "A new school building."
                },
                "answer": "B",
                "rationale": "It explains when final exams will be held."
            },
            {
                "stem": "(audio) What must students bring to every exam?",
                "choices": {
                    "A": "Their textbooks.",
                    "B": "A calculator.",
                    "C": "Their student ID cards.",
                    "D": "A lunch box."
                },
                "answer": "C",
                "rationale": "They are told to bring student ID cards."
            },
            {
                "stem": "(audio) Where can students find the detailed schedule?",
                "choices": {
                    "A": "On the school website.",
                    "B": "On the classroom door.",
                    "C": "On the bulletin board near the gym.",
                    "D": "On the bulletin board outside the teachers’ room."
                },
                "answer": "D",
                "rationale": "The schedule is posted outside the teachers’ room."
            },
        ],
    },

    # 17. 放課後の自習室
    {
        "level": "B1",
        "topic": ["school", "study room"],
        "script": (
            "Attention, students. "
            "The after-school study room will be open from four p.m. to seven p.m. this week. "
            "You can use the room to prepare for exams or work on group projects. "
            "Please remember to keep your voices low and turn off your mobile phones. "
            "Teachers will be available to answer questions between five and six p.m."
        ),
        "questions": [
            {
                "stem": "(audio) What is the purpose of the study room?",
                "choices": {
                    "A": "To practice sports.",
                    "B": "To prepare for exams or projects.",
                    "C": "To hold club meetings.",
                    "D": "To watch movies."
                },
                "answer": "B",
                "rationale": "It is for exam preparation and group projects."
            },
            {
                "stem": "(audio) When will teachers be available to help?",
                "choices": {
                    "A": "From four to five.",
                    "B": "From five to six.",
                    "C": "From six to seven.",
                    "D": "From seven to eight."
                },
                "answer": "B",
                "rationale": "Teachers are available between five and six p.m."
            },
            {
                "stem": "(audio) What are students asked to do in the study room?",
                "choices": {
                    "A": "Discuss loudly.",
                    "B": "Bring food and drinks.",
                    "C": "Turn off their mobile phones.",
                    "D": "Use only the computers."
                },
                "answer": "C",
                "rationale": "They are told to keep voices low and turn off phones."
            },
        ],
    },

    # 18. クラブ紹介デイ
    {
        "level": "B1",
        "topic": ["school", "club introduction"],
        "script": (
            "Good morning, first-year students. "
            "This Friday, we will hold a club introduction day in the gym. "
            "From three to five p.m., each club will give a short presentation and show some activities. "
            "You can visit the booths and ask current members questions. "
            "We hope you find a club that matches your interests."
        ),
        "questions": [
            {
                "stem": "(audio) Who is this announcement mainly for?",
                "choices": {
                    "A": "First-year students.",
                    "B": "Parents.",
                    "C": "Teachers.",
                    "D": "Local residents."
                },
                "answer": "A",
                "rationale": "It is addressed to first-year students."
            },
            {
                "stem": "(audio) Where will the event take place?",
                "choices": {
                    "A": "In the library.",
                    "B": "In the cafeteria.",
                    "C": "In the gym.",
                    "D": "On the playground."
                },
                "answer": "C",
                "rationale": "The club introduction day will be held in the gym."
            },
            {
                "stem": "(audio) What can students do at the event?",
                "choices": {
                    "A": "Take entrance exams.",
                    "B": "Join classes for free.",
                    "C": "Watch movies.",
                    "D": "Talk with current club members."
                },
                "answer": "D",
                "rationale": "They can visit booths and ask members questions."
            },
        ],
    },

    # 19. 図書館の延長開館
    {
        "level": "B1",
        "topic": ["school", "library"],
        "script": (
            "This is an announcement from the school library. "
            "During the examination period, the library will stay open until eight p.m. on weekdays. "
            "Please show your student ID card at the entrance after six p.m. "
            "You may borrow up to five books at a time. "
            "We hope this helps you prepare for your exams."
        ),
        "questions": [
            {
                "stem": "(audio) What change is being announced?",
                "choices": {
                    "A": "The library will open on Sundays.",
                    "B": "The library will close earlier.",
                    "C": "The library will stay open later.",
                    "D": "The library will move to another building."
                },
                "answer": "C",
                "rationale": "The library will stay open until eight p.m."
            },
            {
                "stem": "(audio) What must students show after six p.m.?",
                "choices": {
                    "A": "A reservation ticket.",
                    "B": "Their student ID card.",
                    "C": "A library card from the city.",
                    "D": "A note from a teacher."
                },
                "answer": "B",
                "rationale": "They must show their student ID card at the entrance."
            },
            {
                "stem": "(audio) How many books may students borrow at a time?",
                "choices": {
                    "A": "Two.",
                    "B": "Three.",
                    "C": "Four.",
                    "D": "Five."
                },
                "answer": "D",
                "rationale": "Students may borrow up to five books."
            },
        ],
    },

    # 20. 運動会のお知らせ
    {
        "level": "B1",
        "topic": ["school", "sports day"],
        "script": (
            "Parents and guardians, thank you for coming to our school today. "
            "Our annual sports day will be held next Saturday on the school field. "
            "Events will begin at nine a.m. and finish around three p.m. "
            "Please bring hats and drinks to protect yourselves from the sun. "
            "If it rains, the event will be postponed to Sunday."
        ),
        "questions": [
            {
                "stem": "(audio) What event is being announced?",
                "choices": {
                    "A": "A music concert.",
                    "B": "A school festival.",
                    "C": "A sports day.",
                    "D": "A graduation ceremony."
                },
                "answer": "C",
                "rationale": "The announcement is about the annual sports day."
            },
            {
                "stem": "(audio) What are listeners advised to bring?",
                "choices": {
                    "A": "Umbrellas and boots.",
                    "B": "Hats and drinks.",
                    "C": "Snacks for students only.",
                    "D": "Sports equipment."
                },
                "answer": "B",
                "rationale": "They are asked to bring hats and drinks to avoid strong sun."
            },
            {
                "stem": "(audio) What will happen if it rains?",
                "choices": {
                    "A": "The event will be canceled.",
                    "B": "The event will be held indoors.",
                    "C": "The event will be postponed to Sunday.",
                    "D": "The event will start earlier."
                },
                "answer": "C",
                "rationale": "It will be postponed to Sunday if it rains."
            },
        ],
    },

    # 21. 市内観光パスの案内
    {
        "level": "B1",
        "topic": ["tourism", "city pass"],
        "script": (
            "Welcome to Lakeside City. "
            "For visitors who plan to see many sights, we recommend the one-day city pass. "
            "With this pass, you can ride all city buses and trams and receive discounts at several museums. "
            "The pass is available at the tourist information center and major stations. "
            "Please check the leaflet for details in English, Chinese, and Korean."
        ),
        "questions": [
            {
                "stem": "(audio) What is being recommended to visitors?",
                "choices": {
                    "A": "A hotel membership card.",
                    "B": "A one-day city pass.",
                    "C": "A guided walking tour.",
                    "D": "A rental car service."
                },
                "answer": "B",
                "rationale": "They recommend a one-day city pass."
            },
            {
                "stem": "(audio) What can visitors do with the pass?",
                "choices": {
                    "A": "Use taxis for free.",
                    "B": "Ride city buses and trams.",
                    "C": "Get free meals at restaurants.",
                    "D": "Attend concerts for free."
                },
                "answer": "B",
                "rationale": "The pass allows them to ride all city buses and trams."
            },
            {
                "stem": "(audio) Where can the pass be purchased?",
                "choices": {
                    "A": "Only at hotels.",
                    "B": "Only at the airport.",
                    "C": "At the tourist information center and major stations.",
                    "D": "At souvenir shops only."
                },
                "answer": "C",
                "rationale": "It is available at the information center and major stations."
            },
        ],
    },

    # 22. ガイド付きウォーキングツアー
    {
        "level": "B1",
        "topic": ["tourism", "walking tour"],
        "script": (
            "Thank you for joining the Old Town Walking Tour. "
            "The tour will last about two hours and covers three historical temples and a traditional shopping street. "
            "Please follow your guide and be careful when crossing the streets. "
            "At the end of the tour, you will receive a coupon for a free drink at a local café. "
            "We hope you enjoy learning about the history of our city."
        ),
        "questions": [
            {
                "stem": "(audio) How long will the tour last?",
                "choices": {
                    "A": "About one hour.",
                    "B": "About two hours.",
                    "C": "About three hours.",
                    "D": "About four hours."
                },
                "answer": "B",
                "rationale": "The tour lasts about two hours."
            },
            {
                "stem": "(audio) What places will the tour visit?",
                "choices": {
                    "A": "A zoo and an aquarium.",
                    "B": "Modern office buildings.",
                    "C": "Three temples and a shopping street.",
                    "D": "Only one large temple."
                },
                "answer": "C",
                "rationale": "It covers three historical temples and a traditional street."
            },
            {
                "stem": "(audio) What do participants receive at the end?",
                "choices": {
                    "A": "A free museum ticket.",
                    "B": "A coupon for a free drink.",
                    "C": "A map of hiking trails.",
                    "D": "A discount on hotel rooms."
                },
                "answer": "B",
                "rationale": "They receive a coupon for a free drink at a café."
            },
        ],
    },

    # 23. 観光バスの遅延
    {
        "level": "B1",
        "topic": ["tourism", "bus delay"],
        "script": (
            "Ladies and gentlemen, we are sorry for the delay of this sightseeing bus. "
            "Due to heavy traffic near the city center, our arrival at the next stop will be about fifteen minutes late. "
            "We will shorten the break at the riverside park so that the tour can finish on time. "
            "Thank you for your understanding and please remain seated while the bus is moving."
        ),
        "questions": [
            {
                "stem": "(audio) Why is the sightseeing bus delayed?",
                "choices": {
                    "A": "Because of heavy traffic.",
                    "B": "Because of bad weather.",
                    "C": "Because of a flat tire.",
                    "D": "Because the driver was late."
                },
                "answer": "A",
                "rationale": "It is delayed due to heavy traffic near the city center."
            },
            {
                "stem": "(audio) How late will the bus be?",
                "choices": {
                    "A": "Five minutes.",
                    "B": "Ten minutes.",
                    "C": "Fifteen minutes.",
                    "D": "Thirty minutes."
                },
                "answer": "C",
                "rationale": "The arrival will be about fifteen minutes late."
            },
            {
                "stem": "(audio) What change will be made to keep the schedule?",
                "choices": {
                    "A": "They will skip a museum visit.",
                    "B": "They will shorten the break at the riverside park.",
                    "C": "They will change the driver.",
                    "D": "They will return to the station immediately."
                },
                "answer": "B",
                "rationale": "The break at the riverside park will be shortened."
            },
        ],
    },

    # 24. 観光案内所からの注意喚起
    {
        "level": "B1",
        "topic": ["tourism", "safety"],
        "script": (
            "This is a safety announcement for all visitors. "
            "Please be careful of your bags and cameras, especially in crowded areas such as markets and train stations. "
            "Do not leave your belongings unattended at any time. "
            "If you lose something, contact the nearest police box or tourist information center. "
            "We hope you have a safe and enjoyable stay in our city."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main purpose of this announcement?",
                "choices": {
                    "A": "To advertise local products.",
                    "B": "To warn visitors about their belongings.",
                    "C": "To invite visitors to a festival.",
                    "D": "To explain train schedules."
                },
                "answer": "B",
                "rationale": "It reminds visitors to take care of their bags and cameras."
            },
            {
                "stem": "(audio) Where should visitors be especially careful?",
                "choices": {
                    "A": "In their hotel rooms.",
                    "B": "In quiet residential areas.",
                    "C": "In crowded places like markets and stations.",
                    "D": "On airplanes."
                },
                "answer": "C",
                "rationale": "They are warned about crowded places such as markets and stations."
            },
            {
                "stem": "(audio) What should visitors do if they lose something?",
                "choices": {
                    "A": "Call the embassy.",
                    "B": "Go to the airport immediately.",
                    "C": "Contact a police box or information center.",
                    "D": "Post on social media."
                },
                "answer": "C",
                "rationale": "They should contact the nearest police box or information center."
            },
        ],
    },

    # 25. 観光列車の予約
    {
        "level": "B1",
        "topic": ["tourism", "scenic train"],
        "script": (
            "Thank you for your interest in the Riverside Scenic Train. "
            "This train requires a reserved seat ticket in addition to a regular train ticket. "
            "All window seats are popular during the autumn leaves season, so we recommend booking early. "
            "Tickets can be purchased at JR ticket offices or online. "
            "For more information, please see the pamphlet available at this counter."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about the Riverside Scenic Train?",
                "choices": {
                    "A": "It is free of charge.",
                    "B": "It only runs at night.",
                    "C": "It requires a reserved seat ticket.",
                    "D": "It has no windows."
                },
                "answer": "C",
                "rationale": "Passengers need a reserved seat ticket in addition to a regular one."
            },
            {
                "stem": "(audio) When are window seats especially popular?",
                "choices": {
                    "A": "During the autumn leaves season.",
                    "B": "During winter holidays.",
                    "C": "During the rainy season.",
                    "D": "During New Year’s Day."
                },
                "answer": "A",
                "rationale": "Window seats are popular in the autumn leaves season."
            },
            {
                "stem": "(audio) Where can passengers buy tickets?",
                "choices": {
                    "A": "Only on the train.",
                    "B": "At JR ticket offices or online.",
                    "C": "Only at travel agencies.",
                    "D": "Only at hotels."
                },
                "answer": "B",
                "rationale": "Tickets can be purchased at JR offices or online."
            },
        ],
    },
    # 26. 駅構内工事の案内
    {
        "level": "B1",
        "topic": ["train station", "construction"],
        "script": (
            "Attention, passengers. "
            "Due to construction work, the east ticket gate will be closed from tomorrow until Friday. "
            "Please use the north or south gates instead. "
            "Signs have been placed around the station to guide you. "
            "We apologize for the inconvenience and thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What facility will be closed?",
                "choices": {
                    "A": "The east ticket gate.",
                    "B": "The north ticket gate.",
                    "C": "The south ticket gate.",
                    "D": "The station office."
                },
                "answer": "A",
                "rationale": "The announcement says the east ticket gate will be closed."
            },
            {
                "stem": "(audio) Why will it be closed?",
                "choices": {
                    "A": "For a holiday.",
                    "B": "Because of construction work.",
                    "C": "Because of a power cut.",
                    "D": "Because of bad weather."
                },
                "answer": "B",
                "rationale": "The gate is closed due to construction work."
            },
            {
                "stem": "(audio) What are passengers advised to do?",
                "choices": {
                    "A": "Use the underground passage.",
                    "B": "Use the north or south gates.",
                    "C": "Use buses instead of trains.",
                    "D": "Come to the station earlier."
                },
                "answer": "B",
                "rationale": "They are asked to use the north or south gates."
            },
        ],
    },

    # 27. オフィスビルのエレベーター点検
    {
        "level": "B1",
        "topic": ["office building", "maintenance"],
        "script": (
            "This is a notice from the building management office. "
            "All elevators will be inspected next Sunday between nine a.m. and three p.m. "
            "During this time, please use the stairs. "
            "If you have heavy items, schedule your deliveries for another day. "
            "Thank you for your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) When will the elevators be inspected?",
                "choices": {
                    "A": "Tomorrow morning.",
                    "B": "Next Sunday.",
                    "C": "Every evening.",
                    "D": "On public holidays."
                },
                "answer": "B",
                "rationale": "The inspection will take place next Sunday."
            },
            {
                "stem": "(audio) How should people move between floors during that time?",
                "choices": {
                    "A": "By using the elevator as usual.",
                    "B": "By using a different building.",
                    "C": "By using the stairs.",
                    "D": "By using the emergency exit only."
                },
                "answer": "C",
                "rationale": "They are asked to use the stairs."
            },
            {
                "stem": "(audio) What advice is given for heavy items?",
                "choices": {
                    "A": "Leave them on the first floor.",
                    "B": "Send them by mail.",
                    "C": "Schedule deliveries for another day.",
                    "D": "Ask the security staff to carry them."
                },
                "answer": "C",
                "rationale": "Deliveries with heavy items should be on another day."
            },
        ],
    },

    # 28. 病院の面会時間
    {
        "level": "B1",
        "topic": ["hospital", "visiting hours"],
        "script": (
            "Thank you for visiting City General Hospital. "
            "Please note that visiting hours are from two to seven p.m. on weekdays and from one to six p.m. on weekends. "
            "Children under twelve are not allowed to visit patients without special permission. "
            "Please turn off your mobile phones in the wards. "
            "We appreciate your cooperation in keeping a quiet environment."
        ),
        "questions": [
            {
                "stem": "(audio) What is mainly being explained?",
                "choices": {
                    "A": "How to pay hospital bills.",
                    "B": "How to make an appointment.",
                    "C": "The hospital’s visiting hours.",
                    "D": "The hospital’s parking rules."
                },
                "answer": "C",
                "rationale": "The announcement explains visiting hours and rules."
            },
            {
                "stem": "(audio) What is said about children under twelve?",
                "choices": {
                    "A": "They can visit anytime.",
                    "B": "They can only visit on weekends.",
                    "C": "They cannot visit without special permission.",
                    "D": "They must stay in the waiting room."
                },
                "answer": "C",
                "rationale": "Children under twelve need special permission to visit."
            },
            {
                "stem": "(audio) What must visitors do with their mobile phones?",
                "choices": {
                    "A": "Turn them off in the wards.",
                    "B": "Use them only in the rooms.",
                    "C": "Give them to the nurses.",
                    "D": "Put them in lockers."
                },
                "answer": "A",
                "rationale": "Visitors are told to turn off phones in the wards."
            },
        ],
    },

    # 29. 映画館の注意事項
    {
        "level": "B1",
        "topic": ["cinema", "rules"],
        "script": (
            "Welcome to Grand City Cinema. "
            "Before the movie begins, please make sure to switch your mobile phones to silent mode. "
            "Recording of any kind is strictly prohibited in the theater. "
            "If you need to leave, please do so quietly so as not to disturb other guests. "
            "Thank you for your cooperation and enjoy the film."
        ),
        "questions": [
            {
                "stem": "(audio) Where is this announcement being made?",
                "choices": {
                    "A": "In a shopping mall.",
                    "B": "In a cinema.",
                    "C": "In a museum.",
                    "D": "In a restaurant."
                },
                "answer": "B",
                "rationale": "It talks about movies and the theater."
            },
            {
                "stem": "(audio) What are guests asked to do with their phones?",
                "choices": {
                    "A": "Turn them off completely.",
                    "B": "Leave them at the counter.",
                    "C": "Switch them to silent mode.",
                    "D": "Use them only during the commercials."
                },
                "answer": "C",
                "rationale": "They are asked to switch to silent mode."
            },
            {
                "stem": "(audio) What is strictly prohibited?",
                "choices": {
                    "A": "Eating popcorn.",
                    "B": "Recording the movie.",
                    "C": "Bringing children.",
                    "D": "Asking questions."
                },
                "answer": "B",
                "rationale": "Recording of any kind is prohibited."
            },
        ],
    },

    # 30. 図書館カード更新の案内
    {
        "level": "B1",
        "topic": ["library", "card renewal"],
        "script": (
            "This is a notice from the City Library. "
            "Library cards that expire this month can be renewed at the counter on the first floor. "
            "Please bring your current card and a form of identification. "
            "The renewal process is free of charge and takes only a few minutes. "
            "We encourage you to renew early to continue using our services."
        ),
        "questions": [
            {
                "stem": "(audio) What can library users do at the counter?",
                "choices": {
                    "A": "Return overdue books.",
                    "B": "Renew their library cards.",
                    "C": "Pay for new cards.",
                    "D": "Reserve meeting rooms."
                },
                "answer": "B",
                "rationale": "The announcement is about renewing library cards."
            },
            {
                "stem": "(audio) What must users bring?",
                "choices": {
                    "A": "Only their library card.",
                    "B": "Only a student ID.",
                    "C": "Their card and identification.",
                    "D": "A recommendation letter."
                },
                "answer": "C",
                "rationale": "They must bring the current card and an ID."
            },
            {
                "stem": "(audio) How much does the renewal cost?",
                "choices": {
                    "A": "It is free.",
                    "B": "500 yen.",
                    "C": "1,000 yen.",
                    "D": "It depends on age."
                },
                "answer": "A",
                "rationale": "The renewal is free of charge."
            },
        ],
    },

    # 31. ショッピングセンターの落とし物案内
    {
        "level": "B1",
        "topic": ["shopping mall", "lost and found"],
        "script": (
            "Attention, shoppers. "
            "A wallet has been found near the food court on the third floor. "
            "If you have lost a wallet, please come to the information desk on the first floor and describe it. "
            "You will be asked to show identification before it is returned. "
            "Thank you for your attention."
        ),
        "questions": [
            {
                "stem": "(audio) What item has been found?",
                "choices": {
                    "A": "A mobile phone.",
                    "B": "A wallet.",
                    "C": "A shopping bag.",
                    "D": "A jacket."
                },
                "answer": "B",
                "rationale": "A wallet was found near the food court."
            },
            {
                "stem": "(audio) Where should the owner go?",
                "choices": {
                    "A": "To the security office.",
                    "B": "To the cash register.",
                    "C": "To the information desk.",
                    "D": "To the parking lot booth."
                },
                "answer": "C",
                "rationale": "They should go to the information desk."
            },
            {
                "stem": "(audio) What must the owner do to get the wallet back?",
                "choices": {
                    "A": "Pay a small fee.",
                    "B": "Show a receipt.",
                    "C": "Describe it and show ID.",
                    "D": "Call the police."
                },
                "answer": "C",
                "rationale": "They must describe the wallet and show identification."
            },
        ],
    },

    # 32. スーパーの営業時間変更
    {
        "level": "B1",
        "topic": ["supermarket", "hours"],
        "script": (
            "Dear customers, this is an announcement from Fresh Mart Supermarket. "
            "Starting next month, our weekday opening time will change from nine a.m. to eight thirty a.m. "
            "Closing time will remain the same at nine p.m. "
            "Weekend hours are not affected. "
            "We hope the new hours will be more convenient for your shopping."
        ),
        "questions": [
            {
                "stem": "(audio) What change will occur next month?",
                "choices": {
                    "A": "The store will close earlier.",
                    "B": "The store will open later.",
                    "C": "The store will open earlier on weekdays.",
                    "D": "The store will close on weekends."
                },
                "answer": "C",
                "rationale": "Weekday opening time moves from nine to eight thirty."
            },
            {
                "stem": "(audio) What will happen to closing time?",
                "choices": {
                    "A": "It will be earlier.",
                    "B": "It will be later.",
                    "C": "It will depend on the day.",
                    "D": "It will stay the same."
                },
                "answer": "D",
                "rationale": "Closing time remains nine p.m."
            },
            {
                "stem": "(audio) What is said about weekend hours?",
                "choices": {
                    "A": "They will change completely.",
                    "B": "They will be shorter.",
                    "C": "They are not affected.",
                    "D": "The store will be closed."
                },
                "answer": "C",
                "rationale": "Weekend hours are not affected."
            },
        ],
    },

    # 33. オフィスビルの空調工事
    {
        "level": "B1",
        "topic": ["office building", "air conditioning"],
        "script": (
            "Attention, tenants. "
            "The air conditioning system will be inspected on the tenth floor this Friday from one to three p.m. "
            "During that time, the temperature may be higher than usual. "
            "If you need fans, please contact the building management office in advance. "
            "We apologize for any discomfort this may cause."
        ),
        "questions": [
            {
                "stem": "(audio) Where will the inspection take place?",
                "choices": {
                    "A": "On all floors.",
                    "B": "On the first floor.",
                    "C": "On the tenth floor.",
                    "D": "In the parking area."
                },
                "answer": "C",
                "rationale": "The air conditioning will be inspected on the tenth floor."
            },
            {
                "stem": "(audio) What may happen during the inspection?",
                "choices": {
                    "A": "The lights may go out.",
                    "B": "The temperature may be higher than usual.",
                    "C": "The elevators may stop.",
                    "D": "The fire alarm may sound."
                },
                "answer": "B",
                "rationale": "The temperature may rise during the work."
            },
            {
                "stem": "(audio) What can tenants request in advance?",
                "choices": {
                    "A": "Fans.",
                    "B": "Free drinks.",
                    "C": "Parking tickets.",
                    "D": "New desks."
                },
                "answer": "A",
                "rationale": "They can ask for fans from the management office."
            },
        ],
    },

    # 34. 公園の花火大会
    {
        "level": "B1",
        "topic": ["park", "fireworks"],
        "script": (
            "This Saturday evening, a fireworks display will be held at Riverside Park from seven thirty p.m. "
            "Visitors are encouraged to arrive early, as the park is expected to be crowded. "
            "Please do not reserve space with large sheets or ropes. "
            "After the event, follow the directions of staff when leaving the park. "
            "We hope you enjoy the show."
        ),
        "questions": [
            {
                "stem": "(audio) What event will take place at Riverside Park?",
                "choices": {
                    "A": "A marathon.",
                    "B": "A fireworks display.",
                    "C": "A music festival.",
                    "D": "A food fair."
                },
                "answer": "B",
                "rationale": "The announcement is about a fireworks display."
            },
            {
                "stem": "(audio) What are visitors asked NOT to do?",
                "choices": {
                    "A": "Bring children.",
                    "B": "Bring cameras.",
                    "C": "Reserve space with large sheets or ropes.",
                    "D": "Arrive before seven."
                },
                "answer": "C",
                "rationale": "They are told not to reserve space with large sheets or ropes."
            },
            {
                "stem": "(audio) What should visitors do after the event?",
                "choices": {
                    "A": "Go back into the park.",
                    "B": "Wait quietly until midnight.",
                    "C": "Follow the directions of staff.",
                    "D": "Take pictures of the staff."
                },
                "answer": "C",
                "rationale": "They should follow staff directions when leaving."
            },
        ],
    },

    # 35. 市民ホールのコンサート案内
    {
        "level": "B1",
        "topic": ["concert hall", "event"],
        "script": (
            "Thank you for calling Riverside Civic Hall. "
            "Next month, we will hold a classical music concert by the City Symphony Orchestra. "
            "Tickets go on sale this Saturday at ten a.m. at the hall ticket office and online. "
            "Student discounts are available with a valid student ID. "
            "For more details, please visit our website."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of event is being advertised?",
                "choices": {
                    "A": "A theater play.",
                    "B": "A dance performance.",
                    "C": "A classical music concert.",
                    "D": "A cooking class."
                },
                "answer": "C",
                "rationale": "It is a classical concert by the City Symphony Orchestra."
            },
            {
                "stem": "(audio) When do tickets go on sale?",
                "choices": {
                    "A": "Today at noon.",
                    "B": "This Saturday at ten a.m.",
                    "C": "Next Monday at nine a.m.",
                    "D": "On the day of the concert only."
                },
                "answer": "B",
                "rationale": "Tickets go on sale this Saturday at ten a.m."
            },
            {
                "stem": "(audio) Who can get a discount?",
                "choices": {
                    "A": "Senior citizens.",
                    "B": "Children under ten.",
                    "C": "Tourists.",
                    "D": "Students with ID."
                },
                "answer": "D",
                "rationale": "Student discounts are available with an ID."
            },
        ],
    },

    # 36. スポーツクラブのプール清掃
    {
        "level": "B1",
        "topic": ["gym", "pool cleaning"],
        "script": (
            "Dear members, this is an announcement from Green Wave Sports Club. "
            "Our indoor swimming pool will be closed for cleaning from the first to the third of next month. "
            "Other facilities such as the gym and studio classes will remain open as usual. "
            "We apologize for any inconvenience and thank you for your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) What facility will be closed?",
                "choices": {
                    "A": "The gym area.",
                    "B": "The indoor swimming pool.",
                    "C": "The studio classrooms.",
                    "D": "The locker rooms."
                },
                "answer": "B",
                "rationale": "The indoor pool will be closed for cleaning."
            },
            {
                "stem": "(audio) For how long will it be closed?",
                "choices": {
                    "A": "For one day.",
                    "B": "For two days.",
                    "C": "From the first to the third.",
                    "D": "For a whole month."
                },
                "answer": "C",
                "rationale": "It will be closed from the first to the third."
            },
            {
                "stem": "(audio) What is said about other facilities?",
                "choices": {
                    "A": "They will also be closed.",
                    "B": "They will open only in the morning.",
                    "C": "They will be free to use.",
                    "D": "They will remain open as usual."
                },
                "answer": "D",
                "rationale": "Other facilities stay open as usual."
            },
        ],
    },

    # 37. カフェのポイントカード紹介
    {
        "level": "B1",
        "topic": ["cafe", "loyalty program"],
        "script": (
            "Welcome to Maple Leaf Café. "
            "We would like to introduce our new point card program. "
            "For every 500 yen you spend, you will receive one point, and ten points can be exchanged for a free drink. "
            "You can get a card at the counter today. "
            "Please ask our staff if you have any questions."
        ),
        "questions": [
            {
                "stem": "(audio) What is being introduced?",
                "choices": {
                    "A": "A breakfast menu.",
                    "B": "A point card program.",
                    "C": "A delivery service.",
                    "D": "A new location."
                },
                "answer": "B",
                "rationale": "The announcement is about a point card."
            },
            {
                "stem": "(audio) How many points are given for every 500 yen?",
                "choices": {
                    "A": "One point.",
                    "B": "Two points.",
                    "C": "Five points.",
                    "D": "Ten points."
                },
                "answer": "A",
                "rationale": "Customers get one point for 500 yen."
            },
            {
                "stem": "(audio) What can ten points be exchanged for?",
                "choices": {
                    "A": "A free dessert.",
                    "B": "A discount on coffee beans.",
                    "C": "A free drink.",
                    "D": "A gift card."
                },
                "answer": "C",
                "rationale": "Ten points can be exchanged for a free drink."
            },
        ],
    },

    # 38. オンライン英会話コースの案内
    {
        "level": "B1",
        "topic": ["online course", "English"],
        "script": (
            "Thank you for your interest in our online English conversation course. "
            "Classes are held twice a week in small groups of up to six students. "
            "You can choose morning, afternoon, or evening schedules. "
            "A free trial lesson is available for new students. "
            "Please visit our website to see the details and register."
        ),
        "questions": [
            {
                "stem": "(audio) How often are the classes held?",
                "choices": {
                    "A": "Once a week.",
                    "B": "Twice a week.",
                    "C": "Three times a week.",
                    "D": "Every day."
                },
                "answer": "B",
                "rationale": "The course is held twice a week."
            },
            {
                "stem": "(audio) What is said about class size?",
                "choices": {
                    "A": "There is no limit.",
                    "B": "It is up to ten students.",
                    "C": "It is up to six students.",
                    "D": "It is for one student only."
                },
                "answer": "C",
                "rationale": "Groups are up to six students."
            },
            {
                "stem": "(audio) What can new students receive?",
                "choices": {
                    "A": "A free textbook.",
                    "B": "A free trial lesson.",
                    "C": "A discount on tuition.",
                    "D": "A free dictionary."
                },
                "answer": "B",
                "rationale": "A free trial lesson is available."
            },
        ],
    },

    # 39. ホテルのチェックアウト延長
    {
        "level": "B1",
        "topic": ["hotel", "late checkout"],
        "script": (
            "Good evening, guests. "
            "We would like to inform you that late check-out is available until one p.m. for an additional fee. "
            "Please contact the front desk by ten a.m. tomorrow if you wish to use this service. "
            "Availability may be limited depending on room reservations. "
            "Thank you for staying with us."
        ),
        "questions": [
            {
                "stem": "(audio) Until what time is late check-out available?",
                "choices": {
                    "A": "Until eleven a.m.",
                    "B": "Until noon.",
                    "C": "Until one p.m.",
                    "D": "Until three p.m."
                },
                "answer": "C",
                "rationale": "Late check-out is available until one p.m."
            },
            {
                "stem": "(audio) By when should guests contact the front desk?",
                "choices": {
                    "A": "By eight a.m.",
                    "B": "By ten a.m.",
                    "C": "By noon.",
                    "D": "Any time during the day."
                },
                "answer": "B",
                "rationale": "They should call by ten a.m."
            },
            {
                "stem": "(audio) What may limit the availability of this service?",
                "choices": {
                    "A": "Weather conditions.",
                    "B": "Breakfast reservations.",
                    "C": "Room cleaning time.",
                    "D": "Other room reservations."
                },
                "answer": "D",
                "rationale": "Availability depends on other room reservations."
            },
        ],
    },

    # 40. バスターミナルの遺失物案内
    {
        "level": "B1",
        "topic": ["bus terminal", "lost item"],
        "script": (
            "This is an announcement from the Central Bus Terminal. "
            "A black backpack was found on bus number 16 arriving from the airport. "
            "If you think it may be yours, please come to the information counter on the second floor. "
            "You will be asked to describe the contents of the bag. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What item was found?",
                "choices": {
                    "A": "A suitcase.",
                    "B": "A black backpack.",
                    "C": "A wallet.",
                    "D": "A smartphone."
                },
                "answer": "B",
                "rationale": "A black backpack was found."
            },
            {
                "stem": "(audio) Where should the owner go?",
                "choices": {
                    "A": "To the police station.",
                    "B": "To the first-floor ticket office.",
                    "C": "To the second-floor information counter.",
                    "D": "To the bus driver."
                },
                "answer": "C",
                "rationale": "They should go to the information counter on the second floor."
            },
            {
                "stem": "(audio) What will the owner need to do?",
                "choices": {
                    "A": "Pay a storage fee.",
                    "B": "Describe the contents of the bag.",
                    "C": "Show the bus ticket.",
                    "D": "Call the airport."
                },
                "answer": "B",
                "rationale": "They must describe what is inside the bag."
            },
        ],
    },

    # 41. 学校：保護者会のお知らせ
    {
        "level": "B1",
        "topic": ["school", "parents meeting"],
        "script": (
            "Parents and guardians, this is an announcement from Oak Hill Junior High School. "
            "A parents’ meeting will be held next Thursday evening from six thirty to eight p.m. "
            "Homeroom teachers will explain students’ progress and plans for the next term. "
            "Please come to your child’s classroom ten minutes before the starting time. "
            "We look forward to seeing you."
        ),
        "questions": [
            {
                "stem": "(audio) Who is this announcement mainly for?",
                "choices": {
                    "A": "Students.",
                    "B": "Teachers.",
                    "C": "Parents and guardians.",
                    "D": "Local residents."
                },
                "answer": "C",
                "rationale": "It is addressed to parents and guardians."
            },
            {
                "stem": "(audio) What will homeroom teachers talk about?",
                "choices": {
                    "A": "School lunch menus.",
                    "B": "Students’ progress and future plans.",
                    "C": "Club activity schedules.",
                    "D": "Entrance exam dates."
                },
                "answer": "B",
                "rationale": "They will explain progress and next-term plans."
            },
            {
                "stem": "(audio) When should parents arrive?",
                "choices": {
                    "A": "Exactly at six thirty.",
                    "B": "Ten minutes before the meeting starts.",
                    "C": "After eight p.m.",
                    "D": "Anytime during the day."
                },
                "answer": "B",
                "rationale": "They are asked to come ten minutes before the start."
            },
        ],
    },

    # 42. 学校：清掃ボランティア募集
    {
        "level": "B1",
        "topic": ["school", "volunteer"],
        "script": (
            "Attention, students. "
            "We are looking for volunteers to help clean the school grounds this Saturday morning. "
            "The activity will run from nine to eleven a.m., and gloves and garbage bags will be provided. "
            "If you would like to join, please sign up on the list outside the student council room. "
            "We appreciate your help in keeping our school clean."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of activity is being planned?",
                "choices": {
                    "A": "A sports competition.",
                    "B": "A cleaning volunteer activity.",
                    "C": "A music performance.",
                    "D": "A science fair."
                },
                "answer": "B",
                "rationale": "They are recruiting volunteers to clean the school."
            },
            {
                "stem": "(audio) What will be provided to volunteers?",
                "choices": {
                    "A": "Lunch boxes.",
                    "B": "T-shirts.",
                    "C": "Gloves and garbage bags.",
                    "D": "Bus tickets."
                },
                "answer": "C",
                "rationale": "Gloves and garbage bags will be provided."
            },
            {
                "stem": "(audio) How can students join?",
                "choices": {
                    "A": "By calling the office.",
                    "B": "By sending an e-mail.",
                    "C": "By signing up on a list.",
                    "D": "By telling their homeroom teacher only."
                },
                "answer": "C",
                "rationale": "They must sign up on the list outside the student council room."
            },
        ],
    },

    # 43. 学校：図書館の読み聞かせ会
    {
        "level": "B1",
        "topic": ["school", "reading event"],
        "script": (
            "This is an announcement from the school library. "
            "Next Wednesday during lunchtime, there will be a reading session of English picture books for first- and second-year students. "
            "The event will be held in the reading corner on the second floor. "
            "No registration is necessary; just bring your lunch and listen. "
            "We hope many of you will join us."
        ),
        "questions": [
            {
                "stem": "(audio) Who is this event mainly for?",
                "choices": {
                    "A": "First- and second-year students.",
                    "B": "Third-year students only.",
                    "C": "Parents and teachers.",
                    "D": "Local residents."
                },
                "answer": "A",
                "rationale": "It targets first- and second-year students."
            },
            {
                "stem": "(audio) Where will the session be held?",
                "choices": {
                    "A": "In the gym.",
                    "B": "In the school yard.",
                    "C": "In the reading corner on the second floor.",
                    "D": "In the cafeteria."
                },
                "answer": "C",
                "rationale": "It takes place in the reading corner."
            },
            {
                "stem": "(audio) What should students do if they want to join?",
                "choices": {
                    "A": "Register in advance.",
                    "B": "Bring their lunch and come.",
                    "C": "Pay a small fee.",
                    "D": "Prepare a presentation."
                },
                "answer": "B",
                "rationale": "No registration is needed; they just bring lunch and listen."
            },
        ],
    },

    # 44. 学校：留学生歓迎会
    {
        "level": "B1",
        "topic": ["school", "welcome party"],
        "script": (
            "Students, this Friday after classes, we will hold a welcome party for our new exchange students from overseas. "
            "The party will be in the multipurpose room on the third floor from four to five p.m. "
            "There will be simple games and snacks, and English and Japanese will both be used. "
            "Please come and say hello to our guests."
        ),
        "questions": [
            {
                "stem": "(audio) What is the purpose of the party?",
                "choices": {
                    "A": "To celebrate graduation.",
                    "B": "To welcome exchange students.",
                    "C": "To raise money for charity.",
                    "D": "To choose club leaders."
                },
                "answer": "B",
                "rationale": "It is a welcome party for exchange students."
            },
            {
                "stem": "(audio) Where will the party be held?",
                "choices": {
                    "A": "In the school cafeteria.",
                    "B": "In the gym.",
                    "C": "In the multipurpose room.",
                    "D": "In the library."
                },
                "answer": "C",
                "rationale": "It will be in the multipurpose room on the third floor."
            },
            {
                "stem": "(audio) What is said about the languages used?",
                "choices": {
                    "A": "Only Japanese will be used.",
                    "B": "Only English will be used.",
                    "C": "English and Japanese will both be used.",
                    "D": "Only the exchange students may speak."
                },
                "answer": "C",
                "rationale": "Both English and Japanese will be used at the party."
            },
        ],
    },

    # 45. 学校：校外学習の持ち物
    {
        "level": "B1",
        "topic": ["school", "field trip"],
        "script": (
            "Students in the second year, please listen carefully. "
            "For next Tuesday’s field trip to the science museum, you must bring your lunch, a drink, and a small towel. "
            "Please wear your school uniform and comfortable shoes. "
            "Do not forget to bring your student ID card for the group ticket. "
            "If you have any questions, ask your homeroom teacher."
        ),
        "questions": [
            {
                "stem": "(audio) Where are the students going on their field trip?",
                "choices": {
                    "A": "To a zoo.",
                    "B": "To a science museum.",
                    "C": "To a sports stadium.",
                    "D": "To a theater."
                },
                "answer": "B",
                "rationale": "The trip is to the science museum."
            },
            {
                "stem": "(audio) What must students wear?",
                "choices": {
                    "A": "Casual clothes.",
                    "B": "Sportswear and sandals.",
                    "C": "Their school uniform and comfortable shoes.",
                    "D": "Raincoats."
                },
                "answer": "C",
                "rationale": "They must wear their uniform and comfortable shoes."
            },
            {
                "stem": "(audio) Why do they need their student ID card?",
                "choices": {
                    "A": "For the group ticket.",
                    "B": "For lunch service.",
                    "C": "For using lockers.",
                    "D": "For taking photos."
                },
                "answer": "A",
                "rationale": "The ID is needed for the group ticket."
            },
        ],
    },

    # 46. 観光：展望台の利用案内
    {
        "level": "B1",
        "topic": ["tourism", "observation deck"],
        "script": (
            "Welcome to Sky Tower. "
            "The observation deck is located on the 40th floor and can be reached by the express elevator. "
            "Please note that large luggage is not allowed on the deck; use the coin lockers on the first floor. "
            "On clear days, you can see the mountains in the distance. "
            "We hope you enjoy the view."
        ),
        "questions": [
            {
                "stem": "(audio) Where is the observation deck located?",
                "choices": {
                    "A": "On the 20th floor.",
                    "B": "On the 30th floor.",
                    "C": "On the 40th floor.",
                    "D": "On the rooftop only."
                },
                "answer": "C",
                "rationale": "It is on the 40th floor."
            },
            {
                "stem": "(audio) What is not allowed on the deck?",
                "choices": {
                    "A": "Small bags.",
                    "B": "Large luggage.",
                    "C": "Cameras.",
                    "D": "Children."
                },
                "answer": "B",
                "rationale": "Large luggage is not permitted."
            },
            {
                "stem": "(audio) What can visitors do with large luggage?",
                "choices": {
                    "A": "Leave it with staff for free.",
                    "B": "Take it to the restaurant.",
                    "C": "Keep it on the elevator.",
                    "D": "Put it in coin lockers on the first floor."
                },
                "answer": "D",
                "rationale": "They should use the coin lockers on the first floor."
            },
        ],
    },

    # 47. 観光：ボートクルーズの案内
    {
        "level": "B1",
        "topic": ["tourism", "boat cruise"],
        "script": (
            "Thank you for choosing the Riverside Boat Cruise. "
            "The cruise will last about 50 minutes and circle the central island. "
            "For your safety, please remain seated while the boat is moving and do not lean over the railings. "
            "Life jackets are stored under your seats and staff will assist you in an emergency. "
            "We hope you enjoy the scenery."
        ),
        "questions": [
            {
                "stem": "(audio) How long does the cruise last?",
                "choices": {
                    "A": "About 30 minutes.",
                    "B": "About 50 minutes.",
                    "C": "About 90 minutes.",
                    "D": "Two hours."
                },
                "answer": "B",
                "rationale": "The cruise lasts about 50 minutes."
            },
            {
                "stem": "(audio) What safety instruction is given?",
                "choices": {
                    "A": "Stand up to take photos.",
                    "B": "Walk around freely.",
                    "C": "Remain seated and do not lean over the railings.",
                    "D": "Open the life jacket boxes."
                },
                "answer": "C",
                "rationale": "Passengers should remain seated and not lean over."
            },
            {
                "stem": "(audio) Where are life jackets stored?",
                "choices": {
                    "A": "At the front of the boat.",
                    "B": "Under the seats.",
                    "C": "Near the ticket counter.",
                    "D": "In the captain’s room."
                },
                "answer": "B",
                "rationale": "Life jackets are stored under the seats."
            },
        ],
    },

    # 48. 観光：街歩きマップの案内
    {
        "level": "B1",
        "topic": ["tourism", "city map"],
        "script": (
            "Welcome to Harbor Town. "
            "Free walking maps in four languages are available at the tourist information desk next to the station. "
            "The maps show recommended routes, cafes, and viewpoints. "
            "You can also download a digital version by scanning the QR code on the leaflet. "
            "Please use them to enjoy your stay."
        ),
        "questions": [
            {
                "stem": "(audio) What is available for free?",
                "choices": {
                    "A": "Bus tickets.",
                    "B": "Walking maps.",
                    "C": "Museum passes.",
                    "D": "Restaurant coupons only."
                },
                "answer": "B",
                "rationale": "Free walking maps are provided."
            },
            {
                "stem": "(audio) Where can visitors get the maps?",
                "choices": {
                    "A": "At hotel front desks.",
                    "B": "At the city hall.",
                    "C": "At the tourist information desk.",
                    "D": "On the boat."
                },
                "answer": "C",
                "rationale": "They are available at the tourist information desk."
            },
            {
                "stem": "(audio) How can visitors get a digital version?",
                "choices": {
                    "A": "By sending an e-mail.",
                    "B": "By calling the office.",
                    "C": "By scanning a QR code.",
                    "D": "By buying a CD."
                },
                "answer": "C",
                "rationale": "They can scan the QR code on the leaflet."
            },
        ],
    },

    # 49. 観光：温泉街の注意
    {
        "level": "B1",
        "topic": ["tourism", "hot spring town"],
        "script": (
            "This is a safety announcement for visitors to Yama Hot Spring Town. "
            "The streets are narrow and some have no sidewalks, so please walk carefully and watch for cars and buses. "
            "After dark, use the free shuttle buses instead of walking long distances. "
            "If you need information, visit the tourist office in front of the station. "
            "We hope you have a safe and relaxing stay."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main concern mentioned?",
                "choices": {
                    "A": "High hotel prices.",
                    "B": "Crowded restaurants.",
                    "C": "Narrow streets with little space for walking.",
                    "D": "Lack of hot spring baths."
                },
                "answer": "C",
                "rationale": "The streets are narrow and some have no sidewalks."
            },
            {
                "stem": "(audio) What are visitors encouraged to use after dark?",
                "choices": {
                    "A": "Rental bicycles.",
                    "B": "Free shuttle buses.",
                    "C": "Taxis from the city.",
                    "D": "Cable cars."
                },
                "answer": "B",
                "rationale": "They are advised to use free shuttle buses at night."
            },
            {
                "stem": "(audio) Where can visitors get more information?",
                "choices": {
                    "A": "At hotel front desks only.",
                    "B": "At the town hall.",
                    "C": "At the tourist office in front of the station.",
                    "D": "At the bus stop."
                },
                "answer": "C",
                "rationale": "The tourist office is in front of the station."
            },
        ],
    },

    # 50. 観光：山のハイキングコース
    {
        "level": "B1",
        "topic": ["tourism", "hiking"],
        "script": (
            "Hikers, please listen to this announcement. "
            "Due to recent heavy rain, part of the Blue Ridge hiking trail is closed because of fallen trees. "
            "Please follow the signs and use the Green Ridge trail instead. "
            "The hike will take about 90 minutes longer than usual. "
            "Thank you for your understanding and stay safe."
        ),
        "questions": [
            {
                "stem": "(audio) Why is part of the Blue Ridge trail closed?",
                "choices": {
                    "A": "Because of snow.",
                    "B": "Because of construction.",
                    "C": "Because of fallen trees after heavy rain.",
                    "D": "Because of wild animals."
                },
                "answer": "C",
                "rationale": "Heavy rain caused fallen trees on the trail."
            },
            {
                "stem": "(audio) Which trail should hikers use instead?",
                "choices": {
                    "A": "The Red Ridge trail.",
                    "B": "The Green Ridge trail.",
                    "C": "The River trail.",
                    "D": "The Lake trail."
                },
                "answer": "B",
                "rationale": "They are told to use the Green Ridge trail."
            },
            {
                "stem": "(audio) What effect will this have on the hike?",
                "choices": {
                    "A": "It will be shorter.",
                    "B": "It will take the same time.",
                    "C": "It will take about 90 minutes longer.",
                    "D": "It will be canceled."
                },
                "answer": "C",
                "rationale": "The hike will be about 90 minutes longer."
            },
        ],
    },

    # 51. ラジオ：交通情報
    {
        "level": "B1",
        "topic": ["radio", "traffic"],
        "script": (
            "You are listening to Morning Drive Radio. "
            "Here is the latest traffic update. "
            "There is a ten-kilometer traffic jam on the highway toward the airport due to an earlier accident. "
            "Drivers heading to the airport are advised to leave extra time or use Route 5 instead. "
            "We will bring you another update in thirty minutes."
        ),
        "questions": [
            {
                "stem": "(audio) What is causing the traffic jam?",
                "choices": {
                    "A": "Road construction.",
                    "B": "An earlier accident.",
                    "C": "Heavy rain.",
                    "D": "A sports event."
                },
                "answer": "B",
                "rationale": "The jam is due to an earlier accident."
            },
            {
                "stem": "(audio) What advice is given to drivers going to the airport?",
                "choices": {
                    "A": "Cancel their trip.",
                    "B": "Use the train instead.",
                    "C": "Leave extra time or use Route 5.",
                    "D": "Park their cars and walk."
                },
                "answer": "C",
                "rationale": "They should allow more time or take Route 5."
            },
            {
                "stem": "(audio) When will the next update be given?",
                "choices": {
                    "A": "In ten minutes.",
                    "B": "In twenty minutes.",
                    "C": "In thirty minutes.",
                    "D": "In one hour."
                },
                "answer": "C",
                "rationale": "Another update will come in thirty minutes."
            },
        ],
    },

    # 52. ラジオ：天気予報
    {
        "level": "B1",
        "topic": ["radio", "weather"],
        "script": (
            "And now, here is today’s weather forecast. "
            "This afternoon will be mostly sunny with a high of 27 degrees, but clouds will increase in the evening. "
            "Rain is expected late tonight and tomorrow morning, so please remember to bring an umbrella if you go out early. "
            "Winds will be light throughout the day. "
            "That was the weather report."
        ),
        "questions": [
            {
                "stem": "(audio) What will the weather be like this afternoon?",
                "choices": {
                    "A": "Rainy.",
                    "B": "Snowy.",
                    "C": "Mostly sunny.",
                    "D": "Very windy."
                },
                "answer": "C",
                "rationale": "The afternoon will be mostly sunny."
            },
            {
                "stem": "(audio) When is rain expected?",
                "choices": {
                    "A": "This afternoon.",
                    "B": "Late tonight and tomorrow morning.",
                    "C": "Only on the weekend.",
                    "D": "Only around noon."
                },
                "answer": "B",
                },            {
                "stem": "(audio) What advice is given to listeners?",
                "choices": {
                    "A": "Bring an umbrella if going out early.",
                    "B": "Stay at home all day.",
                    "C": "Close all windows immediately.",
                    "D": "Drive slowly because of snow."
                },
                "answer": "A",
                "rationale": "Listeners are told to bring an umbrella if they go out early."
            },
        ],
    },

    # 53. オフィス：健康診断のお知らせ
    {
        "level": "B1",
        "topic": ["company", "health check"],
        "script": (
            "Attention all employees. "
            "Our annual health check will be held in the meeting room on the fifth floor next Wednesday and Thursday. "
            "Please check the schedule sent by e-mail and come at your assigned time. "
            "Remember not to eat or drink anything except water for eight hours before your check. "
            "If you need to change your time, contact the HR department."
        ),
        "questions": [
            {
                "stem": "(audio) What event will be held?",
                "choices": {
                    "A": "A safety drill.",
                    "B": "An annual health check.",
                    "C": "A training seminar.",
                    "D": "A company party."
                },
                "answer": "B",
                "rationale": "The announcement is about the annual health check."
            },
            {
                "stem": "(audio) What must employees do before the check?",
                "choices": {
                    "A": "Sleep at the office.",
                    "B": "Skip lunch only.",
                    "C": "Not eat or drink anything except water for eight hours.",
                    "D": "Bring a family member."
                },
                "answer": "C",
                "rationale": "They must avoid eating or drinking except water."
            },
            {
                "stem": "(audio) Who should they contact to change the time?",
                "choices": {
                    "A": "The IT department.",
                    "B": "The HR department.",
                    "C": "The accounting department.",
                    "D": "The building manager."
                },
                "answer": "B",
                "rationale": "They should contact the HR department."
            },
        ],
    },

    # 54. オフィス：在宅勤務制度の案内
    {
        "level": "B1",
        "topic": ["company", "remote work"],
        "script": (
            "This is an announcement from the Human Resources Department. "
            "Starting next month, employees may work from home up to two days per week with their manager’s approval. "
            "Please read the remote work guidelines on the intranet site before applying. "
            "Applications should be submitted at least three days in advance. "
            "If you have questions, contact your HR representative."
        ),
        "questions": [
            {
                "stem": "(audio) What change is being announced?",
                "choices": {
                    "A": "The office will move.",
                    "B": "Employees may work from home up to two days a week.",
                    "C": "Working hours will be longer.",
                    "D": "The dress code will change."
                },
                "answer": "B",
                "rationale": "Employees can work from home up to two days weekly."
            },
            {
                "stem": "(audio) What must employees do before applying?",
                "choices": {
                    "A": "Talk to the CEO.",
                    "B": "Read the guidelines on the intranet.",
                    "C": "Buy new computers.",
                    "D": "Move closer to the office."
                },
                "answer": "B",
                "rationale": "They must read the remote work guidelines."
            },
            {
                "stem": "(audio) How early should applications be submitted?",
                "choices": {
                    "A": "One day in advance.",
                    "B": "Two days in advance.",
                    "C": "Three days in advance.",
                    "D": "On the same day."
                },
                "answer": "C",
                "rationale": "Applications should be submitted at least three days before."
            },
        ],
    },

    # 55. オフィス：社内研修の案内
    {
        "level": "B1",
        "topic": ["company", "training"],
        "script": (
            "Attention, staff. "
            "A mandatory customer service training session will be held next Friday from three to five p.m. in Conference Room B. "
            "All full-time employees who deal with customers must attend. "
            "Please arrive on time and bring a notebook and pen. "
            "If you are unable to attend, inform your supervisor in advance."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of training is being offered?",
                "choices": {
                    "A": "Computer skills training.",
                    "B": "Customer service training.",
                    "C": "Foreign language training.",
                    "D": "Safety training."
                },
                "answer": "B",
                "rationale": "The training is about customer service."
            },
            {
                "stem": "(audio) Who must attend the session?",
                "choices": {
                    "A": "Part-time staff only.",
                    "B": "Managers only.",
                    "C": "All full-time employees who deal with customers.",
                    "D": "New employees only."
                },
                "answer": "C",
                "rationale": "Full-time employees dealing with customers must attend."
            },
            {
                "stem": "(audio) What should employees bring?",
                "choices": {
                    "A": "A laptop computer.",
                    "B": "A textbook.",
                    "C": "A notebook and pen.",
                    "D": "Their lunch."
                },
                "answer": "C",
                "rationale": "They should bring a notebook and pen."
            },
        ],
    },

    # 56. オンラインショップ：返品ポリシー
    {
        "level": "B1",
        "topic": ["online shop", "return policy"],
        "script": (
            "Thank you for shopping at SunnyDays Online Store. "
            "If you are not satisfied with your purchase, you may return unused items within 30 days of delivery. "
            "Please fill out the return form on our website and use the label provided in your package. "
            "Refunds will be issued to the original method of payment after the items arrive at our warehouse. "
            "For more details, please check the FAQ page."
        ),
        "questions": [
            {
                "stem": "(audio) Within how many days can customers return items?",
                "choices": {
                    "A": "7 days.",
                    "B": "14 days.",
                    "C": "30 days.",
                    "D": "60 days."
                },
                "answer": "C",
                "rationale": "Returns are accepted within 30 days."
            },
            {
                "stem": "(audio) What must customers do before returning items?",
                "choices": {
                    "A": "Call the warehouse.",
                    "B": "Visit the store in person.",
                    "C": "Fill out a return form on the website.",
                    "D": "Pay an additional fee first."
                },
                "answer": "C",
                "rationale": "They must fill out the online return form."
            },
            {
                "stem": "(audio) How will refunds be issued?",
                "choices": {
                    "A": "In cash only.",
                    "B": "As store points only.",
                    "C": "To the original method of payment.",
                    "D": "As gift vouchers only."
                },
                "answer": "C",
                "rationale": "Refunds go to the original payment method."
            },
        ],
    },

    # 57. 郵便局：窓口営業時間
    {
        "level": "B1",
        "topic": ["post office", "hours"],
        "script": (
            "This is an announcement from the Central Post Office. "
            "From next Monday, our counter hours will be from nine a.m. to six p.m. on weekdays and from nine a.m. to one p.m. on Saturdays. "
            "We will be closed on Sundays and national holidays. "
            "The ATM corner will continue to operate from seven a.m. to eleven p.m. every day. "
            "Thank you for your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) On which days will the counter be closed?",
                "choices": {
                    "A": "Only on Sundays.",
                    "B": "Only on holidays.",
                    "C": "On Sundays and national holidays.",
                    "D": "On Saturdays and Sundays."
                },
                "answer": "C",
                "rationale": "The counter is closed on Sundays and national holidays."
            },
            {
                "stem": "(audio) What is said about the ATM corner?",
                "choices": {
                    "A": "It will also be closed on Sundays.",
                    "B": "It will operate 24 hours a day.",
                    "C": "It will open only on weekdays.",
                    "D": "It will be open from seven a.m. to eleven p.m. every day."
                },
                "answer": "D",
                "rationale": "The ATM runs from 7 a.m. to 11 p.m. every day."
            },
            {
                "stem": "(audio) How late is the counter open on weekdays?",
                "choices": {
                    "A": "Until four p.m.",
                    "B": "Until five p.m.",
                    "C": "Until six p.m.",
                    "D": "Until seven p.m."
                },
                "answer": "C",
                "rationale": "Weekday hours end at six p.m."
            },
        ],
    },

    # 58. 銀行：システムメンテナンス
    {
        "level": "B1",
        "topic": ["bank", "system maintenance"],
        "script": (
            "Thank you for using Green Bank. "
            "Due to system maintenance, our online banking service will be unavailable this Sunday from midnight to six a.m. "
            "Cash withdrawals and deposits at ATMs will still be possible. "
            "We recommend completing important transfers before the maintenance period. "
            "We apologize for any inconvenience."
        ),
        "questions": [
            {
                "stem": "(audio) What will be unavailable during the maintenance?",
                "choices": {
                    "A": "All ATMs.",
                    "B": "Online banking service.",
                    "C": "Branch offices.",
                    "D": "Credit cards."
                },
                "answer": "B",
                "rationale": "Online banking will be unavailable."
            },
            {
                "stem": "(audio) When will the maintenance take place?",
                "choices": {
                    "A": "On Saturday afternoon.",
                    "B": "On Sunday from midnight to six a.m.",
                    "C": "All day Sunday.",
                    "D": "Every night this week."
                },
                "answer": "B",
                "rationale": "It is from midnight to six a.m. on Sunday."
            },
            {
                "stem": "(audio) What does the bank recommend customers do?",
                "choices": {
                    "A": "Visit branches during the night.",
                    "B": "Use credit cards only.",
                    "C": "Complete important transfers beforehand.",
                    "D": "Stop using ATMs."
                },
                "answer": "C",
                "rationale": "Customers should do important transfers before maintenance."
            },
        ],
    },

    # 59. 市役所：ゴミ収集日の変更
    {
        "level": "B1",
        "topic": ["city hall", "trash collection"],
        "script": (
            "This is an announcement from the City Hall Environmental Department. "
            "From next month, the collection day for burnable trash in the Riverside area will change from Tuesday to Wednesday. "
            "Please put your trash bags out by eight a.m. on the new collection day. "
            "The collection schedule for other types of trash remains the same. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What will change next month?",
                "choices": {
                    "A": "The collection place.",
                    "B": "The collection time.",
                    "C": "The collection day for burnable trash.",
                    "D": "The type of trash allowed."
                },
                "answer": "C",
                "rationale": "The day for burnable trash collection will change."
            },
            {
                "stem": "(audio) What is the new collection day for burnable trash?",
                "choices": {
                    "A": "Monday.",
                    "B": "Tuesday.",
                    "C": "Wednesday.",
                    "D": "Thursday."
                },
                "answer": "C",
                "rationale": "It will change from Tuesday to Wednesday."
            },
            {
                "stem": "(audio) By what time should residents put out their trash?",
                "choices": {
                    "A": "By six a.m.",
                    "B": "By seven a.m.",
                    "C": "By eight a.m.",
                    "D": "By nine a.m."
                },
                "answer": "C",
                "rationale": "Trash must be out by eight a.m."
            },
        ],
    },

    # 60. 駅ビル：防災訓練の案内
    {
        "level": "B1",
        "topic": ["station building", "drill"],
        "script": (
            "Attention, customers. "
            "A disaster drill will be conducted in this station building next Tuesday at ten a.m. "
            "During the drill, alarms will sound and staff will guide you to emergency exits. "
            "Please follow their instructions, but there is no need to be alarmed. "
            "Thank you for your cooperation in this important safety exercise."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen next Tuesday at ten a.m.?",
                "choices": {
                    "A": "A train delay.",
                    "B": "A disaster drill.",
                    "C": "A sale event.",
                    "D": "A power outage."
                },
                "answer": "B",
                "rationale": "A disaster drill will be held."
            },
            {
                "stem": "(audio) What will staff do during the drill?",
                "choices": {
                    "A": "Close all exits.",
                    "B": "Guide customers to emergency exits.",
                    "C": "Stop all trains.",
                    "D": "Check tickets."
                },
                "answer": "B",
                "rationale": "Staff will guide people to emergency exits."
            },
            {
                "stem": "(audio) How are customers asked to feel about the alarms?",
                "choices": {
                    "A": "They should be very worried.",
                    "B": "They should ignore them completely.",
                    "C": "They should not be alarmed because it is only a drill.",
                    "D": "They should leave the station immediately."
                },
                "answer": "C",
                "rationale": "It is only a drill, so there is no need to be alarmed."
            },
        ],
    },

    # 61. 空港：保安検査の案内
    {
        "level": "B1",
        "topic": ["airport", "security"],
        "script": (
            "Ladies and gentlemen, please be reminded that all passengers must pass through the security check before entering the departure area. "
            "Please remove laptops and liquids from your bags and place them in separate trays. "
            "Liquids should be in containers of 100 milliliters or less and fit into a clear plastic bag. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What must all passengers do?",
                "choices": {
                    "A": "Check in online.",
                    "B": "Pass through the security check.",
                    "C": "Buy travel insurance.",
                    "D": "Visit the information counter."
                },
                "answer": "B",
                "rationale": "All passengers must go through security."
            },
            {
                "stem": "(audio) What should passengers remove from their bags?",
                "choices": {
                    "A": "Books and magazines.",
                    "B": "Wallets and keys.",
                    "C": "Laptops and liquids.",
                    "D": "Clothes and shoes."
                },
                "answer": "C",
                "rationale": "Laptops and liquids must be placed in separate trays."
            },
            {
                "stem": "(audio) What rule is mentioned about liquids?",
                "choices": {
                    "A": "They must be frozen.",
                    "B": "They must be in containers of 100 milliliters or less.",
                    "C": "They must be checked in.",
                    "D": "They must be thrown away."
                },
                "answer": "B",
                "rationale": "Liquids must be in small containers and in a clear bag."
            },
        ],
    },

    # 62. 空港：手荷物カートの案内
    {
        "level": "B1",
        "topic": ["airport", "baggage carts"],
        "script": (
            "Welcome to Central International Airport. "
            "Free baggage carts are available near the baggage claim area and outside the main exit. "
            "Please return carts to the designated areas after use so that other passengers can use them. "
            "For safety, do not allow children to ride on the carts. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) Where are baggage carts available?",
                "choices": {
                    "A": "Only at check-in counters.",
                    "B": "Only in the parking lot.",
                    "C": "Near baggage claim and outside the main exit.",
                    "D": "Only at the information desk."
                },
                "answer": "C",
                "rationale": "Carts are near baggage claim and the main exit."
            },
            {
                "stem": "(audio) What are passengers asked to do after using carts?",
                "choices": {
                    "A": "Leave them anywhere.",
                    "B": "Take them home.",
                    "C": "Return them to designated areas.",
                    "D": "Bring them to the information counter."
                },
                "answer": "C",
                "rationale": "They should return carts to designated areas."
            },
            {
                "stem": "(audio) What safety instruction is given?",
                "choices": {
                    "A": "Do not push carts too fast.",
                    "B": "Do not allow children to ride on carts.",
                    "C": "Do not use carts at night.",
                    "D": "Do not use carts in the parking area."
                },
                "answer": "B",
                "rationale": "Children should not ride on the carts."
            },
        ],
    },

    # 63. 美術館：撮影マナー
    {
        "level": "B1",
        "topic": ["museum", "photo rules"],
        "script": (
            "Welcome to the City Art Gallery. "
            "Photography is allowed in most areas, but flash and tripods are not permitted. "
            "In special exhibition rooms, please follow the signs that indicate whether photos are allowed. "
            "When taking pictures, be careful not to block other visitors’ view. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What is said about photography?",
                "choices": {
                    "A": "It is completely prohibited.",
                    "B": "It is only allowed with tripods.",
                    "C": "It is allowed in most areas but without flash.",
                    "D": "It is only allowed in the lobby."
                },
                "answer": "C",
                "rationale": "Photography is allowed, but flash and tripods are not."
            },
            {
                "stem": "(audio) What should visitors check in special exhibition rooms?",
                "choices": {
                    "A": "Ticket prices.",
                    "B": "Signs about photography.",
                    "C": "Free drink coupons.",
                    "D": "Seat numbers."
                },
                "answer": "B",
                "rationale": "They must follow signs indicating if photos are allowed."
            },
            {
                "stem": "(audio) What are visitors asked to avoid when taking pictures?",
                "choices": {
                    "A": "Using their phones.",
                    "B": "Talking to staff.",
                    "C": "Blocking other visitors’ view.",
                    "D": "Carrying bags."
                },
                "answer": "C",
                "rationale": "They should not block the view of others."
            },
        ],
    },

    # 64. 博物館：音声ガイドの貸出
    {
        "level": "B1",
        "topic": ["museum", "audio guide"],
        "script": (
            "Audio guides are available for this exhibition in Japanese, English, Chinese, and Korean. "
            "You can rent a device at the counter near the entrance for 500 yen by presenting your ticket. "
            "Please return the device to the same counter after your visit. "
            "Headphones are disinfected after each use. "
            "We hope the audio guide helps you enjoy the exhibition."
        ),
        "questions": [
            {
                "stem": "(audio) In how many languages are audio guides available?",
                "choices": {
                    "A": "Two.",
                    "B": "Three.",
                    "C": "Four.",
                    "D": "Five."
                },
                "answer": "C",
                "rationale": "They are available in four languages."
            },
            {
                "stem": "(audio) What must visitors do to rent a device?",
                "choices": {
                    "A": "Show their passport.",
                    "B": "Present their ticket and pay 500 yen.",
                    "C": "Leave a deposit of 2,000 yen.",
                    "D": "Register online in advance."
                },
                "answer": "B",
                "rationale": "They must show their ticket and pay 500 yen."
            },
            {
                "stem": "(audio) What is said about the headphones?",
                "choices": {
                    "A": "They are for sale only.",
                    "B": "They are not included.",
                    "C": "They are disinfected after each use.",
                    "D": "They must be brought from home."
                },
                "answer": "C",
                "rationale": "Headphones are disinfected after use."
            },
        ],
    },

    # 65. 動物園：えさやり禁止の案内
    {
        "level": "B1",
        "topic": ["zoo", "safety"],
        "script": (
            "Welcome to Green Hills Zoo. "
            "For the safety of both visitors and animals, feeding animals is not allowed except in designated areas. "
            "Please do not put your hands through the fences or tap on the glass. "
            "If you see unsafe behavior, inform a staff member nearby. "
            "Thank you for helping us protect the animals."
        ),
        "questions": [
            {
                "stem": "(audio) What is visitors’ main restriction?",
                "choices": {
                    "A": "They must not take photos.",
                    "B": "They must not feed animals except in special areas.",
                    "C": "They must not talk in loud voices.",
                    "D": "They must not bring children."
                },
                "answer": "B",
                "rationale": "Feeding is not allowed except in designated areas."
            },
            {
                "stem": "(audio) What are visitors told not to do with fences or glass?",
                "choices": {
                    "A": "Decorate them.",
                    "B": "Paint them.",
                    "C": "Put their hands through or tap on them.",
                    "D": "Take them apart."
                },
                "answer": "C",
                "rationale": "They should not put hands through fences or tap on glass."
            },
            {
                "stem": "(audio) What should visitors do if they see unsafe behavior?",
                "choices": {
                    "A": "Ignore it.",
                    "B": "Record it on video.",
                    "C": "Post about it online.",
                    "D": "Inform a staff member."
                },
                "answer": "D",
                "rationale": "They are asked to inform staff."
            },
        ],
    },
    # 66. ショッピングセンター：避難訓練
    {
        "level": "B1",
        "topic": ["shopping mall", "evacuation drill"],
        "script": (
            "Attention, shoppers. "
            "A fire evacuation drill will be held in this shopping center at eleven a.m. today. "
            "During the drill, an alarm will sound and staff will guide you to the nearest emergency exits. "
            "Please follow their instructions and do not use the elevators. "
            "This is only a drill, so there is no danger."
        ),
        "questions": [
            {
                "stem": "(audio) What event will take place at eleven a.m.?",
                "choices": {
                    "A": "A cooking demonstration.",
                    "B": "A fire evacuation drill.",
                    "C": "A music performance.",
                    "D": "A sale at a store."
                },
                "answer": "B",
                "rationale": "The announcement says a fire evacuation drill will be held."
            },
            {
                "stem": "(audio) What are shoppers asked NOT to use?",
                "choices": {
                    "A": "Emergency exits.",
                    "B": "Restrooms.",
                    "C": "Stairs.",
                    "D": "Elevators."
                },
                "answer": "D",
                "rationale": "They are told not to use the elevators."
            },
            {
                "stem": "(audio) How should shoppers feel about the alarm?",
                "choices": {
                    "A": "They should be very worried.",
                    "B": "They should immediately leave the city.",
                    "C": "They should know it is only a drill.",
                    "D": "They should ignore staff instructions."
                },
                "answer": "C",
                "rationale": "The announcement explains it is only a drill."
            },
        ],
    },

    # 67. テーマパーク：閉園時間
    {
        "level": "B1",
        "topic": ["theme park", "closing time"],
        "script": (
            "Welcome to Rainbow Theme Park. "
            "Today the park will close at eight p.m., and the last attraction lines will close at seven thirty p.m. "
            "Please make your way to the exit gates before closing time. "
            "Shops near the entrance will remain open for thirty minutes after the park closes. "
            "We hope you enjoy the rest of your visit."
        ),
        "questions": [
            {
                "stem": "(audio) What time will the park close today?",
                "choices": {
                    "A": "At seven p.m.",
                    "B": "At seven thirty p.m.",
                    "C": "At eight p.m.",
                    "D": "At nine p.m."
                },
                "answer": "C",
                "rationale": "The announcement says the park closes at eight p.m."
            },
            {
                "stem": "(audio) When will the lines for attractions close?",
                "choices": {
                    "A": "At six p.m.",
                    "B": "At seven p.m.",
                    "C": "At seven thirty p.m.",
                    "D": "At eight p.m."
                },
                "answer": "C",
                "rationale": "The last attraction lines close at seven thirty."
            },
            {
                "stem": "(audio) What is said about shops near the entrance?",
                "choices": {
                    "A": "They will close at the same time as the park.",
                    "B": "They will stay open for thirty minutes longer.",
                    "C": "They will close earlier than usual.",
                    "D": "They are closed all day."
                },
                "answer": "B",
                "rationale": "They remain open for thirty minutes after closing."
            },
        ],
    },

    # 68. 図書館：コンピュータ利用
    {
        "level": "B1",
        "topic": ["library", "computer use"],
        "script": (
            "This is a notice about the computer terminals in the city library. "
            "Each user may reserve a computer for up to one hour at a time. "
            "If no one is waiting, you may extend your session once at the information desk. "
            "Please do not save personal files on the computers. "
            "When you finish, remember to log out of all websites."
        ),
        "questions": [
            {
                "stem": "(audio) How long can each user reserve a computer at one time?",
                "choices": {
                    "A": "For thirty minutes.",
                    "B": "For one hour.",
                    "C": "For two hours.",
                    "D": "For three hours."
                },
                "answer": "B",
                "rationale": "Each user may reserve a computer for up to one hour."
            },
            {
                "stem": "(audio) When can users extend their session?",
                "choices": {
                    "A": "When they pay an extra fee.",
                    "B": "When a librarian is absent.",
                    "C": "When no one is waiting.",
                    "D": "Only on weekends."
                },
                "answer": "C",
                "rationale": "They may extend only if no one is waiting."
            },
            {
                "stem": "(audio) What are users reminded to do when they finish?",
                "choices": {
                    "A": "Turn off the lights.",
                    "B": "Move the computers.",
                    "C": "Log out of all websites.",
                    "D": "Return all books."
                },
                "answer": "C",
                "rationale": "They should log out when they finish."
            },
        ],
    },

    # 69. 大学：学生食堂リニューアル
    {
        "level": "B1",
        "topic": ["university", "cafeteria renovation"],
        "script": (
            "Students and staff, this is an announcement from the university cafeteria. "
            "The main cafeteria will be closed for renovation from the first of next month for two weeks. "
            "During this period, a temporary lunch corner will operate in the gym lobby. "
            "The menu will be limited, but vegetarian options will still be available. "
            "We apologize for the inconvenience and appreciate your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen to the main cafeteria?",
                "choices": {
                    "A": "It will move to another campus.",
                    "B": "It will be closed for renovation.",
                    "C": "It will be open all night.",
                    "D": "It will become a library."
                },
                "answer": "B",
                "rationale": "The cafeteria will close for renovation."
            },
            {
                "stem": "(audio) Where will meals be served during the closure?",
                "choices": {
                    "A": "In the gym lobby.",
                    "B": "In the student dormitory.",
                    "C": "In the main library.",
                    "D": "In the parking area."
                },
                "answer": "A",
                "rationale": "A temporary lunch corner is in the gym lobby."
            },
            {
                "stem": "(audio) What is said about vegetarian options?",
                "choices": {
                    "A": "They will not be available.",
                    "B": "They will be available only on weekends.",
                    "C": "They will still be available.",
                    "D": "They will be free of charge."
                },
                "answer": "C",
                "rationale": "Vegetarian options will still be provided."
            },
        ],
    },

    # 70. 病院：インフルエンザ予防接種
    {
        "level": "B1",
        "topic": ["hospital", "flu vaccination"],
        "script": (
            "This is a notice from Greenfield Clinic. "
            "Flu vaccinations are now available on weekdays between nine a.m. and noon, and from two to four p.m. "
            "Please make an appointment by phone or through our website before your visit. "
            "On the day of your vaccination, bring your insurance card and questionnaire form. "
            "If you have a fever, please contact us before coming."
        ),
        "questions": [
            {
                "stem": "(audio) What service is the clinic offering?",
                "choices": {
                    "A": "Blood tests.",
                    "B": "Flu vaccinations.",
                    "C": "Dental checkups.",
                    "D": "Eye examinations."
                },
                "answer": "B",
                "rationale": "The announcement is about flu vaccinations."
            },
            {
                "stem": "(audio) How should patients make an appointment?",
                "choices": {
                    "A": "By fax only.",
                    "B": "By visiting the clinic without notice.",
                    "C": "By phone or through the website.",
                    "D": "By sending a letter."
                },
                "answer": "C",
                "rationale": "Appointments are by phone or website."
            },
            {
                "stem": "(audio) What should patients do if they have a fever?",
                "choices": {
                    "A": "Come earlier than scheduled.",
                    "B": "Cancel without calling.",
                    "C": "Go to another hospital.",
                    "D": "Contact the clinic before coming."
                },
                "answer": "D",
                "rationale": "They are told to contact the clinic first."
            },
        ],
    },

    # 71. 幼稚園：運動会のお知らせ
    {
        "level": "B1",
        "topic": ["kindergarten", "sports day"],
        "script": (
            "Parents and guardians, this is an announcement from Sunny Kindergarten. "
            "Our annual sports day will be held on Saturday the fifteenth at the school playground, starting at nine a.m. "
            "Please bring indoor shoes in case we need to move events into the gym due to rain. "
            "We also ask that you label your child’s water bottle and hat with their name. "
            "We look forward to your support and cheers."
        ),
        "questions": [
            {
                "stem": "(audio) What event is being announced?",
                "choices": {
                    "A": "A music concert.",
                    "B": "A sports day.",
                    "C": "A field trip.",
                    "D": "A graduation ceremony."
                },
                "answer": "B",
                "rationale": "The announcement is about the annual sports day."
            },
            {
                "stem": "(audio) Why should parents bring indoor shoes?",
                "choices": {
                    "A": "For use in the school office.",
                    "B": "For walking to the station.",
                    "C": "In case events move to the gym.",
                    "D": "For cleaning the classrooms."
                },
                "answer": "C",
                "rationale": "They may move events into the gym if it rains."
            },
            {
                "stem": "(audio) What should be labeled with the child’s name?",
                "choices": {
                    "A": "Only their shoes.",
                    "B": "Their uniform and socks.",
                    "C": "Their water bottle and hat.",
                    "D": "Their textbook."
                },
                "answer": "C",
                "rationale": "Parents are asked to label bottles and hats."
            },
        ],
    },

    # 72. 鉄道：ダイヤ変更
    {
        "level": "B1",
        "topic": ["train", "timetable change"],
        "script": (
            "This is an announcement from the North Line Railway Company. "
            "From next Monday, the weekday morning timetable will change on trains heading toward Central Station. "
            "Some trains will depart five minutes earlier than before. "
            "Please check the new timetable on the platform displays or on our website before you travel. "
            "We apologize for any inconvenience this may cause."
        ),
        "questions": [
            {
                "stem": "(audio) What will change next Monday?",
                "choices": {
                    "A": "The ticket prices.",
                    "B": "The train cars.",
                    "C": "The weekday morning timetable.",
                    "D": "The station name."
                },
                "answer": "C",
                "rationale": "The morning timetable will change."
            },
            {
                "stem": "(audio) In what way will some trains change?",
                "choices": {
                    "A": "They will depart five minutes earlier.",
                    "B": "They will stop at fewer stations.",
                    "C": "They will be canceled on weekends.",
                    "D": "They will become express trains."
                },
                "answer": "A",
                "rationale": "Some trains depart five minutes earlier."
            },
            {
                "stem": "(audio) Where can passengers check the new timetable?",
                "choices": {
                    "A": "Only in a printed booklet.",
                    "B": "Only at city hall.",
                    "C": "On platform displays or the website.",
                    "D": "Only on the train."
                },
                "answer": "C",
                "rationale": "They can check on displays or online."
            },
        ],
    },

    # 73. フェリー：悪天候による運休
    {
        "level": "B1",
        "topic": ["ferry", "cancellation"],
        "script": (
            "Passengers waiting for the island ferry, please listen to this announcement. "
            "Due to strong winds and high waves, all ferry services after three p.m. today have been canceled. "
            "Tickets for canceled services can be changed to tomorrow’s ferries or refunded at the ticket counter. "
            "We apologize for the inconvenience and ask for your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) Why were the ferry services canceled?",
                "choices": {
                    "A": "Because of engine trouble.",
                    "B": "Because of strong winds and high waves.",
                    "C": "Because of a staff strike.",
                    "D": "Because of a holiday."
                },
                "answer": "B",
                "rationale": "Bad weather caused the cancellation."
            },
            {
                "stem": "(audio) From what time are all ferries canceled?",
                "choices": {
                    "A": "From noon.",
                    "B": "From one p.m.",
                    "C": "From three p.m.",
                    "D": "From six p.m."
                },
                "answer": "C",
                "rationale": "All ferries after three p.m. are canceled."
            },
            {
                "stem": "(audio) What can passengers do with their tickets?",
                "choices": {
                    "A": "Use them on any train.",
                    "B": "Exchange them for food vouchers.",
                    "C": "Change or refund them at the counter.",
                    "D": "Give them to other passengers."
                },
                "answer": "C",
                "rationale": "Tickets can be changed or refunded."
            },
        ],
    },

    # 74. 空港：搭乗ゲート変更
    {
        "level": "B1",
        "topic": ["airport", "gate change"],
        "script": (
            "Ladies and gentlemen, this is an announcement for passengers on Flight 256 to Vancouver. "
            "Please note that the departure gate has been changed from Gate 18 to Gate 22. "
            "The boarding time remains the same. "
            "We apologize for any confusion and ask you to proceed to the new gate as soon as possible."
        ),
        "questions": [
            {
                "stem": "(audio) What has changed about the flight?",
                "choices": {
                    "A": "The destination.",
                    "B": "The airline.",
                    "C": "The departure gate.",
                    "D": "The departure date."
                },
                "answer": "C",
                "rationale": "The gate changed from 18 to 22."
            },
            {
                "stem": "(audio) What is said about the boarding time?",
                "choices": {
                    "A": "It has been delayed.",
                    "B": "It has been moved earlier.",
                    "C": "It remains the same.",
                    "D": "It has not been decided yet."
                },
                "answer": "C",
                "rationale": "Boarding time remains the same."
            },
            {
                "stem": "(audio) What are passengers asked to do?",
                "choices": {
                    "A": "Go back to the check-in counter.",
                    "B": "Proceed to Gate 22.",
                    "C": "Stay at Gate 18.",
                    "D": "Pick up their baggage."
                },
                "answer": "B",
                "rationale": "They should go to the new gate."
            },
        ],
    },

    # 75. ホテル：改装工事と騒音
    {
        "level": "B1",
        "topic": ["hotel", "renovation noise"],
        "script": (
            "Good evening, guests. "
            "We would like to inform you that renovation work will take place on the seventh floor from nine a.m. to five p.m. this week. "
            "You may hear some noise during these hours, especially in rooms nearby. "
            "If you would like a quieter room, please contact the front desk, and we will do our best to assist you. "
            "We apologize for any inconvenience caused."
        ),
        "questions": [
            {
                "stem": "(audio) What is happening on the seventh floor?",
                "choices": {
                    "A": "A party.",
                    "B": "Renovation work.",
                    "C": "A conference.",
                    "D": "A wedding."
                },
                "answer": "B",
                "rationale": "The seventh floor is under renovation."
            },
            {
                "stem": "(audio) When may guests hear noise?",
                "choices": {
                    "A": "From midnight to six a.m.",
                    "B": "Only on weekends.",
                    "C": "From nine a.m. to five p.m.",
                    "D": "Only during lunchtime."
                },
                "answer": "C",
                "rationale": "Work takes place from nine to five."
            },
            {
                "stem": "(audio) What can guests do if they want a quieter room?",
                "choices": {
                    "A": "Move to another hotel by themselves.",
                    "B": "Pay an extra fee at the restaurant.",
                    "C": "Contact the front desk for assistance.",
                    "D": "Use the gym instead of their room."
                },
                "answer": "C",
                "rationale": "They are asked to contact the front desk."
            },
        ],
    },

    # 76. コンベンションセンター：展示会案内
    {
        "level": "B1",
        "topic": ["convention center", "exhibition"],
        "script": (
            "Welcome to City Convention Center. "
            "The Technology and Innovation Expo is being held in Halls A and B today from ten a.m. to six p.m. "
            "Admission is free, but please register at the reception desk before entering the halls. "
            "Seminar schedules and exhibitor lists are available in the brochure racks. "
            "We hope you enjoy the event."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of event is taking place?",
                "choices": {
                    "A": "A food festival.",
                    "B": "A technology and innovation expo.",
                    "C": "A job interview session.",
                    "D": "A health check event."
                },
                "answer": "B",
                "rationale": "It is a Technology and Innovation Expo."
            },
            {
                "stem": "(audio) What must visitors do before entering the halls?",
                "choices": {
                    "A": "Buy a ticket.",
                    "B": "Register at the reception desk.",
                    "C": "Leave their bags in lockers.",
                    "D": "Show a student ID."
                },
                "answer": "B",
                "rationale": "Visitors need to register at reception."
            },
            {
                "stem": "(audio) Where can they find seminar schedules?",
                "choices": {
                    "A": "Only on the website.",
                    "B": "Only at Hall A.",
                    "C": "In the brochure racks.",
                    "D": "At the parking gate."
                },
                "answer": "C",
                "rationale": "Schedules are in the brochure racks."
            },
        ],
    },

    # 77. スポーツクラブ：会員更新キャンペーン
    {
        "level": "B1",
        "topic": ["gym", "membership campaign"],
        "script": (
            "Dear members, this is an announcement from Blue Wave Fitness Club. "
            "If you renew your membership by the end of this month, you will receive one free personal training session. "
            "Renewal can be completed at the front desk or through our smartphone app. "
            "This offer is available only to current members whose membership expires within the next two months. "
            "Please ask our staff for details."
        ),
        "questions": [
            {
                "stem": "(audio) What benefit is offered for early renewal?",
                "choices": {
                    "A": "Free parking.",
                    "B": "A free personal training session.",
                    "C": "A free gym bag.",
                    "D": "A longer opening time."
                },
                "answer": "B",
                "rationale": "Members receive one free training session."
            },
            {
                "stem": "(audio) How can members renew their membership?",
                "choices": {
                    "A": "Only by mail.",
                    "B": "Only by phone.",
                    "C": "At the front desk or via the app.",
                    "D": "At a convenience store."
                },
                "answer": "C",
                "rationale": "Renewal is possible at the desk or through the app."
            },
            {
                "stem": "(audio) Who can use this offer?",
                "choices": {
                    "A": "New visitors only.",
                    "B": "Former members.",
                    "C": "Any resident of the city.",
                    "D": "Current members whose membership expires soon."
                },
                "answer": "D",
                "rationale": "It is for current members expiring within two months."
            },
        ],
    },

    # 78. 海水浴場：遊泳安全ルール
    {
        "level": "B1",
        "topic": ["beach", "safety rules"],
        "script": (
            "Welcome to Sunrise Beach. "
            "For your safety, please swim only within the area marked by the yellow buoys. "
            "Lifeguards are on duty from nine a.m. to five p.m. "
            "Children must be accompanied by an adult in the water. "
            "If you hear a whistle or announcement, leave the water and follow the instructions of the lifeguards."
        ),
        "questions": [
            {
                "stem": "(audio) Where should visitors swim?",
                "choices": {
                    "A": "Anywhere along the shore.",
                    "B": "Only near the rocks.",
                    "C": "Within the yellow buoys.",
                    "D": "Beyond the buoys in deep water."
                },
                "answer": "C",
                "rationale": "Swimming is limited to the buoy-marked area."
            },
            {
                "stem": "(audio) What is said about children?",
                "choices": {
                    "A": "They may swim alone.",
                    "B": "They must be accompanied by an adult.",
                    "C": "They cannot enter the water.",
                    "D": "They must stay on the sand."
                },
                "answer": "B",
                "rationale": "Children must be with an adult in the water."
            },
            {
                "stem": "(audio) What should visitors do if they hear a whistle?",
                "choices": {
                    "A": "Swim further out.",
                    "B": "Ignore it.",
                    "C": "Leave the water and follow instructions.",
                    "D": "Call the police."
                },
                "answer": "C",
                "rationale": "They should leave the water and follow lifeguards."
            },
        ],
    },

    # 79. スキー場：リフト運休
    {
        "level": "B1",
        "topic": ["ski resort", "lift closure"],
        "script": (
            "This is an announcement for guests at Snow Valley Ski Resort. "
            "Due to strong winds at the top of the mountain, the Summit Chairlift will be closed for the rest of today. "
            "All other lifts are operating as usual. "
            "Lift tickets can be partially refunded at the ticket office for guests who planned to use the Summit Chairlift. "
            "We apologize for any disappointment."
        ),
        "questions": [
            {
                "stem": "(audio) Why is the Summit Chairlift closed?",
                "choices": {
                    "A": "Because of heavy rain.",
                    "B": "Because of strong winds.",
                    "C": "Because of maintenance work.",
                    "D": "Because of a power failure."
                },
                "answer": "B",
                "rationale": "Strong winds caused the closure."
            },
            {
                "stem": "(audio) What is said about the other lifts?",
                "choices": {
                    "A": "They are also closed.",
                    "B": "They open only at night.",
                    "C": "They are operating as usual.",
                    "D": "They are free of charge."
                },
                "answer": "C",
                "rationale": "All other lifts operate normally."
            },
            {
                "stem": "(audio) What can some guests receive at the ticket office?",
                "choices": {
                    "A": "Free ski lessons.",
                    "B": "A full refund for their stay.",
                    "C": "A partial refund for their lift tickets.",
                    "D": "Free rental equipment."
                },
                "answer": "C",
                "rationale": "Partial refunds are available for those who planned to use that lift."
            },
        ],
    },

    # 80. 遊園地：アトラクション点検
    {
        "level": "B1",
        "topic": ["amusement park", "ride maintenance"],
        "script": (
            "Attention, visitors. "
            "The Thunder Loop roller coaster is currently closed for safety inspection. "
            "Engineers are checking the ride, and we expect it to reopen later this afternoon. "
            "Other attractions are operating as scheduled. "
            "We apologize for the inconvenience and thank you for your patience."
        ),
        "questions": [
            {
                "stem": "(audio) Why is the Thunder Loop closed?",
                "choices": {
                    "A": "For repainting.",
                    "B": "For a staff meeting.",
                    "C": "For a safety inspection.",
                    "D": "Because of rain."
                },
                "answer": "C",
                "rationale": "Engineers are checking the ride for safety."
            },
            {
                "stem": "(audio) What is expected to happen later this afternoon?",
                "choices": {
                    "A": "The park will close.",
                    "B": "The ride will reopen.",
                    "C": "Tickets will become cheaper.",
                    "D": "Other rides will stop."
                },
                "answer": "B",
                "rationale": "They expect the ride to reopen later."
            },
            {
                "stem": "(audio) What is said about other attractions?",
                "choices": {
                    "A": "They are also closed.",
                    "B": "They are operating as scheduled.",
                    "C": "Only children may use them.",
                    "D": "They are free for one hour."
                },
                "answer": "B",
                "rationale": "Other attractions are operating normally."
            },
        ],
    },

    # 81. 動物園：夜間開園イベント
    {
        "level": "B1",
        "topic": ["zoo", "night event"],
        "script": (
            "Welcome to City Zoo. "
            "This weekend, we will hold a special Night Zoo event, and the zoo will remain open until nine p.m. "
            "Some animals are more active after sunset, so please enjoy watching their behavior. "
            "Flash photography is not allowed during the event to protect the animals’ eyes. "
            "Tickets for the Night Zoo can be purchased at the regular ticket counter."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about this weekend at the zoo?",
                "choices": {
                    "A": "Entrance is free.",
                    "B": "The zoo opens earlier than usual.",
                    "C": "There is a Night Zoo event.",
                    "D": "All animals will be indoors."
                },
                "answer": "C",
                "rationale": "They are holding a Night Zoo event."
            },
            {
                "stem": "(audio) What rule is mentioned about photography?",
                "choices": {
                    "A": "All photography is banned.",
                    "B": "Only video cameras are allowed.",
                    "C": "Flash photography is not allowed.",
                    "D": "Photos may be taken only at the entrance."
                },
                "answer": "C",
                "rationale": "Flash is not allowed to protect animals."
            },
            {
                "stem": "(audio) Where can visitors buy tickets for the event?",
                "choices": {
                    "A": "Online only.",
                    "B": "At a special booth outside the zoo.",
                    "C": "At the regular ticket counter.",
                    "D": "At the city hall."
                },
                "answer": "C",
                "rationale": "Tickets can be bought at the regular counter."
            },
        ],
    },

    # 82. 水族館：ショーの時間
    {
        "level": "B1",
        "topic": ["aquarium", "show schedule"],
        "script": (
            "Thank you for visiting Blue Ocean Aquarium. "
            "The dolphin show will start at two p.m. in the main pool arena. "
            "Doors will open twenty minutes before the show, and seats may fill up quickly. "
            "Please do not reserve seats with bags or towels. "
            "For your safety, do not lean on the pool fence during the performance."
        ),
        "questions": [
            {
                "stem": "(audio) What time does the dolphin show begin?",
                "choices": {
                    "A": "At one p.m.",
                    "B": "At two p.m.",
                    "C": "At three p.m.",
                    "D": "At four p.m."
                },
                "answer": "B",
                "rationale": "The show starts at two p.m."
            },
            {
                "stem": "(audio) When do the doors open?",
                "choices": {
                    "A": "Ten minutes before the show.",
                    "B": "Twenty minutes before the show.",
                    "C": "Thirty minutes before the show.",
                    "D": "One hour before the show."
                },
                "answer": "B",
                "rationale": "Doors open twenty minutes in advance."
            },
            {
                "stem": "(audio) What are visitors asked not to do?",
                "choices": {
                    "A": "Bring children.",
                    "B": "Buy snacks.",
                    "C": "Reserve seats with bags or towels.",
                    "D": "Take pictures of dolphins."
                },
                "answer": "C",
                "rationale": "They are told not to reserve seats with items."
            },
        ],
    },

    # 83. デパート：新春セール
    {
        "level": "B1",
        "topic": ["department store", "sale"],
        "script": (
            "Welcome to Sunrise Department Store. "
            "Our New Year Sale will start on January second at ten a.m. "
            "The first one hundred customers on each floor will receive a special gift. "
            "Some items will be up to fifty percent off the regular price. "
            "Please check the flyers and posters in the store for details."
        ),
        "questions": [
            {
                "stem": "(audio) When does the New Year Sale begin?",
                "choices": {
                    "A": "On January first.",
                    "B": "On January second.",
                    "C": "On January fifth.",
                    "D": "Next month."
                },
                "answer": "B",
                "rationale": "The sale starts on January second."
            },
            {
                "stem": "(audio) Who will receive a special gift?",
                "choices": {
                    "A": "All customers who visit.",
                    "B": "Only children.",
                    "C": "The first one hundred customers on each floor.",
                    "D": "Customers who spend over 10,000 yen."
                },
                "answer": "C",
                "rationale": "The first hundred on each floor get a gift."
            },
            {
                "stem": "(audio) What is said about some items?",
                "choices": {
                    "A": "They will be free.",
                    "B": "They will be up to fifty percent off.",
                    "C": "They will not be sold during the sale.",
                    "D": "They will be available only online."
                },
                "answer": "B",
                "rationale": "Some items are up to fifty percent off."
            },
        ],
    },

    # 84. レストラン：団体予約ポリシー
    {
        "level": "B1",
        "topic": ["restaurant", "group reservation"],
        "script": (
            "Thank you for calling Green Garden Restaurant. "
            "For groups of ten or more, we ask that you make a reservation at least three days in advance. "
            "A set course menu is required for large groups, and any changes to the number of guests should be reported by the previous day. "
            "If you need to cancel on the day of your reservation, a cancellation fee may be charged. "
            "Please speak with our staff if you have special dietary requests."
        ),
        "questions": [
            {
                "stem": "(audio) When should large groups make a reservation?",
                "choices": {
                    "A": "On the same day.",
                    "B": "One day in advance.",
                    "C": "At least three days in advance.",
                    "D": "Only a week in advance."
                },
                "answer": "C",
                "rationale": "They must reserve at least three days ahead."
            },
            {
                "stem": "(audio) What is required for large groups?",
                "choices": {
                    "A": "Ordering individually from the menu.",
                    "B": "A set course menu.",
                    "C": "Bringing their own food.",
                    "D": "Paying in advance at the bank."
                },
                "answer": "B",
                "rationale": "A set course menu is required."
            },
            {
                "stem": "(audio) What may happen if they cancel on the day?",
                "choices": {
                    "A": "They will receive a free meal.",
                    "B": "They will be banned from the restaurant.",
                    "C": "They may be charged a cancellation fee.",
                    "D": "They must cook in the kitchen."
                },
                "answer": "C",
                "rationale": "A cancellation fee may be charged."
            },
        ],
    },

    # 85. 立体駐車場：点検による閉鎖
    {
        "level": "B1",
        "topic": ["parking", "inspection"],
        "script": (
            "This is an announcement for customers using the Central Parking Garage. "
            "Due to a regular safety inspection, the third and fourth floors of the garage will be closed tomorrow from eight a.m. to two p.m. "
            "Please use the remaining floors or nearby parking lots during this time. "
            "Cars already parked on these floors should be removed before eight a.m. "
            "We apologize for the inconvenience."
        ),
        "questions": [
            {
                "stem": "(audio) Which floors will be closed?",
                "choices": {
                    "A": "The first and second floors.",
                    "B": "The second and third floors.",
                    "C": "The third and fourth floors.",
                    "D": "All floors."
                },
                "answer": "C",
                "rationale": "The third and fourth floors will be closed."
            },
            {
                "stem": "(audio) What should drivers do if their cars are on those floors?",
                "choices": {
                    "A": "Move them before eight a.m.",
                    "B": "Leave them until the next day.",
                    "C": "Pay a special fee.",
                    "D": "Call the police."
                },
                "answer": "A",
                "rationale": "Cars should be removed before eight a.m."
            },
            {
                "stem": "(audio) What is suggested during the closure?",
                "choices": {
                    "A": "Use nearby parking lots or other floors.",
                    "B": "Avoid coming to the city.",
                    "C": "Park on the street for free.",
                    "D": "Bring bicycles instead."
                },
                "answer": "A",
                "rationale": "They can use the remaining floors or nearby lots."
            },
        ],
    },

    # 86. 高速道路サービスエリア：施設休止
    {
        "level": "B1",
        "topic": ["highway", "rest area"],
        "script": (
            "Drivers on the East Highway, please be aware that the shower facilities at Lakeview Service Area will be closed for maintenance next Wednesday. "
            "Restrooms, restaurants, and gas stations will operate as usual. "
            "If you need shower facilities, please use the Mountain Side Service Area instead. "
            "We apologize for any inconvenience this may cause."
        ),
        "questions": [
            {
                "stem": "(audio) Which facility will be closed?",
                "choices": {
                    "A": "The restrooms.",
                    "B": "The gas station.",
                    "C": "The shower facilities.",
                    "D": "The restaurants."
                },
                "answer": "C",
                "rationale": "Only the shower facilities will be closed."
            },
            {
                "stem": "(audio) What is said about other facilities at the service area?",
                "choices": {
                    "A": "They will all be closed.",
                    "B": "They will open only at night.",
                    "C": "They will operate as usual.",
                    "D": "They will also have maintenance."
                },
                "answer": "C",
                "rationale": "Restrooms, restaurants, and gas stations remain open."
            },
            {
                "stem": "(audio) What should drivers do if they need a shower?",
                "choices": {
                    "A": "Use the Mountain Side Service Area.",
                    "B": "Turn back to the city.",
                    "C": "Wait until the next day.",
                    "D": "Shower at the gas station."
                },
                "answer": "A",
                "rationale": "They are told to use the Mountain Side Service Area."
            },
        ],
    },

    # 87. オフィスビル：喫煙所の移転
    {
        "level": "B1",
        "topic": ["office building", "smoking area"],
        "script": (
            "Attention, tenants. "
            "The smoking area on the second floor terrace will be closed at the end of this month. "
            "A new smoking area will open on the rooftop, accessible by Elevator C. "
            "Smoking is not allowed in any other part of the building, including stairwells and restrooms. "
            "Thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What change is being announced?",
                "choices": {
                    "A": "A new cafeteria is opening.",
                    "B": "The building will close earlier.",
                    "C": "The smoking area will move to the rooftop.",
                    "D": "Parking fees will change."
                },
                "answer": "C",
                "rationale": "The smoking area is being relocated to the rooftop."
            },
            {
                "stem": "(audio) How can people reach the new smoking area?",
                "choices": {
                    "A": "By Elevator C.",
                    "B": "By the emergency stairs only.",
                    "C": "By a special outside entrance.",
                    "D": "By Elevator A and B only."
                },
                "answer": "A",
                "rationale": "It is accessible via Elevator C."
            },
            {
                "stem": "(audio) Where is smoking NOT allowed?",
                "choices": {
                    "A": "In the new rooftop area.",
                    "B": "In stairwells and restrooms.",
                    "C": "On the terrace only.",
                    "D": "At the building entrance only."
                },
                "answer": "B",
                "rationale": "Smoking is forbidden except in the designated area."
            },
        ],
    },

    # 88. 大学図書館：試験期間中の延長開館
    {
        "level": "B1",
        "topic": ["university", "library hours"],
        "script": (
            "This is an announcement from the university library. "
            "During the exam period from May tenth to May twenty-fourth, the library will be open until eleven p.m. on weekdays. "
            "On Saturdays and Sundays, opening hours remain unchanged. "
            "Please bring your student ID to enter after six p.m. "
            "We wish you good luck with your studies."
        ),
        "questions": [
            {
                "stem": "(audio) What change will occur during the exam period?",
                "choices": {
                    "A": "The library will close earlier.",
                    "B": "The library will open on holidays only.",
                    "C": "The library will stay open until eleven p.m. on weekdays.",
                    "D": "The library will be closed on weekends."
                },
                "answer": "C",
                "rationale": "Weekday hours are extended to eleven p.m."
            },
            {
                "stem": "(audio) What is required to enter after six p.m.?",
                "choices": {
                    "A": "A library card only.",
                    "B": "A student ID.",
                    "C": "A teacher’s note.",
                    "D": "A reservation ticket."
                },
                "answer": "B",
                "rationale": "Students must show their student ID."
            },
            {
                "stem": "(audio) What is said about weekend hours?",
                "choices": {
                    "A": "They are unchanged.",
                    "B": "They will be longer.",
                    "C": "They will be shorter.",
                    "D": "The library will be closed."
                },
                "answer": "A",
                "rationale": "Weekend hours remain the same."
            },
        ],
    },

    # 89. 鉄道：ICカード利用の注意
    {
        "level": "B1",
        "topic": ["train", "IC card"],
        "script": (
            "Passengers using IC cards, please touch your card firmly to the ticket gate reader when entering and exiting. "
            "If the gate does not open, check the balance on your card at the nearest fare adjustment machine. "
            "Children should use child IC cards to receive the correct fare. "
            "If you have any questions, ask a station staff member."
        ),
        "questions": [
            {
                "stem": "(audio) What should passengers do with their IC cards at the ticket gate?",
                "choices": {
                    "A": "Insert them into a slot.",
                    "B": "Show them to the conductor.",
                    "C": "Touch them firmly to the reader.",
                    "D": "Hand them to other passengers."
                },
                "answer": "C",
                "rationale": "They must touch the card to the reader."
            },
            {
                "stem": "(audio) What should passengers do if the gate does not open?",
                "choices": {
                    "A": "Jump over the gate.",
                    "B": "Check the card balance at a machine.",
                    "C": "Leave the station immediately.",
                    "D": "Break the gate."
                },
                "answer": "B",
                "rationale": "They should check the balance at a fare machine."
            },
            {
                "stem": "(audio) What is said about children?",
                "choices": {
                    "A": "They should pay in cash only.",
                    "B": "They must not use IC cards.",
                    "C": "They should use adult cards.",
                    "D": "They should use child IC cards."
                },
                "answer": "D",
                "rationale": "Children are asked to use child IC cards."
            },
        ],
    },

    # 90. 美術館：無料入館デー
    {
        "level": "B1",
        "topic": ["museum", "free admission day"],
        "script": (
            "This Sunday is Free Admission Day at the City Museum. "
            "Entrance fees will be waived for all visitors, and no reservation is required. "
            "Please note that special exhibitions may still require a separate ticket. "
            "The museum is expected to be crowded, so please consider using public transportation. "
            "For opening hours, please see our website."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about this Sunday at the museum?",
                "choices": {
                    "A": "It will be closed.",
                    "B": "There will be a fireworks show.",
                    "C": "Admission will be free.",
                    "D": "Only members may enter."
                },
                "answer": "C",
                "rationale": "Entrance fees are waived for all visitors."
            },
            {
                "stem": "(audio) What is said about special exhibitions?",
                "choices": {
                    "A": "They are also free.",
                    "B": "They require a separate ticket.",
                    "C": "They are closed on Sundays.",
                    "D": "They are moved outside."
                },
                "answer": "B",
                "rationale": "Special exhibitions may still cost extra."
            },
            {
                "stem": "(audio) What transportation advice is given?",
                "choices": {
                    "A": "Use public transportation.",
                    "B": "Come by taxi only.",
                    "C": "Drive and park for free.",
                    "D": "Do not visit the museum."
                },
                "answer": "A",
                "rationale": "Visitors are asked to consider public transportation."
            },
        ],
    },

    # 91. 観光：無料市内周遊バス
    {
        "level": "B1",
        "topic": ["tourism", "city loop bus"],
        "script": (
            "Welcome to River City. "
            "A free city loop bus runs every twenty minutes from ten a.m. to six p.m. "
            "The bus stops at major sightseeing spots, including the museum, the castle, and the riverside park. "
            "You can board and get off as many times as you like. "
            "Look for the blue bus stop signs with the city logo."
        ),
        "questions": [
            {
                "stem": "(audio) How much does the city loop bus cost?",
                "choices": {
                    "A": "It depends on the distance.",
                    "B": "It costs 200 yen per ride.",
                    "C": "It is free of charge.",
                    "D": "It is free only for children."
                },
                "answer": "C",
                "rationale": "The bus is a free city loop service."
            },
            {
                "stem": "(audio) How often does the bus run?",
                "choices": {
                    "A": "Every ten minutes.",
                    "B": "Every twenty minutes.",
                    "C": "Every hour.",
                    "D": "Only twice a day."
                },
                "answer": "B",
                "rationale": "It runs every twenty minutes."
            },
            {
                "stem": "(audio) What should visitors look for to find the bus stops?",
                "choices": {
                    "A": "Red flags.",
                    "B": "Yellow posters.",
                    "C": "Blue bus stop signs with the city logo.",
                    "D": "Green street signs."
                },
                "answer": "C",
                "rationale": "The stops are marked with blue signs and the city logo."
            },
        ],
    },

    # 92. 空港ラウンジ：利用条件
    {
        "level": "B1",
        "topic": ["airport", "lounge"],
        "script": (
            "This is a notice about the Sky View Lounge. "
            "The lounge is available to business class passengers and members of our gold and platinum frequent flyer programs. "
            "Other passengers may enter the lounge by paying an entrance fee at the reception desk. "
            "Inside the lounge, please speak quietly and set your mobile phones to silent mode. "
            "We hope you have a comfortable time before your flight."
        ),
        "questions": [
            {
                "stem": "(audio) Who can use the lounge for free?",
                "choices": {
                    "A": "All economy class passengers.",
                    "B": "Business class passengers and certain members.",
                    "C": "Only passengers with children.",
                    "D": "Only passengers on domestic flights."
                },
                "answer": "B",
                "rationale": "Business class and gold/platinum members can use it."
            },
            {
                "stem": "(audio) How can other passengers enter the lounge?",
                "choices": {
                    "A": "By buying items in the duty-free shop.",
                    "B": "By joining a tour group.",
                    "C": "By paying an entrance fee.",
                    "D": "By making an online reservation only."
                },
                "answer": "C",
                "rationale": "They may pay a fee at the reception desk."
            },
            {
                "stem": "(audio) What are passengers asked to do with their mobile phones?",
                "choices": {
                    "A": "Turn them off completely.",
                    "B": "Set them to silent mode.",
                    "C": "Leave them at the reception desk.",
                    "D": "Use them only near the windows."
                },
                "answer": "B",
                "rationale": "Phones should be in silent mode inside the lounge."
            },
        ],
    },

    # 93. 市民祭り：スケジュール
    {
        "level": "B1",
        "topic": ["city hall", "festival"],
        "script": (
            "This is an announcement about the Riverside Citizens’ Festival. "
            "The festival will be held this Sunday from ten a.m. to eight p.m. at Riverside Park. "
            "There will be food stalls, stage performances, and a fireworks display starting at seven thirty p.m. "
            "Please use public transportation, as parking near the park is limited. "
            "For more details, see the city website."
        ),
        "questions": [
            {
                "stem": "(audio) Where will the festival be held?",
                "choices": {
                    "A": "At the city hall building.",
                    "B": "At the train station.",
                    "C": "At Riverside Park.",
                    "D": "At the shopping mall."
                },
                "answer": "C",
                "rationale": "The festival takes place at Riverside Park."
            },
            {
                "stem": "(audio) What time will the fireworks start?",
                "choices": {
                    "A": "At six p.m.",
                    "B": "At seven p.m.",
                    "C": "At seven thirty p.m.",
                    "D": "At eight p.m."
                },
                "answer": "C",
                "rationale": "Fireworks begin at seven thirty."
            },
            {
                "stem": "(audio) What transportation advice is given?",
                "choices": {
                    "A": "Everyone must drive.",
                    "B": "Use public transportation.",
                    "C": "Take only taxis.",
                    "D": "Walk from the airport."
                },
                "answer": "B",
                "rationale": "Parking is limited, so public transportation is recommended."
            },
        ],
    },

    # 94. スタジアム：試合観戦マナー
    {
        "level": "B1",
        "topic": ["stadium", "game rules"],
        "script": (
            "Welcome to Central Stadium. "
            "During today’s match, please remain in your seat while the ball is in play. "
            "Standing in the aisles is not permitted for safety reasons. "
            "Please do not bring bottles or cans into the seating area; drinks should be in paper cups or plastic bottles with caps. "
            "Thank you for your cooperation and enjoy the game."
        ),
        "questions": [
            {
                "stem": "(audio) What are spectators asked to do during the match?",
                "choices": {
                    "A": "Move around freely.",
                    "B": "Remain in their seats while the ball is in play.",
                    "C": "Stand in the aisles to cheer.",
                    "D": "Leave before halftime."
                },
                "answer": "B",
                "rationale": "They should remain seated while play is in progress."
            },
            {
                "stem": "(audio) Why is standing in the aisles not permitted?",
                "choices": {
                    "A": "It blocks the view of the players.",
                    "B": "It is dangerous for safety.",
                    "C": "It is too noisy.",
                    "D": "It is against TV rules."
                },
                "answer": "B",
                "rationale": "Standing in aisles is restricted for safety reasons."
            },
            {
                "stem": "(audio) What kind of drink containers are NOT allowed in the seating area?",
                "choices": {
                    "A": "Paper cups.",
                    "B": "Plastic bottles with caps.",
                    "C": "Bottles or cans.",
                    "D": "Drinks from the vending machine."
                },
                "answer": "C",
                "rationale": "Bottles and cans are not allowed."
            },
        ],
    },

    # 95. 音楽フェス：持ち込み禁止物
    {
        "level": "B1",
        "topic": ["music festival", "prohibited items"],
        "script": (
            "Thank you for attending the Green Field Music Festival. "
            "For the safety and comfort of all guests, glass bottles, large umbrellas, and fireworks are not allowed inside the venue. "
            "Please also refrain from bringing large chairs that may block other people’s view. "
            "Bags may be checked at the entrance. "
            "We appreciate your understanding and cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) Which of the following is NOT allowed inside the venue?",
                "choices": {
                    "A": "Glass bottles.",
                    "B": "Plastic raincoats.",
                    "C": "Small folding towels.",
                    "D": "Hats and caps."
                },
                "answer": "A",
                "rationale": "Glass bottles are listed as prohibited."
            },
            {
                "stem": "(audio) Why are large chairs discouraged?",
                "choices": {
                    "A": "They are too expensive.",
                    "B": "They may block other people’s view.",
                    "C": "They are difficult to carry.",
                    "D": "They damage the grass."
                },
                "answer": "B",
                "rationale": "Large chairs can block others’ view."
            },
            {
                "stem": "(audio) What may happen to bags at the entrance?",
                "choices": {
                    "A": "They will be refused.",
                    "B": "They will be sold.",
                    "C": "They may be checked.",
                    "D": "They will be stored overnight."
                },
                "answer": "C",
                "rationale": "Bags may be checked at the entrance."
            },
        ],
    },

    # 96. オンラインセミナー：接続の案内
    {
        "level": "B1",
        "topic": ["online", "webinar"],
        "script": (
            "Thank you for registering for our online seminar. "
            "The seminar will begin at seven p.m., but you can log in from six forty-five p.m. to test your connection. "
            "Please check that your microphone is muted when you join. "
            "If you have technical problems, use the chat window to contact the host. "
            "A recording of the seminar will be sent to all participants afterward."
        ),
        "questions": [
            {
                "stem": "(audio) From what time can participants log in to test their connection?",
                "choices": {
                    "A": "From six p.m.",
                    "B": "From six thirty p.m.",
                    "C": "From six forty-five p.m.",
                    "D": "From seven thirty p.m."
                },
                "answer": "C",
                "rationale": "They can log in from 6:45 p.m."
            },
            {
                "stem": "(audio) What should participants do with their microphones when they join?",
                "choices": {
                    "A": "Turn them up loudly.",
                    "B": "Mute them.",
                    "C": "Use two microphones.",
                    "D": "Disconnect them."
                },
                "answer": "B",
                "rationale": "They are asked to keep microphones muted."
            },
            {
                "stem": "(audio) How will participants receive the seminar recording?",
                "choices": {
                    "A": "On a USB drive.",
                    "B": "By mail only.",
                    "C": "As a link sent afterward.",
                    "D": "At the company office."
                },
                "answer": "C",
                "rationale": "A recording will be sent to participants."
            },
        ],
    },

    # 97. コワーキングスペース：利用ルール
    {
        "level": "B1",
        "topic": ["coworking space", "rules"],
        "script": (
            "Welcome to Bridge Coworking Space. "
            "Please check in at the front desk when you arrive and check out when you leave. "
            "Phone calls should be made in the designated phone booths, not at shared desks. "
            "Meeting rooms must be reserved in advance through our website. "
            "Free coffee and tea are available in the kitchen area, but please keep it clean."
        ),
        "questions": [
            {
                "stem": "(audio) What should users do when they arrive and leave?",
                "choices": {
                    "A": "Call the manager each time.",
                    "B": "Sign a paper contract.",
                    "C": "Check in and check out at the front desk.",
                    "D": "Turn off all lights."
                },
                "answer": "C",
                "rationale": "They must check in and out."
            },
            {
                "stem": "(audio) Where should phone calls be made?",
                "choices": {
                    "A": "At any shared desk.",
                    "B": "In the kitchen area.",
                    "C": "In the designated phone booths.",
                    "D": "In front of the building."
                },
                "answer": "C",
                "rationale": "Phone calls belong in the phone booths."
            },
            {
                "stem": "(audio) How are meeting rooms reserved?",
                "choices": {
                    "A": "By writing names on the door.",
                    "B": "By calling the city office.",
                    "C": "By using the website.",
                    "D": "By talking to other users."
                },
                "answer": "C",
                "rationale": "Meeting rooms must be reserved through the website."
            },
        ],
    },

    # 98. 語学試験：リスニングテストの注意
    {
        "level": "B1",
        "topic": ["language test", "listening section"],
        "script": (
            "You are about to begin the listening section of the language test. "
            "You will hear each question only once. "
            "Mark your answers on the separate answer sheet, not in the test booklet. "
            "If you cannot hear the recording clearly, raise your hand now. "
            "Once the test has started, we cannot stop the CD."
        ),
        "questions": [
            {
                "stem": "(audio) How many times will each question be played?",
                "choices": {
                    "A": "Only once.",
                    "B": "Twice.",
                    "C": "Three times.",
                    "D": "As many times as needed."
                },
                "answer": "A",
                "rationale": "Each question is heard only once."
            },
            {
                "stem": "(audio) Where should test takers mark their answers?",
                "choices": {
                    "A": "In the test booklet.",
                    "B": "On the separate answer sheet.",
                    "C": "On a piece of scrap paper.",
                    "D": "On the desk."
                },
                "answer": "B",
                "rationale": "Answers must be on the answer sheet."
            },
            {
                "stem": "(audio) When should test takers say something if they cannot hear clearly?",
                "choices": {
                    "A": "After the test is finished.",
                    "B": "During the break.",
                    "C": "Right now, before it starts.",
                    "D": "At home."
                },
                "answer": "C",
                "rationale": "They should raise their hand before the test begins."
            },
        ],
    },

    # 99. ホテル：送迎バスの時刻
    {
        "level": "B1",
        "topic": ["hotel", "shuttle bus"],
        "script": (
            "This is a notice about the free shuttle bus to Central Station. "
            "Buses depart from the hotel entrance every hour on the hour from seven a.m. to ten p.m. "
            "Seats are available on a first-come, first-served basis, and reservations are not required. "
            "Please be at the entrance five minutes before departure. "
            "If the bus is full, please wait for the next one."
        ),
        "questions": [
            {
                "stem": "(audio) How often does the shuttle bus depart?",
                "choices": {
                    "A": "Every 30 minutes.",
                    "B": "Every hour.",
                    "C": "Twice a day.",
                    "D": "Only in the morning."
                },
                "answer": "B",
                "rationale": "It departs every hour on the hour."
            },
            {
                "stem": "(audio) Are reservations required to use the bus?",
                "choices": {
                    "A": "Yes, always.",
                    "B": "Only at night.",
                    "C": "Only for groups.",
                    "D": "No, they are not required."
                },
                "answer": "D",
                "rationale": "Seats are first-come, first-served and no reservation is needed."
            },
            {
                "stem": "(audio) What should guests do if the bus is full?",
                "choices": {
                    "A": "Ride on the roof.",
                    "B": "Complain at the front desk.",
                    "C": "Wait for the next bus.",
                    "D": "Walk to the station."
                },
                "answer": "C",
                "rationale": "They are asked to wait for the next bus."
            },
        ],
    },

    # 100. スーパー：エコバッグ推奨
    {
        "level": "B1",
        "topic": ["supermarket", "eco bags"],
        "script": (
            "Dear customers, this is an announcement from Green Leaf Supermarket. "
            "To reduce plastic waste, we encourage you to bring your own shopping bags. "
            "Plastic bags at the checkout counter cost five yen each. "
            "Customers who bring their own bags will receive one point on their point card per visit. "
            "Thank you for helping us protect the environment."
        ),
        "questions": [
            {
                "stem": "(audio) What does the supermarket encourage customers to do?",
                "choices": {
                    "A": "Buy more plastic bags.",
                    "B": "Bring their own shopping bags.",
                    "C": "Leave their bags at home.",
                    "D": "Shop only once a month."
                },
                "answer": "B",
                "rationale": "They are encouraged to bring their own bags."
            },
            {
                "stem": "(audio) How much does each plastic bag cost?",
                "choices": {
                    "A": "One yen.",
                    "B": "Three yen.",
                    "C": "Five yen.",
                    "D": "Ten yen."
                },
                "answer": "C",
                "rationale": "Each plastic bag costs five yen."
            },
            {
                "stem": "(audio) What benefit do customers get if they bring their own bags?",
                "choices": {
                    "A": "Free parking.",
                    "B": "A discount on vegetables.",
                    "C": "One point on their point card.",
                    "D": "A free drink."
                },
                "answer": "C",
                "rationale": "They receive one point per visit."
            },
        ],
    },

    # --- B2 level 30patterns (more challenging) ---
    # 1. 会社の全体ミーティング案内
    {
        "level": "B2",
        "topic": ["company", "town hall", "meeting"],
        "script": (
            "Good morning, everyone. "
            "This is a reminder about our quarterly town hall meeting this Friday. "
            "It will start at three p.m. in the main auditorium and last for about ninety minutes. "
            "Our CEO will first talk about recent sales results, and then each department manager will share their plans for the next three months. "
            "If you cannot attend in person, you may join online using the link on the intranet."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main purpose of the announcement?",
                "choices": {
                    "A": "To remind staff about a company meeting.",
                    "B": "To introduce a new office building.",
                    "C": "To ask employees to update their profiles.",
                    "D": "To explain how to request vacation days."
                },
                "answer": "A",
                "rationale": "It reminds workers about the upcoming town hall meeting."
            },
            {
                "stem": "(audio) What will happen first at the event?",
                "choices": {
                    "A": "A question-and-answer session.",
                    "B": "A speech by the CEO about sales results.",
                    "C": "A workshop on communication skills.",
                    "D": "A tour of the main auditorium."
                },
                "answer": "B",
                "rationale": "The CEO will talk about recent sales before the managers speak."
            },
            {
                "stem": "(audio) What can employees do if they cannot attend in person?",
                "choices": {
                    "A": "Watch a recording next month.",
                    "B": "Call the CEO on the phone.",
                    "C": "Join the meeting online using a link.",
                    "D": "Send written questions to the managers only."
                },
                "answer": "C",
                "rationale": "They may join online using the intranet link."
            },
        ],
    },

    # 2. オンライン研修システムのメンテナンス
    {
        "level": "B2",
        "topic": ["online training", "maintenance"],
        "script": (
            "Attention, employees. "
            "Our online training system will be under maintenance this Saturday from eight a.m. to two p.m. "
            "During this time, you will not be able to watch any training videos or take quizzes. "
            "If you have a deadline for a mandatory course, please complete it before Saturday morning or wait until the system is available again. "
            "We appreciate your understanding."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen to the training system on Saturday?",
                "choices": {
                    "A": "It will be moved to a new building.",
                    "B": "It will not be available during maintenance.",
                    "C": "It will be free for guests to use.",
                    "D": "It will be used only for managers."
                },
                "answer": "B",
                "rationale": "The system will be under maintenance and cannot be used."
            },
            {
                "stem": "(audio) Which activity will NOT be possible during the maintenance?",
                "choices": {
                    "A": "Watching training videos.",
                    "B": "Sending e-mails to coworkers.",
                    "C": "Attending meetings in person.",
                    "D": "Printing documents in the office."
                },
                "answer": "A",
                "rationale": "The announcement says users cannot watch videos or take quizzes."
            },
            {
                "stem": "(audio) What should employees do if they have a course deadline soon?",
                "choices": {
                    "A": "Ignore the deadline.",
                    "B": "Take the course before Saturday or after the maintenance.",
                    "C": "Ask a trainer to change the questions.",
                    "D": "Use another company’s system instead."
                },
                "answer": "B",
                "rationale": "They are told to finish the course before maintenance or after it ends."
            },
        ],
    },

    # 3. 空港の搭乗ゲート変更
    {
        "level": "B2",
        "topic": ["airport", "gate change"],
        "script": (
            "Ladies and gentlemen, this is a gate change announcement for Flight 76 to Toronto. "
            "Due to a scheduling issue, the flight will now depart from Gate 18 instead of Gate 9. "
            "The departure time remains the same. "
            "If you have already been waiting near Gate 9, please move to Gate 18 as soon as possible. "
            "Airport staff members are available in the area to guide you if you need assistance."
        ),
        "questions": [
            {
                "stem": "(audio) What has changed about Flight 76?",
                "choices": {
                    "A": "Its destination.",
                    "B": "Its departure date.",
                    "C": "Its departure gate.",
                    "D": "Its airline."
                },
                "answer": "C",
                "rationale": "Only the gate has changed from 9 to 18."
            },
            {
                "stem": "(audio) What is said about the departure time?",
                "choices": {
                    "A": "It has been moved to an earlier time.",
                    "B": "It stays the same as before.",
                    "C": "It will be delayed by two hours.",
                    "D": "It will be announced later."
                },
                "answer": "B",
                "rationale": "The announcement clearly states the time remains the same."
            },
            {
                "stem": "(audio) What are passengers advised to do?",
                "choices": {
                    "A": "Return to the check-in counter.",
                    "B": "Wait near the baggage claim area.",
                    "C": "Move from Gate 9 to Gate 18.",
                    "D": "Pick up food at the restaurant first."
                },
                "answer": "C",
                "rationale": "They are asked to move to the new gate quickly."
            },
        ],
    },

    # 4. ホテルの改装工事のお知らせ
    {
        "level": "B2",
        "topic": ["hotel", "renovation"],
        "script": (
            "Good evening, guests. "
            "We would like to inform you that our hotel will be doing renovation work on the sixth floor from Tuesday to Friday. "
            "Construction will take place between ten a.m. and four p.m., and you may hear some noise during those hours. "
            "If you prefer a quieter room, please contact the front desk, and we will do our best to move you to a different floor. "
            "Thank you for your understanding and cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen at the hotel from Tuesday to Friday?",
                "choices": {
                    "A": "A large wedding party.",
                    "B": "Renovation work on one floor.",
                    "C": "A special discount campaign.",
                    "D": "A staff training seminar."
                },
                "answer": "B",
                "rationale": "Renovation work will be done on the sixth floor."
            },
            {
                "stem": "(audio) During which hours might guests hear noise?",
                "choices": {
                    "A": "From ten a.m. to four p.m.",
                    "B": "From six a.m. to eight a.m.",
                    "C": "From five p.m. to midnight.",
                    "D": "Only on weekend nights."
                },
                "answer": "A",
                "rationale": "Construction will happen between ten and four."
            },
            {
                "stem": "(audio) What can guests do if they want a quieter stay?",
                "choices": {
                    "A": "Cancel their reservation online.",
                    "B": "Ask to be moved to a different floor.",
                    "C": "Request free meals in the restaurant.",
                    "D": "Use only the sixth floor lounge."
                },
                "answer": "B",
                "rationale": "The hotel offers to move them to another floor if possible."
            },
        ],
    },

    # 5. 美術館の音声ガイド案内
    {
        "level": "B2",
        "topic": ["museum", "audio guide"],
        "script": (
            "Welcome to the City Art Museum. "
            "For this special exhibition, we offer an audio guide in four languages. "
            "You can rent a device at the entrance for a small fee, or download the guide to your own phone using the QR code on the brochure. "
            "Please remember to return the rental device to the counter before you leave the museum."
        ),
        "questions": [
            {
                "stem": "(audio) What service is being introduced in the announcement?",
                "choices": {
                    "A": "A guided tour by the curator.",
                    "B": "An audio guide for the exhibition.",
                    "C": "A free drawing workshop.",
                    "D": "A new museum café."
                },
                "answer": "B",
                "rationale": "The message explains how to use the audio guide."
            },
            {
                "stem": "(audio) How can visitors use the audio guide?",
                "choices": {
                    "A": "Only by buying CDs at the shop.",
                    "B": "Only by borrowing a printed book.",
                    "C": "By renting a device or downloading it to their phone.",
                    "D": "By listening to a radio station at home."
                },
                "answer": "C",
                "rationale": "They can rent a device or use a QR code for their phone."
            },
            {
                "stem": "(audio) What are visitors asked to do before leaving?",
                "choices": {
                    "A": "Return the rental device to the counter.",
                    "B": "Pay for parking at the machine.",
                    "C": "Fill out a satisfaction survey.",
                    "D": "Visit the museum shop."
                },
                "answer": "A",
                "rationale": "They must return any rental audio devices."
            },
        ],
    },

    # 6. 大学図書館の試験期間中の利用案内
    {
        "level": "B2",
        "topic": ["university library", "exam period"],
        "script": (
            "Attention, students. "
            "During the exam period, the university library will open one hour earlier on weekdays. "
            "From next Monday, the doors will open at eight a.m. instead of nine a.m. "
            "Group study rooms must be booked in advance through the library website. "
            "Please keep your voice low in all open areas so that everyone can concentrate."
        ),
        "questions": [
            {
                "stem": "(audio) What change will happen to the library’s opening time?",
                "choices": {
                    "A": "It will open one hour earlier on weekdays.",
                    "B": "It will close earlier on weekends.",
                    "C": "It will be open twenty-four hours.",
                    "D": "It will be closed for two weeks."
                },
                "answer": "A",
                "rationale": "The library will open at eight instead of nine."
            },
            {
                "stem": "(audio) How can students reserve group study rooms?",
                "choices": {
                    "A": "By calling the city office.",
                    "B": "By visiting the cafeteria.",
                    "C": "By booking through the library website.",
                    "D": "By writing their names on the door."
                },
                "answer": "C",
                "rationale": "Reservations must be made via the website."
            },
            {
                "stem": "(audio) Why are students asked to keep their voices low?",
                "choices": {
                    "A": "Because there is a meeting in the lobby.",
                    "B": "Because many people are trying to study.",
                    "C": "Because the building is under repair.",
                    "D": "Because the heating system is loud."
                },
                "answer": "B",
                "rationale": "A quiet environment helps everyone focus during exams."
            },
        ],
    },

    # 7. 人事部による福利厚生説明セッション
    {
        "level": "B2",
        "topic": ["HR", "benefits session"],
        "script": (
            "Hello, this is a message from the human resources department. "
            "Next Wednesday at four p.m., we will hold an information session about the company’s health insurance and other benefits. "
            "The session will take place in Meeting Room 4B and is open to all full-time employees. "
            "If you plan to attend, please sign up on the HR portal so we can prepare enough materials."
        ),
        "questions": [
            {
                "stem": "(audio) What will be explained at the session?",
                "choices": {
                    "A": "New vacation destinations.",
                    "B": "Health insurance and other benefits.",
                    "C": "The history of the company.",
                    "D": "Basic computer skills."
                },
                "answer": "B",
                "rationale": "The session focuses on insurance and benefits."
            },
            {
                "stem": "(audio) Who can attend the session?",
                "choices": {
                    "A": "Only part-time workers.",
                    "B": "Only people from the sales team.",
                    "C": "All full-time employees.",
                    "D": "Only new interns."
                },
                "answer": "C",
                "rationale": "It is open to all full-time staff."
            },
            {
                "stem": "(audio) What are employees asked to do before attending?",
                "choices": {
                    "A": "Bring their lunch to the room.",
                    "B": "Sign up on the HR portal.",
                    "C": "Call their managers about it.",
                    "D": "Prepare a presentation."
                },
                "answer": "B",
                "rationale": "They should register so materials can be prepared."
            },
        ],
    },

    # 8. 会社カフェテリアのメニュー変更
    {
        "level": "B2",
        "topic": ["cafeteria", "menu change"],
        "script": (
            "Good afternoon. "
            "We would like to let you know about some changes in the company cafeteria. "
            "From next month, the daily lunch menu will always include one vegetarian option and one low-salt option. "
            "Nutritional information will be shown on the menu board, so you can choose a meal that fits your needs. "
            "We hope these changes make it easier for you to enjoy a healthy lunch."
        ),
        "questions": [
            {
                "stem": "(audio) What new options will be added to the lunch menu?",
                "choices": {
                    "A": "Only spicy dishes.",
                    "B": "Vegetarian and low-salt choices.",
                    "C": "Desserts with ice cream.",
                    "D": "Free drinks for all staff."
                },
                "answer": "B",
                "rationale": "One vegetarian and one low-salt dish will always be available."
            },
            {
                "stem": "(audio) Where will nutritional information be displayed?",
                "choices": {
                    "A": "On the company website only.",
                    "B": "On signs near the elevators.",
                    "C": "On the menu board in the cafeteria.",
                    "D": "In the monthly newsletter."
                },
                "answer": "C",
                "rationale": "The information will appear on the cafeteria menu board."
            },
            {
                "stem": "(audio) What is the goal of these changes?",
                "choices": {
                    "A": "To make lunch faster to prepare.",
                    "B": "To reduce the number of customers.",
                    "C": "To make it easier to choose healthy food.",
                    "D": "To replace the cafeteria with vending machines."
                },
                "answer": "C",
                "rationale": "The changes are meant to support healthy eating."
            },
        ],
    },

    # 9. コールセンターの営業時間変更
    {
        "level": "B2",
        "topic": ["call center", "business hours"],
        "script": (
            "Thank you for calling Starline Customer Service. "
            "Our business hours have changed. "
            "From April first, our phone lines will be open on weekdays from eight a.m. to seven p.m., and on Saturdays from nine a.m. to one p.m. "
            "We will be closed on Sundays and national holidays. "
            "You can also contact us anytime through the help page on our website."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main topic of the announcement?",
                "choices": {
                    "A": "New product prices.",
                    "B": "Changes to customer service hours.",
                    "C": "A new office address.",
                    "D": "A system error report."
                },
                "answer": "B",
                "rationale": "The message explains new phone hours."
            },
            {
                "stem": "(audio) When will the call center be closed?",
                "choices": {
                    "A": "On Saturdays only.",
                    "B": "On Sundays and holidays.",
                    "C": "Every weekday evening.",
                    "D": "During the lunch hour."
                },
                "answer": "B",
                "rationale": "It is closed on Sundays and national holidays."
            },
            {
                "stem": "(audio) How can customers contact the company outside business hours?",
                "choices": {
                    "A": "By using the help page on the website.",
                    "B": "By visiting the office in person.",
                    "C": "By sending a fax to the manager.",
                    "D": "By calling a private number at night."
                },
                "answer": "A",
                "rationale": "They can use the online help page at any time."
            },
        ],
    },

    # 10. 地域の健康講座のお知らせ
    {
        "level": "B2",
        "topic": ["community", "health seminar"],
        "script": (
            "Residents, this is an announcement from the city health center. "
            "Next month, we will hold a free seminar about healthy eating and simple exercises. "
            "A nutritionist will give a short talk, and then participants can join a light stretching session. "
            "The event will take place in the community hall on the third floor. "
            "If you would like to join, please register by phone or on our website."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main theme of the seminar?",
                "choices": {
                    "A": "Advanced medical research.",
                    "B": "Healthy eating and simple exercises.",
                    "C": "Local history and culture.",
                    "D": "Computer programming."
                },
                "answer": "B",
                "rationale": "It focuses on diet and light exercise."
            },
            {
                "stem": "(audio) What will happen after the nutritionist’s talk?",
                "choices": {
                    "A": "A cooking competition.",
                    "B": "A stretching session for participants.",
                    "C": "A long written test.",
                    "D": "A guided tour of the building."
                },
                "answer": "B",
                "rationale": "Participants can join a light stretching session."
            },
            {
                "stem": "(audio) How can residents sign up for the event?",
                "choices": {
                    "A": "By sending a letter to the hospital.",
                    "B": "By visiting the library in person.",
                    "C": "By registering by phone or online.",
                    "D": "By paying at the supermarket."
                },
                "answer": "C",
                "rationale": "They may register by phone or through the website."
            },
        ],
    },

    # 11. マンションの断水予定
    {
        "level": "B2",
        "topic": ["apartment", "water outage"],
        "script": (
            "Dear residents, this is a notice from the building management office. "
            "Due to maintenance work, the water supply will be stopped on Wednesday from ten a.m. to two p.m. "
            "During this time, you will not be able to use taps, toilets, or showers. "
            "Please store enough water in advance for drinking and basic needs. "
            "We apologize for the inconvenience and thank you for your cooperation."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen on Wednesday?",
                "choices": {
                    "A": "Elevators will stop.",
                    "B": "The water supply will be cut off for several hours.",
                    "C": "The parking lot will be closed.",
                    "D": "The building will have a fire drill."
                },
                "answer": "B",
                "rationale": "Water will not be available from ten to two."
            },
            {
                "stem": "(audio) Which facilities will residents NOT be able to use?",
                "choices": {
                    "A": "Taps, toilets, and showers.",
                    "B": "Internet and TV.",
                    "C": "Elevators and stairs.",
                    "D": "Trash rooms and mailboxes."
                },
                "answer": "A",
                "rationale": "Anything depending on water cannot be used."
            },
            {
                "stem": "(audio) What are residents asked to do before the outage?",
                "choices": {
                    "A": "Leave their keys at the office.",
                    "B": "Move to another building.",
                    "C": "Store enough water in advance.",
                    "D": "Call the police about the work."
                },
                "answer": "C",
                "rationale": "They are told to prepare water for basic needs."
            },
        ],
    },

    # 12. ジムのレッスン予約ポリシー
    {
        "level": "B2",
        "topic": ["gym", "reservation policy"],
        "script": (
            "Thank you for using River Fit Gym. "
            "From next week, all group lessons will require a reservation. "
            "You can book a spot through our mobile app or at the front desk up to three days in advance. "
            "If you cannot attend, please cancel your reservation at least two hours before the class, so someone else can join."
        ),
        "questions": [
            {
                "stem": "(audio) What change is being introduced for group lessons?",
                "choices": {
                    "A": "They will be free for everyone.",
                    "B": "They will be recorded for online viewing.",
                    "C": "They will require a reservation.",
                    "D": "They will be shorter than before."
                },
                "answer": "C",
                "rationale": "All group lessons now need to be booked."
            },
            {
                "stem": "(audio) How long in advance can members reserve a spot?",
                "choices": {
                    "A": "Up to one day in advance.",
                    "B": "Up to three days in advance.",
                    "C": "Up to one month in advance.",
                    "D": "Only on the same day."
                },
                "answer": "B",
                "rationale": "Reservations are possible up to three days before the class."
            },
            {
                "stem": "(audio) Why should people cancel at least two hours before the lesson?",
                "choices": {
                    "A": "So the instructor can change the music.",
                    "B": "So the gym can clean the room.",
                    "C": "So another member can use the spot.",
                    "D": "So the lesson can be moved online."
                },
                "answer": "C",
                "rationale": "Canceling early allows other members to join."
            },
        ],
    },

    # 13. マラソン大会による道路封鎖
    {
        "level": "B2",
        "topic": ["city", "marathon", "road closure"],
        "script": (
            "Residents and drivers, this is an announcement about Sunday’s city marathon. "
            "Several main streets in the downtown area will be closed to cars from eight a.m. to one p.m. "
            "If you need to drive through the center of town, please use the ring road instead. "
            "Buses will follow special routes during this time, so travel may take longer than usual."
        ),
        "questions": [
            {
                "stem": "(audio) Why will some streets be closed on Sunday?",
                "choices": {
                    "A": "Because of road construction.",
                    "B": "Because of a city marathon.",
                    "C": "Because of a film shoot.",
                    "D": "Because of heavy snow."
                },
                "answer": "B",
                "rationale": "The road closure is due to the marathon."
            },
            {
                "stem": "(audio) What are drivers asked to do if they must go through town?",
                "choices": {
                    "A": "Use the ring road instead of downtown streets.",
                    "B": "Park in front of the city hall.",
                    "C": "Drive very slowly in the closed area.",
                    "D": "Call the bus company for directions."
                },
                "answer": "A",
                "rationale": "They should use the ring road as an alternative route."
            },
            {
                "stem": "(audio) What is said about bus services during the event?",
                "choices": {
                    "A": "They will stop completely.",
                    "B": "They will be free of charge.",
                    "C": "They will follow special routes and may be slower.",
                    "D": "They will run only at night."
                },
                "answer": "C",
                "rationale": "Buses will use special routes, so trips may take longer."
            },
        ],
    },

    # 14. 国際会議での同時通訳案内
    {
        "level": "B2",
        "topic": ["conference", "interpretation"],
        "script": (
            "Ladies and gentlemen, welcome to the International Business Forum. "
            "Simultaneous interpretation is available in English, Japanese, and Spanish during today’s sessions. "
            "If you need a headset, please pick one up at the table near the entrance and choose the channel for your language. "
            "After the final session, return your headset to the same table."
        ),
        "questions": [
            {
                "stem": "(audio) What service is offered to participants?",
                "choices": {
                    "A": "Free city tours.",
                    "B": "Simultaneous interpretation in several languages.",
                    "C": "Personal coaching sessions.",
                    "D": "Airport pick-up and drop-off."
                },
                "answer": "B",
                "rationale": "Headsets provide interpretation for the forum sessions."
            },
            {
                "stem": "(audio) Where can attendees get a headset?",
                "choices": {
                    "A": "At the hotel front desk.",
                    "B": "At the table near the entrance.",
                    "C": "From the speakers on stage.",
                    "D": "Inside the cafeteria."
                },
                "answer": "B",
                "rationale": "They must pick it up at the entrance table."
            },
            {
                "stem": "(audio) What should participants do after the final session?",
                "choices": {
                    "A": "Keep the headset as a gift.",
                    "B": "Return the headset to the same table.",
                    "C": "Mail the headset back later.",
                    "D": "Exchange the headset for a book."
                },
                "answer": "B",
                "rationale": "They have to return the headset at the end."
            },
        ],
    },

    # 15. 見本市の開場時間と入場手続き
    {
        "level": "B2",
        "topic": ["trade fair", "opening hours"],
        "script": (
            "Welcome to the City Technology Fair. "
            "The exhibition hall opens to visitors at nine thirty each morning and closes at six p.m. "
            "Please show your registration badge to staff at the entrance every time you enter the hall. "
            "If you have not registered yet, you can do so at the desk on the left side of the lobby."
        ),
        "questions": [
            {
                "stem": "(audio) When does the exhibition hall open?",
                "choices": {
                    "A": "At eight a.m.",
                    "B": "At nine thirty a.m.",
                    "C": "At noon.",
                    "D": "At six p.m."
                },
                "answer": "B",
                "rationale": "The hall opens at nine thirty in the morning."
            },
            {
                "stem": "(audio) What must visitors show at the entrance?",
                "choices": {
                    "A": "Their hotel key.",
                    "B": "Their registration badge.",
                    "C": "A printed ticket from a store.",
                    "D": "Their passport."
                },
                "answer": "B",
                "rationale": "They need to show a badge each time they enter."
            },
            {
                "stem": "(audio) Where can unregistered visitors sign up?",
                "choices": {
                    "A": "At the desk on the left side of the lobby.",
                    "B": "Inside the main exhibition hall.",
                    "C": "At the nearby train station.",
                    "D": "On the fourth floor rooftop."
                },
                "answer": "A",
                "rationale": "Registration takes place at the desk to the left in the lobby."
            },
        ],
    },

    # 16. 語学学校のレベル分けテスト案内
    {
        "level": "B2",
        "topic": ["language school", "placement test"],
        "script": (
            "Thank you for choosing Bright Steps Language School. "
            "Before you join a regular class, you will take a placement test so that we can find the right level for you. "
            "The test includes a short listening section and a writing task that takes about thirty minutes. "
            "Please arrive ten minutes early and bring a pen and your ID card."
        ),
        "questions": [
            {
                "stem": "(audio) Why do students take a placement test?",
                "choices": {
                    "A": "To decide which teacher will visit them.",
                    "B": "To choose the color of their textbook.",
                    "C": "To find a suitable class level.",
                    "D": "To check the school’s internet speed."
                },
                "answer": "C",
                "rationale": "The test helps place students in the right level."
            },
            {
                "stem": "(audio) What parts are included in the test?",
                "choices": {
                    "A": "Only reading aloud.",
                    "B": "A listening section and a writing task.",
                    "C": "A long speaking interview only.",
                    "D": "A physical fitness section."
                },
                "answer": "B",
                "rationale": "The announcement mentions listening and writing."
            },
            {
                "stem": "(audio) What are students asked to bring?",
                "choices": {
                    "A": "A laptop and headphones.",
                    "B": "A pen and an ID card.",
                    "C": "Snacks and drinks.",
                    "D": "Their passport and camera."
                },
                "answer": "B",
                "rationale": "They should come early with a pen and ID."
            },
        ],
    },

    # 17. 銀行のキャッシュカード安全利用案内
    {
        "level": "B2",
        "topic": ["bank", "ATM security"],
        "script": (
            "This is a message from Riverbank. "
            "To keep your cash card safe, never tell anyone your PIN number, even if they say they are from the bank. "
            "When you use an ATM, make sure nobody can see the keypad while you enter your number. "
            "If your card is lost or stolen, call our emergency number immediately."
        ),
        "questions": [
            {
                "stem": "(audio) What is the main purpose of the announcement?",
                "choices": {
                    "A": "To invite customers to a party.",
                    "B": "To explain how to get a new card.",
                    "C": "To give safety advice about cash cards.",
                    "D": "To advertise a new bank branch."
                },
                "answer": "C",
                "rationale": "The focus is on safe use of bank cards."
            },
            {
                "stem": "(audio) What should customers do with their PIN number?",
                "choices": {
                    "A": "Write it on the card.",
                    "B": "Tell it to family and friends.",
                    "C": "Only tell it to bank staff.",
                    "D": "Keep it secret and tell no one."
                },
                "answer": "D",
                "rationale": "They must never share their PIN."
            },
            {
                "stem": "(audio) What should customers do if their card is stolen?",
                "choices": {
                    "A": "Wait a few days and see what happens.",
                    "B": "Call the bank’s emergency number at once.",
                    "C": "Post a message on social media.",
                    "D": "Ask a neighbor to look for it."
                },
                "answer": "B",
                "rationale": "They are told to contact the emergency line immediately."
            },
        ],
    },

    # 18. バス会社のダイヤ改正
    {
        "level": "B2",
        "topic": ["bus company", "timetable change"],
        "script": (
            "Thank you for using Hillside Bus Company. "
            "Starting next Monday, the timetable for Route 5 will change. "
            "Buses will run more frequently during the morning rush hour, but fewer buses will run late at night. "
            "For details, please check the new schedule posted at the bus stop or on our website."
        ),
        "questions": [
            {
                "stem": "(audio) What will change about Route 5?",
                "choices": {
                    "A": "Its ticket prices.",
                    "B": "Its timetable.",
                    "C": "Its destination.",
                    "D": "Its bus drivers."
                },
                "answer": "B",
                "rationale": "The announcement is about a timetable change."
            },
            {
                "stem": "(audio) How will the morning service change?",
                "choices": {
                    "A": "Buses will be less frequent.",
                    "B": "There will be no buses.",
                    "C": "Buses will run more often.",
                    "D": "Buses will start later."
                },
                "answer": "C",
                "rationale": "There will be more buses during rush hour."
            },
            {
                "stem": "(audio) Where can passengers find the new schedule?",
                "choices": {
                    "A": "Only at the city hall.",
                    "B": "On the bus driver’s seat.",
                    "C": "At the stop or on the website.",
                    "D": "In a local newspaper only."
                },
                "answer": "C",
                "rationale": "The new timetable is posted at stops and online."
            },
        ],
    },

    # 19. コワーキングスペースの月例交流会
    {
        "level": "B2",
        "topic": ["coworking", "networking event"],
        "script": (
            "Hello, members of Bridge Hub. "
            "Next Thursday evening, we will hold our monthly networking event in the main lounge. "
            "You can meet freelancers and small business owners from different fields and share ideas. "
            "Light snacks and soft drinks will be provided, but please register in advance so we know how many people will come."
        ),
        "questions": [
            {
                "stem": "(audio) What kind of event is being announced?",
                "choices": {
                    "A": "A job interview session.",
                    "B": "A monthly networking event.",
                    "C": "A language exam.",
                    "D": "A sports competition."
                },
                "answer": "B",
                "rationale": "The announcement is about a networking event."
            },
            {
                "stem": "(audio) What can participants do at the event?",
                "choices": {
                    "A": "Cook meals together in the kitchen.",
                    "B": "Practice musical instruments.",
                    "C": "Meet people from different fields and share ideas.",
                    "D": "Watch a movie in silence."
                },
                "answer": "C",
                "rationale": "It’s a chance to meet various professionals and talk."
            },
            {
                "stem": "(audio) Why are members asked to register beforehand?",
                "choices": {
                    "A": "So the staff can prepare enough snacks and drinks.",
                    "B": "So they can receive homework by e-mail.",
                    "C": "So they can get free office furniture.",
                    "D": "So the event can be moved outdoors."
                },
                "answer": "A",
                "rationale": "Registration helps the staff estimate how much to prepare."
            },
        ],
    },

    # 20. チャリティーランの参加受付
    {
        "level": "B2",
        "topic": ["charity run", "registration"],
        "script": (
            "Good afternoon, everyone. "
            "The annual charity run will take place in the riverside park on May twelfth. "
            "Participants can choose between a five-kilometer and a ten-kilometer course. "
            "All entry fees will be donated to a local children’s hospital. "
            "If you would like to join, please sign up online by the end of this month."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about the event being announced?",
                "choices": {
                    "A": "It is a race for professional athletes only.",
                    "B": "It is a charity run to support a hospital.",
                    "C": "It is a music festival in the evening.",
                    "D": "It is a free concert in the park."
                },
                "answer": "B",
                "rationale": "Entry fees go to a children’s hospital."
            },
            {
                "stem": "(audio) What choices do participants have?",
                "choices": {
                    "A": "A five-kilometer or a ten-kilometer course.",
                    "B": "Running or cycling only.",
                    "C": "Morning or late-night start times.",
                    "D": "Individual or team swimming events."
                },
                "answer": "A",
                "rationale": "They can choose between two distances."
            },
            {
                "stem": "(audio) How should people register for the event?",
                "choices": {
                    "A": "By sending cash by mail.",
                    "B": "By signing up online.",
                    "C": "By calling the hospital.",
                    "D": "By visiting the city hall in person."
                },
                "answer": "B",
                "rationale": "Registration is done through an online form."
            },
        ],
    },

    # 21. 美術館の展示室一時閉鎖
    {
        "level": "B2",
        "topic": ["art museum", "temporary closure"],
        "script": (
            "Ladies and gentlemen, we would like to inform you that Gallery 3 on the second floor "
            "will be closed this afternoon from two to four p.m. for maintenance work. "
            "Other galleries remain open as usual. "
            "If you planned to see the modern art exhibition in Gallery 3, please visit it before two p.m. or after four p.m."
        ),
        "questions": [
            {
                "stem": "(audio) Why will Gallery 3 be closed this afternoon?",
                "choices": {
                    "A": "Because of a private party.",
                    "B": "Because of maintenance work.",
                    "C": "Because of a staff meeting.",
                    "D": "Because of a holiday."
                },
                "answer": "B",
                "rationale": "It will be closed for maintenance."
            },
            {
                "stem": "(audio) What is said about other galleries?",
                "choices": {
                    "A": "They will also be closed.",
                    "B": "They will be moved to another building.",
                    "C": "They will remain open as usual.",
                    "D": "They will open only in the morning."
                },
                "answer": "C",
                "rationale": "Other galleries are not affected."
            },
            {
                "stem": "(audio) When can visitors see the modern art exhibition?",
                "choices": {
                    "A": "Only between two and four p.m.",
                    "B": "Only early in the morning.",
                    "C": "Before two p.m. or after four p.m.",
                    "D": "Only on the weekend."
                },
                "answer": "C",
                "rationale": "They must visit before the closure or after it ends."
            },
        ],
    },

    # 22. 病院の面会時間変更
    {
        "level": "B2",
        "topic": ["hospital", "visiting hours"],
        "script": (
            "This is an announcement from Sunrise Hospital. "
            "For patient safety, visiting hours will change beginning next Monday. "
            "Family members may visit from one p.m. to seven p.m. on weekdays and from ten a.m. to six p.m. on weekends. "
            "Children under twelve must stay in the waiting area unless a nurse gives permission to enter a room."
        ),
        "questions": [
            {
                "stem": "(audio) What is changing at Sunrise Hospital?",
                "choices": {
                    "A": "The number of doctors on duty.",
                    "B": "The price of treatments.",
                    "C": "The visiting hours for family members.",
                    "D": "The location of the emergency room."
                },
                "answer": "C",
                "rationale": "The announcement explains new visiting times."
            },
            {
                "stem": "(audio) When may family members visit on weekdays?",
                "choices": {
                    "A": "From nine a.m. to noon.",
                    "B": "From one p.m. to seven p.m.",
                    "C": "From seven p.m. to midnight.",
                    "D": "All day and all night."
                },
                "answer": "B",
                "rationale": "Weekday visiting hours are one to seven p.m."
            },
            {
                "stem": "(audio) What rule applies to children under twelve?",
                "choices": {
                    "A": "They may not enter the hospital at all.",
                    "B": "They may only stay in the waiting area without permission.",
                    "C": "They must always wear a uniform.",
                    "D": "They must come alone without adults."
                },
                "answer": "B",
                "rationale": "They must remain in the waiting area unless a nurse allows entry."
            },
        ],
    },

    # 23. 映画館の上映時間変更
    {
        "level": "B2",
        "topic": ["cinema", "schedule change"],
        "script": (
            "Thank you for calling City Lights Cinema. "
            "From this weekend, the evening showing of our most popular film will start thirty minutes later, at seven thirty p.m. instead of seven. "
            "The afternoon showing will remain at two p.m. as usual. "
            "If you have already bought a ticket for the evening show, it will still be valid for the new time."
        ),
        "questions": [
            {
                "stem": "(audio) What change is announced about the film?",
                "choices": {
                    "A": "The evening showing will start later.",
                    "B": "The afternoon showing will be canceled.",
                    "C": "The film will be shown in another cinema.",
                    "D": "The language of the film will change."
                },
                "answer": "A",
                "rationale": "The evening show now starts at seven thirty p.m."
            },
            {
                "stem": "(audio) What remains the same about the schedule?",
                "choices": {
                    "A": "The number of daily showings.",
                    "B": "The afternoon showing at two p.m.",
                    "C": "The ticket price on weekends.",
                    "D": "The length of the movie."
                },
                "answer": "B",
                "rationale": "The afternoon showing stays at two p.m."
            },
            {
                "stem": "(audio) What is said about tickets already bought?",
                "choices": {
                    "A": "They must be exchanged at the counter.",
                    "B": "They are not valid on the weekend.",
                    "C": "They are still valid for the new time.",
                    "D": "They can only be used for another film."
                },
                "answer": "C",
                "rationale": "Existing tickets remain valid for the later start time."
            },
        ],
    },

    # 24. スーパーのポイントカード説明
    {
        "level": "B2",
        "topic": ["supermarket", "loyalty program"],
        "script": (
            "Welcome to Green Market. "
            "With our store point card, you can earn one point for every hundred yen you spend. "
            "When you collect five hundred points, you can exchange them for a five-hundred-yen coupon at the service counter. "
            "If you would like to join the program, please fill out the simple form near the entrance."
        ),
        "questions": [
            {
                "stem": "(audio) How can customers earn points with the card?",
                "choices": {
                    "A": "By visiting the store once a week.",
                    "B": "By paying the annual membership fee.",
                    "C": "By spending money on their purchases.",
                    "D": "By bringing their own shopping bags."
                },
                "answer": "C",
                "rationale": "They earn points based on how much they spend."
            },
            {
                "stem": "(audio) What can five hundred points be exchanged for?",
                "choices": {
                    "A": "A free delivery service.",
                    "B": "A five-hundred-yen coupon.",
                    "C": "A free point card for a friend.",
                    "D": "A ticket to a movie."
                },
                "answer": "B",
                "rationale": "Five hundred points become a coupon of the same value."
            },
            {
                "stem": "(audio) What must customers do if they want to join the program?",
                "choices": {
                    "A": "Sign up only on the website.",
                    "B": "Call the supermarket manager directly.",
                    "C": "Fill out a form near the entrance.",
                    "D": "Send a letter by mail."
                },
                "answer": "C",
                "rationale": "They should complete a simple paper form at the entrance."
            },
        ],
    },

    # 25. 電車の臨時列車運行案内
    {
        "level": "B2",
        "topic": ["train", "extra service"],
        "script": (
            "Attention, passengers. "
            "Because of the fireworks festival tonight, an extra train will run on the Riverside Line. "
            "The special train will leave Central Station at eleven ten p.m., after the regular last train. "
            "All stations on the line will be served, but reserved seats are not available. "
            "Please check the information board for details."
        ),
        "questions": [
            {
                "stem": "(audio) Why is an extra train being added?",
                "choices": {
                    "A": "Because of a sports game.",
                    "B": "Because of road construction.",
                    "C": "Because of a fireworks festival.",
                    "D": "Because of a train accident."
                },
                "answer": "C",
                "rationale": "An extra train runs due to the festival."
            },
            {
                "stem": "(audio) When will the special train leave Central Station?",
                "choices": {
                    "A": "At ten p.m.",
                    "B": "At eleven ten p.m.",
                    "C": "At midnight.",
                    "D": "At six a.m."
                },
                "answer": "B",
                "rationale": "It departs at eleven ten p.m."
            },
            {
                "stem": "(audio) What is said about seats on the extra train?",
                "choices": {
                    "A": "Reserved seats are not available.",
                    "B": "Only first-class seats are sold.",
                    "C": "All seats are free of charge.",
                    "D": "Seats must be booked online."
                },
                "answer": "A",
                "rationale": "The announcement mentions that reserved seats are not offered."
            },
        ],
    },

    # 26. 空港の保安検査の注意
    {
        "level": "B2",
        "topic": ["airport", "security check"],
        "script": (
            "Passengers, before you go through the security check, please take laptops and tablets out of your bags "
            "and place them in a separate tray. "
            "Liquids must be in small containers and put inside a clear plastic bag. "
            "To make the line move smoothly, be ready to remove belts and metal items from your pockets."
        ),
        "questions": [
            {
                "stem": "(audio) What must passengers do with laptops and tablets?",
                "choices": {
                    "A": "Keep them inside their bags.",
                    "B": "Give them to the airline staff.",
                    "C": "Place them in a separate tray.",
                    "D": "Turn them on during the scan."
                },
                "answer": "C",
                "rationale": "Devices must be removed and placed separately."
            },
            {
                "stem": "(audio) How should passengers pack liquids?",
                "choices": {
                    "A": "In large bottles in checked luggage.",
                    "B": "In small containers inside a clear plastic bag.",
                    "C": "In paper bags in their pockets.",
                    "D": "In open cups for inspection."
                },
                "answer": "B",
                "rationale": "Liquids have to be in small containers in a clear bag."
            },
            {
                "stem": "(audio) Why are passengers asked to be ready to remove belts and metal items?",
                "choices": {
                    "A": "To move through security more quickly.",
                    "B": "To prepare for a long interview.",
                    "C": "To sit comfortably while waiting.",
                    "D": "To show the items to the ticket counter."
                },
                "answer": "A",
                "rationale": "Being prepared helps the line move smoothly."
            },
        ],
    },

    # 27. 美術館の夜間開館日のお知らせ
    {
        "level": "B2",
        "topic": ["museum", "late opening"],
        "script": (
            "Good evening. "
            "On the first Friday of each month, our museum stays open until nine p.m. "
            "On those nights, visitors can enjoy the exhibitions in a quieter atmosphere and listen to short talks by curators. "
            "The museum café will also be open until closing time."
        ),
        "questions": [
            {
                "stem": "(audio) What is special about the first Friday of each month at the museum?",
                "choices": {
                    "A": "Entrance is free all day.",
                    "B": "The museum stays open later than usual.",
                    "C": "Only the gift shop is open.",
                    "D": "All exhibitions are closed."
                },
                "answer": "B",
                "rationale": "The museum remains open until nine p.m."
            },
            {
                "stem": "(audio) What extra activities are mentioned for those evenings?",
                "choices": {
                    "A": "Cooking classes in the lobby.",
                    "B": "Long movies in the theater.",
                    "C": "Short talks by curators.",
                    "D": "Sports games in the courtyard."
                },
                "answer": "C",
                "rationale": "Curators give short talks on those nights."
            },
            {
                "stem": "(audio) What is said about the museum café?",
                "choices": {
                    "A": "It closes earlier than the museum.",
                    "B": "It is closed on Fridays.",
                    "C": "It stays open until the museum closes.",
                    "D": "It serves only breakfast."
                },
                "answer": "C",
                "rationale": "The café remains open until closing time."
            },
        ],
    },

    # 28. オンラインショップの返品ポリシー
    {
        "level": "B2",
        "topic": ["online shop", "return policy"],
        "script": (
            "Thank you for shopping at BrightHome Online Store. "
            "If you are not satisfied with a product, you may return it within thirty days of delivery. "
            "Items must be unused and in their original packaging. "
            "To start a return, log in to your account and follow the steps on the orders page."
        ),
        "questions": [
            {
                "stem": "(audio) How long do customers have to return a product?",
                "choices": {
                    "A": "Seven days after ordering.",
                    "B": "Thirty days after delivery.",
                    "C": "Three months after payment.",
                    "D": "One year after purchase."
                },
                "answer": "B",
                "rationale": "Returns are accepted within thirty days of delivery."
            },
            {
                "stem": "(audio) In what condition must the items be?",
                "choices": {
                    "A": "Used but clean.",
                    "B": "Repaired at a local shop.",
                    "C": "Unused and in original packaging.",
                    "D": "Without any labels."
                },
                "answer": "C",
                "rationale": "Items must be unused and in original packaging."
            },
            {
                "stem": "(audio) How can customers begin the return process?",
                "choices": {
                    "A": "By calling the local post office.",
                    "B": "By visiting a physical store.",
                    "C": "By logging in and using the orders page.",
                    "D": "By sending a fax to customer support."
                },
                "answer": "C",
                "rationale": "They start the process online from their account."
            },
        ],
    },

    # 29. スポーツクラブの会員更新案内
    {
        "level": "B2",
        "topic": ["sports club", "membership renewal"],
        "script": (
            "Members of CityFit Club, this is a reminder about your annual membership renewal. "
            "If your card expires this month, please visit the front desk to renew it. "
            "Members who renew before the end of the month will receive a small discount on the next year’s fee. "
            "If you have any questions about your membership, our staff will be happy to help."
        ),
        "questions": [
            {
                "stem": "(audio) What is the announcement mainly about?",
                "choices": {
                    "A": "New exercise classes.",
                    "B": "Annual membership renewal.",
                    "C": "Changes to parking rules.",
                    "D": "An upcoming competition."
                },
                "answer": "B",
                "rationale": "It reminds members to renew their membership."
            },
            {
                "stem": "(audio) What benefit do early renewals receive?",
                "choices": {
                    "A": "Free training shoes.",
                    "B": "A discount on next year’s fee.",
                    "C": "Free access for friends.",
                    "D": "A free vacation trip."
                },
                "answer": "B",
                "rationale": "Renewing before the month ends gives a discount."
            },
            {
                "stem": "(audio) Where should members go to renew their card?",
                "choices": {
                    "A": "To the front desk.",
                    "B": "To the swimming pool.",
                    "C": "To the city office.",
                    "D": "To a nearby supermarket."
                },
                "answer": "A",
                "rationale": "They must visit the club’s front desk."
            },
        ],
    },

    # 30. 市役所オンラインサービスの一時停止
    {
        "level": "B2",
        "topic": ["city hall", "online service maintenance"],
        "script": (
            "This is an announcement from the city office. "
            "Our online service for address changes and tax documents will be unavailable this weekend due to a system upgrade. "
            "From Friday night at ten p.m. until Monday morning at six a.m., you will not be able to log in to your account. "
            "If you need to submit any forms soon, please do so before the upgrade period or visit the city office in person."
        ),
        "questions": [
            {
                "stem": "(audio) What will happen to the city’s online service this weekend?",
                "choices": {
                    "A": "It will be expanded to more languages.",
                    "B": "It will be unavailable during an upgrade.",
                    "C": "It will be free for non-residents.",
                    "D": "It will move to another website."
                },
                "answer": "B",
                "rationale": "The service will be down for a system upgrade."
            },
            {
                "stem": "(audio) During which period will the service be stopped?",
                "choices": {
                    "A": "From Friday night to Monday morning.",
                    "B": "For one hour every evening.",
                    "C": "Only on Sunday afternoon.",
                    "D": "Only during national holidays."
                },
                "answer": "A",
                "rationale": "The upgrade lasts from Friday night until Monday morning."
            },
            {
                "stem": "(audio) What can residents do if they must submit forms soon?",
                "choices": {
                    "A": "Wait until the next holiday.",
                    "B": "Use a different city’s website.",
                    "C": "Submit them before the upgrade or visit in person.",
                    "D": "Send them by text message."
                },
                "answer": "C",
                "rationale": "They are told to submit forms early or go to the office directly."
            },
        ],
    },
]