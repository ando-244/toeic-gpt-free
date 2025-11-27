# patterns_part3.py
# Part3の問題パターン集だけをまとめたモジュール

# === Part3 用の会話パターン集（会話＋設問3本セット） ===
PART3_PATTERNS = [
    # --- A2 level 30patterns (easy) ---
    # 1. オフィス：会議室の場所
    {
        "level": "A2",
        "topic": ["office", "meeting room"],
        "dialog": [
            ("W", "Do you know where the meeting room is?"),
            ("M", "Yes, it's next to the printer on the second floor."),
            ("W", "Thanks. I always forget where it is.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask about?",
                "choices": {
                    "A": "Where the meeting room is.",
                    "B": "How to use the printer.",
                    "C": "Who will join the meeting.",
                    "D": "When the meeting starts."
                },
                "answer": "A",
                "rationale": "She asks where the meeting room is."
            },
            {
                "stem": "(audio) Where is the meeting room?",
                "choices": {
                    "A": "On the first floor.",
                    "B": "Next to the printer.",
                    "C": "Across from the cafeteria.",
                    "D": "Near the entrance."
                },
                "answer": "B",
                "rationale": "The man says it is next to the printer."
            },
            {
                "stem": "(audio) How does the woman feel?",
                "choices": {
                    "A": "She is confused about the location.",
                    "B": "She is angry at her coworker.",
                    "C": "She is worried about the meeting.",
                    "D": "She is tired after work."
                },
                "answer": "A",
                "rationale": "She says she always forgets the location."
            },
        ],
    },

    # 2. オフィス：プリンター用紙
    {
        "level": "A2",
        "topic": ["office", "printer"],
        "dialog": [
            ("M", "The printer ran out of paper again."),
            ("W", "I'll bring some from the storage room."),
            ("M", "Thanks. I need to print these files soon.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the problem?",
                "choices": {
                    "A": "The printer has no paper.",
                    "B": "The printer is broken.",
                    "C": "The man lost his files.",
                    "D": "The storage room is locked."
                },
                "answer": "A",
                "rationale": "The man says the printer ran out of paper."
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Fix the printer.",
                    "B": "Bring more paper.",
                    "C": "Call maintenance.",
                    "D": "Move the printer."
                },
                "answer": "B",
                "rationale": "She says she will bring paper."
            },
            {
                "stem": "(audio) Why is the man in a hurry?",
                "choices": {
                    "A": "He needs to print files.",
                    "B": "He is leaving the office.",
                    "C": "He has a phone call.",
                    "D": "He must meet a client."
                },
                "answer": "A",
                "rationale": "He says he needs to print files soon."
            },
        ],
    },

    # 3. オフィス：上司の探しもの
    {
        "level": "A2",
        "topic": ["office", "manager"],
        "dialog": [
            ("W", "Have you seen the manager today?"),
            ("M", "Yes, he went to the meeting room."),
            ("W", "Okay, I need to give him this form.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman looking for?",
                "choices": {
                    "A": "The manager.",
                    "B": "Her keys.",
                    "C": "A document on her desk.",
                    "D": "A meeting schedule."
                },
                "answer": "A",
                "rationale": "She asks if the man has seen the manager."
            },
            {
                "stem": "(audio) Where is the manager now?",
                "choices": {
                    "A": "In the lobby.",
                    "B": "In the cafeteria.",
                    "C": "In the meeting room.",
                    "D": "At home."
                },
                "answer": "C",
                "rationale": "The man says he went to the meeting room."
            },
            {
                "stem": "(audio) What does the woman need to give him?",
                "choices": {
                    "A": "A phone.",
                    "B": "A form.",
                    "C": "A book.",
                    "D": "A laptop."
                },
                "answer": "B",
                "rationale": "She mentions she needs to give him a form."
            },
        ],
    },

    # 4. オフィス：昼休み
    {
        "level": "A2",
        "topic": ["office", "lunch"],
        "dialog": [
            ("M", "Are you taking your lunch break now?"),
            ("W", "Yes, I'm going to the café downstairs."),
            ("M", "Nice. I'll join you.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman going to do?",
                "choices": {
                    "A": "Buy a new phone.",
                    "B": "Go on a trip.",
                    "C": "Take her lunch break.",
                    "D": "Move to another office."
                },
                "answer": "C",
                "rationale": "She says she is taking her lunch break."
            },
            {
                "stem": "(audio) Where is she going?",
                "choices": {
                    "A": "To the café downstairs.",
                    "B": "To the rooftop.",
                    "C": "To the bank.",
                    "D": "To a bookstore."
                },
                "answer": "A",
                "rationale": "She says she is going to the café."
            },
            {
                "stem": "(audio) What does the man decide?",
                "choices": {
                    "A": "To stay at his desk.",
                    "B": "To join the woman.",
                    "C": "To buy groceries.",
                    "D": "To take a taxi."
                },
                "answer": "B",
                "rationale": "He says he will join her."
            },
        ],
    },

    # 5. オフィス：忘れ物
    {
        "level": "A2",
        "topic": ["office", "forgot"],
        "dialog": [
            ("W", "Did you bring the documents for the meeting?"),
            ("M", "Oh no, I left them on my desk."),
            ("W", "Hurry! The meeting starts in five minutes.")
        ],
        "questions": [
            {
                "stem": "(audio) What did the man forget?",
                "choices": {
                    "A": "The documents.",
                    "B": "His phone.",
                    "C": "His lunch.",
                    "D": "The meeting room key."
                },
                "answer": "A",
                "rationale": "He says he left the documents on his desk."
            },
            {
                "stem": "(audio) When does the meeting start?",
                "choices": {
                    "A": "In five minutes.",
                    "B": "At noon.",
                    "C": "Tomorrow morning.",
                    "D": "In one hour."
                },
                "answer": "A",
                "rationale": "She says it starts in five minutes."
            },
            {
                "stem": "(audio) How does the woman feel?",
                "choices": {
                    "A": "In a hurry.",
                    "B": "Very tired.",
                    "C": "Happy and relaxed.",
                    "D": "Confused about the schedule."
                },
                "answer": "A",
                "rationale": "Her words show urgency."
            },
        ],
    },
    # 6. 買い物：サイズ確認
    {
        "level": "A2",
        "topic": ["shopping", "clothing"],
        "dialog": [
            ("W", "Excuse me, do you have this shirt in a larger size?"),
            ("M", "Yes, we have it in large and extra-large."),
            ("W", "Great, can I try the large one first?")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman looking for?",
                "choices": {
                    "A": "A larger shirt.",
                    "B": "A cheaper jacket.",
                    "C": "A different color.",
                    "D": "A new pair of shoes."
                },
                "answer": "A",
                "rationale": "She asks for a larger size of the same shirt."
            },
            {
                "stem": "(audio) What does the man say they have?",
                "choices": {
                    "A": "Only small sizes.",
                    "B": "Large and extra-large sizes.",
                    "C": "Special discount items.",
                    "D": "New arrivals in the back."
                },
                "answer": "B",
                "rationale": "He says they have large and extra-large."
            },
            {
                "stem": "(audio) What will the woman do next?",
                "choices": {
                    "A": "Try on a large size.",
                    "B": "Buy the shirt online.",
                    "C": "Look for another store.",
                    "D": "Return the item she bought."
                },
                "answer": "A",
                "rationale": "She says she wants to try the large one."
            }
        ]
    },

    # 7. 買い物：レジでの支払い
    {
        "level": "A2",
        "topic": ["shopping", "payment"],
        "dialog": [
            ("M", "Is this the line to pay for items?"),
            ("W", "Yes, please wait behind the sign."),
            ("M", "Thanks. It doesn’t look too long today.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man want to do?",
                "choices": {
                    "A": "Pay for his items.",
                    "B": "Find the restroom.",
                    "C": "Ask about a return.",
                    "D": "Speak to a manager."
                },
                "answer": "A",
                "rationale": "He asks if it's the line to pay."
            },
            {
                "stem": "(audio) What does the woman tell him?",
                "choices": {
                    "A": "To move to a different floor.",
                    "B": "To wait behind the sign.",
                    "C": "To fill out a form.",
                    "D": "To leave his items here."
                },
                "answer": "B",
                "rationale": "She asks him to wait behind the sign."
            },
            {
                "stem": "(audio) How does the man feel?",
                "choices": {
                    "A": "He thinks the line is short.",
                    "B": "He is angry about the wait.",
                    "C": "He wants to go home quickly.",
                    "D": "He is confused about prices."
                },
                "answer": "A",
                "rationale": "He comments that the line doesn't look long."
            }
        ]
    },

    # 8. 郵便局：荷物の発送
    {
        "level": "A2",
        "topic": ["post office", "shipping"],
        "dialog": [
            ("W", "I'd like to send this package to Osaka."),
            ("M", "Sure. Would you like standard or express shipping?"),
            ("W", "Standard is fine. It's not urgent.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to do?",
                "choices": {
                    "A": "Send a package.",
                    "B": "Buy stamps.",
                    "C": "Pick up a letter.",
                    "D": "Change her address."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the man ask?",
                "choices": {
                    "A": "Which shipping type she wants.",
                    "B": "Why the package is heavy.",
                    "C": "Where she bought the box.",
                    "D": "Whether she wants insurance."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the woman choose?",
                "choices": {
                    "A": "Express shipping.",
                    "B": "Standard shipping.",
                    "C": "No shipping service.",
                    "D": "Same-day delivery."
                },
                "answer": "B"
            }
        ]
    },

    # 9. 銀行：口座の質問
    {
        "level": "A2",
        "topic": ["bank", "account"],
        "dialog": [
            ("M", "Excuse me, how can I check my account balance?"),
            ("W", "You can use the ATM near the entrance."),
            ("M", "Thank you. I’ll go there now.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man want to check?",
                "choices": {
                    "A": "His account balance.",
                    "B": "His credit card bill.",
                    "C": "The loan application.",
                    "D": "Foreign currency rates."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the woman recommend?",
                "choices": {
                    "A": "Calling customer service.",
                    "B": "Using the ATM.",
                    "C": "Visiting another branch.",
                    "D": "Filling out a form."
                },
                "answer": "B"
            },
            {
                "stem": "(audio) Where is the ATM?",
                "choices": {
                    "A": "Near the entrance.",
                    "B": "On the second floor.",
                    "C": "Next to the café.",
                    "D": "Across from the post office."
                },
                "answer": "A"
            }
        ]
    },

    # 10. 銀行：待ち時間
    {
        "level": "A2",
        "topic": ["bank", "waiting"],
        "dialog": [
            ("W", "How long is the wait today?"),
            ("M", "About ten minutes."),
            ("W", "That's not too bad. I'll wait here.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask about?",
                "choices": {
                    "A": "The waiting time.",
                    "B": "Loan documents.",
                    "C": "Bank hours.",
                    "D": "A lost card."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How long is the wait?",
                "choices": {
                    "A": "Ten minutes.",
                    "B": "One hour.",
                    "C": "All afternoon.",
                    "D": "Two minutes."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Wait there.",
                    "B": "Go home.",
                    "C": "Speak to a manager.",
                    "D": "Come back tomorrow."
                },
                "answer": "A"
            }
        ]
    },

    # 11. 病院：受付
    {
        "level": "A2",
        "topic": ["hospital", "reception"],
        "dialog": [
            ("M", "Hi, I have an appointment at three."),
            ("W", "Please check in at the front desk."),
            ("M", "Okay, thank you.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man have?",
                "choices": {
                    "A": "An appointment.",
                    "B": "A prescription.",
                    "C": "A bill to pay.",
                    "D": "A broken phone."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) When is the appointment?",
                "choices": {
                    "A": "At three.",
                    "B": "At noon.",
                    "C": "Tomorrow morning.",
                    "D": "Next week."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the woman ask him to do?",
                "choices": {
                    "A": "Check in.",
                    "B": "Take a seat.",
                    "C": "See the doctor.",
                    "D": "Fill out a survey."
                },
                "answer": "A"
            }
        ]
    },

    # 12. 病院：診察の遅れ
    {
        "level": "A2",
        "topic": ["hospital", "delay"],
        "dialog": [
            ("W", "Is the doctor running late today?"),
            ("M", "Yes, about fifteen minutes."),
            ("W", "Okay, I'll wait a little longer.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to know?",
                "choices": {
                    "A": "If the doctor is late.",
                    "B": "If the doctor is new.",
                    "C": "If the office is closed.",
                    "D": "If the bill is ready."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How late is the doctor?",
                "choices": {
                    "A": "Fifteen minutes.",
                    "B": "Five hours.",
                    "C": "All day.",
                    "D": "One minute."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Wait longer.",
                    "B": "Leave the hospital.",
                    "C": "Visit another doctor.",
                    "D": "Ask for a refund."
                },
                "answer": "A"
            }
        ]
    },

    # 13. レストラン：予約確認
    {
        "level": "A2",
        "topic": ["restaurant", "reservation"],
        "dialog": [
            ("M", "Hello, I have a reservation under Tanaka."),
            ("W", "Yes, a table for two at six."),
            ("M", "Great, thank you.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man have?",
                "choices": {
                    "A": "A reservation.",
                    "B": "A delivery.",
                    "C": "A discount coupon.",
                    "D": "A complaint."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How many people are in the reservation?",
                "choices": {
                    "A": "Two.",
                    "B": "Four.",
                    "C": "Six.",
                    "D": "Ten."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) When is the reservation?",
                "choices": {
                    "A": "At six.",
                    "B": "At noon.",
                    "C": "At eight.",
                    "D": "At nine."
                },
                "answer": "A"
            }
        ]
    },

    # 14. レストラン：注文
    {
        "level": "A2",
        "topic": ["restaurant", "order"],
        "dialog": [
            ("W", "Are you ready to order?"),
            ("M", "Yes, I'll have the pasta."),
            ("W", "Sure. Would you like a drink?"),
            ("M", "Just water, please.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man order?",
                "choices": {
                    "A": "Pasta.",
                    "B": "Soup.",
                    "C": "Salad.",
                    "D": "Fish."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What drink does he want?",
                "choices": {
                    "A": "Water.",
                    "B": "Coffee.",
                    "C": "Juice.",
                    "D": "Tea."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) Who is the woman?",
                "choices": {
                    "A": "A server.",
                    "B": "A friend.",
                    "C": "A chef.",
                    "D": "A store owner."
                },
                "answer": "A"
            }
        ]
    },

    # 15. レストラン：支払い
    {
        "level": "A2",
        "topic": ["restaurant", "payment"],
        "dialog": [
            ("W", "Can I get the check, please?"),
            ("M", "Of course, I'll bring it right away."),
            ("W", "Thank you.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask for?",
                "choices": {
                    "A": "The check.",
                    "B": "A menu.",
                    "C": "A fork.",
                    "D": "A napkin."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Bring the check.",
                    "B": "Bring more water.",
                    "C": "Prepare the food.",
                    "D": "Show the dessert list."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the woman respond?",
                "choices": {
                    "A": "She thanks him.",
                    "B": "She complains.",
                    "C": "She refuses the check.",
                    "D": "She orders more food."
                },
                "answer": "A"
            }
        ]
    },

    # 16. ホテル：チェックイン
    {
        "level": "A2",
        "topic": ["hotel", "check-in"],
        "dialog": [
            ("M", "Hi, I'd like to check in."),
            ("W", "Sure, may I have your name?"),
            ("M", "Yes, it's Suzuki."),
            ("W", "Your room is on the third floor.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man want to do?",
                "choices": {
                    "A": "Check in.",
                    "B": "Check out.",
                    "C": "Book a tour.",
                    "D": "Order breakfast."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What is the man's name?",
                "choices": {
                    "A": "Suzuki.",
                    "B": "Tanaka.",
                    "C": "Ito.",
                    "D": "Kato."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) Where is his room?",
                "choices": {
                    "A": "On the third floor.",
                    "B": "On the first floor.",
                    "C": "Next to the lobby.",
                    "D": "In another building."
                },
                "answer": "A"
            }
        ]
    },

    # 17. ホテル：タクシー
    {
        "level": "A2",
        "topic": ["hotel", "taxi"],
        "dialog": [
            ("W", "Do you need a taxi to the airport?"),
            ("M", "Yes, could you call one for me?"),
            ("W", "Sure, it will arrive in ten minutes.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask?",
                "choices": {
                    "A": "If he needs a taxi.",
                    "B": "If he wants a wake-up call.",
                    "C": "If he lost something.",
                    "D": "If he wants breakfast."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Call a taxi.",
                    "B": "Bring breakfast.",
                    "C": "Check his room.",
                    "D": "Print his ticket."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) When will the taxi arrive?",
                "choices": {
                    "A": "In ten minutes.",
                    "B": "In one hour.",
                    "C": "Right now.",
                    "D": "Tomorrow morning."
                },
                "answer": "A"
            }
        ]
    },

    # 18. 旅行：電車の乗り場
    {
        "level": "A2",
        "topic": ["travel", "train"],
        "dialog": [
            ("M", "Is this the platform for the train to Kyoto?"),
            ("W", "Yes, but the train is five minutes late."),
            ("M", "No problem. I'll wait here.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is the man going?",
                "choices": {
                    "A": "Kyoto.",
                    "B": "Tokyo.",
                    "C": "Osaka.",
                    "D": "Nagoya."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the woman say about the train?",
                "choices": {
                    "A": "It is late.",
                    "B": "It is full.",
                    "C": "It is canceled.",
                    "D": "It is leaving now."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Wait on the platform.",
                    "B": "Buy a new ticket.",
                    "C": "Go to another station.",
                    "D": "Change trains."
                },
                "answer": "A"
            }
        ]
    },

    # 19. 旅行：道案内
    {
        "level": "A2",
        "topic": ["travel", "directions"],
        "dialog": [
            ("W", "Excuse me, how do I get to the museum?"),
            ("M", "Go straight and turn left at the second light."),
            ("W", "Thank you so much.")
        ],
        "questions": [
            {
                "stem": "(audio) Where does the woman want to go?",
                "choices": {
                    "A": "The museum.",
                    "B": "The station.",
                    "C": "The hotel.",
                    "D": "The supermarket."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the man tell her to do?",
                "choices": {
                    "A": "Go straight and turn left.",
                    "B": "Take the train.",
                    "C": "Turn right at the corner.",
                    "D": "Go back to the bus stop."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the woman respond?",
                "choices": {
                    "A": "She thanks him.",
                    "B": "She refuses his help.",
                    "C": "She asks for a restaurant.",
                    "D": "She says the museum is closed."
                },
                "answer": "A"
            }
        ]
    },

    # 20. 学校：先生への質問
    {
        "level": "A2",
        "topic": ["school", "teacher"],
        "dialog": [
            ("M", "Excuse me, when is the homework due?"),
            ("W", "It’s due on Friday."),
            ("M", "Okay, I’ll finish it by then.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man ask?",
                "choices": {
                    "A": "When the homework is due.",
                    "B": "Where the class is.",
                    "C": "What the topic is.",
                    "D": "How many pages it is."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) When is the homework due?",
                "choices": {
                    "A": "On Friday.",
                    "B": "Today.",
                    "C": "Next month.",
                    "D": "Tomorrow morning."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Finish the homework by Friday.",
                    "B": "Ask another student for help.",
                    "C": "Skip the assignment.",
                    "D": "Change his class."
                },
                "answer": "A"
            }
        ]
    },

    # 21. 学校：授業の場所
    {
        "level": "A2",
        "topic": ["school", "classroom"],
        "dialog": [
            ("W", "Do you know where the English class is today?"),
            ("M", "Yes, it's in Room 204 upstairs."),
            ("W", "Thanks, I almost went to the wrong room.")
        ],
        "questions": [
            {
                "stem": "(audio) What class are they talking about?",
                "choices": {
                    "A": "English.",
                    "B": "Math.",
                    "C": "Science.",
                    "D": "History."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) Where is the class?",
                "choices": {
                    "A": "Room 204.",
                    "B": "Room 101.",
                    "C": "Room 310.",
                    "D": "The gym."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What almost happened?",
                "choices": {
                    "A": "The woman almost went to the wrong room.",
                    "B": "They almost missed the bus.",
                    "C": "The class was almost canceled.",
                    "D": "They almost took the wrong book."
                },
                "answer": "A"
            }
        ]
    },

    # 22. 家：電球切れ
    {
        "level": "A2",
        "topic": ["home", "lightbulb"],
        "dialog": [
            ("M", "The light in the kitchen went out."),
            ("W", "I have a spare bulb. I'll change it."),
            ("M", "Great. Thank you.")
        ],
        "questions": [
            {
                "stem": "(audio) What happened in the kitchen?",
                "choices": {
                    "A": "The light went out.",
                    "B": "The sink broke.",
                    "C": "The stove is on.",
                    "D": "The door is locked."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Change the bulb.",
                    "B": "Repair the sink.",
                    "C": "Cook dinner.",
                    "D": "Call a repair worker."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the man feel?",
                "choices": {
                    "A": "He is thankful.",
                    "B": "He is angry.",
                    "C": "He is confused.",
                    "D": "He is scared."
                },
                "answer": "A"
            }
        ]
    },

    # 23. 家：荷物の受け取り
    {
        "level": "A2",
        "topic": ["home", "delivery"],
        "dialog": [
            ("W", "A package came for you today."),
            ("M", "Really? I was waiting for it."),
            ("W", "It's on the table in the living room.")
        ],
        "questions": [
            {
                "stem": "(audio) What arrived today?",
                "choices": {
                    "A": "A package.",
                    "B": "A letter.",
                    "C": "A visitor.",
                    "D": "A pizza."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the man feel?",
                "choices": {
                    "A": "He was expecting the package.",
                    "B": "He forgot about it.",
                    "C": "He didn’t want it.",
                    "D": "He lost it."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) Where is the package now?",
                "choices": {
                    "A": "On the table.",
                    "B": "In the car.",
                    "C": "At the store.",
                    "D": "Near the door."
                },
                "answer": "A"
            }
        ]
    },

    # 24. 家：掃除
    {
        "level": "A2",
        "topic": ["home", "cleaning"],
        "dialog": [
            ("M", "The living room is messy."),
            ("W", "I’ll vacuum now."),
            ("M", "Thanks, I’ll clean the table.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the problem?",
                "choices": {
                    "A": "The living room is messy.",
                    "B": "The lights are broken.",
                    "C": "The TV is too loud.",
                    "D": "The door won't open."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Vacuum.",
                    "B": "Go shopping.",
                    "C": "Cook dinner.",
                    "D": "Fix the TV."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Clean the table.",
                    "B": "Take a nap.",
                    "C": "Leave the house.",
                    "D": "Wash the car."
                },
                "answer": "A"
            }
        ]
    },

    # 25. 修理：パソコン
    {
        "level": "A2",
        "topic": ["repair", "computer"],
        "dialog": [
            ("W", "My computer won't turn on."),
            ("M", "Maybe the cable is loose. Let me check."),
            ("W", "Thanks, I hope that's the problem.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the problem?",
                "choices": {
                    "A": "Her computer won't turn on.",
                    "B": "Her phone is broken.",
                    "C": "Her printer is jammed.",
                    "D": "Her mouse is missing."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Check the cable.",
                    "B": "Buy a new laptop.",
                    "C": "Fix the printer.",
                    "D": "Restart the router."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the woman hope?",
                "choices": {
                    "A": "That the cable is the problem.",
                    "B": "That she gets a new job.",
                    "C": "That she leaves early.",
                    "D": "That the store is open."
                },
                "answer": "A"
            }
        ]
    },

    # 26. 修理：水漏れ
    {
        "level": "A2",
        "topic": ["repair", "leak"],
        "dialog": [
            ("M", "There's water under the sink."),
            ("W", "Really? I'll call a plumber now."),
            ("M", "Good idea.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the issue?",
                "choices": {
                    "A": "Water is leaking.",
                    "B": "The stove won't turn off.",
                    "C": "The door is broken.",
                    "D": "The window won't open."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Call a plumber.",
                    "B": "Fix the leak herself.",
                    "C": "Clean the floor.",
                    "D": "Go to the store."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the man respond?",
                "choices": {
                    "A": "He agrees.",
                    "B": "He refuses.",
                    "C": "He leaves the house.",
                    "D": "He buys tools."
                },
                "answer": "A"
            }
        ]
    },

    # 27. 受付：予約確認
    {
        "level": "A2",
        "topic": ["reception", "reservation"],
        "dialog": [
            ("W", "Hi, I have a reservation for a haircut."),
            ("M", "Yes, at two p.m., right?"),
            ("W", "That's right.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman have?",
                "choices": {
                    "A": "A haircut reservation.",
                    "B": "A job interview.",
                    "C": "A hotel booking.",
                    "D": "A medical appointment."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What time is the appointment?",
                "choices": {
                    "A": "Two p.m.",
                    "B": "Ten a.m.",
                    "C": "Five p.m.",
                    "D": "Seven p.m."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) How does the woman respond?",
                "choices": {
                    "A": "She confirms the time.",
                    "B": "She changes the time.",
                    "C": "She cancels it.",
                    "D": "She asks for a discount."
                },
                "answer": "A"
            }
        ]
    },

    # 28. 受付：案内
    {
        "level": "A2",
        "topic": ["reception", "information"],
        "dialog": [
            ("M", "Where is the waiting area?"),
            ("W", "It's across from the counter."),
            ("M", "Thanks, I'll wait there.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man ask?",
                "choices": {
                    "A": "Where the waiting area is.",
                    "B": "Where the restroom is.",
                    "C": "Where the exit is.",
                    "D": "Where the manager is."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) Where is the waiting area?",
                "choices": {
                    "A": "Across from the counter.",
                    "B": "On the second floor.",
                    "C": "Next to the parking lot.",
                    "D": "Inside the office."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Wait there.",
                    "B": "Make a phone call.",
                    "C": "Go home.",
                    "D": "Speak to a manager."
                },
                "answer": "A"
            }
        ]
    },

    # 29. 予定調整：会議
    {
        "level": "A2",
        "topic": ["schedule", "meeting"],
        "dialog": [
            ("W", "Can we move our meeting to three?"),
            ("M", "Sure, I’m free then."),
            ("W", "Great, see you at three.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask?",
                "choices": {
                    "A": "To move the meeting.",
                    "B": "To cancel the meeting.",
                    "C": "To add more people.",
                    "D": "To change the topic."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What time will the meeting be?",
                "choices": {
                    "A": "Three.",
                    "B": "Noon.",
                    "C": "Nine.",
                    "D": "Six."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the man say?",
                "choices": {
                    "A": "He is free at that time.",
                    "B": "He is busy.",
                    "C": "He will be late.",
                    "D": "He cannot join."
                },
                "answer": "A"
            }
        ]
    },

    # 30. 予定調整：ランチ
    {
        "level": "A2",
        "topic": ["schedule", "lunch"],
        "dialog": [
            ("M", "Do you want to have lunch at one?"),
            ("W", "I can’t. How about one thirty?"),
            ("M", "Sure, that works.")
        ],
        "questions": [
            {
                "stem": "(audio) What do they want to arrange?",
                "choices": {
                    "A": "Lunch time.",
                    "B": "A meeting.",
                    "C": "A trip.",
                    "D": "A movie."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) When can the woman have lunch?",
                "choices": {
                    "A": "At one thirty.",
                    "B": "At one.",
                    "C": "At noon.",
                    "D": "At three."
                },
                "answer": "A"
            },
            {
                "stem": "(audio) What does the man say?",
                "choices": {
                    "A": "One thirty works for him.",
                    "B": "He already ate.",
                    "C": "He prefers one o’clock.",
                    "D": "He wants to cancel lunch."
                },
                "answer": "A"
            }
        ]
    },

    # --- B1 level 75patterns (standard) ---
    # 1. 会議のスケジュール
    {
        "level": "B1",
        "topic": ["office", "schedule"],
        "dialog": [
            ("M", "Good morning. Did you check the new meeting schedule?"),
            ("W", "Yes, it starts at ten instead of nine."),
            ("M", "Right, and we’ll meet in room B now.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers mainly discussing?",
                "choices": {
                    "A": "A change in travel plans.",
                    "B": "A change in meeting time.",
                    "C": "A new employee policy.",
                    "D": "A customer complaint."
                },
                "answer": "B",
                "rationale": "They talk about a schedule change, so B is correct."
            },
            {
                "stem": "(audio) When will the meeting start?",
                "choices": {
                    "A": "At nine o’clock.",
                    "B": "At ten o’clock.",
                    "C": "At eleven o’clock.",
                    "D": "At noon."
                },
                "answer": "B",
                "rationale": "The woman says it starts at ten instead of nine."
            },
            {
                "stem": "(audio) Where will they meet?",
                "choices": {
                    "A": "In room A.",
                    "B": "In room B.",
                    "C": "In the cafeteria.",
                    "D": "In the lobby."
                },
                "answer": "B",
                "rationale": "The man says they’ll meet in room B."
            },
        ],
    },
    # 2. 出張先ホテルの予約
    {
        "level": "B1",
        "topic": ["business trip", "hotel"],
        "dialog": [
            ("W", "Did you book a hotel for your business trip?"),
            ("M", "Yes, but they changed my reservation to another branch."),
            ("W", "Is it still close to the client’s office?"),
            ("M", "Yes, it’s just a five-minute walk.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers mainly talking about?",
                "choices": {
                    "A": "A delayed flight.",
                    "B": "A hotel reservation.",
                    "C": "A job interview.",
                    "D": "A training workshop."
                },
                "answer": "B",
                "rationale": "They discuss the man’s hotel booking for a business trip."
            },
            {
                "stem": "(audio) What change was made to the man’s reservation?",
                "choices": {
                    "A": "The check-in time was moved.",
                    "B": "His room type was upgraded.",
                    "C": "He was moved to another branch.",
                    "D": "Breakfast was canceled."
                },
                "answer": "C",
                "rationale": "He says they changed his reservation to another branch."
            },
            {
                "stem": "(audio) What is said about the new hotel?",
                "choices": {
                    "A": "It is far from the client’s office.",
                    "B": "It is within walking distance.",
                    "C": "It is under renovation.",
                    "D": "It does not have Internet access."
                },
                "answer": "B",
                "rationale": "He says it is just a five-minute walk."
            },
        ],
    },
    # 3. レストランの予約
    {
        "level": "B1",
        "topic": ["restaurant", "reservation"],
        "dialog": [
            ("M", "I’d like to confirm our dinner reservation for tonight."),
            ("W", "Sure. Is it under the name Tanaka?"),
            ("M", "Yes, for four people at seven thirty."),
            ("W", "All right, we’ll have your table ready.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation taking place?",
                "choices": {
                    "A": "In a restaurant.",
                    "B": "At a travel agency.",
                    "C": "In a company lobby.",
                    "D": "At a supermarket."
                },
                "answer": "A",
                "rationale": "They are confirming a dinner reservation and a table."
            },
            {
                "stem": "(audio) How many people will be in the group?",
                "choices": {
                    "A": "Two.",
                    "B": "Three.",
                    "C": "Four.",
                    "D": "Five."
                },
                "answer": "C",
                "rationale": "The man says the reservation is for four people."
            },
            {
                "stem": "(audio) What time is the reservation for?",
                "choices": {
                    "A": "Six o’clock.",
                    "B": "Seven o’clock.",
                    "C": "Seven thirty.",
                    "D": "Eight thirty."
                },
                "answer": "C",
                "rationale": "He says, “for four people at seven thirty.”"
            },
        ],
    },

    # 4. 通勤・電車の遅延
    {
        "level": "B1",
        "topic": ["commute", "train delay"],
        "dialog": [
            ("W", "You’re late today. Was the train delayed again?"),
            ("M", "Yes, there was an accident on the line."),
            ("W", "Did they announce how long the delay would be?"),
            ("M", "They said about twenty minutes.")
        ],
        "questions": [
            {
                "stem": "(audio) Why was the man late?",
                "choices": {
                    "A": "He overslept.",
                    "B": "The train was delayed.",
                    "C": "He missed his bus.",
                    "D": "He had a meeting at home."
                },
                "answer": "B",
                "rationale": "He explains that there was a delay on the train line."
            },
            {
                "stem": "(audio) What caused the problem on the train line?",
                "choices": {
                    "A": "Construction work.",
                    "B": "Bad weather.",
                    "C": "An accident.",
                    "D": "A power outage."
                },
                "answer": "C",
                "rationale": "He says there was an accident on the line."
            },
            {
                "stem": "(audio) How long was the delay?",
                "choices": {
                    "A": "About ten minutes.",
                    "B": "About twenty minutes.",
                    "C": "About thirty minutes.",
                    "D": "About one hour."
                },
                "answer": "B",
                "rationale": "The man mentions a delay of about twenty minutes."
            },
        ],
    },

    # 5. コピー機の故障
    {
        "level": "B1",
        "topic": ["office", "equipment"],
        "dialog": [
            ("M", "The copier stopped working again."),
            ("W", "Really? Did you call the maintenance company?"),
            ("M", "Not yet. I wanted to ask if we should replace it first."),
            ("W", "Let’s call them today and talk about a new one later.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers mainly talking about?",
                "choices": {
                    "A": "Ordering office furniture.",
                    "B": "Fixing a broken copier.",
                    "C": "Hiring a new employee.",
                    "D": "Changing the lunch schedule."
                },
                "answer": "B",
                "rationale": "They focus on the copier that stopped working."
            },
            {
                "stem": "(audio) What has the man NOT done yet?",
                "choices": {
                    "A": "Used the copier.",
                    "B": "Called the maintenance company.",
                    "C": "Talked to his boss.",
                    "D": "Printed the documents."
                },
                "answer": "B",
                "rationale": "He says he has not called the maintenance company yet."
            },
            {
                "stem": "(audio) What do they decide to do?",
                "choices": {
                    "A": "Buy a new copier immediately.",
                    "B": "Cancel the printing job.",
                    "C": "Call the maintenance company today.",
                    "D": "Use the copier on another floor."
                },
                "answer": "C",
                "rationale": "The woman says they should call the company today."
            },
        ],
    },

    # 6. イベント準備
    {
        "level": "B1",
        "topic": ["company event", "preparation"],
        "dialog": [
            ("W", "Are we ready for tomorrow’s company event?"),
            ("M", "Almost. We still need to set up the projector."),
            ("W", "Did anyone test the sound system?"),
            ("M", "Yes, Ken checked it this morning.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers preparing for?",
                "choices": {
                    "A": "A job interview.",
                    "B": "A company event.",
                    "C": "A business trip.",
                    "D": "A staff meeting."
                },
                "answer": "B",
                "rationale": "They mention preparations for tomorrow’s company event."
            },
            {
                "stem": "(audio) What still needs to be done?",
                "choices": {
                    "A": "Sending invitations.",
                    "B": "Cleaning the office.",
                    "C": "Setting up the projector.",
                    "D": "Ordering lunch."
                },
                "answer": "C",
                "rationale": "The man says they still need to set up the projector."
            },
            {
                "stem": "(audio) What is said about the sound system?",
                "choices": {
                    "A": "It is broken.",
                    "B": "It will arrive tomorrow.",
                    "C": "It was checked in the morning.",
                    "D": "It cannot be used at the event."
                },
                "answer": "C",
                "rationale": "Ken already checked the sound system in the morning."
            },
        ],
    },

    # 7. 荷物の再配達
    {
        "level": "B1",
        "topic": ["delivery", "redelivery"],
        "dialog": [
            ("M", "I found a notice from the delivery company on my door."),
            ("W", "Oh, did they try to deliver a package while you were out?"),
            ("M", "Yes, it says they will come again tomorrow afternoon."),
            ("W", "You should call them if you need to change the time.")
        ],
        "questions": [
            {
                "stem": "(audio) What happened while the man was out?",
                "choices": {
                    "A": "His neighbor visited him.",
                    "B": "A package was delivered successfully.",
                    "C": "A delivery attempt was made.",
                    "D": "The electricity was turned off."
                },
                "answer": "C",
                "rationale": "The notice shows that the company tried to deliver a package."
            },
            {
                "stem": "(audio) When will the company come again?",
                "choices": {
                    "A": "Tomorrow morning.",
                    "B": "Tomorrow afternoon.",
                    "C": "Tomorrow evening.",
                    "D": "Next week."
                },
                "answer": "B",
                "rationale": "The notice says they will come again tomorrow afternoon."
            },
            {
                "stem": "(audio) What does the woman suggest the man do?",
                "choices": {
                    "A": "Call the delivery company.",
                    "B": "Visit the company office.",
                    "C": "Send an e-mail to the client.",
                    "D": "Ask a neighbor to wait at home."
                },
                "answer": "A",
                "rationale": "She tells him to call if he needs to change the time."
            },
        ],
    },

    # 8. 英会話クラスの変更
    {
        "level": "B1",
        "topic": ["language school", "class change"],
        "dialog": [
            ("W", "I’m thinking about changing my English class to a higher level."),
            ("M", "Did you talk to your teacher about it?"),
            ("W", "Yes, she said I can move starting next month."),
            ("M", "That’s great. You’ll learn even faster.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to change?",
                "choices": {
                    "A": "Her teacher.",
                    "B": "Her class level.",
                    "C": "Her school.",
                    "D": "Her textbook."
                },
                "answer": "B",
                "rationale": "She wants to move to a higher-level class."
            },
            {
                "stem": "(audio) When can the woman move to the new class?",
                "choices": {
                    "A": "Next week.",
                    "B": "Next month.",
                    "C": "In three months.",
                    "D": "At the end of the year."
                },
                "answer": "B",
                "rationale": "The teacher said she can move starting next month."
            },
            {
                "stem": "(audio) How does the man feel about the change?",
                "choices": {
                    "A": "He is worried.",
                    "B": "He is disappointed.",
                    "C": "He is surprised.",
                    "D": "He is pleased."
                },
                "answer": "D",
                "rationale": "He says she will learn faster and sounds positive."
            },
        ],
    },

    # 9. プレゼン準備
    {
        "level": "B1",
        "topic": ["presentation", "slides"],
        "dialog": [
            ("M", "Have you finished the slides for tomorrow’s presentation?"),
            ("W", "Almost. I still need to add the sales figures."),
            ("M", "Do you want me to check the graphs later?"),
            ("W", "Yes, please. A second opinion would help.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers working on?",
                "choices": {
                    "A": "A travel plan.",
                    "B": "A company newsletter.",
                    "C": "Presentation slides.",
                    "D": "An employee handbook."
                },
                "answer": "C",
                "rationale": "They talk about finishing slides and graphs."
            },
            {
                "stem": "(audio) What does the woman still need to add?",
                "choices": {
                    "A": "Sales figures.",
                    "B": "Customer comments.",
                    "C": "New pictures.",
                    "D": "Speaker notes."
                },
                "answer": "A",
                "rationale": "She mentions adding the sales figures."
            },
            {
                "stem": "(audio) What does the man offer to do?",
                "choices": {
                    "A": "Print the slides.",
                    "B": "Call the manager.",
                    "C": "Check the graphs.",
                    "D": "Reserve a meeting room."
                },
                "answer": "C",
                "rationale": "He asks if she wants him to check the graphs."
            },
        ],
    },

    # 10. 旅行の計画
    {
        "level": "B1",
        "topic": ["travel", "vacation"],
        "dialog": [
            ("W", "Have you decided where to go for your summer vacation?"),
            ("M", "Yes, I’m planning to visit Hokkaido."),
            ("W", "Are you going by plane or by train?"),
            ("M", "By plane. It’s faster and not too expensive.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers mainly talking about?",
                "choices": {
                    "A": "A business conference.",
                    "B": "A summer vacation plan.",
                    "C": "A job transfer.",
                    "D": "A school event."
                },
                "answer": "B",
                "rationale": "They discuss where to go for summer vacation."
            },
            {
                "stem": "(audio) Where does the man plan to go?",
                "choices": {
                    "A": "Okinawa.",
                    "B": "Kyoto.",
                    "C": "Hokkaido.",
                    "D": "Tokyo."
                },
                "answer": "C",
                "rationale": "He says he is planning to visit Hokkaido."
            },
            {
                "stem": "(audio) How will he travel there?",
                "choices": {
                    "A": "By train.",
                    "B": "By car.",
                    "C": "By bus.",
                    "D": "By plane."
                },
                "answer": "D",
                "rationale": "He says he will go by plane."
            },
        ],
    },

    # 11. 家電の修理
    {
        "level": "B1",
        "topic": ["home", "repair"],
        "dialog": [
            ("M", "Our washing machine stopped working yesterday."),
            ("W", "Did you call the repair service?"),
            ("M", "Yes, they’ll come on Saturday morning."),
            ("W", "That’s good. I hope they can fix it quickly.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem does the man have?",
                "choices": {
                    "A": "His refrigerator is noisy.",
                    "B": "His washing machine is not working.",
                    "C": "His air conditioner is leaking.",
                    "D": "His television will not turn on."
                },
                "answer": "B",
                "rationale": "He says the washing machine stopped working."
            },
            {
                "stem": "(audio) When will the repair service visit?",
                "choices": {
                    "A": "On Friday morning.",
                    "B": "On Friday afternoon.",
                    "C": "On Saturday morning.",
                    "D": "On Sunday evening."
                },
                "answer": "C",
                "rationale": "They are scheduled to come Saturday morning."
            },
            {
                "stem": "(audio) How does the woman feel?",
                "choices": {
                    "A": "Relieved.",
                    "B": "Angry.",
                    "C": "Uninterested.",
                    "D": "Confused."
                },
                "answer": "A",
                "rationale": "She says it is good and hopes for a quick repair."
            },
        ],
    },

    # 12. オンライン会議
    {
        "level": "B1",
        "topic": ["online meeting", "technical issue"],
        "dialog": [
            ("W", "I couldn’t hear you well in the online meeting."),
            ("M", "Really? My microphone might have been too far away."),
            ("W", "Maybe you should use a headset next time."),
            ("M", "Good idea. I’ll buy one this week.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem did the woman have?",
                "choices": {
                    "A": "She couldn’t log in.",
                    "B": "She couldn’t hear the man clearly.",
                    "C": "Her camera didn’t work.",
                    "D": "Her computer shut down."
                },
                "answer": "B",
                "rationale": "She says she could not hear him well."
            },
            {
                "stem": "(audio) What was probably wrong with the man’s device?",
                "choices": {
                    "A": "The camera was off.",
                    "B": "The screen was too dark.",
                    "C": "The microphone was too far away.",
                    "D": "The battery was low."
                },
                "answer": "C",
                "rationale": "He thinks his microphone was too far away."
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Change the meeting time.",
                    "B": "Move to another office.",
                    "C": "Use a different computer.",
                    "D": "Buy a headset."
                },
                "answer": "D",
                "rationale": "He says he will buy a headset this week."
            },
        ],
    },

    # 13. 学校行事
    {
        "level": "B1",
        "topic": ["school", "event"],
        "dialog": [
            ("M", "Are you going to the school festival this weekend?"),
            ("W", "Yes, my son will play the piano on stage."),
            ("M", "Really? What time is his performance?"),
            ("W", "At two in the afternoon.")
        ],
        "questions": [
            {
                "stem": "(audio) What event are they talking about?",
                "choices": {
                    "A": "A sports day.",
                    "B": "A school festival.",
                    "C": "A graduation ceremony.",
                    "D": "A music competition."
                },
                "answer": "B",
                "rationale": "They mention the school festival this weekend."
            },
            {
                "stem": "(audio) What will the woman’s son do?",
                "choices": {
                    "A": "Sing a song.",
                    "B": "Act in a play.",
                    "C": "Play the piano.",
                    "D": "Give a speech."
                },
                "answer": "C",
                "rationale": "She says he will play the piano on stage."
            },
            {
                "stem": "(audio) When will he perform?",
                "choices": {
                    "A": "At ten in the morning.",
                    "B": "At noon.",
                    "C": "At two in the afternoon.",
                    "D": "At six in the evening."
                },
                "answer": "C",
                "rationale": "His performance is at two in the afternoon."
            },
        ],
    },

    # 14. 病院の予約
    {
        "level": "B1",
        "topic": ["hospital", "appointment"],
        "dialog": [
            ("W", "I need to make an appointment with a doctor."),
            ("M", "There’s a clinic near the station. They open at nine."),
            ("W", "Do I need to call in advance?"),
            ("M", "Yes, it’s better to make a reservation by phone.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to do?",
                "choices": {
                    "A": "Change her job.",
                    "B": "Make a doctor’s appointment.",
                    "C": "Book a hotel room.",
                    "D": "Cancel a meeting."
                },
                "answer": "B",
                "rationale": "She needs to make an appointment with a doctor."
            },
            {
                "stem": "(audio) Where is the clinic located?",
                "choices": {
                    "A": "Next to her office.",
                    "B": "Inside a shopping mall.",
                    "C": "Near the station.",
                    "D": "Across from a library."
                },
                "answer": "C",
                "rationale": "The man says there is a clinic near the station."
            },
            {
                "stem": "(audio) What does the man recommend?",
                "choices": {
                    "A": "Going without an appointment.",
                    "B": "Sending an e-mail.",
                    "C": "Using their website.",
                    "D": "Calling in advance."
                },
                "answer": "D",
                "rationale": "He says it is better to make a reservation by phone."
            },
        ],
    },

    # 15. 買い物の相談
    {
        "level": "B1",
        "topic": ["shopping", "advice"],
        "dialog": [
            ("M", "I want to buy a new smartphone, but I’m not sure which model to choose."),
            ("W", "What do you usually use it for?"),
            ("M", "Mostly e-mail and taking photos."),
            ("W", "Then you should pick one with a good camera and enough storage.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the man thinking about buying?",
                "choices": {
                    "A": "A laptop.",
                    "B": "A tablet.",
                    "C": "A smartphone.",
                    "D": "A camera."
                },
                "answer": "C",
                "rationale": "He says he wants to buy a new smartphone."
            },
            {
                "stem": "(audio) What does he mainly use his device for?",
                "choices": {
                    "A": "Online games and music.",
                    "B": "Watching movies.",
                    "C": "E-mail and taking photos.",
                    "D": "Reading newspapers."
                },
                "answer": "C",
                "rationale": "He mentions e-mail and taking photos."
            },
            {
                "stem": "(audio) What advice does the woman give?",
                "choices": {
                    "A": "Choose the cheapest model.",
                    "B": "Wait for a sale next month.",
                    "C": "Buy two phones with different plans.",
                    "D": "Choose a phone with a good camera and enough storage."
                },
                "answer": "D",
                "rationale": "She recommends a phone with a strong camera and storage."
            },
        ],
    },

    # 16. 宿題の締切 ---
    {
        "level": "B1",
        "topic": ["school", "homework"],
        "dialog": [
            ("W", "Did you finish the English homework for tomorrow?"),
            ("M", "Not yet. I forgot we had to write an essay."),
            ("W", "The teacher said we can hand it in by Friday."),
            ("M", "Really? Then I’ll work on it tonight and tomorrow.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the students talking about?",
                "choices": {
                    "A": "A school trip.",
                    "B": "An English homework assignment.",
                    "C": "A math test.",
                    "D": "A club activity."
                },
                "answer": "B",
                "rationale": "They mention finishing English homework and writing an essay."
            },
            {
                "stem": "(audio) When is the final deadline for the homework?",
                "choices": {
                    "A": "Tomorrow.",
                    "B": "Friday.",
                    "C": "Next Monday.",
                    "D": "Next month."
                },
                "answer": "B",
                "rationale": "The girl says they can hand it in by Friday."
            },
            {
                "stem": "(audio) What will the boy do?",
                "choices": {
                    "A": "Ask the teacher for help.",
                    "B": "Work on the essay this weekend.",
                    "C": "Do the essay tonight and tomorrow.",
                    "D": "Give up on the assignment."
                },
                "answer": "C",
                "rationale": "He says he’ll work on it tonight and tomorrow."
            },
        ],
    },

    # 17. 期末テスト ---
    {
        "level": "B1",
        "topic": ["school", "exam"],
        "dialog": [
            ("M", "Have you started studying for the final exam?"),
            ("W", "Yes, but I’m having trouble with history."),
            ("M", "Our teacher will give a review lesson after school today."),
            ("W", "Great. I’ll stay and ask some questions.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the main topic of the conversation?",
                "choices": {
                    "A": "Choosing a new textbook.",
                    "B": "Preparing for the final exam.",
                    "C": "Planning a school festival.",
                    "D": "Joining a sports team."
                },
                "answer": "B",
                "rationale": "They talk about studying for the final exam."
            },
            {
                "stem": "(audio) Which subject is difficult for the girl?",
                "choices": {
                    "A": "Math.",
                    "B": "History.",
                    "C": "Science.",
                    "D": "English."
                },
                "answer": "B",
                "rationale": "She says she is having trouble with history."
            },
            {
                "stem": "(audio) What will the girl do after school?",
                "choices": {
                    "A": "Play basketball with friends.",
                    "B": "Go home early.",
                    "C": "Stay for a review lesson.",
                    "D": "Take the exam again."
                },
                "answer": "C",
                "rationale": "She decides to stay and ask questions in the review lesson."
            },
        ],
    },

    # 18. クラブ活動 ---
    {
        "level": "B1",
        "topic": ["school", "club activity"],
        "dialog": [
            ("W", "Are you going to the tennis club practice today?"),
            ("M", "I’m not sure. I have a lot of homework."),
            ("W", "The coach said today’s practice will be shorter."),
            ("M", "In that case, I’ll go for the first hour and leave early.")
        ],
        "questions": [
            {
                "stem": "(audio) What club are they talking about?",
                "choices": {
                    "A": "The music club.",
                    "B": "The art club.",
                    "C": "The tennis club.",
                    "D": "The science club."
                },
                "answer": "C",
                "rationale": "They mention tennis club practice."
            },
            {
                "stem": "(audio) Why was the boy unsure about going to practice?",
                "choices": {
                    "A": "He hurt his ankle.",
                    "B": "He had to help at home.",
                    "C": "He didn’t like the coach.",
                    "D": "He had a lot of homework."
                },
                "answer": "D",
                "rationale": "He says he has a lot of homework."
            },
            {
                "stem": "(audio) What does the boy decide to do?",
                "choices": {
                    "A": "Skip practice completely.",
                    "B": "Go only for the first hour.",
                    "C": "Arrive late to practice.",
                    "D": "Talk to the coach tomorrow."
                },
                "answer": "B",
                "rationale": "He says he’ll go for the first hour and leave early."
            },
        ],
    },

    # 19. 三者面談 ---
    {
        "level": "B1",
        "topic": ["school", "parent-teacher meeting"],
        "dialog": [
            ("M", "My parents are coming to school next Tuesday."),
            ("W", "Is it for the parent-teacher meeting?"),
            ("M", "Yes, my homeroom teacher wants to talk about my grades."),
            ("W", "I hope it goes well. Have you shown your report card to them?")
        ],
        "questions": [
            {
                "stem": "(audio) Why are the boy’s parents coming to school?",
                "choices": {
                    "A": "To join a school trip.",
                    "B": "To watch a concert.",
                    "C": "To attend a parent-teacher meeting.",
                    "D": "To help at a school festival."
                },
                "answer": "C",
                "rationale": "He says it is for the parent-teacher meeting."
            },
            {
                "stem": "(audio) What does the teacher want to talk about?",
                "choices": {
                    "A": "The boy’s club activities.",
                    "B": "The boy’s grades.",
                    "C": "The boy’s future job.",
                    "D": "The boy’s health."
                },
                "answer": "B",
                "rationale": "He mentions that the teacher wants to talk about his grades."
            },
            {
                "stem": "(audio) What does the girl ask at the end?",
                "choices": {
                    "A": "If he has done his homework.",
                    "B": "If he has joined a new club.",
                    "C": "If he has changed his homeroom teacher.",
                    "D": "If he has shown his report card to his parents."
                },
                "answer": "D",
                "rationale": "She asks whether he has shown his report card."
            },
        ],
    },

    # 20. 修学旅行 ---
    {
        "level": "B1",
        "topic": ["school", "school trip"],
        "dialog": [
            ("W", "Where are you going for your school trip this year?"),
            ("M", "We’re visiting Kyoto for three days."),
            ("W", "Are you staying at a hotel or with host families?"),
            ("M", "At a hotel near the station, so we can walk to many temples.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers discussing?",
                "choices": {
                    "A": "A sports competition.",
                    "B": "A part-time job.",
                    "C": "A school trip.",
                    "D": "A language test."
                },
                "answer": "C",
                "rationale": "They talk about where they are going for the school trip."
            },
            {
                "stem": "(audio) Where will the students visit?",
                "choices": {
                    "A": "Osaka.",
                    "B": "Kyoto.",
                    "C": "Nagoya.",
                    "D": "Sapporo."
                },
                "answer": "B",
                "rationale": "He says they will visit Kyoto."
            },
            {
                "stem": "(audio) Where will they stay?",
                "choices": {
                    "A": "At a campground.",
                    "B": "With host families.",
                    "C": "In a school dormitory.",
                    "D": "At a hotel near the station."
                },
                "answer": "D",
                "rationale": "He says they will stay at a hotel near the station."
            },
        ],
    },

    # 21. 市内観光ツアー ---
    {
        "level": "B1",
        "topic": ["travel", "city tour"],
        "dialog": [
            ("M", "Do you want to join the city bus tour tomorrow?"),
            ("W", "Maybe. How long does it last?"),
            ("M", "About three hours, and it stops at the castle and the museum."),
            ("W", "Sounds good. Let’s book the morning tour.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers planning to do?",
                "choices": {
                    "A": "Rent bicycles.",
                    "B": "Join a city bus tour.",
                    "C": "Take a night train.",
                    "D": "Visit a theme park."
                },
                "answer": "B",
                "rationale": "They are talking about joining a city bus tour."
            },
            {
                "stem": "(audio) How long does the tour last?",
                "choices": {
                    "A": "One hour.",
                    "B": "Two hours.",
                    "C": "Three hours.",
                    "D": "Four hours."
                },
                "answer": "C",
                "rationale": "He says the tour lasts about three hours."
            },
            {
                "stem": "(audio) Which tour do they decide to take?",
                "choices": {
                    "A": "The morning tour.",
                    "B": "The afternoon tour.",
                    "C": "The evening tour.",
                    "D": "The two-day tour."
                },
                "answer": "A",
                "rationale": "The woman suggests booking the morning tour."
            },
        ],
    },

    # 22. 観光案内所 ---
    {
        "level": "B1",
        "topic": ["travel", "information center"],
        "dialog": [
            ("W", "Excuse me, is there a tourist information center nearby?"),
            ("M", "Yes, there’s one inside the train station."),
            ("W", "Do they have maps in English?"),
            ("M", "They do, and they can also recommend sightseeing spots.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman looking for?",
                "choices": {
                    "A": "A souvenir shop.",
                    "B": "A tourist information center.",
                    "C": "A coffee shop.",
                    "D": "A bus stop."
                },
                "answer": "B",
                "rationale": "She asks about a tourist information center."
            },
            {
                "stem": "(audio) Where is the information center located?",
                "choices": {
                    "A": "In front of the city hall.",
                    "B": "Inside the train station.",
                    "C": "Next to the museum.",
                    "D": "Across from the hotel."
                },
                "answer": "B",
                "rationale": "The man says it is inside the train station."
            },
            {
                "stem": "(audio) What service is mentioned?",
                "choices": {
                    "A": "Bike rental.",
                    "B": "Currency exchange.",
                    "C": "English maps and sightseeing advice.",
                    "D": "Free airport shuttle."
                },
                "answer": "C",
                "rationale": "He says they provide English maps and recommendations."
            },
        ],
    },

    # 23. ホテルチェックイン ---
    {
        "level": "B1",
        "topic": ["travel", "hotel check-in"],
        "dialog": [
            ("M", "I have a reservation under the name Suzuki."),
            ("W", "Welcome. May I see your passport, please?"),
            ("M", "Here it is. Is breakfast included in my plan?"),
            ("W", "Yes, it’s served on the second floor from seven to ten.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation taking place?",
                "choices": {
                    "A": "At an airport counter.",
                    "B": "At a hotel front desk.",
                    "C": "At a travel agency.",
                    "D": "At a restaurant."
                },
                "answer": "B",
                "rationale": "They talk about a reservation and check-in procedures."
            },
            {
                "stem": "(audio) What does the man ask about?",
                "choices": {
                    "A": "The Wi-Fi password.",
                    "B": "Laundry service.",
                    "C": "The breakfast plan.",
                    "D": "Late check-out."
                },
                "answer": "C",
                "rationale": "He asks whether breakfast is included."
            },
            {
                "stem": "(audio) When is breakfast served?",
                "choices": {
                    "A": "From six to nine.",
                    "B": "From seven to ten.",
                    "C": "From eight to eleven.",
                    "D": "From nine to noon."
                },
                "answer": "B",
                "rationale": "The clerk says breakfast is from seven to ten."
            },
        ],
    },

    # 24. 観光地の入場券 ---
    {
        "level": "B1",
        "topic": ["travel", "ticket"],
        "dialog": [
            ("W", "Do we need to buy tickets in advance for the castle?"),
            ("M", "On weekends it’s better to reserve online."),
            ("W", "Today is Saturday, right?"),
            ("M", "Yes, so let’s book now before we leave the hotel.")
        ],
        "questions": [
            {
                "stem": "(audio) What are they planning to visit?",
                "choices": {
                    "A": "A zoo.",
                    "B": "A castle.",
                    "C": "An aquarium.",
                    "D": "A theme park."
                },
                "answer": "B",
                "rationale": "They talk about buying tickets for the castle."
            },
            {
                "stem": "(audio) Why should they buy tickets in advance?",
                "choices": {
                    "A": "Because it is closed on weekdays.",
                    "B": "Because it is cheaper online.",
                    "C": "Because it is crowded on weekends.",
                    "D": "Because they lost their tickets."
                },
                "answer": "C",
                "rationale": "He says it is better on weekends, implying it is crowded."
            },
            {
                "stem": "(audio) When will they book the tickets?",
                "choices": {
                    "A": "After they arrive at the castle.",
                    "B": "Tomorrow morning.",
                    "C": "Next week.",
                    "D": "Before leaving the hotel."
                },
                "answer": "D",
                "rationale": "He suggests booking now before leaving the hotel."
            },
        ],
    },

    # 25. 空港への行き方 ---
    {
        "level": "B1",
        "topic": ["travel", "transportation"],
        "dialog": [
            ("M", "How are you going to the airport tomorrow?"),
            ("W", "I’ll take the airport limousine bus from the station."),
            ("M", "What time does it leave?"),
            ("W", "At eight fifteen. I’m going to catch that one.")
        ],
        "questions": [
            {
                "stem": "(audio) What are they mainly discussing?",
                "choices": {
                    "A": "Where to stay during the trip.",
                    "B": "Which airline to choose.",
                    "C": "How to get to the airport.",
                    "D": "What to do at the airport."
                },
                "answer": "C",
                "rationale": "They talk about transportation to the airport."
            },
            {
                "stem": "(audio) How will the woman go to the airport?",
                "choices": {
                    "A": "By taxi.",
                    "B": "By airport bus.",
                    "C": "By local train.",
                    "D": "By rental car."
                },
                "answer": "B",
                "rationale": "She says she will take the airport limousine bus."
            },
            {
                "stem": "(audio) When does the bus leave?",
                "choices": {
                    "A": "At seven thirty.",
                    "B": "At eight fifteen.",
                    "C": "At nine o’clock.",
                    "D": "At ten fifteen."
                },
                "answer": "B",
                "rationale": "She says it leaves at eight fifteen."
            },
        ],
    },
    # 26. オフィス：昼食の予定
    {
        "level": "B1",
        "topic": ["office", "lunch"],
        "dialog": [
            ("W", "Do you have plans for lunch today?"),
            ("M", "Not really. I was just going to eat at my desk."),
            ("W", "Why don’t we try the new cafe across the street?"),
            ("M", "Sounds good. Let’s leave at twelve.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers mainly talking about?",
                "choices": {
                    "A": "A meeting schedule.",
                    "B": "Their lunch plans.",
                    "C": "An office party.",
                    "D": "A business trip."
                },
                "answer": "B",
                "rationale": "They discuss where to go for lunch."
            },
            {
                "stem": "(audio) Where does the woman suggest going?",
                "choices": {
                    "A": "The company cafeteria.",
                    "B": "A restaurant in the station.",
                    "C": "The new cafe across the street.",
                    "D": "A convenience store nearby."
                },
                "answer": "C",
                "rationale": "She suggests the new cafe across the street."
            },
            {
                "stem": "(audio) When will they go out?",
                "choices": {
                    "A": "At eleven thirty.",
                    "B": "At twelve.",
                    "C": "At one.",
                    "D": "At two."
                },
                "answer": "B",
                "rationale": "The man says they will leave at twelve."
            },
        ],
    },

    # 27. オフィス：席替え
    {
        "level": "B1",
        "topic": ["office", "seating"],
        "dialog": [
            ("M", "I heard they’re changing the seating plan next month."),
            ("W", "Yes, our team will move closer to the window."),
            ("M", "Really? Then we’ll be right next to the design team."),
            ("W", "That should make it easier to work together.")
        ],
        "questions": [
            {
                "stem": "(audio) What change will happen next month?",
                "choices": {
                    "A": "The office will close earlier.",
                    "B": "The company will hire new staff.",
                    "C": "The seating plan will be changed.",
                    "D": "The computers will be replaced."
                },
                "answer": "C",
                "rationale": "They mention changing the seating plan."
            },
            {
                "stem": "(audio) Where will their team move?",
                "choices": {
                    "A": "Closer to the entrance.",
                    "B": "Closer to the window.",
                    "C": "To another floor.",
                    "D": "To the warehouse."
                },
                "answer": "B",
                "rationale": "The woman says they will move closer to the window."
            },
            {
                "stem": "(audio) Why is the woman happy about the change?",
                "choices": {
                    "A": "She will get a bigger desk.",
                    "B": "She will have a shorter commute.",
                    "C": "She will work fewer hours.",
                    "D": "She can work more easily with another team."
                },
                "answer": "D",
                "rationale": "She says it will be easier to work with the design team."
            },
        ],
    },

    # 28. オフィス：電話の取次ぎ
    {
        "level": "B1",
        "topic": ["office", "phone"],
        "dialog": [
            ("W", "Mr. Kimura, you have a call from a client."),
            ("M", "Could you ask her to hold for a minute?"),
            ("W", "Sure. Should I transfer the call to your desk?"),
            ("M", "Yes, please. I’ll be ready in a moment.")
        ],
        "questions": [
            {
                "stem": "(audio) Who is trying to contact the man?",
                "choices": {
                    "A": "His coworker.",
                    "B": "His manager.",
                    "C": "A client.",
                    "D": "A delivery driver."
                },
                "answer": "C",
                "rationale": "The woman says the call is from a client."
            },
            {
                "stem": "(audio) What does the man ask the woman to do?",
                "choices": {
                    "A": "Take a message.",
                    "B": "Transfer the call.",
                    "C": "Call the client back.",
                    "D": "Cancel the meeting."
                },
                "answer": "B",
                "rationale": "He wants her to transfer the call to his desk."
            },
            {
                "stem": "(audio) What will the client be asked to do?",
                "choices": {
                    "A": "Send an e-mail.",
                    "B": "Call again later.",
                    "C": "Wait on the line.",
                    "D": "Visit the office."
                },
                "answer": "C",
                "rationale": "He asks her to hold for a minute."
            },
        ],
    },

    # 29. オフィス：在宅勤務
    {
        "level": "B1",
        "topic": ["office", "remote work"],
        "dialog": [
            ("M", "Are you working from home on Friday?"),
            ("W", "Yes, I’ll join the meeting online."),
            ("M", "Then I’ll send you the documents by e-mail."),
            ("W", "Thanks. I’ll print them out at home.")
        ],
        "questions": [
            {
                "stem": "(audio) Where will the woman work on Friday?",
                "choices": {
                    "A": "At home.",
                    "B": "At a client’s office.",
                    "C": "At a hotel.",
                    "D": "At a coworking space."
                },
                "answer": "A",
                "rationale": "She says she is working from home."
            },
            {
                "stem": "(audio) How will she join the meeting?",
                "choices": {
                    "A": "By phone.",
                    "B": "By video call.",
                    "C": "In person.",
                    "D": "By sending a report."
                },
                "answer": "B",
                "rationale": "She says she’ll join the meeting online."
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Bring the documents to her house.",
                    "B": "Print the documents for her.",
                    "C": "Send the documents by e-mail.",
                    "D": "Cancel the meeting."
                },
                "answer": "C",
                "rationale": "He offers to e-mail the documents."
            },
        ],
    },

    # 30. オフィス：新入社員の紹介
    {
        "level": "B1",
        "topic": ["office", "new employee"],
        "dialog": [
            ("W", "Have you met the new assistant in our department?"),
            ("M", "Not yet. What’s she like?"),
            ("W", "She’s very friendly and good with computers."),
            ("M", "Great. I’ll introduce myself this afternoon.")
        ],
        "questions": [
            {
                "stem": "(audio) Who are the speakers talking about?",
                "choices": {
                    "A": "A new assistant.",
                    "B": "A new manager.",
                    "C": "A new client.",
                    "D": "A new teacher."
                },
                "answer": "A",
                "rationale": "They mention a new assistant in their department."
            },
            {
                "stem": "(audio) What does the woman say about the new employee?",
                "choices": {
                    "A": "She is very strict.",
                    "B": "She is good with computers.",
                    "C": "She lives far from the office.",
                    "D": "She has worked there for years."
                },
                "answer": "B",
                "rationale": "The woman says she is good with computers."
            },
            {
                "stem": "(audio) What does the man plan to do?",
                "choices": {
                    "A": "Give her training.",
                    "B": "Send her an e-mail.",
                    "C": "Have lunch with her.",
                    "D": "Introduce himself later."
                },
                "answer": "D",
                "rationale": "He says he’ll introduce himself in the afternoon."
            },
        ],
    },

    # 31. 会社：プロジェクトの締切
    {
        "level": "B1",
        "topic": ["office", "deadline"],
        "dialog": [
            ("M", "Do you think we can finish the project by Friday?"),
            ("W", "It will be tight, but possible if we work late today."),
            ("M", "Should we ask Ken to help with the data?"),
            ("W", "Yes, he’s fast at checking numbers.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers worried about?",
                "choices": {
                    "A": "Travel expenses.",
                    "B": "A project deadline.",
                    "C": "A client visit.",
                    "D": "A job interview."
                },
                "answer": "B",
                "rationale": "They are concerned about finishing the project by Friday."
            },
            {
                "stem": "(audio) What might they do today?",
                "choices": {
                    "A": "Leave work early.",
                    "B": "Cancel a meeting.",
                    "C": "Work late.",
                    "D": "Visit a customer."
                },
                "answer": "C",
                "rationale": "The woman says they may need to work late."
            },
            {
                "stem": "(audio) Why do they want Ken’s help?",
                "choices": {
                    "A": "He knows the client well.",
                    "B": "He can speak several languages.",
                    "C": "He is good at data checking.",
                    "D": "He has extra free time."
                },
                "answer": "C",
                "rationale": "She says he is fast at checking numbers."
            },
        ],
    },

    # 32. 会社：出張の準備
    {
        "level": "B1",
        "topic": ["business trip", "preparation"],
        "dialog": [
            ("W", "Have you booked your train for the Osaka trip?"),
            ("M", "Not yet. I’m still waiting for the final schedule."),
            ("W", "You should book soon. The seats fill up quickly."),
            ("M", "You’re right. I’ll do it during my break.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is the man going on a business trip?",
                "choices": {
                    "A": "Nagoya.",
                    "B": "Osaka.",
                    "C": "Sapporo.",
                    "D": "Fukuoka."
                },
                "answer": "B",
                "rationale": "They mention his trip to Osaka."
            },
            {
                "stem": "(audio) What has the man NOT done yet?",
                "choices": {
                    "A": "Packed his suitcase.",
                    "B": "Called the client.",
                    "C": "Booked his train.",
                    "D": "Reserved a hotel room."
                },
                "answer": "C",
                "rationale": "He says he has not booked the train yet."
            },
            {
                "stem": "(audio) When will he book it?",
                "choices": {
                    "A": "During his break.",
                    "B": "Tomorrow morning.",
                    "C": "Next week.",
                    "D": "After the trip."
                },
                "answer": "A",
                "rationale": "He says he will book it during his break."
            },
        ],
    },

    # 33. 会社：取引先訪問
    {
        "level": "B1",
        "topic": ["client visit", "office"],
        "dialog": [
            ("M", "Our clients from Korea are visiting on Wednesday."),
            ("W", "Should we prepare a presentation for them?"),
            ("M", "Yes, just a short one about our new products."),
            ("W", "Okay, I’ll make the slides tomorrow.")
        ],
        "questions": [
            {
                "stem": "(audio) Who will visit the office?",
                "choices": {
                    "A": "New employees.",
                    "B": "Clients from Korea.",
                    "C": "Job applicants.",
                    "D": "Students on a tour."
                },
                "answer": "B",
                "rationale": "The man mentions clients from Korea."
            },
            {
                "stem": "(audio) What do they decide to prepare?",
                "choices": {
                    "A": "A company brochure.",
                    "B": "A long report.",
                    "C": "A short presentation.",
                    "D": "A product sample set."
                },
                "answer": "C",
                "rationale": "They agree to make a short presentation."
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Reserve a meeting room.",
                    "B": "Book their hotel.",
                    "C": "Translate the documents.",
                    "D": "Create the slides."
                },
                "answer": "D",
                "rationale": "She says she will make the slides."
            },
        ],
    },

    # 34. 会社：新人研修
    {
        "level": "B1",
        "topic": ["office", "training"],
        "dialog": [
            ("W", "Did you attend the training for the new system?"),
            ("M", "No, I was out of the office yesterday."),
            ("W", "They recorded it, so you can watch it online."),
            ("M", "Great. I’ll check it this evening.")
        ],
        "questions": [
            {
                "stem": "(audio) What did the company hold yesterday?",
                "choices": {
                    "A": "A job interview.",
                    "B": "A farewell party.",
                    "C": "A training session.",
                    "D": "A client meeting."
                },
                "answer": "C",
                "rationale": "They talk about training for a new system."
            },
            {
                "stem": "(audio) Why didn’t the man attend?",
                "choices": {
                    "A": "He was feeling sick.",
                    "B": "He was out of the office.",
                    "C": "He forgot about it.",
                    "D": "He didn’t receive the e-mail."
                },
                "answer": "B",
                "rationale": "He says he was out of the office."
            },
            {
                "stem": "(audio) How will he catch up?",
                "choices": {
                    "A": "By asking a coworker.",
                    "B": "By reading a manual.",
                    "C": "By watching a recording online.",
                    "D": "By attending another class."
                },
                "answer": "C",
                "rationale": "She says it was recorded and he can watch it online."
            },
        ],
    },

    # 35. 会社：プリンターの紙切れ
    {
        "level": "B1",
        "topic": ["office", "printer"],
        "dialog": [
            ("M", "The printer on the third floor is out of paper."),
            ("W", "Really? I’ll bring a new pack from the storage room."),
            ("M", "Thanks. I need to print these reports soon."),
            ("W", "No problem. It’ll take just a minute.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the problem with the printer?",
                "choices": {
                    "A": "It is out of ink.",
                    "B": "It is out of paper.",
                    "C": "It is turned off.",
                    "D": "It is jammed with paper."
                },
                "answer": "B",
                "rationale": "The man says it is out of paper."
            },
            {
                "stem": "(audio) Where will the woman get more paper?",
                "choices": {
                    "A": "From her desk drawer.",
                    "B": "From the first floor.",
                    "C": "From the storage room.",
                    "D": "From the manager’s office."
                },
                "answer": "C",
                "rationale": "She mentions bringing a pack from the storage room."
            },
            {
                "stem": "(audio) Why is the man in a hurry?",
                "choices": {
                    "A": "He needs to copy a textbook.",
                    "B": "He has to leave for a trip.",
                    "C": "He must scan some photos.",
                    "D": "He needs to print some reports."
                },
                "answer": "D",
                "rationale": "He says he needs to print reports soon."
            },
        ],
    },

    # 36. レストラン：席の希望
    {
        "level": "B1",
        "topic": ["restaurant", "seating"],
        "dialog": [
            ("W", "Good evening. Do you have a reservation?"),
            ("M", "Yes, under the name Yamada."),
            ("W", "Would you prefer a table by the window or near the counter?"),
            ("M", "By the window, please.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation taking place?",
                "choices": {
                    "A": "At a hotel front desk.",
                    "B": "At a restaurant entrance.",
                    "C": "At a travel agency.",
                    "D": "At a supermarket cashier."
                },
                "answer": "B",
                "rationale": "They talk about a reservation and where to sit."
            },
            {
                "stem": "(audio) Under what name is the reservation?",
                "choices": {
                    "A": "Suzuki.",
                    "B": "Tanaka.",
                    "C": "Yamada.",
                    "D": "Sato."
                },
                "answer": "C",
                "rationale": "The man says the reservation is under Yamada."
            },
            {
                "stem": "(audio) What kind of table does the man choose?",
                "choices": {
                    "A": "Near the counter.",
                    "B": "In a private room.",
                    "C": "By the window.",
                    "D": "Outside on the terrace."
                },
                "answer": "C",
                "rationale": "He asks for a table by the window."
            },
        ],
    },

    # 37. レストラン：料理の変更
    {
        "level": "B1",
        "topic": ["restaurant", "order"],
        "dialog": [
            ("M", "Excuse me, may I change my order?"),
            ("W", "Sure. What would you like instead?"),
            ("M", "I’ll have the grilled fish instead of the steak."),
            ("W", "No problem. I’ll tell the kitchen right away.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man want to do?",
                "choices": {
                    "A": "Pay the bill.",
                    "B": "Cancel the reservation.",
                    "C": "Change his order.",
                    "D": "Move to another table."
                },
                "answer": "C",
                "rationale": "He asks if he can change his order."
            },
            {
                "stem": "(audio) What does he order instead of the steak?",
                "choices": {
                    "A": "Grilled chicken.",
                    "B": "Grilled fish.",
                    "C": "Pasta with sauce.",
                    "D": "A vegetarian meal."
                },
                "answer": "B",
                "rationale": "He changes to the grilled fish."
            },
            {
                "stem": "(audio) What will the waitress do?",
                "choices": {
                    "A": "Bring the dessert menu.",
                    "B": "Offer a discount.",
                    "C": "Move his seat.",
                    "D": "Inform the kitchen."
                },
                "answer": "D",
                "rationale": "She says she’ll tell the kitchen right away."
            },
        ],
    },

    # 38. レストラン：混み具合
    {
        "level": "B1",
        "topic": ["restaurant", "waiting"],
        "dialog": [
            ("W", "How long is the wait for a table?"),
            ("M", "About twenty minutes, but the counter seats are free."),
            ("W", "That’s fine. We’ll take the counter seats."),
            ("M", "Great. Please follow me.")
        ],
        "questions": [
            {
                "stem": "(audio) What information does the woman ask for?",
                "choices": {
                    "A": "The price of the meal.",
                    "B": "The size of the table.",
                    "C": "The waiting time.",
                    "D": "The restaurant’s address."
                },
                "answer": "C",
                "rationale": "She asks how long the wait is."
            },
            {
                "stem": "(audio) How long is the wait for a table?",
                "choices": {
                    "A": "Five minutes.",
                    "B": "Ten minutes.",
                    "C": "Twenty minutes.",
                    "D": "One hour."
                },
                "answer": "C",
                "rationale": "The man says about twenty minutes."
            },
            {
                "stem": "(audio) Where will they sit?",
                "choices": {
                    "A": "At a window table.",
                    "B": "At a large table.",
                    "C": "At a table outside.",
                    "D": "At the counter."
                },
                "answer": "D",
                "rationale": "They decide to take the counter seats."
            },
        ],
    },

    # 39. ショッピング：返品
    {
        "level": "B1",
        "topic": ["shopping", "return"],
        "dialog": [
            ("M", "I’d like to return this shirt. It’s too small."),
            ("W", "Do you have the receipt with you?"),
            ("M", "Yes, here it is."),
            ("W", "Thank you. Would you like a refund or a larger size?")
        ],
        "questions": [
            {
                "stem": "(audio) Why does the man want to return the shirt?",
                "choices": {
                    "A": "He doesn’t like the color.",
                    "B": "It was on sale.",
                    "C": "It is too small.",
                    "D": "It has a stain."
                },
                "answer": "C",
                "rationale": "He says the shirt is too small."
            },
            {
                "stem": "(audio) What does the clerk ask for?",
                "choices": {
                    "A": "The price tag.",
                    "B": "The man’s ID card.",
                    "C": "The payment card.",
                    "D": "The receipt."
                },
                "answer": "D",
                "rationale": "She asks if he has the receipt."
            },
            {
                "stem": "(audio) What choice does the man receive?",
                "choices": {
                    "A": "A different color or a refund.",
                    "B": "A refund or a larger size.",
                    "C": "A discount or a coupon.",
                    "D": "Free delivery or free gift wrapping."
                },
                "answer": "B",
                "rationale": "She offers a refund or a larger size."
            },
        ],
    },

    # 40. ショッピング：在庫確認
    {
        "level": "B1",
        "topic": ["shopping", "stock"],
        "dialog": [
            ("W", "Do you have this bag in another color?"),
            ("M", "Let me check in the back for you."),
            ("W", "Thank you. I’m looking for a navy one."),
            ("M", "You’re in luck. We have one left in navy.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want?",
                "choices": {
                    "A": "A different size of the bag.",
                    "B": "A different color of the bag.",
                    "C": "A discount on the bag.",
                    "D": "A repair for the bag."
                },
                "answer": "B",
                "rationale": "She asks for another color."
            },
            {
                "stem": "(audio) Which color is she looking for?",
                "choices": {
                    "A": "Black.",
                    "B": "White.",
                    "C": "Navy.",
                    "D": "Red."
                },
                "answer": "C",
                "rationale": "She says she wants a navy one."
            },
            {
                "stem": "(audio) What does the clerk find?",
                "choices": {
                    "A": "No bags in stock.",
                    "B": "Many bags in navy.",
                    "C": "Only one bag in navy.",
                    "D": "A bag in a different style."
                },
                "answer": "C",
                "rationale": "He says they have one left in navy."
            },
        ],
    },

    # 41. スーパー：ポイントカード
    {
        "level": "B1",
        "topic": ["shopping", "membership"],
        "dialog": [
            ("M", "Do you have a point card for this supermarket?"),
            ("W", "No, I don’t. Do I need one?"),
            ("M", "If you sign up, you can get discounts on some items."),
            ("W", "Okay, I’ll fill out the form.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the man asking about?",
                "choices": {
                    "A": "A gift card.",
                    "B": "A point card.",
                    "C": "A credit card.",
                    "D": "A student card."
                },
                "answer": "B",
                "rationale": "He asks if she has a point card."
            },
            {
                "stem": "(audio) What benefit does the card give?",
                "choices": {
                    "A": "Free parking.",
                    "B": "Free home delivery.",
                    "C": "Discounts on some items.",
                    "D": "Free drinks at the cafe."
                },
                "answer": "C",
                "rationale": "He mentions discounts on some items."
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Refuse to sign up.",
                    "B": "Sign up by phone.",
                    "C": "Fill out the form.",
                    "D": "Apply online at home."
                },
                "answer": "C",
                "rationale": "She says she will fill out the form."
            },
        ],
    },

    # 42. 病院：受付での会話
    {
        "level": "B1",
        "topic": ["hospital", "reception"],
        "dialog": [
            ("W", "Good morning. Do you have an appointment?"),
            ("M", "Yes, at ten o’clock with Dr. Sato."),
            ("W", "Please fill in this form and have a seat."),
            ("M", "Thank you. I’ll bring it back when I’m done.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation taking place?",
                "choices": {
                    "A": "At a bank counter.",
                    "B": "At a hospital reception desk.",
                    "C": "At a hotel lobby.",
                    "D": "At a post office."
                },
                "answer": "B",
                "rationale": "They mention an appointment with a doctor."
            },
            {
                "stem": "(audio) What time is the man’s appointment?",
                "choices": {
                    "A": "At nine o’clock.",
                    "B": "At ten o’clock.",
                    "C": "At eleven o’clock.",
                    "D": "At noon."
                },
                "answer": "B",
                "rationale": "He says he has an appointment at ten."
            },
            {
                "stem": "(audio) What does the woman ask the man to do?",
                "choices": {
                    "A": "Pay the fee first.",
                    "B": "Go directly to the doctor’s office.",
                    "C": "Wait outside the building.",
                    "D": "Fill in a form and wait."
                },
                "answer": "D",
                "rationale": "She tells him to fill in a form and have a seat."
            },
        ],
    },

    # 43. 病院：検査結果
    {
        "level": "B1",
        "topic": ["hospital", "test result"],
        "dialog": [
            ("M", "When can I get the results of my blood test?"),
            ("W", "They should be ready tomorrow afternoon."),
            ("M", "Can I check them online?"),
            ("W", "Yes, we’ll send you an e-mail when they are available.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the man waiting for?",
                "choices": {
                    "A": "An X-ray.",
                    "B": "A bill.",
                    "C": "Blood test results.",
                    "D": "A prescription."
                },
                "answer": "C",
                "rationale": "He asks about the results of his blood test."
            },
            {
                "stem": "(audio) When will the results be ready?",
                "choices": {
                    "A": "This morning.",
                    "B": "This evening.",
                    "C": "Tomorrow afternoon.",
                    "D": "Next week."
                },
                "answer": "C",
                "rationale": "The woman says they will be ready tomorrow afternoon."
            },
            {
                "stem": "(audio) How will he know they are available?",
                "choices": {
                    "A": "He will receive a phone call.",
                    "B": "He will get a letter.",
                    "C": "He will be told at the reception desk.",
                    "D": "He will get an e-mail."
                },
                "answer": "D",
                "rationale": "She says they will send an e-mail."
            },
        ],
    },

    # 44. 薬局：薬の説明
    {
        "level": "B1",
        "topic": ["pharmacy", "medicine"],
        "dialog": [
            ("W", "Here is your medicine. Please take one tablet after each meal."),
            ("M", "For how many days should I take it?"),
            ("W", "For five days. And don’t drive if you feel sleepy."),
            ("M", "I understand. Thank you.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation most likely taking place?",
                "choices": {
                    "A": "In a supermarket.",
                    "B": "In a pharmacy.",
                    "C": "In a library.",
                    "D": "In a bank."
                },
                "answer": "B",
                "rationale": "They are talking about how to take medicine."
            },
            {
                "stem": "(audio) How often should the man take the tablets?",
                "choices": {
                    "A": "Once a day.",
                    "B": "Twice a day.",
                    "C": "After each meal.",
                    "D": "Only when he has pain."
                },
                "answer": "C",
                "rationale": "She says to take one tablet after each meal."
            },
            {
                "stem": "(audio) What warning does the woman give?",
                "choices": {
                    "A": "Don’t use a mobile phone.",
                    "B": "Don’t eat before taking it.",
                    "C": "Don’t drink coffee.",
                    "D": "Don’t drive if he feels sleepy."
                },
                "answer": "D",
                "rationale": "She warns him not to drive if he feels sleepy."
            },
        ],
    },

    # 45. 学校：宿題の提出
    {
        "level": "B1",
        "topic": ["school", "assignment"],
        "dialog": [
            ("M", "Did you hand in the science report?"),
            ("W", "Not yet. I’m going to give it to the teacher after lunch."),
            ("M", "Is today the last day?"),
            ("W", "Yes, she said she won’t accept it tomorrow.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the students talking about?",
                "choices": {
                    "A": "A school trip.",
                    "B": "A science report.",
                    "C": "A club activity.",
                    "D": "An entrance exam."
                },
                "answer": "B",
                "rationale": "They mention handing in the science report."
            },
            {
                "stem": "(audio) When will the girl submit her report?",
                "choices": {
                    "A": "Before school.",
                    "B": "During class.",
                    "C": "After lunch.",
                    "D": "Tomorrow morning."
                },
                "answer": "C",
                "rationale": "She plans to give it to the teacher after lunch."
            },
            {
                "stem": "(audio) What did the teacher say?",
                "choices": {
                    "A": "She will collect reports next week.",
                    "B": "She will accept late reports.",
                    "C": "She will cancel the homework.",
                    "D": "She won’t accept reports tomorrow."
                },
                "answer": "D",
                "rationale": "The girl says the teacher won’t accept it tomorrow."
            },
        ],
    },

    # 46. 学校：グループ発表
    {
        "level": "B1",
        "topic": ["school", "presentation"],
        "dialog": [
            ("W", "Our group presentation is next Tuesday."),
            ("M", "Who will speak first?"),
            ("W", "You will explain the graph, and I’ll talk about the survey."),
            ("M", "Okay. I’ll practice my part tonight.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the students preparing for?",
                "choices": {
                    "A": "A sports competition.",
                    "B": "A school festival performance.",
                    "C": "A group presentation.",
                    "D": "A field trip."
                },
                "answer": "C",
                "rationale": "They are talking about their group presentation."
            },
            {
                "stem": "(audio) What will the boy talk about?",
                "choices": {
                    "A": "The survey results.",
                    "B": "The graph.",
                    "C": "The school rules.",
                    "D": "The schedule."
                },
                "answer": "B",
                "rationale": "She says he will explain the graph."
            },
            {
                "stem": "(audio) What will the girl do?",
                "choices": {
                    "A": "Talk about the survey.",
                    "B": "Draw the graph on the board.",
                    "C": "Introduce the teacher.",
                    "D": "Take photos of the class."
                },
                "answer": "A",
                "rationale": "She says she will talk about the survey."
            },
        ],
    },

    # 47. 学校：クラブの見学
    {
        "level": "B1",
        "topic": ["school", "club visit"],
        "dialog": [
            ("M", "Are you going to visit any clubs after school?"),
            ("W", "Yes, I want to see the art club and the brass band."),
            ("M", "I’ll go to the soccer club. Maybe we can meet later."),
            ("W", "Sure, let’s meet at the school gate at five.")
        ],
        "questions": [
            {
                "stem": "(audio) What will the students do after school?",
                "choices": {
                    "A": "Visit some club activities.",
                    "B": "Go straight home.",
                    "C": "Take an extra class.",
                    "D": "Study in the library."
                },
                "answer": "A",
                "rationale": "They plan to visit clubs after school."
            },
            {
                "stem": "(audio) Which clubs does the girl want to see?",
                "choices": {
                    "A": "Soccer and tennis.",
                    "B": "Art and brass band.",
                    "C": "Brass band and soccer.",
                    "D": "Art and soccer."
                },
                "answer": "B",
                "rationale": "She mentions the art club and the brass band."
            },
            {
                "stem": "(audio) When will they meet again?",
                "choices": {
                    "A": "At four.",
                    "B": "At four thirty.",
                    "C": "At five.",
                    "D": "At five thirty."
                },
                "answer": "C",
                "rationale": "They agree to meet at five."
            },
        ],
    },

    # 48. 学校：先生との面談予約
    {
        "level": "B1",
        "topic": ["school", "teacher meeting"],
        "dialog": [
            ("W", "I need to talk to Ms. Brown about my grade."),
            ("M", "She said she is free after school on Thursday."),
            ("W", "Should I make an appointment?"),
            ("M", "Yes, you should write your name on the list outside her room.")
        ],
        "questions": [
            {
                "stem": "(audio) Why does the girl want to talk to the teacher?",
                "choices": {
                    "A": "About her homework.",
                    "B": "About her grade.",
                    "C": "About a club activity.",
                    "D": "About a school trip."
                },
                "answer": "B",
                "rationale": "She wants to talk about her grade."
            },
            {
                "stem": "(audio) When is the teacher free?",
                "choices": {
                    "A": "Before school on Monday.",
                    "B": "At lunchtime on Tuesday.",
                    "C": "After school on Thursday.",
                    "D": "On Saturday morning."
                },
                "answer": "C",
                "rationale": "He says she is free after school on Thursday."
            },
            {
                "stem": "(audio) How can the girl make an appointment?",
                "choices": {
                    "A": "By sending an e-mail.",
                    "B": "By calling the office.",
                    "C": "By talking to the principal.",
                    "D": "By writing her name on a list."
                },
                "answer": "D",
                "rationale": "She should write her name on the list outside the room."
            },
        ],
    },

    # 49. 学校：図書館の利用
    {
        "level": "B1",
        "topic": ["school", "library"],
        "dialog": [
            ("M", "Do you know how long we can keep library books?"),
            ("W", "Yes, we can borrow them for two weeks."),
            ("M", "What happens if we return them late?"),
            ("W", "We have to pay a small fine.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the students talking about?",
                "choices": {
                    "A": "Using the computer room.",
                    "B": "Borrowing books from the library.",
                    "C": "Joining a club.",
                    "D": "Taking a school bus."
                },
                "answer": "B",
                "rationale": "They mention borrowing library books."
            },
            {
                "stem": "(audio) How long can they keep the books?",
                "choices": {
                    "A": "For one week.",
                    "B": "For ten days.",
                    "C": "For two weeks.",
                    "D": "For one month."
                },
                "answer": "C",
                "rationale": "The girl says they can borrow them for two weeks."
            },
            {
                "stem": "(audio) What happens if they return books late?",
                "choices": {
                    "A": "They cannot borrow books anymore.",
                    "B": "They must write an apology.",
                    "C": "They have to pay a fine.",
                    "D": "They must talk to the principal."
                },
                "answer": "C",
                "rationale": "She says they have to pay a small fine."
            },
        ],
    },

    # 50. 学校：忘れ物
    {
        "level": "B1",
        "topic": ["school", "lost item"],
        "dialog": [
            ("W", "I can’t find my math textbook."),
            ("M", "Did you check the lost and found box in the office?"),
            ("W", "Not yet. I’ll go there after class."),
            ("M", "Good idea. I saw some textbooks in it yesterday.")
        ],
        "questions": [
            {
                "stem": "(audio) What has the girl lost?",
                "choices": {
                    "A": "Her notebook.",
                    "B": "Her homework.",
                    "C": "Her math textbook.",
                    "D": "Her pencil case."
                },
                "answer": "C",
                "rationale": "She says she can’t find her math textbook."
            },
            {
                "stem": "(audio) Where does the boy suggest she look?",
                "choices": {
                    "A": "In the locker room.",
                    "B": "In the classroom.",
                    "C": "In the library.",
                    "D": "In the office’s lost and found box."
                },
                "answer": "D",
                "rationale": "He suggests the lost and found in the office."
            },
            {
                "stem": "(audio) When will she go there?",
                "choices": {
                    "A": "Before class.",
                    "B": "During lunch break.",
                    "C": "After class.",
                    "D": "Tomorrow morning."
                },
                "answer": "C",
                "rationale": "She says she’ll go there after class."
            },
        ],
    },

    # 51. 旅行：ホテルの朝食
    {
        "level": "B1",
        "topic": ["travel", "hotel breakfast"],
        "dialog": [
            ("M", "Is breakfast included in this room rate?"),
            ("W", "Yes, it is. It’s a buffet in the restaurant on the first floor."),
            ("M", "What time is it served until?"),
            ("W", "Until ten o’clock in the morning.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man ask about?",
                "choices": {
                    "A": "Laundry service.",
                    "B": "Check-out time.",
                    "C": "Breakfast.",
                    "D": "Room cleaning."
                },
                "answer": "C",
                "rationale": "He asks if breakfast is included."
            },
            {
                "stem": "(audio) Where is breakfast served?",
                "choices": {
                    "A": "In the lobby.",
                    "B": "On the rooftop.",
                    "C": "In a cafe outside.",
                    "D": "In the restaurant on the first floor."
                },
                "answer": "D",
                "rationale": "She says it’s in the first-floor restaurant."
            },
            {
                "stem": "(audio) Until what time is breakfast available?",
                "choices": {
                    "A": "Nine o’clock.",
                    "B": "Ten o’clock.",
                    "C": "Eleven o’clock.",
                    "D": "Noon."
                },
                "answer": "B",
                "rationale": "Breakfast is served until ten o’clock."
            },
        ],
    },

    # 52. 旅行：チェックアウト時間
    {
        "level": "B1",
        "topic": ["travel", "checkout"],
        "dialog": [
            ("W", "What time is check-out tomorrow?"),
            ("M", "It’s at eleven, but we can keep your luggage at the front desk."),
            ("W", "That’s helpful. We want to do some sightseeing in the morning."),
            ("M", "No problem. Just bring your bags here when you leave the room.")
        ],
        "questions": [
            {
                "stem": "(audio) What time is check-out?",
                "choices": {
                    "A": "At nine.",
                    "B": "At ten.",
                    "C": "At eleven.",
                    "D": "At noon."
                },
                "answer": "C",
                "rationale": "The clerk says check-out is at eleven."
            },
            {
                "stem": "(audio) What service does the hotel offer?",
                "choices": {
                    "A": "Free breakfast.",
                    "B": "Late check-out for free.",
                    "C": "Airport shuttle.",
                    "D": "Luggage storage."
                },
                "answer": "D",
                "rationale": "They can keep luggage at the front desk."
            },
            {
                "stem": "(audio) What will the guests do in the morning?",
                "choices": {
                    "A": "Go shopping at a mall.",
                    "B": "Have a meeting.",
                    "C": "Do some sightseeing.",
                    "D": "Stay in their room."
                },
                "answer": "C",
                "rationale": "The woman says they want to do sightseeing."
            },
        ],
    },

    # 53. 旅行：観光バスの予約
    {
        "level": "B1",
        "topic": ["travel", "bus tour"],
        "dialog": [
            ("M", "I’d like to book two seats on tomorrow’s city tour bus."),
            ("W", "Morning or afternoon tour?"),
            ("M", "The afternoon one, please."),
            ("W", "All right. It departs at two from in front of this hotel.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man want to do?",
                "choices": {
                    "A": "Rent a car.",
                    "B": "Book a taxi.",
                    "C": "Reserve seats on a bus tour.",
                    "D": "Buy train tickets."
                },
                "answer": "C",
                "rationale": "He wants two seats on a city tour bus."
            },
            {
                "stem": "(audio) Which tour does he choose?",
                "choices": {
                    "A": "The morning tour.",
                    "B": "The afternoon tour.",
                    "C": "The evening tour.",
                    "D": "A two-day tour."
                },
                "answer": "B",
                "rationale": "He chooses the afternoon tour."
            },
            {
                "stem": "(audio) When and where does the bus leave?",
                "choices": {
                    "A": "At ten from the station.",
                    "B": "At eleven from the museum.",
                    "C": "At one from the airport.",
                    "D": "At two from the hotel."
                },
                "answer": "D",
                "rationale": "It departs at two from in front of the hotel."
            },
        ],
    },

    # 54. 旅行：駅での案内
    {
        "level": "B1",
        "topic": ["travel", "station"],
        "dialog": [
            ("W", "Excuse me, which platform does the train to Nagoya leave from?"),
            ("M", "From platform four. The next one leaves in ten minutes."),
            ("W", "Do I need to reserve a seat?"),
            ("M", "No, you can sit in the non-reserved cars.")
        ],
        "questions": [
            {
                "stem": "(audio) What destination is the woman asking about?",
                "choices": {
                    "A": "Osaka.",
                    "B": "Nagoya.",
                    "C": "Kyoto.",
                    "D": "Tokyo."
                },
                "answer": "B",
                "rationale": "She asks about the train to Nagoya."
            },
            {
                "stem": "(audio) Which platform does the train leave from?",
                "choices": {
                    "A": "Platform one.",
                    "B": "Platform two.",
                    "C": "Platform three.",
                    "D": "Platform four."
                },
                "answer": "D",
                "rationale": "The man says it leaves from platform four."
            },
            {
                "stem": "(audio) What does the man say about seat reservations?",
                "choices": {
                    "A": "They are required.",
                    "B": "They are not necessary.",
                    "C": "They are sold out.",
                    "D": "They are only for children."
                },
                "answer": "B",
                "rationale": "He says she can sit in non-reserved cars."
            },
        ],
    },

    # 55. 旅行：空港の手荷物
    {
        "level": "B1",
        "topic": ["travel", "airport"],
        "dialog": [
            ("M", "Excuse me, where can I pick up my checked baggage?"),
            ("W", "Please go down the stairs to the baggage claim area."),
            ("M", "Which carousel is for flight 325?"),
            ("W", "It’s number three, just to the left.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is the man now?",
                "choices": {
                    "A": "At a hotel.",
                    "B": "At a train station.",
                    "C": "At an airport.",
                    "D": "At a bus terminal."
                },
                "answer": "C",
                "rationale": "He asks about checked baggage and baggage claim."
            },
            {
                "stem": "(audio) What does the woman tell him to do first?",
                "choices": {
                    "A": "Go up to the second floor.",
                    "B": "Go down to the baggage claim area.",
                    "C": "Go outside to the bus stop.",
                    "D": "Go to the check-in counter."
                },
                "answer": "B",
                "rationale": "She tells him to go down to baggage claim."
            },
            {
                "stem": "(audio) Which carousel should he go to?",
                "choices": {
                    "A": "Number one.",
                    "B": "Number two.",
                    "C": "Number three.",
                    "D": "Number four."
                },
                "answer": "C",
                "rationale": "Carousel number three is for his flight."
            },
        ],
    },

    # 56. 旅行：観光地での写真
    {
        "level": "B1",
        "topic": ["travel", "tourist spot"],
        "dialog": [
            ("W", "Could you take a picture of us in front of the castle?"),
            ("M", "Sure. Just press this button, right?"),
            ("W", "Yes, and please take two, just in case."),
            ("M", "No problem. Say cheese!")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman ask the man to do?",
                "choices": {
                    "A": "Show her the way to the castle.",
                    "B": "Explain the history of the castle.",
                    "C": "Take a picture of her group.",
                    "D": "Hold her bag while she takes a photo."
                },
                "answer": "C",
                "rationale": "She asks him to take their picture."
            },
            {
                "stem": "(audio) What does she request about the photos?",
                "choices": {
                    "A": "Take only one quickly.",
                    "B": "Take two photos.",
                    "C": "Take a video instead.",
                    "D": "Take photos with her own camera."
                },
                "answer": "B",
                "rationale": "She asks him to take two, just in case."
            },
            {
                "stem": "(audio) Where are they probably standing?",
                "choices": {
                    "A": "In front of a museum.",
                    "B": "In front of a station.",
                    "C": "In front of a castle.",
                    "D": "In front of a hotel."
                },
                "answer": "C",
                "rationale": "She wants a picture in front of the castle."
            },
        ],
    },

    # 57. 日常：ゴミ出し
    {
        "level": "B1",
        "topic": ["home", "trash"],
        "dialog": [
            ("M", "Don’t forget that tomorrow is burnable trash day."),
            ("W", "Really? I thought it was on Friday."),
            ("M", "No, they changed the schedule last month."),
            ("W", "Okay, I’ll take out the trash tonight.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers talking about?",
                "choices": {
                    "A": "The weather forecast.",
                    "B": "The trash collection schedule.",
                    "C": "A neighborhood event.",
                    "D": "A power outage."
                },
                "answer": "B",
                "rationale": "They discuss when trash will be collected."
            },
            {
                "stem": "(audio) What did the woman misunderstand?",
                "choices": {
                    "A": "The kind of trash.",
                    "B": "The number of trash bags.",
                    "C": "The location of the trash area.",
                    "D": "The collection day."
                },
                "answer": "D",
                "rationale": "She thought the day was Friday."
            },
            {
                "stem": "(audio) What will the woman do?",
                "choices": {
                    "A": "Take out the trash tonight.",
                    "B": "Call the city office.",
                    "C": "Complain to the neighbor.",
                    "D": "Throw the trash away at work."
                },
                "answer": "A",
                "rationale": "She says she will take out the trash tonight."
            },
        ],
    },

    # 58. 日常：電気料金
    {
        "level": "B1",
        "topic": ["home", "utility bill"],
        "dialog": [
            ("W", "Our electricity bill is higher this month."),
            ("M", "Maybe because we used the air conditioner a lot."),
            ("W", "We should turn it off when we leave the room."),
            ("M", "You’re right. Let’s be more careful.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem do the speakers mention?",
                "choices": {
                    "A": "The water is not running.",
                    "B": "The gas bill is missing.",
                    "C": "The electricity bill is high.",
                    "D": "The Internet is too slow."
                },
                "answer": "C",
                "rationale": "They say the electricity bill is higher."
            },
            {
                "stem": "(audio) What may be the cause of the problem?",
                "choices": {
                    "A": "Using the heater too much.",
                    "B": "Using the air conditioner a lot.",
                    "C": "Leaving the lights on all night.",
                    "D": "Buying a new refrigerator."
                },
                "answer": "B",
                "rationale": "He thinks they used the air conditioner a lot."
            },
            {
                "stem": "(audio) What will they try to do?",
                "choices": {
                    "A": "Use the air conditioner more often.",
                    "B": "Move to another apartment.",
                    "C": "Stop using electricity at night.",
                    "D": "Turn off the air conditioner when leaving the room."
                },
                "answer": "D",
                "rationale": "They agree to turn it off when leaving the room."
            },
        ],
    },

    # 59. 日常：宅配ピザ
    {
        "level": "B1",
        "topic": ["home", "delivery"],
        "dialog": [
            ("M", "Shall we order pizza for dinner?"),
            ("W", "Sure. Let’s get a large one and some salad."),
            ("M", "Do you want to order online or by phone?"),
            ("W", "Online is easier. I’ll use the app.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers planning to do?",
                "choices": {
                    "A": "Cook dinner at home.",
                    "B": "Go out to a restaurant.",
                    "C": "Order pizza delivery.",
                    "D": "Buy food at a supermarket."
                },
                "answer": "C",
                "rationale": "They want to order pizza for dinner."
            },
            {
                "stem": "(audio) What else will they order besides pizza?",
                "choices": {
                    "A": "Soup.",
                    "B": "Salad.",
                    "C": "Drinks.",
                    "D": "Dessert."
                },
                "answer": "B",
                "rationale": "They decide to get salad too."
            },
            {
                "stem": "(audio) How will they place the order?",
                "choices": {
                    "A": "By fax.",
                    "B": "By phone.",
                    "C": "On the website.",
                    "D": "Using an app."
                },
                "answer": "D",
                "rationale": "The woman says she will use the app."
            },
        ],
    },

    # 60. 日常：友人との待ち合わせ
    {
        "level": "B1",
        "topic": ["daily life", "meeting"],
        "dialog": [
            ("W", "Where should we meet on Saturday?"),
            ("M", "How about in front of the station clock at three?"),
            ("W", "That’s easy to find."),
            ("M", "Great. I’ll be there a little early.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers arranging?",
                "choices": {
                    "A": "A hotel stay.",
                    "B": "A phone interview.",
                    "C": "A time and place to meet.",
                    "D": "A delivery time."
                },
                "answer": "C",
                "rationale": "They are deciding when and where to meet."
            },
            {
                "stem": "(audio) Where will they meet?",
                "choices": {
                    "A": "Inside a cafe.",
                    "B": "At the bus stop.",
                    "C": "At the park entrance.",
                    "D": "In front of the station clock."
                },
                "answer": "D",
                "rationale": "They agree to meet in front of the station clock."
            },
            {
                "stem": "(audio) When will they meet?",
                "choices": {
                    "A": "At one o’clock.",
                    "B": "At two o’clock.",
                    "C": "At three o’clock.",
                    "D": "At four o’clock."
                },
                "answer": "C",
                "rationale": "The man suggests three o’clock."
            },
        ],
    },

    # 61. 職場：ランチミーティング
    {
        "level": "B1",
        "topic": ["office", "lunch meeting"],
        "dialog": [
            ("M", "Shall we invite the new salesperson to our lunch meeting?"),
            ("W", "Yes, that will help her learn about our products."),
            ("M", "I’ll send her an e-mail with the time and place."),
            ("W", "Good idea. Let’s book a larger table this time.")
        ],
        "questions": [
            {
                "stem": "(audio) Why do they want to invite the new salesperson?",
                "choices": {
                    "A": "To introduce her to the clients.",
                    "B": "To show her the city.",
                    "C": "To help her learn about the products.",
                    "D": "To discuss her salary."
                },
                "answer": "C",
                "rationale": "They say the lunch will help her learn about their products."
            },
            {
                "stem": "(audio) How will the man contact her?",
                "choices": {
                    "A": "By phone.",
                    "B": "By text message.",
                    "C": "By e-mail.",
                    "D": "By letter."
                },
                "answer": "C",
                "rationale": "He says he will send her an e-mail."
            },
            {
                "stem": "(audio) What will they change about the lunch meeting?",
                "choices": {
                    "A": "The restaurant.",
                    "B": "The menu.",
                    "C": "The day.",
                    "D": "The table size."
                },
                "answer": "D",
                "rationale": "They plan to book a larger table."
            },
        ],
    },

    # 62. 職場：コピーサービスの利用
    {
        "level": "B1",
        "topic": ["office", "copy center"],
        "dialog": [
            ("W", "The office copier is still broken."),
            ("M", "Then we should use the copy center on the first floor."),
            ("W", "Do we need a special card for that?"),
            ("M", "Yes, you can borrow one from the reception desk.")
        ],
        "questions": [
            {
                "stem": "(audio) Why can’t they use the office copier?",
                "choices": {
                    "A": "It has no paper.",
                    "B": "It is reserved for another department.",
                    "C": "It is being moved.",
                    "D": "It is broken."
                },
                "answer": "D",
                "rationale": "The woman says the copier is still broken."
            },
            {
                "stem": "(audio) Where is the copy center?",
                "choices": {
                    "A": "On the first floor.",
                    "B": "In another building.",
                    "C": "Next to the cafeteria.",
                    "D": "Across the street."
                },
                "answer": "A",
                "rationale": "The man mentions the copy center on the first floor."
            },
            {
                "stem": "(audio) What must they borrow to use it?",
                "choices": {
                    "A": "A key.",
                    "B": "A special card.",
                    "C": "A USB drive.",
                    "D": "A password list."
                },
                "answer": "B",
                "rationale": "They need a special card from the reception desk."
            },
        ],
    },

    # 63. 職場：残業のお願い
    {
        "level": "B1",
        "topic": ["office", "overtime"],
        "dialog": [
            ("M", "Can you stay a little late today to finish these orders?"),
            ("W", "I can stay until seven, but I have a lesson after that."),
            ("M", "That should be enough. Thank you for helping."),
            ("W", "No problem. I’ll start with the urgent ones.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the man asking the woman to do?",
                "choices": {
                    "A": "Come in early tomorrow.",
                    "B": "Call some customers.",
                    "C": "Stay late at the office.",
                    "D": "Move to another department."
                },
                "answer": "C",
                "rationale": "He asks if she can stay a little late."
            },
            {
                "stem": "(audio) How long can the woman stay?",
                "choices": {
                    "A": "Until six o’clock.",
                    "B": "Until seven o’clock.",
                    "C": "Until eight o’clock.",
                    "D": "Until nine o’clock."
                },
                "answer": "B",
                "rationale": "She says she can stay until seven."
            },
            {
                "stem": "(audio) Which orders will she work on first?",
                "choices": {
                    "A": "The smallest ones.",
                    "B": "The most urgent ones.",
                    "C": "The international ones.",
                    "D": "The online ones."
                },
                "answer": "B",
                "rationale": "She says she’ll start with the urgent ones."
            },
        ],
    },

    # 64. 職場：会議室の予約
    {
        "level": "B1",
        "topic": ["office", "meeting room"],
        "dialog": [
            ("W", "Is the meeting room free at three this afternoon?"),
            ("M", "Let me check the calendar. No, it’s booked until four."),
            ("W", "Then we’ll have to start at four thirty."),
            ("M", "I’ll update the schedule and inform the team.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to know?",
                "choices": {
                    "A": "If the meeting room has a projector.",
                    "B": "If the meeting room is air-conditioned.",
                    "C": "If the meeting room is free at three.",
                    "D": "If the meeting room is on the second floor."
                },
                "answer": "C",
                "rationale": "She asks whether it is free at three."
            },
            {
                "stem": "(audio) Until what time is the room booked?",
                "choices": {
                    "A": "Until two.",
                    "B": "Until three.",
                    "C": "Until four.",
                    "D": "Until five."
                },
                "answer": "C",
                "rationale": "The man says it’s booked until four."
            },
            {
                "stem": "(audio) When will they start their meeting?",
                "choices": {
                    "A": "At three.",
                    "B": "At three thirty.",
                    "C": "At four.",
                    "D": "At four thirty."
                },
                "answer": "D",
                "rationale": "They decide to start at four thirty."
            },
        ],
    },

    # 65. 職場：名刺の注文
    {
        "level": "B1",
        "topic": ["office", "business cards"],
        "dialog": [
            ("M", "I’m running out of business cards."),
            ("W", "You can order more through the company website."),
            ("M", "Do I need my manager’s approval?"),
            ("W", "Yes, ask him to check your order before you send it.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man need?",
                "choices": {
                    "A": "A new ID card.",
                    "B": "More business cards.",
                    "C": "A printer cartridge.",
                    "D": "A new computer."
                },
                "answer": "B",
                "rationale": "He says he is running out of business cards."
            },
            {
                "stem": "(audio) How can he order them?",
                "choices": {
                    "A": "By phone.",
                    "B": "By fax.",
                    "C": "Through the company website.",
                    "D": "At the reception desk."
                },
                "answer": "C",
                "rationale": "The woman mentions the company website."
            },
            {
                "stem": "(audio) What must he do before sending the order?",
                "choices": {
                    "A": "Show it to his manager.",
                    "B": "Pay in cash.",
                    "C": "Print the form.",
                    "D": "Call the supplier."
                },
                "answer": "A",
                "rationale": "He needs the manager’s approval."
            },
        ],
    },

    # 66. 旅行：美術館の案内
    {
        "level": "B1",
        "topic": ["travel", "museum"],
        "dialog": [
            ("W", "How much is the entrance fee for the museum?"),
            ("M", "It’s eight hundred yen for adults and free for children."),
            ("W", "Is there an audio guide in English?"),
            ("M", "Yes, you can rent one at the entrance.")
        ],
        "questions": [
            {
                "stem": "(audio) What are they talking about?",
                "choices": {
                    "A": "A zoo.",
                    "B": "A museum.",
                    "C": "A theater.",
                    "D": "A sports stadium."
                },
                "answer": "B",
                "rationale": "They mention the entrance fee for the museum."
            },
            {
                "stem": "(audio) How much is the fee for adults?",
                "choices": {
                    "A": "Five hundred yen.",
                    "B": "Six hundred yen.",
                    "C": "Eight hundred yen.",
                    "D": "One thousand yen."
                },
                "answer": "C",
                "rationale": "The fee is eight hundred yen."
            },
            {
                "stem": "(audio) What English service is available?",
                "choices": {
                    "A": "A guided tour.",
                    "B": "Subtitle displays.",
                    "C": "An audio guide.",
                    "D": "A free brochure."
                },
                "answer": "C",
                "rationale": "They say there is an audio guide in English."
            },
        ],
    },

    # 67. 旅行：温泉の利用
    {
        "level": "B1",
        "topic": ["travel", "hot spring"],
        "dialog": [
            ("M", "Is there anything I should know before using the hot spring bath?"),
            ("W", "Yes, please wash your body at the shower area first."),
            ("M", "Do I need to bring a towel from my room?"),
            ("W", "No, we provide towels at the entrance.")
        ],
        "questions": [
            {
                "stem": "(audio) What facility are they talking about?",
                "choices": {
                    "A": "A swimming pool.",
                    "B": "A gym.",
                    "C": "A hot spring bath.",
                    "D": "A restaurant."
                },
                "answer": "C",
                "rationale": "They discuss how to use the hot spring bath."
            },
            {
                "stem": "(audio) What must the man do before getting into the bath?",
                "choices": {
                    "A": "Pay an extra fee.",
                    "B": "Reserve a time slot.",
                    "C": "Wash his body at the shower area.",
                    "D": "Talk to the manager."
                },
                "answer": "C",
                "rationale": "She says he should wash at the shower area first."
            },
            {
                "stem": "(audio) Where can he get a towel?",
                "choices": {
                    "A": "Only in his room.",
                    "B": "Only at the front desk.",
                    "C": "At the souvenir shop.",
                    "D": "At the entrance to the bath."
                },
                "answer": "D",
                "rationale": "Towels are provided at the entrance."
            },
        ],
    },

    # 68. 旅行：自転車レンタル
    {
        "level": "B1",
        "topic": ["travel", "bicycle rental"],
        "dialog": [
            ("W", "Do you rent bicycles here?"),
            ("M", "Yes, it’s one thousand yen per day."),
            ("W", "Can I return it at another shop near the station?"),
            ("M", "Sure, just show this receipt when you return it.")
        ],
        "questions": [
            {
                "stem": "(audio) What service is the woman asking about?",
                "choices": {
                    "A": "Car rental.",
                    "B": "Bicycle rental.",
                    "C": "Boat rental.",
                    "D": "Camera rental."
                },
                "answer": "B",
                "rationale": "She asks if they rent bicycles."
            },
            {
                "stem": "(audio) How much does it cost per day?",
                "choices": {
                    "A": "Five hundred yen.",
                    "B": "Eight hundred yen.",
                    "C": "One thousand yen.",
                    "D": "One thousand five hundred yen."
                },
                "answer": "C",
                "rationale": "The cost is one thousand yen per day."
            },
            {
                "stem": "(audio) Where can she return the bicycle?",
                "choices": {
                    "A": "Only at this shop.",
                    "B": "At any shop in the city.",
                    "C": "At another shop near the station.",
                    "D": "At the hotel front desk."
                },
                "answer": "C",
                "rationale": "She may return it at another shop near the station."
            },
        ],
    },

    # 69. 旅行：土産物選び
    {
        "level": "B1",
        "topic": ["travel", "souvenirs"],
        "dialog": [
            ("M", "What kind of souvenirs should I buy for my coworkers?"),
            ("W", "Snacks are easy to share, like local cookies."),
            ("M", "Good idea. Do they come in small packages?"),
            ("W", "Yes, this box has individually wrapped pieces.")
        ],
        "questions": [
            {
                "stem": "(audio) Who are the souvenirs for?",
                "choices": {
                    "A": "The man’s family.",
                    "B": "The man’s classmates.",
                    "C": "The man’s coworkers.",
                    "D": "The man’s neighbors."
                },
                "answer": "C",
                "rationale": "He wants souvenirs for his coworkers."
            },
            {
                "stem": "(audio) What kind of item does the woman recommend?",
                "choices": {
                    "A": "Key chains.",
                    "B": "Local snacks.",
                    "C": "Postcards.",
                    "D": "Stationery."
                },
                "answer": "B",
                "rationale": "She recommends snacks like local cookies."
            },
            {
                "stem": "(audio) What is special about the box she shows?",
                "choices": {
                    "A": "It is very cheap.",
                    "B": "It is handmade.",
                    "C": "It is limited to this season.",
                    "D": "It contains individually wrapped pieces."
                },
                "answer": "D",
                "rationale": "She says the pieces are individually wrapped."
            },
        ],
    },

    # 70. 日常：クリーニング店
    {
        "level": "B1",
        "topic": ["daily life", "dry cleaner"],
        "dialog": [
            ("W", "When will this jacket be ready?"),
            ("M", "You can pick it up on Thursday after three."),
            ("W", "Can you remove this stain on the sleeve?"),
            ("M", "We’ll do our best, but it may not come out completely.")
        ],
        "questions": [
            {
                "stem": "(audio) Where is this conversation most likely taking place?",
                "choices": {
                    "A": "At a tailor’s shop.",
                    "B": "At a dry cleaner’s.",
                    "C": "At a clothing store.",
                    "D": "At a shoe repair shop."
                },
                "answer": "B",
                "rationale": "They discuss cleaning a jacket and a stain."
            },
            {
                "stem": "(audio) When can the woman pick up her jacket?",
                "choices": {
                    "A": "On Wednesday morning.",
                    "B": "On Thursday after three.",
                    "C": "On Friday evening.",
                    "D": "Next Monday."
                },
                "answer": "B",
                "rationale": "It will be ready on Thursday after three."
            },
            {
                "stem": "(audio) What does the clerk say about the stain?",
                "choices": {
                    "A": "It can definitely be removed.",
                    "B": "It will get bigger.",
                    "C": "It may not be completely removed.",
                    "D": "It is not visible."
                },
                "answer": "C",
                "rationale": "He cannot guarantee that it will come out completely."
            },
        ],
    },

    # 71. 日常：美容室の予約
    {
        "level": "B1",
        "topic": ["daily life", "hair salon"],
        "dialog": [
            ("M", "I’d like to make an appointment for a haircut."),
            ("W", "When would you like to come?"),
            ("M", "Is Saturday morning available?"),
            ("W", "Yes, we have a slot at ten thirty.")
        ],
        "questions": [
            {
                "stem": "(audio) What service does the man want?",
                "choices": {
                    "A": "A massage.",
                    "B": "A haircut.",
                    "C": "A facial treatment.",
                    "D": "A manicure."
                },
                "answer": "B",
                "rationale": "He wants to make an appointment for a haircut."
            },
            {
                "stem": "(audio) When does he want to come?",
                "choices": {
                    "A": "On Friday afternoon.",
                    "B": "On Saturday morning.",
                    "C": "On Sunday evening.",
                    "D": "On Monday night."
                },
                "answer": "B",
                "rationale": "He asks about Saturday morning."
            },
            {
                "stem": "(audio) What time is offered?",
                "choices": {
                    "A": "Nine o’clock.",
                    "B": "Ten thirty.",
                    "C": "Eleven thirty.",
                    "D": "Noon."
                },
                "answer": "B",
                "rationale": "She offers a slot at ten thirty."
            },
        ],
    },

    # 72. 日常：銀行での手続き
    {
        "level": "B1",
        "topic": ["daily life", "bank"],
        "dialog": [
            ("W", "I’d like to open a savings account."),
            ("M", "Please fill out this form and show me your ID."),
            ("W", "Can I get a cash card today?"),
            ("M", "We’ll send it to your address in about a week.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the woman want to do?",
                "choices": {
                    "A": "Exchange money.",
                    "B": "Apply for a loan.",
                    "C": "Open a savings account.",
                    "D": "Close her account."
                },
                "answer": "C",
                "rationale": "She says she’d like to open a savings account."
            },
            {
                "stem": "(audio) What does the clerk ask her to do?",
                "choices": {
                    "A": "Pay a fee first.",
                    "B": "Fill out a form and show ID.",
                    "C": "Call again tomorrow.",
                    "D": "Go to another branch."
                },
                "answer": "B",
                "rationale": "He asks her to fill out a form and show ID."
            },
            {
                "stem": "(audio) When will she receive the cash card?",
                "choices": {
                    "A": "Today.",
                    "B": "Tomorrow.",
                    "C": "In a few days.",
                    "D": "In about a week."
                },
                "answer": "D",
                "rationale": "He says it will be sent in about a week."
            },
        ],
    },

    # 73. 日常：郵便の再配達
    {
        "level": "B1",
        "topic": ["daily life", "redelivery"],
        "dialog": [
            ("M", "I missed a delivery while I was at work."),
            ("W", "You can request redelivery on this website."),
            ("M", "Can I choose the evening time slot?"),
            ("W", "Yes, from seven to nine p.m. is available.")
        ],
        "questions": [
            {
                "stem": "(audio) Why did the man miss the delivery?",
                "choices": {
                    "A": "He was sleeping.",
                    "B": "He was out shopping.",
                    "C": "He was at work.",
                    "D": "He was on vacation."
                },
                "answer": "C",
                "rationale": "He says he was at work."
            },
            {
                "stem": "(audio) How can he request redelivery?",
                "choices": {
                    "A": "By fax.",
                    "B": "By postcard.",
                    "C": "By phone only.",
                    "D": "On a website."
                },
                "answer": "D",
                "rationale": "The woman mentions using a website."
            },
            {
                "stem": "(audio) Which time slot does he want?",
                "choices": {
                    "A": "From nine to eleven a.m.",
                    "B": "From one to three p.m.",
                    "C": "From four to six p.m.",
                    "D": "From seven to nine p.m."
                },
                "answer": "D",
                "rationale": "He asks for the evening time slot from seven to nine."
            },
        ],
    },

    # 74. 日常：家賃の支払い
    {
        "level": "B1",
        "topic": ["daily life", "rent"],
        "dialog": [
            ("W", "Did you pay the rent for this month?"),
            ("M", "Yes, I set up automatic payment from my bank."),
            ("W", "That’s convenient. I still go to the bank every month."),
            ("M", "You should try it. It saves a lot of time.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers talking about?",
                "choices": {
                    "A": "Electricity bills.",
                    "B": "Internet fees.",
                    "C": "Rent payments.",
                    "D": "Parking fees."
                },
                "answer": "C",
                "rationale": "They mention paying the rent."
            },
            {
                "stem": "(audio) How does the man pay his rent now?",
                "choices": {
                    "A": "In cash at the landlord’s office.",
                    "B": "By sending a check.",
                    "C": "By credit card.",
                    "D": "By automatic bank payment."
                },
                "answer": "D",
                "rationale": "He says he set up automatic payment."
            },
            {
                "stem": "(audio) What does the man suggest the woman do?",
                "choices": {
                    "A": "Move to another apartment.",
                    "B": "Use automatic payment.",
                    "C": "Pay the rent late.",
                    "D": "Ask for a discount."
                },
                "answer": "B",
                "rationale": "He suggests she also use automatic payment."
            },
        ],
    },

    # 75. 日常：オンライン注文
    {
        "level": "B1",
        "topic": ["daily life", "online shopping"],
        "dialog": [
            ("M", "The shoes I ordered online haven’t arrived yet."),
            ("W", "Did you check the tracking number?"),
            ("M", "Yes, it says they’re still at the warehouse."),
            ("W", "Maybe there’s a delay. You should contact customer service.")
        ],
        "questions": [
            {
                "stem": "(audio) What did the man order?",
                "choices": {
                    "A": "A jacket.",
                    "B": "A laptop.",
                    "C": "Shoes.",
                    "D": "Books."
                },
                "answer": "C",
                "rationale": "He mentions the shoes he ordered."
            },
            {
                "stem": "(audio) What does the tracking information say?",
                "choices": {
                    "A": "The package was delivered.",
                    "B": "The package is on the truck.",
                    "C": "The package is at the warehouse.",
                    "D": "The package was returned."
                },
                "answer": "C",
                "rationale": "He says it’s still at the warehouse."
            },
            {
                "stem": "(audio) What does the woman suggest?",
                "choices": {
                    "A": "Cancel the order.",
                    "B": "Visit the warehouse.",
                    "C": "Order a different size.",
                    "D": "Contact customer service."
                },
                "answer": "D",
                "rationale": "She says he should contact customer service."
            },
        ],
    },

    # --- B2 level patterns (more challenging) ---
    # 1. ビジネス：クライアント訪問の準備
    {
        "level": "B2",
        "topic": ["office", "client visit", "preparation"],
        "dialog": [
            ("W", "The client from Seoul is coming tomorrow morning, but the sample products still haven’t arrived."),
            ("M", "If they don’t make it by the end of today, we should at least prepare photos and a short demo video."),
            ("W", "Good idea. I’ll collect the images, and could you ask the design team to help with the video?"),
            ("M", "Sure. Once I talk to them, I’ll send you an update so we can finalize the plan.")
        ],
        "questions": [
            {
                "stem": "(audio) What are the speakers worried about?",
                "choices": {
                    "A": "The sample products may not arrive in time.",
                    "B": "The client meeting might be canceled.",
                    "C": "The design team does not have enough members.",
                    "D": "The office will be closed tomorrow morning."
                },
                "answer": "A",
                "rationale": "They are concerned because the sample products have not arrived and the client is coming soon."
            },
            {
                "stem": "(audio) What do they decide to prepare as a backup?",
                "choices": {
                    "A": "Photos and a short demonstration video.",
                    "B": "Printed manuals for every product.",
                    "C": "An online survey for the visitors.",
                    "D": "A detailed financial report."
                },
                "answer": "A",
                "rationale": "The man suggests photos and a short video as an alternative, and the woman agrees."
            },
            {
                "stem": "(audio) What will the man do next?",
                "choices": {
                    "A": "Talk with the design team about the video.",
                    "B": "Call the client to postpone the meeting.",
                    "C": "Ask the manager to cancel the order.",
                    "D": "Book hotel rooms for the visitors."
                },
                "answer": "A",
                "rationale": "He says he will talk to the design team and then send an update."
            }
        ]
    },

    # 2. ビジネス：オンライン会議のトラブル
    {
        "level": "B2",
        "topic": ["office", "online meeting", "technical issue"],
        "dialog": [
            ("M", "The sound keeps cutting out in our online meeting. I’m afraid the foreign partners can’t hear us well."),
            ("W", "If we switch to audio only and turn off the cameras, the connection might become more stable."),
            ("M", "That’s worth a try. Could you also send them a quick message explaining what we’re doing?"),
            ("W", "Sure. I’ll write a short note in the chat so they know why the video disappears.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem are the speakers having?",
                "choices": {
                    "A": "The sound is cutting in and out.",
                    "B": "The presentation file was deleted.",
                    "C": "The meeting time was changed suddenly.",
                    "D": "The partners did not receive the agenda."
                },
                "answer": "A",
                "rationale": "The man says the sound keeps cutting out during the online meeting."
            },
            {
                "stem": "(audio) What solution do they want to try?",
                "choices": {
                    "A": "Turning off the cameras and keeping audio only.",
                    "B": "Restarting all of the computers in the office.",
                    "C": "Moving everyone to a different conference room.",
                    "D": "Sending the recording after the meeting ends."
                },
                "answer": "A",
                "rationale": "The woman suggests turning off the cameras so the connection may improve."
            },
            {
                "stem": "(audio) What will the woman do during the meeting?",
                "choices": {
                    "A": "Send a message in the chat to explain the change.",
                    "B": "Call the partners on the telephone instead.",
                    "C": "Stop the meeting and reschedule it.",
                    "D": "Share the screen with the meeting notes."
                },
                "answer": "A",
                "rationale": "She says she will write a short note so the partners understand why the video stops."
            }
        ]
    },

    # 3. ビジネス：展示会ブースの運営
    {
        "level": "B2",
        "topic": ["exhibition", "booth", "planning"],
        "dialog": [
            ("W", "Our booth was crowded last year, but many visitors left before talking to us."),
            ("M", "Maybe we should have a simple sign that shows the three main products instead of a lot of small posters."),
            ("W", "That makes sense. If people can see the key items right away, they may decide to stop and ask questions."),
            ("M", "Right. And we could prepare a short handout so they remember us after walking around the hall.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem did they have at last year’s event?",
                "choices": {
                    "A": "Visitors left before speaking with them.",
                    "B": "The booth was in the wrong building.",
                    "C": "The company name was printed incorrectly.",
                    "D": "Their products were not allowed inside."
                },
                "answer": "A",
                "rationale": "The woman says many visitors left before talking to them."
            },
            {
                "stem": "(audio) What change does the man suggest for the booth?",
                "choices": {
                    "A": "Using a simple sign with only three main products.",
                    "B": "Playing loud music to attract more attention.",
                    "C": "Hiring actors to demonstrate the products.",
                    "D": "Covering the walls with many small posters."
                },
                "answer": "A",
                "rationale": "He says they should have a simple sign with three main products instead of many posters."
            },
            {
                "stem": "(audio) Why do they want to prepare a handout?",
                "choices": {
                    "A": "So visitors remember their booth after walking around.",
                    "B": "So they can collect visitors’ contact numbers.",
                    "C": "So other booths can advertise on it.",
                    "D": "So staff can avoid explaining products."
                },
                "answer": "A",
                "rationale": "The man explains that a handout will help visitors remember them later."
            }
        ]
    },

    # 4. ビジネス：新人研修の内容
    {
        "level": "B2",
        "topic": ["training", "new employee", "orientation"],
        "dialog": [
            ("M", "The new hires said yesterday’s training felt a bit too theoretical."),
            ("W", "Then we should add more simple examples and maybe a short role-play, especially for the customer-service part."),
            ("M", "That’s true. If they can practice typical questions, they’ll be more confident on their first day."),
            ("W", "I can rewrite the materials this afternoon, and you could check if the schedule still fits.")
        ],
        "questions": [
            {
                "stem": "(audio) What did the new employees say about the training?",
                "choices": {
                    "A": "It was too theoretical.",
                    "B": "It was too short.",
                    "C": "It was too noisy.",
                    "D": "It was too expensive."
                },
                "answer": "A",
                "rationale": "The man says they felt the training was too theoretical."
            },
            {
                "stem": "(audio) What does the woman want to add?",
                "choices": {
                    "A": "More simple examples and a short role-play.",
                    "B": "Extra reading homework after work.",
                    "C": "A written test for every session.",
                    "D": "A second instructor from outside."
                },
                "answer": "A",
                "rationale": "She suggests more examples and a role-play, especially for customer-service situations."
            },
            {
                "stem": "(audio) What will the man do?",
                "choices": {
                    "A": "Check whether the schedule still works.",
                    "B": "Interview all the new employees again.",
                    "C": "Cancel the customer-service lesson.",
                    "D": "Move the training to another building."
                },
                "answer": "A",
                "rationale": "She asks him to check if the schedule can include the new activities."
            }
        ]
    },

    # 5. ビジネス：シフトの調整
    {
        "level": "B2",
        "topic": ["schedule", "shift", "adjustment"],
        "dialog": [
            ("W", "Two staff members asked for Friday afternoon off, but we still need someone at the service counter."),
            ("M", "If we move Ken’s shift from the morning to the afternoon, he could cover that time."),
            ("W", "That could work, but he already worked late this week. We don’t want to overwork him."),
            ("M", "Then maybe we should offer him another day off next week so it feels fair.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman’s concern about Friday?",
                "choices": {
                    "A": "There may not be enough staff in the afternoon.",
                    "B": "Too many customers made reservations.",
                    "C": "The store might close earlier than usual.",
                    "D": "The service counter equipment is broken."
                },
                "answer": "A",
                "rationale": "She says two staff requested time off but they still need someone at the counter."
            },
            {
                "stem": "(audio) What does the man suggest doing with Ken’s shift?",
                "choices": {
                    "A": "Moving it from morning to afternoon.",
                    "B": "Canceling it entirely.",
                    "C": "Asking him to work on Saturday instead.",
                    "D": "Sending him to another branch."
                },
                "answer": "A",
                "rationale": "He suggests moving Ken’s shift so he can cover the afternoon."
            },
            {
                "stem": "(audio) How do they plan to treat Ken fairly?",
                "choices": {
                    "A": "By giving him another day off next week.",
                    "B": "By giving him extra cash immediately.",
                    "C": "By asking him to refuse other requests.",
                    "D": "By reducing his lunch breaks."
                },
                "answer": "A",
                "rationale": "They talk about offering him another day off so the schedule change feels fair."
            }
        ]
    },

    # 6. ビジネス：メールの書き方
    {
        "level": "B2",
        "topic": ["email", "communication", "business writing"],
        "dialog": [
            ("M", "I wrote a message to the supplier about the delay, but it sounds a bit too direct."),
            ("W", "Maybe you could start by thanking them for their support and then explain the problem more gently."),
            ("M", "You’re right. If I show appreciation first, they might be more willing to help."),
            ("W", "Exactly. And you could end by suggesting a new delivery date, instead of only complaining.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man feel about his message?",
                "choices": {
                    "A": "It sounds too direct.",
                    "B": "It is too long.",
                    "C": "It has many spelling mistakes.",
                    "D": "It is difficult to understand."
                },
                "answer": "A",
                "rationale": "He says the message sounds too direct."
            },
            {
                "stem": "(audio) What does the woman suggest he do at the beginning?",
                "choices": {
                    "A": "Thank the supplier before discussing the problem.",
                    "B": "Write in a different language.",
                    "C": "Attach more documents to the e-mail.",
                    "D": "Ask his manager to sign the message."
                },
                "answer": "A",
                "rationale": "She advises starting with appreciation and then explaining the issue more gently."
            },
            {
                "stem": "(audio) What should he include at the end of the message?",
                "choices": {
                    "A": "A suggestion for a new delivery date.",
                    "B": "A list of all previous orders.",
                    "C": "A note saying they will change suppliers.",
                    "D": "A request for a personal meeting overseas."
                },
                "answer": "A",
                "rationale": "She recommends ending with a suggestion instead of only complaining."
            }
        ]
    },

    # 7. ビジネス：プロジェクトの優先順位
    {
        "level": "B2",
        "topic": ["project", "priority", "management"],
        "dialog": [
            ("W", "We have three projects starting this month, and the team already feels overloaded."),
            ("M", "If we delay the internal training project by two weeks, we can focus on the client work first."),
            ("W", "That might help. The training is important, but it doesn’t have a strict deadline."),
            ("M", "Let’s talk to HR so they know why the schedule is changing and can inform the trainers.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the main issue the speakers are facing?",
                "choices": {
                    "A": "They have too many projects at the same time.",
                    "B": "They cannot find enough meeting rooms.",
                    "C": "They lost an important client last month.",
                    "D": "They need to hire new staff immediately."
                },
                "answer": "A",
                "rationale": "The woman says the team feels overloaded because three projects start this month."
            },
            {
                "stem": "(audio) Which project do they want to delay?",
                "choices": {
                    "A": "The internal training project.",
                    "B": "The new client’s main project.",
                    "C": "The office renovation project.",
                    "D": "The marketing campaign at the mall."
                },
                "answer": "A",
                "rationale": "The man suggests delaying the internal training by two weeks."
            },
            {
                "stem": "(audio) Who do they plan to inform about the schedule change?",
                "choices": {
                    "A": "The human resources department.",
                    "B": "The building manager.",
                    "C": "The delivery company.",
                    "D": "The local government office."
                },
                "answer": "A",
                "rationale": "They say they will talk to HR so the trainers can be informed."
            }
        ]
    },

    # 8. ビジネス：顧客クレームへの対応
    {
        "level": "B2",
        "topic": ["customer service", "complaint", "solution"],
        "dialog": [
            ("M", "The customer said the replacement product also arrived damaged."),
            ("W", "Then we should apologize again and offer a refund, not just another replacement."),
            ("M", "I agree. If we show that we take it seriously, they may decide to keep buying from us."),
            ("W", "I’ll call them this afternoon and follow up with an e-mail so everything is clear.")
        ],
        "questions": [
            {
                "stem": "(audio) What happened with the replacement product?",
                "choices": {
                    "A": "It arrived damaged again.",
                    "B": "It was sent to the wrong address.",
                    "C": "It was more expensive than expected.",
                    "D": "It arrived one week early."
                },
                "answer": "A",
                "rationale": "The man says the replacement also arrived damaged."
            },
            {
                "stem": "(audio) What does the woman think they should offer now?",
                "choices": {
                    "A": "A refund instead of another replacement.",
                    "B": "A discount on future advertising.",
                    "C": "Free training for the customer’s staff.",
                    "D": "A visit from the company president."
                },
                "answer": "A",
                "rationale": "She says they should apologize again and offer a refund."
            },
            {
                "stem": "(audio) What will the woman do in the afternoon?",
                "choices": {
                    "A": "Call the customer and then send an e-mail.",
                    "B": "Visit the customer’s office in person.",
                    "C": "Meet with the delivery driver.",
                    "D": "Check the warehouse inventory."
                },
                "answer": "A",
                "rationale": "She plans to call and follow up with an e-mail."
            }
        ]
    },

    # 9. ビジネス：出張費の相談
    {
        "level": "B2",
        "topic": ["business trip", "budget", "expense"],
        "dialog": [
            ("W", "The budget for the business trip is tight, and hotel prices have gone up."),
            ("M", "If we stay a little farther from the city center, we can find cheaper rooms."),
            ("W", "That’s true, but then we’ll spend more time commuting to the meetings."),
            ("M", "Maybe we should compare the total cost, including transport, before we decide.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem do they have with the business trip?",
                "choices": {
                    "A": "The hotel prices are high.",
                    "B": "The meeting rooms are too small.",
                    "C": "The flights are all fully booked.",
                    "D": "The schedule is not confirmed."
                },
                "answer": "A",
                "rationale": "The woman mentions that hotel prices have gone up."
            },
            {
                "stem": "(audio) What does the man suggest to save money?",
                "choices": {
                    "A": "Staying farther from the city center.",
                    "B": "Canceling one of the meetings.",
                    "C": "Reducing the number of participants.",
                    "D": "Bringing their own food."
                },
                "answer": "A",
                "rationale": "He suggests staying in a cheaper area away from the center."
            },
            {
                "stem": "(audio) What do they decide to compare?",
                "choices": {
                    "A": "The total cost, including transport.",
                    "B": "The size of different hotel rooms.",
                    "C": "The quality of restaurant menus.",
                    "D": "The design of conference badges."
                },
                "answer": "A",
                "rationale": "They decide to compare the full cost before choosing."
            }
        ]
    },

    # 10. ビジネス：プレゼン資料の分担
    {
        "level": "B2",
        "topic": ["presentation", "teamwork", "division of work"],
        "dialog": [
            ("M", "The presentation is in three days, and I’m still working on the market research slides."),
            ("W", "If you focus on the data part, I can prepare the introduction and the conclusion."),
            ("M", "That would really help. Could you also check that the design looks consistent across all slides?"),
            ("W", "Sure. Once I finish my sections, I’ll adjust the layout so everything feels like one story.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the man worried about?",
                "choices": {
                    "A": "He may not finish the market research slides in time.",
                    "B": "He forgot to book the meeting room.",
                    "C": "He lost the client’s contact information.",
                    "D": "He doesn’t know the presentation topic."
                },
                "answer": "A",
                "rationale": "He says the presentation is soon and he is still working on those slides."
            },
            {
                "stem": "(audio) What will the woman prepare?",
                "choices": {
                    "A": "The introduction and the conclusion.",
                    "B": "Only the budget details.",
                    "C": "The technical manual.",
                    "D": "The video equipment."
                },
                "answer": "A",
                "rationale": "She offers to handle the beginning and ending parts."
            },
            {
                "stem": "(audio) What additional task will she do?",
                "choices": {
                    "A": "Make the slide design consistent.",
                    "B": "Print all materials in color.",
                    "C": "Invite more people to the meeting.",
                    "D": "Change the time of the presentation."
                },
                "answer": "A",
                "rationale": "She says she’ll adjust the layout so everything feels unified."
            }
        ]
    },

    # 11. 生活：家族の予定調整
    {
        "level": "B2",
        "topic": ["family", "schedule", "weekend"],
        "dialog": [
            ("W", "This weekend we promised to visit your parents, but our son also has a soccer match on Sunday morning."),
            ("M", "If we drive there on Saturday and stay overnight, we can watch his game and still have lunch with my parents."),
            ("W", "That sounds possible, as long as we leave early enough on Saturday."),
            ("M", "I’ll check the traffic report and book a small hotel near the stadium.")
        ],
        "questions": [
            {
                "stem": "(audio) What is making their weekend schedule complicated?",
                "choices": {
                    "A": "They need to visit family and attend a soccer match.",
                    "B": "They must travel overseas for work.",
                    "C": "They are moving to a new house.",
                    "D": "They forgot about a birthday party."
                },
                "answer": "A",
                "rationale": "They promised to visit his parents, but their son has a game."
            },
            {
                "stem": "(audio) What plan do they consider?",
                "choices": {
                    "A": "Driving on Saturday and staying overnight.",
                    "B": "Canceling the visit to the parents.",
                    "C": "Skipping the soccer match entirely.",
                    "D": "Sending the son alone by train."
                },
                "answer": "A",
                "rationale": "The man suggests traveling on Saturday and staying in a hotel."
            },
            {
                "stem": "(audio) What will the man check?",
                "choices": {
                    "A": "The traffic report and hotel options.",
                    "B": "The price of new sports shoes.",
                    "C": "The weather for next weekend only.",
                    "D": "The opening hours of the museum."
                },
                "answer": "A",
                "rationale": "He says he’ll check traffic and book a hotel near the stadium."
            }
        ]
    },

    # 12. 生活：アパートの騒音問題
    {
        "level": "B2",
        "topic": ["apartment", "noise", "neighbor"],
        "dialog": [
            ("M", "The neighbors upstairs play music late at night again. I couldn’t sleep well yesterday."),
            ("W", "Maybe we should talk to them politely first before calling the building manager."),
            ("M", "You’re right. If we explain how it affects us, they might turn it down."),
            ("W", "Let’s visit them this evening when they get home from work.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem does the man mention?",
                "choices": {
                    "A": "Loud music from the neighbors at night.",
                    "B": "Water leaking from the ceiling.",
                    "C": "Trash left in the hallway.",
                    "D": "A broken lock on the entrance."
                },
                "answer": "A",
                "rationale": "He says the neighbors play music late at night."
            },
            {
                "stem": "(audio) What is the woman’s first suggestion?",
                "choices": {
                    "A": "Talk to the neighbors politely.",
                    "B": "Move to another building.",
                    "C": "Write a letter to the city office.",
                    "D": "Turn on their own music loudly."
                },
                "answer": "A",
                "rationale": "She suggests speaking politely before involving the manager."
            },
            {
                "stem": "(audio) When will they try to speak with the neighbors?",
                "choices": {
                    "A": "In the evening after work.",
                    "B": "Very early in the morning.",
                    "C": "During the lunch break.",
                    "D": "Late on Sunday night."
                },
                "answer": "A",
                "rationale": "She says they should visit them this evening."
            }
        ]
    },

    # 13. 生活：語学学校選び
    {
        "level": "B2",
        "topic": ["language school", "decision", "course"],
        "dialog": [
            ("W", "I want to improve my English, but I’m not sure which language school to choose."),
            ("M", "If you prefer small classes, that school near the station might be better, even though it’s more expensive."),
            ("W", "True. A small group could give me more chances to speak."),
            ("M", "You should also check if the lessons fit your work schedule before you sign up.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman trying to decide?",
                "choices": {
                    "A": "Which language school to attend.",
                    "B": "Which city to move to.",
                    "C": "Which sport to take up.",
                    "D": "Which computer to buy."
                },
                "answer": "A",
                "rationale": "She says she wants to improve English but doesn’t know which school to pick."
            },
            {
                "stem": "(audio) What advantage does the man mention about the school near the station?",
                "choices": {
                    "A": "It has small classes.",
                    "B": "It is the cheapest choice.",
                    "C": "It offers free textbooks.",
                    "D": "It is open twenty-four hours."
                },
                "answer": "A",
                "rationale": "He says that school might be better if she prefers small classes."
            },
            {
                "stem": "(audio) What does the man suggest checking before she joins?",
                "choices": {
                    "A": "Whether the lesson times match her work schedule.",
                    "B": "If her friends are studying there too.",
                    "C": "How many students are in every course.",
                    "D": "Whether the building has a parking lot."
                },
                "answer": "A",
                "rationale": "He advises her to confirm the lesson schedule works with her job."
            }
        ]
    },

    # 14. 生活：健康診断の予約
    {
        "level": "B2",
        "topic": ["health check", "appointment", "planning"],
        "dialog": [
            ("M", "My doctor told me to get a full health check, but the clinic is always busy."),
            ("W", "If you go on a weekday morning, it might be less crowded than on Saturdays."),
            ("M", "That could work, but I’ll have to ask my manager for half a day off."),
            ("W", "It’s better to do it soon rather than wait until you feel unwell.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the man need to do?",
                "choices": {
                    "A": "Get a full health check.",
                    "B": "Change his doctor.",
                    "C": "Find a new apartment.",
                    "D": "Attend a training session."
                },
                "answer": "A",
                "rationale": "He says his doctor told him to get a full check."
            },
            {
                "stem": "(audio) When does the woman think the clinic is less crowded?",
                "choices": {
                    "A": "On weekday mornings.",
                    "B": "On holiday evenings.",
                    "C": "At lunchtime on Fridays.",
                    "D": "Late at night."
                },
                "answer": "A",
                "rationale": "She suggests going on a weekday morning."
            },
            {
                "stem": "(audio) What does the man need to ask his manager for?",
                "choices": {
                    "A": "Half a day off.",
                    "B": "Permission to work from home.",
                    "C": "Extra overtime pay.",
                    "D": "A new project assignment."
                },
                "answer": "A",
                "rationale": "He mentions needing half a day off from work."
            }
        ]
    },

    # 15. 生活：家計の見直し
    {
        "level": "B2",
        "topic": ["budget", "household", "expenses"],
        "dialog": [
            ("W", "Our utility bills have been higher these past few months."),
            ("M", "If we start turning off the heater when we leave a room, we might cut them a little."),
            ("W", "And we could compare different internet plans to see if there’s a cheaper option."),
            ("M", "Good idea. Let’s list all our regular payments and decide which ones we can reduce.")
        ],
        "questions": [
            {
                "stem": "(audio) What has increased recently?",
                "choices": {
                    "A": "Their utility bills.",
                    "B": "Their rent payment.",
                    "C": "Their car insurance.",
                    "D": "Their travel expenses."
                },
                "answer": "A",
                "rationale": "The woman says the utility bills have been higher."
            },
            {
                "stem": "(audio) What daily habit does the man want to change?",
                "choices": {
                    "A": "Turning off the heater when leaving a room.",
                    "B": "Eating out several times a week.",
                    "C": "Buying coffee on the way to work.",
                    "D": "Using the car for short trips."
                },
                "answer": "A",
                "rationale": "He suggests turning off the heater to reduce costs."
            },
            {
                "stem": "(audio) What do they plan to do with their regular payments?",
                "choices": {
                    "A": "List them and see which can be reduced.",
                    "B": "Pay all of them one year in advance.",
                    "C": "Stop paying them for a month.",
                    "D": "Ask friends to share the bills."
                },
                "answer": "A",
                "rationale": "They decide to list all payments and check what can be lowered."
            }
        ]
    },

    # 16. 生活：旅行のキャンセル
    {
        "level": "B2",
        "topic": ["trip", "cancellation", "refund"],
        "dialog": [
            ("M", "My sister got sick, so we might have to cancel our weekend trip."),
            ("W", "You should check the hotel’s policy. Some places let you change the dates instead of canceling."),
            ("M", "That would be better than losing the money completely."),
            ("W", "If you call them today, they might still be flexible about it.")
        ],
        "questions": [
            {
                "stem": "(audio) Why might the man cancel the trip?",
                "choices": {
                    "A": "His sister is sick.",
                    "B": "The hotel is under repair.",
                    "C": "The weather is very bad.",
                    "D": "The train tickets were lost."
                },
                "answer": "A",
                "rationale": "He says his sister got sick."
            },
            {
                "stem": "(audio) What does the woman suggest checking?",
                "choices": {
                    "A": "The hotel’s policy on changes.",
                    "B": "The weather forecast for next month.",
                    "C": "The local bus routes near the beach.",
                    "D": "The museum opening hours."
                },
                "answer": "A",
                "rationale": "She tells him to check whether the hotel allows changing dates."
            },
            {
                "stem": "(audio) What advantage does the woman see in changing the dates?",
                "choices": {
                    "A": "He wouldn’t lose all the money.",
                    "B": "He could invite more people.",
                    "C": "He would get a free breakfast.",
                    "D": "He could stay for an extra day."
                },
                "answer": "A",
                "rationale": "She mentions it is better than losing the money fully."
            }
        ]
    },

    # 17. 生活：ペットの世話
    {
        "level": "B2",
        "topic": ["pet", "care", "neighbor"],
        "dialog": [
            ("W", "We’ll be away next week, and I’m worried about who will take care of our cat."),
            ("M", "If we ask our neighbor, he might be willing to feed her and check on her once a day."),
            ("W", "He likes animals, so that could work, but we should write down clear instructions."),
            ("M", "I’ll prepare a short note with feeding times and the vet’s phone number just in case.")
        ],
        "questions": [
            {
                "stem": "(audio) Why is the woman worried?",
                "choices": {
                    "A": "They need someone to care for their cat.",
                    "B": "They cannot find their passport.",
                    "C": "They have not packed their clothes.",
                    "D": "They lost the house keys."
                },
                "answer": "A",
                "rationale": "She is concerned about who will take care of the cat while they’re away."
            },
            {
                "stem": "(audio) What does the man say about the neighbor?",
                "choices": {
                    "A": "He might agree to feed the cat.",
                    "B": "He is allergic to animals.",
                    "C": "He is leaving town tomorrow.",
                    "D": "He has never met the cat."
                },
                "answer": "A",
                "rationale": "He suggests asking the neighbor to feed the cat daily."
            },
            {
                "stem": "(audio) What will the man write in the note?",
                "choices": {
                    "A": "Feeding times and the vet’s contact.",
                    "B": "Directions to the train station.",
                    "C": "A list of favorite movies.",
                    "D": "The neighbor’s phone number."
                },
                "answer": "A",
                "rationale": "He says he’ll include feeding times and the veterinarian’s phone number."
            }
        ]
    },

    # 18. 生活：共有スペースの掃除当番
    {
        "level": "B2",
        "topic": ["shared house", "cleaning", "responsibility"],
        "dialog": [
            ("M", "The kitchen is getting messy again, and nobody seems to remember the cleaning schedule."),
            ("W", "Maybe we should put a simple calendar on the fridge and write the names for each week."),
            ("M", "That way, it’s easier to see who hasn’t done their turn yet."),
            ("W", "I’ll draw the calendar tonight, and we can talk about it at dinner.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem do they have in the kitchen?",
                "choices": {
                    "A": "It has become messy again.",
                    "B": "The stove is broken.",
                    "C": "The refrigerator is leaking.",
                    "D": "The dishes are missing."
                },
                "answer": "A",
                "rationale": "The man says the kitchen is getting messy."
            },
            {
                "stem": "(audio) What does the woman suggest putting on the fridge?",
                "choices": {
                    "A": "A calendar with names for each week.",
                    "B": "A list of new recipes.",
                    "C": "Pictures from their last trip.",
                    "D": "A map of the neighborhood."
                },
                "answer": "A",
                "rationale": "She suggests a calendar to show who cleans when."
            },
            {
                "stem": "(audio) When will they discuss the new system?",
                "choices": {
                    "A": "At dinner.",
                    "B": "Next month.",
                    "C": "After the landlord visits.",
                    "D": "Before going to work."
                },
                "answer": "A",
                "rationale": "She says they can talk about it at dinner."
            }
        ]
    },

    # 19. 生活：オンラインレッスンの続け方
    {
        "level": "B2",
        "topic": ["online lesson", "motivation", "plan"],
        "dialog": [
            ("W", "I started an online exercise class, but I keep skipping it when I’m tired after work."),
            ("M", "Maybe you should choose shorter lessons and set a reminder so you don’t forget."),
            ("W", "That might make it easier to continue, especially on busy days."),
            ("M", "You could also ask a friend to join, so you encourage each other.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem does the woman have with her class?",
                "choices": {
                    "A": "She often skips the online exercise lessons.",
                    "B": "She cannot connect to the internet.",
                    "C": "She thinks the lessons are too easy.",
                    "D": "She does not like the instructor’s voice."
                },
                "answer": "A",
                "rationale": "She says she keeps skipping the class when she’s tired."
            },
            {
                "stem": "(audio) What suggestion does the man make about lesson length?",
                "choices": {
                    "A": "Choose shorter lessons.",
                    "B": "Take only weekend lessons.",
                    "C": "Stop the class completely.",
                    "D": "Switch to a different language course."
                },
                "answer": "A",
                "rationale": "He recommends shorter lessons, along with a reminder."
            },
            {
                "stem": "(audio) Why does he suggest inviting a friend?",
                "choices": {
                    "A": "So they can motivate each other to continue.",
                    "B": "So the class becomes cheaper per person.",
                    "C": "So the teacher cannot cancel easily.",
                    "D": "So they can record the lessons together."
                },
                "answer": "A",
                "rationale": "He says they can encourage each other if they join together."
            }
        ]
    },

    # 20. 生活：中古家具の購入
    {
        "level": "B2",
        "topic": ["furniture", "second-hand", "decision"],
        "dialog": [
            ("M", "I found a used sofa online that looks nice, but the seller lives in another city."),
            ("W", "If the price includes delivery, it might still be a good deal."),
            ("M", "True, but I want to see it in person before I decide."),
            ("W", "Then you could ask the seller for more photos and details about any damage.")
        ],
        "questions": [
            {
                "stem": "(audio) What item is the man considering buying?",
                "choices": {
                    "A": "A used sofa.",
                    "B": "A new computer.",
                    "C": "A dining table.",
                    "D": "A bicycle."
                },
                "answer": "A",
                "rationale": "He says he found a used sofa online."
            },
            {
                "stem": "(audio) What concern does he have about the seller?",
                "choices": {
                    "A": "The seller is in another city.",
                    "B": "The seller does not answer messages.",
                    "C": "The seller does not accept cash.",
                    "D": "The seller has no reviews."
                },
                "answer": "A",
                "rationale": "The distance makes it harder to see the sofa."
            },
            {
                "stem": "(audio) What does the woman suggest he ask for?",
                "choices": {
                    "A": "More photos and information about damage.",
                    "B": "Free storage for a few months.",
                    "C": "A discount on a second sofa.",
                    "D": "A chance to try the sofa for a week."
                },
                "answer": "A",
                "rationale": "She advises him to request extra photos and details."
            }
        ]
    },

    # 21. 生活：図書館の利用
    {
        "level": "B2",
        "topic": ["library", "membership", "rules"],
        "dialog": [
            ("W", "I want to use the library more, but I’m not sure how long I can keep the books."),
            ("M", "With a regular card, you can borrow them for two weeks, and you can extend once online."),
            ("W", "That’s convenient. What happens if I return them late?"),
            ("M", "You pay a small fee, so it’s better to set a reminder before the due date.")
        ],
        "questions": [
            {
                "stem": "(audio) What information is the woman asking about?",
                "choices": {
                    "A": "How long she can keep library books.",
                    "B": "How to print documents cheaply.",
                    "C": "How to reserve a study room.",
                    "D": "How to pay for a new card."
                },
                "answer": "A",
                "rationale": "She wants to know the borrowing period."
            },
            {
                "stem": "(audio) What is possible with a regular card?",
                "choices": {
                    "A": "Borrowing books for two weeks and extending once.",
                    "B": "Keeping books for three months.",
                    "C": "Borrowing unlimited e-books only.",
                    "D": "Using the library late at night."
                },
                "answer": "A",
                "rationale": "The man explains the two-week period and one online extension."
            },
            {
                "stem": "(audio) What happens if books are returned late?",
                "choices": {
                    "A": "A small fee is charged.",
                    "B": "Membership is canceled.",
                    "C": "The books are lost.",
                    "D": "The user must buy new shelves."
                },
                "answer": "A",
                "rationale": "He says there is a small fee, so it’s better to set a reminder."
            }
        ]
    },

    # 22. 生活：ボランティア活動
    {
        "level": "B2",
        "topic": ["volunteer", "community", "event"],
        "dialog": [
            ("M", "Our neighborhood is planning a cleanup day, but I’m not sure how I can help."),
            ("W", "If you’re free in the morning, you could collect trash in the park, and I’ll work near the river."),
            ("M", "That sounds fair. We should also ask the city office for extra garbage bags."),
            ("W", "I’ll send them an e-mail, and we can post the details on the community board.")
        ],
        "questions": [
            {
                "stem": "(audio) What event are they talking about?",
                "choices": {
                    "A": "A neighborhood cleanup day.",
                    "B": "A local sports competition.",
                    "C": "A fundraising concert.",
                    "D": "A school festival."
                },
                "answer": "A",
                "rationale": "They mention a cleanup day in their neighborhood."
            },
            {
                "stem": "(audio) Where will the man help?",
                "choices": {
                    "A": "Collecting trash in the park.",
                    "B": "Working inside the library.",
                    "C": "Selling drinks at a booth.",
                    "D": "Checking tickets at the gate."
                },
                "answer": "A",
                "rationale": "He agrees to work in the park while she works near the river."
            },
            {
                "stem": "(audio) Who will the woman contact?",
                "choices": {
                    "A": "The city office.",
                    "B": "Her old classmates.",
                    "C": "The local supermarket.",
                    "D": "A travel agency."
                },
                "answer": "A",
                "rationale": "She says she will e-mail the city office to ask for bags."
            }
        ]
    },

    # 23. 生活：中古車の試乗
    {
        "level": "B2",
        "topic": ["used car", "test drive", "purchase decision"],
        "dialog": [
            ("W", "The used car we saw online looks good, but I’m worried about the mileage."),
            ("M", "If the owner kept good maintenance records, the mileage might not be a big problem."),
            ("W", "I’d like to see those records and maybe take a test drive this weekend."),
            ("M", "Let’s contact the owner and ask if we can meet on Saturday morning.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the woman worried about?",
                "choices": {
                    "A": "The mileage of the used car.",
                    "B": "The color of the car seats.",
                    "C": "The size of the parking space.",
                    "D": "The cost of car insurance."
                },
                "answer": "A",
                "rationale": "She says she is worried about the mileage."
            },
            {
                "stem": "(audio) What does the man say might reduce that worry?",
                "choices": {
                    "A": "Good maintenance records from the owner.",
                    "B": "A brand-new set of tires.",
                    "C": "A free navigation system.",
                    "D": "A detailed car-wash report."
                },
                "answer": "A",
                "rationale": "He mentions that good maintenance could make mileage less concerning."
            },
            {
                "stem": "(audio) What do they plan to ask the owner?",
                "choices": {
                    "A": "If they can meet for a test drive on Saturday.",
                    "B": "If the car can be painted a different color.",
                    "C": "If the car can be shipped overseas.",
                    "D": "If the car can be kept at the dealership."
                },
                "answer": "A",
                "rationale": "They want to meet the owner for a test drive on the weekend."
            }
        ]
    },

    # 24. 生活：オンライン注文の配達時間
    {
        "level": "B2",
        "topic": ["online shopping", "delivery", "time window"],
        "dialog": [
            ("M", "The furniture delivery company said they would come sometime between nine and one."),
            ("W", "That’s a long time window. If we choose the morning slot, one of us has to stay home."),
            ("M", "I can work from home that day, but we should ask them to call when they are on the way."),
            ("W", "Good idea. That way, you can plan your online meetings more easily.")
        ],
        "questions": [
            {
                "stem": "(audio) What is the problem with the delivery schedule?",
                "choices": {
                    "A": "The time window is very long.",
                    "B": "The company only delivers at night.",
                    "C": "They charge extra for weekends.",
                    "D": "They do not deliver furniture."
                },
                "answer": "A",
                "rationale": "The delivery is scheduled between nine and one, which is a long period."
            },
            {
                "stem": "(audio) What can the man do to solve part of the problem?",
                "choices": {
                    "A": "Work from home that day.",
                    "B": "Cancel all his meetings.",
                    "C": "Refuse the furniture delivery.",
                    "D": "Move to a different apartment."
                },
                "answer": "A",
                "rationale": "He says he can work from home on that day."
            },
            {
                "stem": "(audio) Why do they want the company to call before arriving?",
                "choices": {
                    "A": "So he can arrange his online meetings around it.",
                    "B": "So they can cancel the order faster.",
                    "C": "So the neighbors know they are coming.",
                    "D": "So they can take pictures of the truck."
                },
                "answer": "A",
                "rationale": "A call would help him plan his meetings more easily."
            }
        ]
    },

    # 25. 生活：スマホの機種変更
    {
        "level": "B2",
        "topic": ["smartphone", "upgrade", "decision"],
        "dialog": [
            ("W", "My phone battery dies so quickly now, but a new model is expensive."),
            ("M", "If you only need a better battery, you might choose last year’s model instead of the newest one."),
            ("W", "That could save money, as long as the camera is still decent."),
            ("M", "Let’s compare the features online before you decide.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem does the woman have with her phone?",
                "choices": {
                    "A": "The battery runs out quickly.",
                    "B": "The screen is cracked.",
                    "C": "The speaker is broken.",
                    "D": "The charger is missing."
                },
                "answer": "A",
                "rationale": "She says the battery dies quickly."
            },
            {
                "stem": "(audio) What option does the man suggest?",
                "choices": {
                    "A": "Buying last year’s model.",
                    "B": "Not using a smartphone at all.",
                    "C": "Leasing a phone from her company.",
                    "D": "Waiting five years to upgrade."
                },
                "answer": "A",
                "rationale": "He suggests choosing last year’s model instead of the newest."
            },
            {
                "stem": "(audio) What will they do before she makes a decision?",
                "choices": {
                    "A": "Compare the phone features online.",
                    "B": "Visit several phone repair shops.",
                    "C": "Ask her manager to pay for it.",
                    "D": "Send her old phone to a friend."
                },
                "answer": "A",
                "rationale": "They agree to compare features online first."
            }
        ]
    },

    # 26. 生活：ジムの会員プラン
    {
        "level": "B2",
        "topic": ["gym", "membership", "plan"],
        "dialog": [
            ("M", "The gym near our house offers a cheaper plan if we go only on weekdays."),
            ("W", "That might work for you, but I usually have time only on Saturday mornings."),
            ("M", "Then maybe we should choose the regular plan, so we’re not limited."),
            ("W", "Let’s calculate how often we really go before we sign anything.")
        ],
        "questions": [
            {
                "stem": "(audio) What does the gym offer?",
                "choices": {
                    "A": "A cheaper plan for weekday use.",
                    "B": "Free membership for one month.",
                    "C": "A family plan at no cost.",
                    "D": "Personal trainers every day."
                },
                "answer": "A",
                "rationale": "The man mentions a cheaper weekday-only plan."
            },
            {
                "stem": "(audio) Why might the woman not benefit from that plan?",
                "choices": {
                    "A": "She usually has time only on Saturdays.",
                    "B": "She dislikes exercising indoors.",
                    "C": "She already belongs to another gym.",
                    "D": "She never exercises in the morning."
                },
                "answer": "A",
                "rationale": "She says she usually goes on Saturday mornings."
            },
            {
                "stem": "(audio) What do they decide to do before choosing a plan?",
                "choices": {
                    "A": "Check how often they actually go to the gym.",
                    "B": "Visit every gym in the city.",
                    "C": "Ask their friends for money.",
                    "D": "Buy new sports clothes together."
                },
                "answer": "A",
                "rationale": "They want to calculate their real usage before signing."
            }
        ]
    },

    # 27. 生活：オンライン英会話の講師変更
    {
        "level": "B2",
        "topic": ["online English", "teacher change", "learning"],
        "dialog": [
            ("W", "My online English teacher speaks very fast, and I can’t catch everything."),
            ("M", "You could ask her to slow down, but you might also try another teacher whose level matches yours better."),
            ("W", "I feel a bit nervous about changing, but it might help my confidence."),
            ("M", "It’s your course, so it’s fine to find a style that works for you.")
        ],
        "questions": [
            {
                "stem": "(audio) What difficulty does the woman have in her lessons?",
                "choices": {
                    "A": "Her teacher speaks too fast.",
                    "B": "Her internet is too slow.",
                    "C": "Her microphone doesn’t work.",
                    "D": "Her lessons are too short."
                },
                "answer": "A",
                "rationale": "She says she can’t catch everything because the teacher speaks quickly."
            },
            {
                "stem": "(audio) What option does the man suggest besides asking the teacher to slow down?",
                "choices": {
                    "A": "Trying another teacher whose level suits her.",
                    "B": "Quitting the course completely.",
                    "C": "Switching to a different language.",
                    "D": "Only taking lessons once a month."
                },
                "answer": "A",
                "rationale": "He recommends looking for a teacher whose level matches hers."
            },
            {
                "stem": "(audio) How does the man encourage her?",
                "choices": {
                    "A": "He says it’s her course, so she can choose what suits her.",
                    "B": "He tells her to stop studying entirely.",
                    "C": "He says she should never ask questions.",
                    "D": "He insists she stay with the same teacher."
                },
                "answer": "A",
                "rationale": "He reminds her that the course should fit her needs."
            }
        ]
    },

    # 28. 生活：友人とのカフェの待ち合わせ
    {
        "level": "B2",
        "topic": ["meeting friend", "cafe", "delay"],
        "dialog": [
            ("M", "I’m going to be about fifteen minutes late to the café. The train stopped for a while."),
            ("W", "No problem. I’ll order a drink and find a table near the window."),
            ("M", "Thanks. If they ask about the food order, can you tell them we’ll decide after I arrive?"),
            ("W", "Sure. I’ll let the staff know we’re waiting for one more person.")
        ],
        "questions": [
            {
                "stem": "(audio) Why will the man be late?",
                "choices": {
                    "A": "The train stopped unexpectedly.",
                    "B": "He missed the bus completely.",
                    "C": "He went to the wrong station.",
                    "D": "He forgot his wallet at home."
                },
                "answer": "A",
                "rationale": "He explains that the train stopped for a while."
            },
            {
                "stem": "(audio) What does the woman plan to do while waiting?",
                "choices": {
                    "A": "Order a drink and choose a table.",
                    "B": "Go shopping at the mall.",
                    "C": "Leave the café and go home.",
                    "D": "Cancel their reservation."
                },
                "answer": "A",
                "rationale": "She says she will order a drink and find a table."
            },
            {
                "stem": "(audio) What does the man ask her to tell the staff?",
                "choices": {
                    "A": "That they will decide on the food after he arrives.",
                    "B": "That they want to change tables.",
                    "C": "That they need the bill immediately.",
                    "D": "That they want to reserve the whole room."
                },
                "answer": "A",
                "rationale": "He asks her to tell the staff they’ll order food later."
            }
        ]
    },

    # 29. 生活：引っ越しの日程調整
    {
        "level": "B2",
        "topic": ["moving", "schedule", "friends help"],
        "dialog": [
            ("W", "The moving company is free next Saturday, but most of our friends can help only on Sunday."),
            ("M", "If we move the big furniture with the company on Saturday, our friends can help with boxes the next day."),
            ("W", "That could reduce the cost and still make it manageable."),
            ("M", "I’ll call the company to confirm Saturday, and we can message our friends about Sunday.")
        ],
        "questions": [
            {
                "stem": "(audio) What problem do they have with their moving schedule?",
                "choices": {
                    "A": "The company and friends are free on different days.",
                    "B": "They cannot find a moving company at all.",
                    "C": "Their friends refuse to help them.",
                    "D": "The landlord changed the moving date."
                },
                "answer": "A",
                "rationale": "The company is free Saturday, but friends can help Sunday."
            },
            {
                "stem": "(audio) What solution do they consider?",
                "choices": {
                    "A": "Using the company for furniture and friends for boxes.",
                    "B": "Canceling the moving company entirely.",
                    "C": "Moving everything very late at night.",
                    "D": "Leaving all heavy items behind."
                },
                "answer": "A",
                "rationale": "They think to divide tasks between the company and friends."
            },
            {
                "stem": "(audio) What will the man do next?",
                "choices": {
                    "A": "Confirm Saturday with the company and contact friends.",
                    "B": "Buy a new apartment instead.",
                    "C": "Ask the landlord to delay the move.",
                    "D": "Sell all their furniture online."
                },
                "answer": "A",
                "rationale": "He plans to call the company and message friends."
            }
        ]
    },

    # 30. 生活：休日の過ごし方の相談
    {
        "level": "B2",
        "topic": ["holiday", "plan", "choice"],
        "dialog": [
            ("M", "We’ve both been busy lately. On the next holiday, should we take a short trip or just relax at home?"),
            ("W", "If we stay home, we’ll save money and finally have time to clean the closet."),
            ("M", "True, but getting away, even for one night, might help us forget about work."),
            ("W", "Let’s check the travel costs first, and if they’re high, we can enjoy a quiet day at home instead.")
        ],
        "questions": [
            {
                "stem": "(audio) What are they trying to decide about the holiday?",
                "choices": {
                    "A": "Whether to travel or stay home.",
                    "B": "Which relatives to visit.",
                    "C": "What gifts to buy for friends.",
                    "D": "Which movie to watch at the theater."
                },
                "answer": "A",
                "rationale": "They are choosing between a trip and relaxing at home."
            },
            {
                "stem": "(audio) What advantage does the woman see in staying home?",
                "choices": {
                    "A": "They save money and can clean the closet.",
                    "B": "They can meet new people at a hotel.",
                    "C": "They will avoid cooking completely.",
                    "D": "They can try extreme sports."
                },
                "answer": "A",
                "rationale": "She mentions saving money and having time to clean."
            },
            {
                "stem": "(audio) What will they do before making a final decision?",
                "choices": {
                    "A": "Check how much the trip would cost.",
                    "B": "Ask their boss for more holidays.",
                    "C": "Invite friends to join them.",
                    "D": "Move all furniture around the house."
                },
                "answer": "A",
                "rationale": "They plan to check travel costs first, then decide."
            }
        ]
    },
]