# patterns_part2.py
# Part2の問題パターン集だけをまとめたモジュール

# === Part2 用の問題パターン集 ===
PART2_PATTERNS = [
    # --- A2 level 30patterns (easy) ---
    {
        "level": "A2",
        "question": "What time does the morning meeting start?",
        "responses": [
            "It starts at nine o’clock.",
            "In the main conference room.",
            "With the sales manager."
        ],
        "answer": "A",
        "rationale": "Option A gives a specific time, which correctly answers the 'what time' question. B gives a place, and C mentions a person."
    },
    {
        "level": "A2",
        "question": "Where is the nearest bus stop?",
        "responses": [
            "Turn left at the corner.",
            "At the end of this street.",
            "Every twenty minutes."
        ],
        "answer": "B",
        "rationale": "Option B clearly states the location of the bus stop. A is a direction without a destination, and C talks about frequency, not place."
    },
    {
        "level": "A2",
        "question": "Who is our new manager?",
        "responses": [
            "The woman in the gray jacket.",
            "In the human resources office.",
            "Next Monday morning."
        ],
        "answer": "A",
        "rationale": "Option A identifies a person, which answers the 'who' question. B gives a place, and C gives a time."
    },
    {
        "level": "A2",
        "question": "Why is the shop closed today?",
        "responses": [
            "Because it is a national holiday.",
            "Because it is on the corner.",
            "Because the prices are low."
        ],
        "answer": "A",
        "rationale": "Option A gives a clear reason, which answers the 'why' question. B describes the location, and C talks about prices."
    },
    {
        "level": "A2",
        "question": "How will you get to work today?",
        "responses": [
            "By bicycle, if it doesn’t rain.",
            "At around seven thirty.",
            "In the small office upstairs."
        ],
        "answer": "A",
        "rationale": "Option A explains the method of transportation, answering the 'how' question. B gives a time, and C gives a place."
    },
    {
        "level": "A2",
        "question": "Which floor is the cafeteria on?",
        "responses": [
            "On the second floor near the stairs.",
            "Every day at noon.",
            "With my coworkers from sales."
        ],
        "answer": "A",
        "rationale": "Option A states a floor and a nearby landmark, which answers the question. B is a time, and C talks about people."
    },
    {
        "level": "A2",
        "question": "When is your English class?",
        "responses": [
            "On Tuesday and Thursday evenings.",
            "In the classroom upstairs.",
            "With my younger brother."
        ],
        "answer": "A",
        "rationale": "Option A gives days and time, which answers the 'when' question. B is a place, and C is a person."
    },
    {
        "level": "A2",
        "question": "Where can I buy a train ticket?",
        "responses": [
            "At the machine next to the gate.",
            "At ten forty-five tonight.",
            "With a credit card only."
        ],
        "answer": "A",
        "rationale": "Option A tells the location of the ticket machine. B is a time, and C describes a payment method only."
    },
    {
        "level": "A2",
        "question": "Who is answering the phone today?",
        "responses": [
            "Mr. Sato at the front desk.",
            "In the meeting room downstairs.",
            "After the lunch break."
        ],
        "answer": "A",
        "rationale": "Option A names the person responsible, which fits the 'who' question. B is a location, and C is a time."
    },
    {
        "level": "A2",
        "question": "Why are you late for work?",
        "responses": [
            "Because the train was delayed.",
            "Because the office is crowded.",
            "Because the meeting is important."
        ],
        "answer": "A",
        "rationale": "Option A gives a clear reason for being late. B describes the office, and C describes the meeting."
    },
    {
        "level": "A2",
        "question": "How many people are coming to the party?",
        "responses": [
            "About fifteen coworkers.",
            "At the restaurant near the station.",
            "On Friday after work."
        ],
        "answer": "A",
        "rationale": "Option A gives a number of people, which answers the 'how many' question. B and C give place and time."
    },
    {
        "level": "A2",
        "question": "Which desk is mine?",
        "responses": [
            "The one next to the window.",
            "On the third floor.",
            "At nine in the morning."
        ],
        "answer": "A",
        "rationale": "Option A points to a specific desk, which answers the question. B is a floor, and C is a time."
    },
    {
        "level": "A2",
        "question": "When does the movie start?",
        "responses": [
            "It starts at seven fifteen.",
            "In the large theater.",
            "With my best friend."
        ],
        "answer": "A",
        "rationale": "Option A gives a start time. B is a location, and C is a person."
    },
    {
        "level": "A2",
        "question": "Where are the restrooms?",
        "responses": [
            "Down the hall on the right.",
            "After we finish lunch.",
            "For the staff only."
        ],
        "answer": "A",
        "rationale": "Option A gives directions, which matches the 'where' question. B is a time, and C is a condition."
    },
    {
        "level": "A2",
        "question": "Who will pick up the children?",
        "responses": [
            "Their grandfather will pick them up.",
            "At the school gate.",
            "Before the last class."
        ],
        "answer": "A",
        "rationale": "Option A names the person, which answers the 'who' question. B is a place, and C is a time."
    },
    {
        "level": "A2",
        "question": "Why are the lights off in this room?",
        "responses": [
            "Because no one is using it now.",
            "Because it is on the first floor.",
            "Because the windows are open."
        ],
        "answer": "A",
        "rationale": "Option A explains the reason, fitting the 'why' question. B and C describe the room but not the reason for the lights."
    },
    {
        "level": "A2",
        "question": "How long is your lunch break?",
        "responses": [
            "It’s one hour today.",
            "In the company cafeteria.",
            "With my team leader."
        ],
        "answer": "A",
        "rationale": "Option A gives a length of time, which answers the 'how long' question. B and C give place and people."
    },
    {
        "level": "A2",
        "question": "Which bus goes to the airport?",
        "responses": [
            "Take the blue bus number twenty.",
            "At the second platform.",
            "Every half an hour."
        ],
        "answer": "A",
        "rationale": "Option A identifies a specific bus, answering the 'which' question. B is a platform, and C is a frequency."
    },
    {
        "level": "A2",
        "question": "When is the next train to Tokyo?",
        "responses": [
            "It leaves in ten minutes.",
            "From platform three.",
            "With a reserved seat."
        ],
        "answer": "A",
        "rationale": "Option A gives a departure time, which answers the 'when' question. B and C describe place and seat type."
    },
    {
        "level": "A2",
        "question": "Where should I park my car?",
        "responses": [
            "In the visitors’ parking area.",
            "Before eight in the morning.",
            "With the hazard lights on."
        ],
        "answer": "A",
        "rationale": "Option A tells the correct parking area. B is a time, and C is a driving condition."
    },
    {
        "level": "A2",
        "question": "Who will open the shop tomorrow?",
        "responses": [
            "Ms. Kim from the morning shift.",
            "In front of the building.",
            "After the cleaning is done."
        ],
        "answer": "A",
        "rationale": "Option A names a specific person, which fits the 'who' question. B and C are place and time information."
    },
    {
        "level": "A2",
        "question": "Why is the meeting room busy now?",
        "responses": [
            "Because another team is using it.",
            "Because it is on the top floor.",
            "Because the chairs are new."
        ],
        "answer": "A",
        "rationale": "Option A explains the reason, answering the 'why' question. B and C describe the room, not the reason."
    },
    {
        "level": "A2",
        "question": "How much is this sandwich?",
        "responses": [
            "It’s four hundred yen.",
            "It’s in the glass case.",
            "It comes with a drink."
        ],
        "answer": "A",
        "rationale": "Option A gives a price, which matches the 'how much' question. B is a location, and C is extra information."
    },
    {
        "level": "A2",
        "question": "Which door should I use to enter?",
        "responses": [
            "Please use the side entrance.",
            "Please come before ten o’clock.",
            "Please wait near the counter."
        ],
        "answer": "A",
        "rationale": "Option A specifies a door, answering the 'which door' question. B and C give time and place, not a door choice."
    },
    {
        "level": "A2",
        "question": "When is the homework due?",
        "responses": [
            "It’s due this Friday.",
            "In the English classroom.",
            "With a short presentation."
        ],
        "answer": "A",
        "rationale": "Option A gives a deadline, which answers the 'when' question. B and C describe place and style."
    },
    {
        "level": "A2",
        "question": "Where is the manager right now?",
        "responses": [
            "She is in a meeting upstairs.",
            "She is very busy this week.",
            "She is our new colleague."
        ],
        "answer": "A",
        "rationale": "Option A tells her current location. B describes her schedule, and C describes who she is."
    },
    {
        "level": "A2",
        "question": "Who is giving the next presentation?",
        "responses": [
            "Our designer from Osaka.",
            "In the large meeting room.",
            "At three in the afternoon."
        ],
        "answer": "A",
        "rationale": "Option A names the presenter, which answers the 'who' question. B and C give place and time."
    },
    {
        "level": "A2",
        "question": "Why is the class canceled today?",
        "responses": [
            "Because the teacher is sick.",
            "Because the room is large.",
            "Because the exam is easy."
        ],
        "answer": "A",
        "rationale": "Option A gives the reason for cancellation. B and C are unrelated descriptions."
    },
    {
        "level": "A2",
        "question": "How often do you clean this room?",
        "responses": [
            "We clean it twice a week.",
            "We clean it at the back.",
            "We clean it after class."
        ],
        "answer": "A",
        "rationale": "Option A gives a frequency, matching the 'how often' question. B and C talk about place and timing, but not frequency."
    },
    {
        "level": "A2",
        "question": "Which menu item do you recommend?",
        "responses": [
            "The chicken curry is very popular.",
            "The kitchen closes at nine o’clock.",
            "The tables are near the window."
        ],
        "answer": "A",
        "rationale": "Option A suggests a specific item, answering the 'which' question. B and C describe time and seating."
    },

    # --- B1 level 100patterns (standard) ---
    # 1: C
    {
        "level": "B1",
        "question": "Could you send me the draft by noon?",
        "responses": [
            "I’ll send it before lunch.",
            "I’m meeting her at the cafeteria.",
            "Sure, I’ll e-mail it by twelve."
        ],
        "answer": "C",
        "rationale": "Option C clearly agrees to send the draft by the requested time. A is vague about what will be sent, and B talks about a meeting, not the request."
    },
    # 2: A
    {
        "level": "B1",
        "question": "When will the client arrive?",
        "responses": [
            "He should be here around three.",
            "No, I haven’t met him.",
            "At the central station."
        ],
        "answer": "A",
        "rationale": "Option A gives a time, which correctly answers the question about when. B and C talk about familiarity and location, not the time of arrival."
    },
    # 3: B
    {
        "level": "B1",
        "question": "Where should I put these documents?",
        "responses": [
            "They were sent yesterday.",
            "Please leave them on my desk.",
            "About the new project."
        ],
        "answer": "B",
        "rationale": "Option B tells the listener the place to put the documents. A talks about when they were sent, and C introduces a topic, not a location."
    },
    # 4: A
    {
        "level": "B1",
        "question": "Why was the meeting canceled?",
        "responses": [
            "Because the manager is on a business trip.",
            "In the main conference room.",
            "Next Wednesday afternoon."
        ],
        "answer": "A",
        "rationale": "Option A gives a reason, which answers the why-question. B and C give a place and a time, which do not explain the cancellation."
    },

    # 5: A
    {
        "level": "B1",
        "question": "How often do we need to back up the data?",
        "responses": [
            "We’re supposed to do it every Friday.",
            "It’s on the top shelf.",
            "For the new marketing team."
        ],
        "answer": "A",
        "rationale": "Option A states a frequency, which answers the how-often question. B refers to a location, and C refers to a purpose or group, not frequency."
    },
    # 6: B
    {
        "level": "B1",
        "question": "Who will give the presentation tomorrow?",
        "responses": [
            "In the small conference room.",
            "Ms. Lee from the sales department.",
            "Because the system was down."
        ],
        "answer": "B",
        "rationale": "Option B names a person, which answers the who-question. A gives a place, and C gives a reason, which do not identify the presenter."
    },
    # 7: C
    {
        "level": "B1",
        "question": "What does the man suggest they do about the report?",
        "responses": [
            "He will call the main office.",
            "He already sent the invoice.",
            "He thinks they should shorten it.",
        ],
        "answer": "C",
        "rationale": "Option C describes a specific suggestion about the report itself. A and B mention other actions that do not relate to revising the report."
    },
    # 8: A
    {
        "level": "B1",
        "question": "Why can’t she attend the afternoon meeting?",
        "responses": [
            "She has a doctor’s appointment then.",
            "She finished the report last night.",
            "She’ll be in the conference room."
        ],
        "answer": "A",
        "rationale": "Option A gives a conflicting appointment, which is a valid reason for not attending. B and C describe past work or location but not a reason for absence."
    },
    # 9: B
    {
        "level": "B1",
        "question": "Where will they have lunch together?",
        "responses": [
            "He has a lunch meeting with a client.",
            "At the café across the street.",
            "At eleven thirty."
        ],
        "answer": "B",
        "rationale": "Option B gives a place, which answers the where-question. A and C talk about a meeting and a time, not the location of lunch."
    },
    # 10: C
    {
        "level": "B1",
        "question": "What does the woman ask the man to do?",
        "responses": [
            "To change the office layout.",
            "To check the train schedule.",
            "To print ten more copies.",
        ],
        "answer": "C",
        "rationale": "Option C describes a clear request for action. A and B mention other possible tasks but are not the specific favor mentioned in the conversation."
    },
    # 11: A
    {
        "level": "B1",
        "question": "When is the project deadline?",
        "responses": [
            "It’s been moved to next Monday.",
            "He already submitted the form.",
            "In the accounting department."
        ],
        "answer": "A",
        "rationale": "Option A gives a deadline date, which answers the when-question. B and C describe a completed action and a place, not the timing."
    },
    # 12: B
    {
        "level": "B1",
        "question": "Why is the man calling the hotel?",
        "responses": [
            "To confirm the flight number.",
            "To change his reservation date.",
            "To order room service."
        ],
        "answer": "B",
        "rationale": "Option B states a reason related to a hotel reservation. A and C talk about a flight and room service, which do not match the purpose."
    },
    # 13: C
    {
        "level": "B1",
        "question": "What does the speaker say about the training session?",
        "responses": [
            "It will be held in the lobby.",
            "It was canceled yesterday.",
            "It has been extended by one hour.",
        ],
        "answer": "C",
        "rationale": "Option C mentions a change in duration, which is new information about the session. A and B give location or cancellation that may not fit the statement."
    },
    # 14: A
    {
        "level": "B1",
        "question": "What does the boss want the team to do today?",
        "responses": [
            "Finish the presentation slides.",
            "Move to a different office.",
            "Invite a new member."
        ],
        "answer": "A",
        "rationale": "Option A describes a specific task to be completed today. B and C mention other actions that are not clearly today’s main instruction."
    },
    # 15: B
    {
        "level": "B1",
        "question": "What are the employees discussing?",
        "responses": [
            "The cost of new computers.",
            "The schedule for next week’s shifts.",
            "The design of the company logo."
        ],
        "answer": "B",
        "rationale": "Option B refers to a schedule, which matches a typical topic of discussion in planning. A and C are different topics that do not fit the described conversation."
    },
    # 16: C
    {
        "level": "B1",
        "question": "Where should visitors check in?",
        "responses": [
            "They have already checked in.",
            "At the main station entrance.",
            "At the security desk on the first floor.",
        ],
        "answer": "C",
        "rationale": "Option C gives a specific check-in location. A comments on a past action, and B mentions a station entrance, which is unlikely to be the correct check-in point."
    },
    # 17: A
    {
        "level": "B1",
        "question": "Why does he need to leave the office early?",
        "responses": [
            "He has to pick up his daughter.",
            "He finished the report already.",
            "He works from home on Fridays."
        ],
        "answer": "A",
        "rationale": "Option A provides a personal obligation that explains leaving early. B and C describe work status or routine but not the immediate reason."
    },
    # 18: B
    {
        "level": "B1",
        "question": "What is the woman worried about?",
        "responses": [
            "The hotel is fully booked.",
            "The package may not arrive on time.",
            "Her colleague will be late."
        ],
        "answer": "B",
        "rationale": "Option B expresses concern about a package and timing, matching the idea of being worried. A and C mention other issues that do not clearly fit her concern."
    },
    # 19: C
    {
        "level": "B1",
        "question": "How will the manager contact the staff?",
        "responses": [
            "By posting a notice on the door.",
            "By calling everyone individually.",
            "By sending a group e-mail.",
        ],
        "answer": "C",
        "rationale": "Option C gives a specific communication method that fits contacting staff efficiently. A and B describe less efficient or different methods."
    },
    # 20: A
    {
        "level": "B1",
        "question": "What does the speaker say about tomorrow’s workshop?",
        "responses": [
            "Participants need to bring their laptops.",
            "It will be held in another city.",
            "It starts at six in the evening."
        ],
        "answer": "A",
        "rationale": "Option A gives a requirement for participants, which is typical workshop information. B and C focus on place and time rather than preparation."
    },
    # 21: B
    {
        "level": "B1",
        "question": "What is the man asking about?",
        "responses": [
            "The price of a train ticket.",
            "The status of his job application.",
            "The location of the nearest bank."
        ],
        "answer": "B",
        "rationale": "Option B states a question about an application status, matching an inquiry about progress. A and C are questions on unrelated topics."
    },
    # 22: C
    {
        "level": "B1",
        "question": "What are listeners encouraged to do?",
        "responses": [
            "Call the store before visiting.",
            "Bring their own food and drinks.",
            "Register online by Friday.",
        ],
        "answer": "C",
        "rationale": "Option C describes a clear action by a deadline, which matches an encouragement or instruction. A and B mention other actions not tied to the main request."
    },
    # 23: A
    {
        "level": "B1",
        "question": "Where will the staff meeting take place?",
        "responses": [
            "In the large conference hall.",
            "On the second floor of the hotel.",
            "Near the main entrance."
        ],
        "answer": "A",
        "rationale": "Option A provides a specific meeting location. B and C are vague or different places that do not necessarily match the official venue."
    },
    # 24: B
    {
        "level": "B1",
        "question": "Why is the store offering discounts?",
        "responses": [
            "Because they extended their business hours.",
            "Because they are celebrating their tenth anniversary.",
            "Because the weather is bad today."
        ],
        "answer": "B",
        "rationale": "Option B gives a special occasion that commonly leads to discounts. A and C mention unrelated reasons that are less typical for a big sale."
    },
    # 25: C
    {
        "level": "B1",
        "question": "What does the speaker tell passengers to do?",
        "responses": [
            "Switch to another train line.",
            "Remain seated until the doors open.",
            "Move toward the rear of the bus.",
        ],
        "answer": "C",
        "rationale": "Option C is a clear instruction about where to stand or sit on the vehicle. A and B give different directions that do not match the described announcement."
    },
    # 26: A
    {
        "level": "B1",
        "question": "Why is the report being revised?",
        "responses": [
            "Because there were several spelling errors.",
            "In the conference room on the third floor.",
            "By the end of this afternoon."
        ],
        "answer": "A",
        "rationale": "Option A provides a reason for revision, which answers the why-question. B and C give a place and a time, not a reason."
    },
    # 27: B
    {
        "level": "B1",
        "question": "What does the woman say about the new intern?",
        "responses": [
            "He will arrive next month.",
            "She seems very motivated.",
            "They worked together last year."
        ],
        "answer": "B",
        "rationale": "Option B evaluates the intern’s attitude, which is a comment about her. A and C discuss timing and history, not her qualities."
    },
    # 28: C
    {
        "level": "B1",
        "question": "How should employees submit their travel expenses?",
        "responses": [
            "He checked them yesterday.",
            "At the reception desk.",
            "By filling out the online form.",
        ],
        "answer": "C",
        "rationale": "Option C explains the correct method for submission, which answers the how-question. A and B refer to past checking or location, not procedure."
    },
    # 29: A
    {
        "level": "B1",
        "question": "Why will the office close early on Friday?",
        "responses": [
            "Because there will be electrical maintenance.",
            "Because the meeting is running late.",
            "Because the manager is on a business trip."
        ],
        "answer": "A",
        "rationale": "Option A gives a maintenance reason, which justifies closing early. B and C mention scheduling and travel that do not require closing the office."
    },
    # 30: B
    {
        "level": "B1",
        "question": "What does the speaker say about the new software?",
        "responses": [
            "It was installed last year.",
            "It is easier to use than the old one.",
            "It will only be used in the warehouse."
        ],
        "answer": "B",
        "rationale": "Option B compares the new software to the old one, which is typical evaluative information. A and C focus on timing and limited use instead."
    },
    # 31: C
    {
        "level": "B1",
        "question": "How often will the team have progress meetings?",
        "responses": [
            "They finished the final report.",
            "In the small meeting room.",
            "Once a week on Monday mornings.",
        ],
        "answer": "C",
        "rationale": "Option C states a regular schedule, answering the how-often question. A and B talk about completion and place, not frequency."
    },
    # 32: A
    {
        "level": "B1",
        "question": "Why is the man calling the IT department?",
        "responses": [
            "Because his computer won’t start.",
            "Because he needs a larger office.",
            "Because the meeting was canceled."
        ],
        "answer": "A",
        "rationale": "Option A describes a technical problem that IT can help with. B and C describe issues unrelated to IT support."
    },
    # 33: B
    {
        "level": "B1",
        "question": "Where will the training session be held?",
        "responses": [
            "She will give an online lecture.",
            "In Room 402 of the main building.",
            "Next Friday morning."
        ],
        "answer": "B",
        "rationale": "Option B provides a specific room, which answers the where-question. A and C talk about format and time, not location."
    },
    # 34: C
    {
        "level": "B1",
        "question": "What does the woman ask the man to bring?",
        "responses": [
            "The revised schedule.",
            "The sales figures from last year.",
            "A copy of the contract.",
        ],
        "answer": "C",
        "rationale": "Option C specifies an item to bring, answering the what-question. A and B are different documents that do not match the request."
    },
    # 35: A
    {
        "level": "B1",
        "question": "What is the main reason for hiring another employee?",
        "responses": [
            "The department has too much work.",
            "The office is being renovated.",
            "The company is moving next month."
        ],
        "answer": "A",
        "rationale": "Option A gives a workload-based reason, which fits hiring more staff. B and C mention other changes that do not directly require new staff."
    },
    # 36: B
    {
        "level": "B1",
        "question": "What does the speaker say about the parking lot?",
        "responses": [
            "It will be closed for three days.",
            "It is often full in the morning.",
            "It is reserved for delivery trucks."
        ],
        "answer": "B",
        "rationale": "Option B describes a frequent condition of the lot, which matches a comment. A and C give specific restrictions that may contradict the announcement."
    },
    # 37: C
    {
        "level": "B1",
        "question": "How should staff confirm their attendance at the workshop?",
        "responses": [
            "By visiting the reception desk.",
            "By paying the fee in cash.",
            "By replying to the e-mail invitation.",
        ],
        "answer": "C",
        "rationale": "Option C gives a clear confirmation method tied to the invitation. A and B describe other actions that are not explicitly requested."
    },
    # 38: A
    {
        "level": "B1",
        "question": "Why is the woman unable to answer the phone right now?",
        "responses": [
            "She is speaking with a customer.",
            "She will return from lunch soon.",
            "She has already left the office."
        ],
        "answer": "A",
        "rationale": "Option A explains her current situation that prevents her from answering. B and C refer to timing and absence that do not match “right now.”"
    },
    # 39: B
    {
        "level": "B1",
        "question": "What does the man suggest they do about the schedule?",
        "responses": [
            "Change the meeting room.",
            "Move the meeting to next week.",
            "Shorten the lunch break."
        ],
        "answer": "B",
        "rationale": "Option B suggests changing the date, which is a direct adjustment to the schedule. A and C change room or break length, not the schedule itself."
    },
    # 40: C
    {
        "level": "B1",
        "question": "What does the speaker ask passengers to have ready?",
        "responses": [
            "Their hotel reservation number.",
            "Their return flight ticket.",
            "Their boarding passes and passports.",
        ],
        "answer": "C",
        "rationale": "Option C lists the typical documents needed for boarding, which fits the request. A and B mention single items that are not enough for boarding."
    },
    # 41: A
    {
        "level": "B1",
        "question": "Why is the store opening earlier than usual tomorrow?",
        "responses": [
            "Because they are having a special sale.",
            "Because the manager is away on business.",
            "Because some shelves are being replaced."
        ],
        "answer": "A",
        "rationale": "Option A gives a promotional reason for early opening. B and C describe unrelated circumstances that do not require opening earlier."
    },
    # 42: B
    {
        "level": "B1",
        "question": "Where is the man supposed to meet the delivery driver?",
        "responses": [
            "At the main reception desk.",
            "In front of the side entrance.",
            "On the second floor near the elevator."
        ],
        "answer": "B",
        "rationale": "Option B gives a clear meeting point outside, which suits a delivery. A and C are indoor locations that are less typical for initial delivery meeting."
    },
    # 43: C
    {
        "level": "B1",
        "question": "What should visitors do if they arrive after six o’clock?",
        "responses": [
            "They should call the restaurant.",
            "They should pay the entrance fee.",
            "They should use the night entrance.",
        ],
        "answer": "C",
        "rationale": "Option C gives a specific procedure for arriving late. A and B describe other actions that are not clearly related to after-hours access."
    },
    # 44: A
    {
        "level": "B1",
        "question": "Why will the company’s website be unavailable tonight?",
        "responses": [
            "Because of a system upgrade.",
            "Because of a power failure.",
            "Because of a holiday event."
        ],
        "answer": "A",
        "rationale": "Option A gives a planned technical reason that often requires downtime. B and C describe other problems or events not mentioned in the announcement."
    },
    # 45: B
    {
        "level": "B1",
        "question": "What does the woman say about the hotel room?",
        "responses": [
            "It has already been cleaned.",
            "It has a view of the ocean.",
            "It is not available this weekend."
        ],
        "answer": "B",
        "rationale": "Option B comments on the room’s view, which is a descriptive feature. A and C talk about cleaning status and availability, not the special feature."
    },
    # 46: C
    {
        "level": "B1",
        "question": "How can customers receive the discount?",
        "responses": [
            "By showing their passport.",
            "By paying in cash only.",
            "By presenting the coupon at the register.",
        ],
        "answer": "C",
        "rationale": "Option C specifies the condition for getting the discount. A and B mention requirements that are not tied to the stated promotion."
    },
    # 47: A
    {
        "level": "B1",
        "question": "Why is the man asking for another copy of the invoice?",
        "responses": [
            "He accidentally deleted the e-mail.",
            "He needs it for the delivery company.",
            "He wants to change the order quantity."
        ],
        "answer": "A",
        "rationale": "Option A explains that he lost the original copy, justifying the request. B and C describe other reasons that are not directly about needing a new copy."
    },
    # 48: B
    {
        "level": "B1",
        "question": "What does the speaker say about the museum today?",
        "responses": [
            "It will open one hour earlier than usual.",
            "It is offering free admission to students.",
            "It is closing the second-floor gallery."
        ],
        "answer": "B",
        "rationale": "Option B describes a special offer for a group, which matches an announcement. A and C talk about schedule or closures, which are different types of information."
    },
    # 49: C
    {
        "level": "B1",
        "question": "How should participants submit their questions to the speaker?",
        "responses": [
            "By calling the office before the event.",
            "By writing them on a feedback form.",
            "By typing them into the chat window.",
        ],
        "answer": "C",
        "rationale": "Option C matches an online or live event format where chat is used. A and B involve other channels not mentioned in the instructions."
    },
    # 50: A
    {
        "level": "B1",
        "question": "Why is the bus driver making this announcement?",
        "responses": [
            "Because the bus will take a different route.",
            "Because the fare has recently increased.",
            "Because the air conditioner is not working."
        ],
        "answer": "A",
        "rationale": "Option A explains a change that passengers must know, justifying an announcement. B and C are other issues that may not require immediate route information."
    },
    # 51: B
    {
        "level": "B1",
        "question": "What does the woman say about the restaurant?",
        "responses": [
            "It closes earlier on weekends.",
            "It is fully booked this evening.",
            "It has just changed its name."
        ],
        "answer": "B",
        "rationale": "Option B describes the restaurant’s reservation status, which affects her plans. A and C describe other details not directly related to tonight’s availability."
    },
    # 52: C
    {
        "level": "B1",
        "question": "How does the company ask customers to respond to the survey?",
        "responses": [
            "By filling out a card at the counter.",
            "By speaking to a staff member directly.",
            "By completing it on the company website.",
        ],
        "answer": "C",
        "rationale": "Option C specifies the requested response method through the website. A and B mention other ways not indicated in the announcement."
    },
    # 53: A
    {
        "level": "B1",
        "question": "Why is the woman going to the post office?",
        "responses": [
            "To send an important document by express mail.",
            "To meet her colleague for lunch.",
            "To pick up a package for her neighbor."
        ],
        "answer": "A",
        "rationale": "Option A explains a task that clearly requires the post office. B and C describe other activities that are not stated as her purpose."
    },
    # 54: B
    {
        "level": "B1",
        "question": "What does the speaker say about the guided tour?",
        "responses": [
            "It has been canceled due to rain.",
            "It will start in front of the information desk.",
            "It is available only in the afternoon."
        ],
        "answer": "B",
        "rationale": "Option B gives the starting point, which matches a typical tour announcement detail. A and C describe cancellation or timing, which differ."
    },
    # 55: C
    {
        "level": "B1",
        "question": "What should passengers do with large luggage?",
        "responses": [
            "Place it under their seats.",
            "Take it with them to the upper deck.",
            "Store it in the racks at the end of the carriage.",
        ],
        "answer": "C",
        "rationale": "Option C provides a specific and safe storage location for large luggage. A and B give locations that are less suitable for large items."
    },
    # 56: A
    {
        "level": "B1",
        "question": "Why does the teacher want students to arrive early?",
        "responses": [
            "Because there will be a short quiz at the beginning.",
            "Because the classroom has changed.",
            "Because a guest speaker will join later."
        ],
        "answer": "A",
        "rationale": "Option A gives a clear academic reason related to the start of class. B and C describe other changes that do not require arriving early."
    },
    # 57: B
    {
        "level": "B1",
        "question": "What does the man say about the conference?",
        "responses": [
            "It was held last spring.",
            "It will last for three days.",
            "It is only for new employees."
        ],
        "answer": "B",
        "rationale": "Option B states the duration, which is typical conference information. A and C mention timing and target audience, not how long it will last."
    },
    # 58: C
    {
        "level": "B1",
        "question": "How should students hand in their assignments?",
        "responses": [
            "By bringing them to the office in person.",
            "By sending them by regular mail.",
            "By uploading them to the school system.",
        ],
        "answer": "C",
        "rationale": "Option C reflects a modern submission method specified by the school. A and B describe other methods not requested in the instructions."
    },
    # 59: A
    {
        "level": "B1",
        "question": "Why is the gym closing earlier tonight?",
        "responses": [
            "Because the staff will clean the equipment.",
            "Because the trainer is on vacation.",
            "Because the pool is under repair."
        ],
        "answer": "A",
        "rationale": "Option A gives a clear operational reason that affects closing time. B and C mention unrelated issues that do not require closing the entire gym early."
    },
    # 60: B
    {
        "level": "B1",
        "question": "What does the coach say about tomorrow’s practice?",
        "responses": [
            "It will be held indoors.",
            "It will start thirty minutes later.",
            "It will be canceled if it rains."
        ],
        "answer": "B",
        "rationale": "Option B directly states a change in starting time. A and C talk about location or conditional cancellation, which are different types of changes."
    },
    # 61: C
    {
        "level": "B1",
        "question": "How can members renew their library cards?",
        "responses": [
            "By calling the city office.",
            "By filling out a paper form at home.",
            "By visiting the counter with their ID.",
        ],
        "answer": "C",
        "rationale": "Option C describes the correct in-person procedure for renewal. A and B suggest other methods that are not the specified process."
    },
    # 62: A
    {
        "level": "B1",
        "question": "Why is the man visiting the clinic?",
        "responses": [
            "He needs a checkup before his business trip.",
            "He wants to pick up his daughter.",
            "He plans to apply for a part-time job."
        ],
        "answer": "A",
        "rationale": "Option A gives a medical reason suitable for a clinic visit. B and C describe purposes unrelated to a medical checkup."
    },
    # 63: B
    {
        "level": "B1",
        "question": "What does the receptionist tell the caller about the doctor?",
        "responses": [
            "He is away on holiday this month.",
            "He is fully booked this afternoon.",
            "He has moved to another hospital."
        ],
        "answer": "B",
        "rationale": "Option B explains the doctor’s schedule for today, which affects making an appointment. A and C describe longer-term absence or relocation."
    },
    # 64: C
    {
        "level": "B1",
        "question": "What should patients do if they need to cancel an appointment?",
        "responses": [
            "Pay a small cancellation fee at the counter.",
            "Send a letter to the hospital.",
            "Call the clinic at least one day in advance.",
        ],
        "answer": "C",
        "rationale": "Option C gives a clear cancellation procedure and time frame. A and B offer other actions that are not mentioned as the proper procedure."
    },
    # 65: A
    {
        "level": "B1",
        "question": "Why is the woman looking for a pharmacy?",
        "responses": [
            "She needs to buy some medicine.",
            "She wants to print some documents.",
            "She is meeting a friend there."
        ],
        "answer": "A",
        "rationale": "Option A states a typical reason for visiting a pharmacy. B and C mention unrelated purposes."
    },
    # 66: B
    {
        "level": "B1",
        "question": "What does the man say about the bus stop?",
        "responses": [
            "It is on the opposite side of the street.",
            "It is just around the corner.",
            "It is only used on weekends."
        ],
        "answer": "B",
        "rationale": "Option B gives a simple direction close by, which fits helping someone find it. A and C describe different situations that may not match the explanation."
    },
    # 67: C
    {
        "level": "B1",
        "question": "How does the woman plan to get to the station?",
        "responses": [
            "By taking a taxi from her office.",
            "By walking with her colleague.",
            "By taking the next express bus.",
        ],
        "answer": "C",
        "rationale": "Option C names a specific transport method, answering the how-question. A and B give other options that do not match her stated plan."
    },
    # 68: A
    {
        "level": "B1",
        "question": "Why is the train arriving later than scheduled?",
        "responses": [
            "Because of heavy rain along the line.",
            "Because the driver missed the signal.",
            "Because the platform is under construction."
        ],
        "answer": "A",
        "rationale": "Option A gives a weather-related delay, a common cause. B and C describe other issues not typically given as the official reason."
    },
    # 69: B
    {
        "level": "B1",
        "question": "What does the announcement say about seat reservations?",
        "responses": [
            "They are not available today.",
            "They are required on this train.",
            "They can only be made at the station."
        ],
        "answer": "B",
        "rationale": "Option B states a clear rule that reservations are necessary. A and C mention other conditions that do not match the message."
    },
    # 70: C
    {
        "level": "B1",
        "question": "How can passengers find out which platform their train leaves from?",
        "responses": [
            "By asking the driver directly.",
            "By checking the information brochure.",
            "By looking at the electronic display board.",
        ],
        "answer": "C",
        "rationale": "Option C points to the standard source of live platform information. A and B are less practical or not updated in real time."
    },
    # 71: A
    {
        "level": "B1",
        "question": "Why is the traveler speaking with the airline staff?",
        "responses": [
            "His suitcase did not arrive.",
            "His hotel was overbooked.",
            "His taxi did not show up."
        ],
        "answer": "A",
        "rationale": "Option A involves lost baggage, which is handled by airline staff. B and C concern hotel and taxi issues, not the airline."
    },
    # 72: B
    {
        "level": "B1",
        "question": "What does the woman say about the flight to Paris?",
        "responses": [
            "It has already departed.",
            "It has been delayed by one hour.",
            "It has changed to a smaller plane."
        ],
        "answer": "B",
        "rationale": "Option B reports a delay, which is typical in flight announcements. A and C describe other changes not specified in the description."
    },
    # 73: C
    {
        "level": "B1",
        "question": "What are passengers asked to do with electronic devices?",
        "responses": [
            "Place them in their checked baggage.",
            "Switch them to silent mode.",
            "Turn them off during takeoff.",
        ],
        "answer": "C",
        "rationale": "Option C matches common safety instructions for takeoff. A and B mention actions that do not fully meet standard safety rules."
    },
    # 74: A
    {
        "level": "B1",
        "question": "Why is the hotel offering a free drink ticket?",
        "responses": [
            "Because the guest’s room was not ready on time.",
            "Because the restaurant has a new menu.",
            "Because the guest is staying for a week."
        ],
        "answer": "A",
        "rationale": "Option A explains the hotel’s compensation for an inconvenience. B and C refer to other reasons not clearly tied to an apology."
    },
    # 75: B
    {
        "level": "B1",
        "question": "What does the receptionist say about breakfast?",
        "responses": [
            "It is served only in the guest rooms.",
            "It is included in the room price.",
            "It must be reserved a day in advance."
        ],
        "answer": "B",
        "rationale": "Option B states that breakfast is included, which is a key detail about cost. A and C describe different arrangements not mentioned as true."
    },
    # 76: C
    {
        "level": "B1",
        "question": "How can guests request extra towels?",
        "responses": [
            "By filling out a card on the desk.",
            "By visiting the front desk in person.",
            "By calling the housekeeping extension.",
        ],
        "answer": "C",
        "rationale": "Option C gives the specific method the hotel prefers for such requests. A and B mention other methods not specified in the instructions."
    },
    # 77: A
    {
        "level": "B1",
        "question": "Why is the woman calling the restaurant?",
        "responses": [
            "To change the number of people in her reservation.",
            "To ask about today’s special menu.",
            "To check if they accept credit cards."
        ],
        "answer": "A",
        "rationale": "Option A explains a change in her booking details, a common reason to call. B and C are other questions not stated as her purpose."
    },
    # 78: B
    {
        "level": "B1",
        "question": "What does the waiter say about outdoor seating?",
        "responses": [
            "It will be closed this evening.",
            "It is available if they don’t mind the cold.",
            "It costs more than indoor seating."
        ],
        "answer": "B",
        "rationale": "Option B describes the condition under which they can sit outside. A and C introduce restrictions or costs not mentioned in the scenario."
    },
    # 79: C
    {
        "level": "B1",
        "question": "How should customers pay the delivery fee?",
        "responses": [
            "By bank transfer before the delivery.",
            "By credit card on the company website.",
            "By giving cash to the driver.",
        ],
        "answer": "C",
        "rationale": "Option C states the payment method requested in the announcement. A and B are different payment methods that are not specified as correct."
    },
    # 80: A
    {
        "level": "B1",
        "question": "Why is the store temporarily closing the second floor?",
        "responses": [
            "Because they are rearranging the furniture.",
            "Because they have run out of stock.",
            "Because they are hosting a private event."
        ],
        "answer": "A",
        "rationale": "Option A gives a practical reason that affects only that floor. B and C describe conditions that do not necessarily require a temporary closure."
    },
    # 81: B
    {
        "level": "B1",
        "question": "What does the clerk say about returning items?",
        "responses": [
            "It can only be done on weekends.",
            "It is possible with the receipt.",
            "It is free for all customers."
        ],
        "answer": "B",
        "rationale": "Option B explains the condition needed to return items. A and C give rules that contradict typical store policies or the described situation."
    },
    # 82: C
    {
        "level": "B1",
        "question": "How can customers receive the store’s newsletter?",
        "responses": [
            "By visiting the store every month.",
            "By calling the customer service center.",
            "By registering their e-mail address online.",
        ],
        "answer": "C",
        "rationale": "Option C specifies the method for signing up, matching the question. A and B describe other actions not directly linked to newsletter registration."
    },
    # 83: A
    {
        "level": "B1",
        "question": "Why is the speaker asking listeners to keep their receipts?",
        "responses": [
            "They are needed for a lottery drawing.",
            "They must be shown at the exit gate.",
            "They will be collected by the cashier."
        ],
        "answer": "A",
        "rationale": "Option A gives a special reason to keep receipts for a drawing. B and C describe uses that are not indicated in the announcement."
    },
    # 84: B
    {
        "level": "B1",
        "question": "What does the announcement say about the elevator?",
        "responses": [
            "It is reserved for staff members.",
            "It is out of service at the moment.",
            "It will stop only on the first floor."
        ],
        "answer": "B",
        "rationale": "Option B states its current status, which is the key information. A and C mention restrictions that are not described as true in the notice."
    },
    # 85: C
    {
        "level": "B1",
        "question": "How are visitors asked to enter the building after nine p.m.?",
        "responses": [
            "By using the main front door.",
            "By registering at the parking gate.",
            "By ringing the bell at the side entrance.",
        ],
        "answer": "C",
        "rationale": "Option C gives the specific after-hours entry procedure. A and B describe other methods not mentioned in the instructions."
    },
    # 86: A
    {
        "level": "B1",
        "question": "Why is the speaker reminding employees about the dress code?",
        "responses": [
            "Because clients will be visiting the office tomorrow.",
            "Because the weather is getting colder.",
            "Because the air conditioner is being repaired."
        ],
        "answer": "A",
        "rationale": "Option A provides a clear reason related to appearance and visitors. B and C mention conditions that do not directly relate to dress code."
    },
    # 87: B
    {
        "level": "B1",
        "question": "What does the manager say about working from home?",
        "responses": [
            "It will not be allowed next month.",
            "It is permitted once a week with approval.",
            "It is only for employees who live far away."
        ],
        "answer": "B",
        "rationale": "Option B explains the new policy on frequency and approval. A and C describe restrictions that differ from the stated rule."
    },
    # 88: C
    {
        "level": "B1",
        "question": "How should staff record their overtime hours?",
        "responses": [
            "By sending them to the team leader.",
            "By writing them on a paper form.",
            "By entering them into the timekeeping system.",
        ],
        "answer": "C",
        "rationale": "Option C gives the official system to use, answering the how-question. A and B mention other methods not specified by the company."
    },
    # 89: A
    {
        "level": "B1",
        "question": "Why is the company organizing a health check for employees?",
        "responses": [
            "To help them monitor their condition.",
            "To reduce the number of meetings.",
            "To prepare for the annual party."
        ],
        "answer": "A",
        "rationale": "Option A states a health-related purpose, which matches a checkup. B and C describe goals unrelated to health monitoring."
    },
    # 90: B
    {
        "level": "B1",
        "question": "What does the speaker say about the staff cafeteria?",
        "responses": [
            "It will be closed all week.",
            "It will start serving breakfast from next month.",
            "It now accepts cashless payments only."
        ],
        "answer": "B",
        "rationale": "Option B provides new information about breakfast service. A and C describe different changes not mentioned in the announcement."
    },
    # 91: C
    {
        "level": "B1",
        "question": "How can employees sign up for the language course?",
        "responses": [
            "By sending a message to the teacher.",
            "By visiting the HR office on the third floor.",
            "By filling out the form on the intranet site.",
        ],
        "answer": "C",
        "rationale": "Option C gives the official registration method. A and B suggest other contacts that are not identified as the correct sign-up process."
    },
    # 92: A
    {
        "level": "B1",
        "question": "Why is the office being rearranged this weekend?",
        "responses": [
            "To make space for a new team.",
            "To prepare for the company anniversary.",
            "To install new kitchen equipment."
        ],
        "answer": "A",
        "rationale": "Option A explains a staffing-related reason, which suits rearranging desks. B and C mention events and equipment not clearly connected to layout changes."
    },
    # 93: B
    {
        "level": "B1",
        "question": "What does the announcement say about personal belongings?",
        "responses": [
            "They must be checked at security.",
            "They should not be left unattended.",
            "They need to be labeled with names."
        ],
        "answer": "B",
        "rationale": "Option B warns about leaving items unattended, a common safety message. A and C add requirements not mentioned in the notice."
    },
    # 94: C
    {
        "level": "B1",
        "question": "How should participants confirm that they received the documents?",
        "responses": [
            "By returning them by post.",
            "By signing at the reception desk.",
            "By sending a short reply e-mail.",
        ],
        "answer": "C",
        "rationale": "Option C describes a quick confirmation method that matches the context of sending documents. A and B use slower or different confirmation methods."
    },
    # 95: A
    {
        "level": "B1",
        "question": "Why is the speaker apologizing to the customers?",
        "responses": [
            "Because the order will arrive later than expected.",
            "Because the store will be closed tomorrow.",
            "Because the phone lines are busy."
        ],
        "answer": "A",
        "rationale": "Option A explains a delayed order, which commonly requires an apology. B and C mention other issues not clearly linked to this apology."
    },
    # 96: B
    {
        "level": "B1",
        "question": "What does the woman say about the printer?",
        "responses": [
            "It needs new paper.",
            "It is out of ink again.",
            "It is going to be replaced soon."
        ],
        "answer": "B",
        "rationale": "Option B states the current problem with the printer. A and C mention different conditions not identified as the present issue."
    },
    # 97: C
    {
        "level": "B1",
        "question": "How can staff get help with using the new system?",
        "responses": [
            "By reading the manual at home.",
            "By asking their clients directly.",
            "By attending a short training session.",
        ],
        "answer": "C",
        "rationale": "Option C provides the official support method for learning the system. A and B mention actions that are less effective or inappropriate."
    },
    # 98: A
    {
        "level": "B1",
        "question": "Why does the manager want to reschedule the interview?",
        "responses": [
            "He has to attend an urgent meeting.",
            "He has already hired someone else.",
            "He prefers to do it online."
        ],
        "answer": "A",
        "rationale": "Option A gives a schedule conflict, which is a realistic reason for rescheduling. B and C introduce different situations not stated in the context."
    },
    # 99: B
    {
        "level": "B1",
        "question": "What does the speaker say about the company picnic?",
        "responses": [
            "It will be held at a different park.",
            "It will be postponed if it rains.",
            "It will be canceled this year."
        ],
        "answer": "B",
        "rationale": "Option B describes a conditional postponement due to weather, which matches a typical announcement. A and C describe other changes not given."
    },
    # 100: C
    {
        "level": "B1",
        "question": "How are employees asked to respond to the invitation?",
        "responses": [
            "By giving the card back to the receptionist.",
            "By calling the organizer’s mobile phone.",
            "By clicking the link in the e-mail.",
        ],
        "answer": "C",
        "rationale": "Option C matches an e-mail invitation with a response link. A and B describe different reply methods not specified in the message."
    },

    # --- B2 level 30patterns (more challenging) ---
    {
        "level": "B2",
        "question": "Would you mind taking over my presentation if the video call drops again?",
        "responses": [
            "I can do that, so please send me your slides beforehand.",
            "Yes, it will probably start a little later than planned.",
            "The room is already booked for another department."
        ],
        "answer": "A",
        "rationale": "Option A directly and appropriately agrees to take over and asks for the slides, which matches the request. B talks about timing, and C mentions room usage, so they do not address the favor."
    },
    {
        "level": "B2",
        "question": "I’m not sure these figures are accurate. What should we do before we send the report?",
        "responses": [
            "Let’s check them against last quarter’s data once more.",
            "I already sent a reminder to the whole team yesterday.",
            "We can ask the client to sign the contract next week."
        ],
        "answer": "A",
        "rationale": "Option A suggests verifying the figures, which responds to the concern about accuracy. B and C are about unrelated actions."
    },
    {
        "level": "B2",
        "question": "Do you think we can still meet the deadline if the designer is on leave this week?",
        "responses": [
            "Only if we reduce the number of layout changes we request.",
            "We’re planning to invite the client to the next workshop.",
            "The printer said they can deliver sooner than expected."
        ],
        "answer": "A",
        "rationale": "Option A gives a conditional answer directly tied to the deadline and the missing designer. B and C mention other plans that are not connected to the deadline issue."
    },
    {
        "level": "B2",
        "question": "I’m worried the client might not like the new pricing. How should we approach the meeting?",
        "responses": [
            "We could start by explaining the added services before showing the numbers.",
            "We should probably move the meeting to a larger conference room.",
            "We might need to ask the finance team to review the budget again."
        ],
        "answer": "A",
        "rationale": "Option A talks about the strategy for presenting the pricing, which matches the concern. B is about room size, and C is about internal review, not meeting approach."
    },
    {
        "level": "B2",
        "question": "Since the software update changed the interface, how can we help the team adjust quickly?",
        "responses": [
            "We could organize a short training session with live demonstrations.",
            "We should ask the supplier to send the replacement parts soon.",
            "We might want to repaint the reception area this summer."
        ],
        "answer": "A",
        "rationale": "Option A is directly about supporting the team with the new interface. B and C are completely unrelated topics."
    },
    {
        "level": "B2",
        "question": "If the client cancels tomorrow’s visit at the last minute, what would be the best way to react?",
        "responses": [
            "We should politely suggest a video call so we can still review the proposal.",
            "We could order extra snacks in case more guests arrive unexpectedly.",
            "We should ask the IT department to replace the router immediately."
        ],
        "answer": "A",
        "rationale": "Option A proposes a constructive alternative to a canceled visit. B and C do not address the cancellation scenario."
    },
    {
        "level": "B2",
        "question": "The hotel has overbooked our rooms, so what can we do to avoid upsetting the team?",
        "responses": [
            "We might arrange transportation to a nearby hotel and cover the cost.",
            "We can ask them to move the meeting to the afternoon session.",
            "We should ask everyone to submit their travel receipts by Friday."
        ],
        "answer": "A",
        "rationale": "Option A presents a concrete solution to the overbooking problem. B and C deal with different issues unrelated to lodging."
    },
    {
        "level": "B2",
        "question": "Given that the supplier keeps delaying the shipment, how should we handle the next negotiation?",
        "responses": [
            "We could request a small discount and a written delivery schedule.",
            "We might want to invite them to the company’s year-end party.",
            "We should ask our interns to help with the data entry work."
        ],
        "answer": "A",
        "rationale": "Option A addresses both the delays and the negotiation strategy. B and C are unrelated social and internal tasks."
    },
    {
        "level": "B2",
        "question": "If we move the training session online, what potential problem do you see?",
        "responses": [
            "Some staff may not have a quiet place at home to join the session.",
            "The cafeteria might need to change the lunch menu this week.",
            "The parking lot is usually full after eight in the morning."
        ],
        "answer": "A",
        "rationale": "Option A points out a realistic drawback of online training. B and C talk about unrelated facility issues."
    },
    {
        "level": "B2",
        "question": "I’m afraid our presentation is too technical for the audience. How can we make it clearer?",
        "responses": [
            "We should replace some charts with simple examples and shorter sentences.",
            "We can extend the Q&A session so that it lasts for one full hour.",
            "We might send the slides only to people who attended last year."
        ],
        "answer": "A",
        "rationale": "Option A addresses clarity by simplifying the content. B and C adjust format or distribution but not understandability."
    },
    {
        "level": "B2",
        "question": "Since the customer is still unhappy after our apology, what else could we offer?",
        "responses": [
            "We might give them a partial refund and a discount on their next order.",
            "We can ask them to write a detailed review on our website.",
            "We should tell them that all complaints must be sent by e-mail."
        ],
        "answer": "A",
        "rationale": "Option A suggests a concrete gesture to restore satisfaction. B and C would likely make the situation worse."
    },
    {
        "level": "B2",
        "question": "If the new policy is confusing to staff, how can we gather useful feedback?",
        "responses": [
            "We could create an anonymous survey and share it at the end of the week.",
            "We might ask everyone to stay at their desks during lunchtime.",
            "We can rearrange the office furniture to make more open space."
        ],
        "answer": "A",
        "rationale": "Option A offers a direct way to collect opinions about the policy. B and C are unrelated decisions."
    },
    {
        "level": "B2",
        "question": "Because several team members are working remotely, how can we keep communication smooth?",
        "responses": [
            "We should schedule short daily check-ins and use one shared chat channel.",
            "We need to print all documents and store them in the main office.",
            "We can ask them to submit their vacation requests in writing."
        ],
        "answer": "A",
        "rationale": "Option A provides specific actions to improve communication for remote work. B and C are administrative tasks."
    },
    {
        "level": "B2",
        "question": "Now that the project has fallen behind schedule, what should we tell the client?",
        "responses": [
            "We ought to explain the reason honestly and present a revised timeline.",
            "We should ask them to send more staff to help our team.",
            "We could ignore the delay and send the original plan anyway."
        ],
        "answer": "A",
        "rationale": "Option A suggests transparent communication and a concrete plan. B is unrealistic, and C is irresponsible."
    },
    {
        "level": "B2",
        "question": "If the workshop runs longer than expected, how can we minimize the disruption?",
        "responses": [
            "We can shorten the final activity and send the remaining materials by e-mail.",
            "We should cancel all future workshops for the rest of the year.",
            "We might not allow any questions from the participants at all."
        ],
        "answer": "A",
        "rationale": "Option A offers a balanced way to handle a time overrun. B and C are extreme and unhelpful responses."
    },
    {
        "level": "B2",
        "question": "The candidate’s experience looks impressive, but what should we ask during the interview?",
        "responses": [
            "We should ask for specific examples of how they handled difficult clients.",
            "We can tell them the salary range and end the interview quickly.",
            "We might ask them to sign the contract before speaking with HR."
        ],
        "answer": "A",
        "rationale": "Option A suggests a focused, behavior-based question relevant to the role. B and C skip proper evaluation steps."
    },
    {
        "level": "B2",
        "question": "If the printer breaks down again right before the deadline, what’s our safest backup plan?",
        "responses": [
            "We could keep a digital copy ready and use a nearby copy shop if needed.",
            "We should ask everyone to stop using color ink in their reports.",
            "We might cancel the deadline and start the project from scratch."
        ],
        "answer": "A",
        "rationale": "Option A outlines a realistic contingency plan. B and C are unrelated or extreme measures."
    },
    {
        "level": "B2",
        "question": "Given that some employees feel uncomfortable speaking in large meetings, what can we do?",
        "responses": [
            "We could collect their opinions in small groups or through written comments.",
            "We might move all meetings to an earlier time in the morning.",
            "We should ask them to give longer presentations each week."
        ],
        "answer": "A",
        "rationale": "Option A reduces pressure and offers alternative ways to share ideas. B and C ignore the issue or make it worse."
    },
    {
        "level": "B2",
        "question": "The budget for travel has been reduced. How should we change our visit schedule?",
        "responses": [
            "We should combine trips so that we can meet several clients in one visit.",
            "We can book the most expensive hotel to impress our main client.",
            "We might stop answering calls from smaller customers completely."
        ],
        "answer": "A",
        "rationale": "Option A suggests an efficient adjustment consistent with a smaller budget. B and C go against the constraint or client service."
    },
    {
        "level": "B2",
        "question": "Since the training materials are only available in English, what problem might arise?",
        "responses": [
            "Some participants may struggle to follow the content or ask questions.",
            "The office might need to order more paper and pens for the session.",
            "The instructor may have to turn off the lights in the classroom."
        ],
        "answer": "A",
        "rationale": "Option A correctly identifies a language barrier as a likely issue. B and C do not relate to the language of the materials."
    },
    {
        "level": "B2",
        "question": "If the team keeps missing internal deadlines, what should we review first?",
        "responses": [
            "We should check whether the workload and priorities are clear to everyone.",
            "We might redecorate the office to make it look more modern.",
            "We can ask the clients to change their product requirements again."
        ],
        "answer": "A",
        "rationale": "Option A targets the internal process causing delays. B and C focus on unrelated cosmetic or client-side changes."
    },
    {
        "level": "B2",
        "question": "A few customers have complained about slow responses. How can we improve our service?",
        "responses": [
            "We could set a standard reply time and monitor how quickly we answer.",
            "We should ask customers to call only during lunchtime.",
            "We might stop using e-mail and rely on paper letters instead."
        ],
        "answer": "A",
        "rationale": "Option A introduces a measurable service standard. B and C would likely worsen the response time issue."
    },
    {
        "level": "B2",
        "question": "The project review meeting is likely to be tense. How should we prepare the team?",
        "responses": [
            "We should go over the key issues together and agree on who will explain each point.",
            "We can shorten the meeting by skipping the question-and-answer portion.",
            "We might bring snacks so that people will not leave the room early."
        ],
        "answer": "A",
        "rationale": "Option A focuses on preparing clear explanations and roles, which fits the situation. B and C avoid the real issue."
    },
    {
        "level": "B2",
        "question": "If the conference program changes at the last minute, what should we tell the participants?",
        "responses": [
            "We ought to send an updated schedule and highlight the main differences clearly.",
            "We should ask them to find the information by checking the posters themselves.",
            "We might cancel all afternoon talks without any explanation."
        ],
        "answer": "A",
        "rationale": "Option A provides transparent communication about changes. B and C place the burden on participants or offer no explanation."
    },
    {
        "level": "B2",
        "question": "Since our intern made a serious mistake, how can we turn this into a learning chance?",
        "responses": [
            "We could review what went wrong with them and show how to avoid it next time.",
            "We should stop giving any tasks to interns for the rest of the year.",
            "We might move the intern to a desk far away from the rest of the team."
        ],
        "answer": "A",
        "rationale": "Option A is constructive and educational. B and C are overly negative and do not promote learning."
    },
    {
        "level": "B2",
        "question": "If the online system is down during business hours, how can we keep taking orders?",
        "responses": [
            "We can accept orders by phone and enter them into the system later.",
            "We should ask customers to try again after the weekend holiday.",
            "We might tell customers that we are closing the store permanently."
        ],
        "answer": "A",
        "rationale": "Option A offers a practical temporary solution. B and C unnecessarily delay or exaggerate the situation."
    },
    {
        "level": "B2",
        "question": "Our new colleague seems hesitant to share ideas. What might help them participate more?",
        "responses": [
            "We could ask for their opinion on smaller topics first in a relaxed setting.",
            "We should assign them the most difficult task in the project immediately.",
            "We might tell them not to speak until they fully understand everything."
        ],
        "answer": "A",
        "rationale": "Option A gently encourages contribution in a low-pressure way. B and C are likely to increase anxiety."
    },
    {
        "level": "B2",
        "question": "If the doctor’s appointment schedule is fully booked today, what should the receptionist suggest?",
        "responses": [
            "They can offer the first available slot tomorrow and add the patient to a waiting list.",
            "They should ask the patient to come without an appointment and wait all day.",
            "They might refuse to speak with the patient and end the call quickly."
        ],
        "answer": "A",
        "rationale": "Option A provides a reasonable alternative with a waiting list. B and C show poor service."
    },
    {
        "level": "B2",
        "question": "Because the exam results were lower than expected, what could the teacher do?",
        "responses": [
            "The teacher could review common mistakes in class and adjust future lessons.",
            "The teacher should give exactly the same exam again next week.",
            "The teacher might ignore the results and keep the same homework."
        ],
        "answer": "A",
        "rationale": "Option A uses the results to improve teaching. B and C repeat or ignore the problem."
    },
    {
        "level": "B2",
        "question": "If the restaurant receives many online reviews about slow service, what change would be helpful?",
        "responses": [
            "They might add one more server during busy hours to shorten waiting times.",
            "They should remove the dessert menu and serve only drinks.",
            "They can ask customers not to post any comments on the internet."
        ],
        "answer": "A",
        "rationale": "Option A responds directly to the complaint by increasing staff when needed. B and C do not solve the core issue."
    },
]

def _auto_topic_from_question(question: str, max_words: int = 3) -> list[str]:
    #"""
    #Part2のquestionから、内容語っぽい単語を抜き出して topic にする。
    #例: "Could you send me the draft by noon?"
    #    → ["send", "draft", "noon"]
    #"""
    if not isinstance(question, str):
        return ["question"]

    # よくある機能語・疑問詞は除外する簡易ストップリスト
    stop_words = {
        "the", "a", "an", "to", "for", "in", "on", "at", "of",
        "is", "are", "was", "were", "do", "does", "did",
        "you", "we", "they", "he", "she", "it",
        "this", "that", "these", "those",
        "will", "can", "could", "would", "should", "must",
        "why", "how", "what", "when", "where", "who", "whom", "which"
    }

    # 記号を軽く取り除いて小文字化
    raw_words = [
        w.strip("?,.!").lower()
        for w in question.split()
        if w.strip("?,.!")
    ]

    # 内容語だけに絞る
    content = [w for w in raw_words if w not in stop_words]

    if content:
        return content[:max_words]
    # 万一全部ストップワードだった場合は、とりあえず先頭から数語
    if raw_words:
        return raw_words[:max_words]
    return ["question"]


# すべてのパターンに topic を付与（既にtopicがある場合は尊重）
for p in PART2_PATTERNS:
    if "topic" not in p:
        q = p.get("question", "")
        p["topic"] = _auto_topic_from_question(q)
