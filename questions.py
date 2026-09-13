INTEREST_QUESTIONS = [
    {
        "id": 1,
        "type": "interest",
        "question": "If you were given PKR 500,000 to lead a university project, which role would you choose?",
        "options": {
            "A": "Build a software app or automated dashboard for student productivity.",
            "B": "Design the branding, UI/UX, and marketing campaigns.",
            "C": "Analyze budget distribution, calculate ROI, and manage investment logistics.",
            "D": "Conduct lab research or develop a health/safety awareness program."
        },
        "tag_mapping": {"A": ["coding", "automation"], "B": ["design", "creativity"], "C": ["money", "business"], "D": ["lab", "health"]}
    },
    {
        "id": 2,
        "type": "interest",
        "question": "Which type of content do you find yourself consuming most frequently online?",
        "options": {
            "A": "Tech reviews, coding tutorials, AI developments, or cyber hacks.",
            "B": "Stock market trends, crypto analysis, business success stories.",
            "C": "Design portfolios, video editing breakdowns, digital art.",
            "D": "Scientific breakdowns, medical breakthroughs, or nature documentaries."
        },
        "tag_mapping": {"A": ["technology", "coding"], "B": ["business", "money"], "C": ["creativity", "media"], "D": ["research", "nature"]}
    },
    {
        "id": 3,
        "type": "interest",
        "question": "During a free weekend, which activity sounds most fulfilling to you?",
        "options": {
            "A": "Customizing your PC/phone settings, playing strategy games, or tinkering with smart tools.",
            "B": "Drafting articles, designing graphics, or working on freelance creative gigs.",
            "C": "Tutoring younger students or planning a social community service drive.",
            "D": "Reading about economics, managing a personal budget, or studying market trends."
        },
        "tag_mapping": {"A": ["hardware", "problem_solving"], "B": ["design", "writing"], "C": ["teaching", "helping"], "D": ["charts", "money"]}
    },
    {
        "id": 4,
        "type": "interest",
        "question": "When solving a real-world problem, what is your preferred approach?",
        "options": {
            "A": "Write a script or process to automate the repetitive parts.",
            "B": "Visualize data and charts to identify logical patterns.",
            "C": "Talk directly to people to understand their emotional and social needs.",
            "D": "Investigate underlying physical, biological, or chemical root causes."
        },
        "tag_mapping": {"A": ["automation", "coding"], "B": ["data", "charts"], "C": ["helping", "teaching"], "D": ["lab", "nature"]}
    },
    {
        "id": 5,
        "type": "interest",
        "question": "What kind of work environment excites you the most?",
        "options": {
            "A": "A remote setup earning in USD via global freelancing platforms.",
            "B": "A fast-paced IT software house or AI lab.",
            "C": "A corporate banking tower or financial consulting room.",
            "D": "A modern hospital, biological laboratory, or research facility."
        },
        "tag_mapping": {"A": ["creativity", "coding"], "B": ["technology", "problem_solving"], "C": ["business", "money"], "D": ["health", "research"]}
    },
    {
        "id": 6,
        "type": "interest",
        "question": "If you were asked to solve an issue in Pakistan's agriculture or health sector, you would prefer to:",
        "options": {
            "A": "Deploy IoT sensors and automated drone software for crop health.",
            "B": "Develop novel bio-fertilizers or genetic research models.",
            "C": "Create an educational portal to train farmers and workers.",
            "D": "Analyze market price fluctuations and supply chain data."
        },
        "tag_mapping": {"A": ["hardware", "automation"], "B": ["lab", "research"], "C": ["teaching", "writing"], "D": ["data", "business"]}
    },
    {
        "id": 7,
        "type": "interest",
        "question": "Imagine you are launching a startup with friends. What role fits you naturally?",
        "options": {
            "A": "Chief Technology Officer (CTO) managing backend tech.",
            "B": "Chief Design Officer (CDO) crafting customer experience.",
            "C": "Chief Financial Officer (CFO) handling accounting and revenue.",
            "D": "Chief Research Officer (CRO) testing biological/scientific viability."
        },
        "tag_mapping": {"A": ["coding", "technology"], "B": ["design", "creativity"], "C": ["money", "charts"], "D": ["research", "health"]}
    },
    {
        "id": 8,
        "type": "interest",
        "question": "What kind of dynamic challenges keep you engaged without stressing you out?",
        "options": {
            "A": "Debugging complex logical errors in a system.",
            "B": "Fixing security vulnerabilities and investigating breaches.",
            "C": "Balancing complex equations, spreadsheets, and budgets.",
            "D": "Diagnosing symptoms and coming up with care solutions."
        },
        "tag_mapping": {"A": ["problem_solving", "coding"], "B": ["security", "investigation"], "C": ["math", "charts"], "D": ["health", "helping"]}
    },
    {
        "id": 9,
        "type": "interest",
        "question": "Which global trend in the Pakistani market excites you the most?",
        "options": {
            "A": "The rise of Generative AI tools and automated agents.",
            "B": "The booming freelance economy and international remote work.",
            "C": "The expansion of FinTech apps like Nayapay, Sadapay, and JazzCash.",
            "D": "Advanced biotech developments and health-tech solutions."
        },
        "tag_mapping": {"A": ["automation", "data"], "B": ["creativity", "writing"], "C": ["money", "business"], "D": ["health", "lab"]}
    },
    {
        "id": 10,
        "type": "interest",
        "question": "If you were to publish a blog post today, what would the topic be?",
        "options": {
            "A": "How to optimize code or secure your online privacy.",
            "B": "Strategies for investing and building wealth as a student.",
            "C": "A guide to modern UI design and creative content creation.",
            "D": "The impact of climate change or new scientific discoveries."
        },
        "tag_mapping": {"A": ["security", "coding"], "B": ["money", "business"], "C": ["design", "writing"], "D": ["nature", "research"]}
    }
]

APTITUDE_QUESTIONS = [
    {
        "id": 11,
        "type": "aptitude",
        "category": "logic",
        "question": "Look at this series: 2, 6, 12, 20, 30, ... What number should come next?",
        "options": {"A": "36", "B": "40", "C": "42", "D": "48"},
        "correct": "C"
    },
    {
        "id": 12,
        "type": "aptitude",
        "category": "math",
        "question": "A product price in Pakistan increased by 20% and then decreased by 20%. What is the net percentage change?",
        "options": {"A": "No change (0%)", "B": "4% increase", "C": "4% decrease", "D": "2% decrease"},
        "correct": "C"
    },
    {
        "id": 13,
        "type": "aptitude",
        "category": "analytical",
        "question": "If all Software Engineers are Problem Solvers, and some Problem Solvers are Designers, which statement MUST be true?",
        "options": {
            "A": "All Designers are Software Engineers.",
            "B": "Some Software Engineers might be Designers.",
            "C": "No Software Engineer is a Designer.",
            "D": "All Problem Solvers are Software Engineers."
        },
        "correct": "B"
    },
    {
        "id": 14,
        "type": "aptitude",
        "category": "english",
        "question": "Choose the word that is most nearly OPPOSITE in meaning to 'AMBIGUOUS':",
        "options": {"A": "Vague", "B": "Explicit", "C": "Equivocal", "D": "Complex"},
        "correct": "B"
    },
    {
        "id": 15,
        "type": "aptitude",
        "category": "science",
        "question": "In computer science and biological modeling, what is the basic function of an enzyme or algorithmic catalyst?",
        "options": {
            "A": "To increase activation energy.",
            "B": "To decrease activation energy and speed up reactions.",
            "C": "To act as a permanent energy storage unit.",
            "D": "To destroy waste products completely."
        },
        "correct": "B"
    },
    {
        "id": 16,
        "type": "aptitude",
        "category": "problem_solving",
        "question": "A server processes 150 requests every 3 minutes. How many requests can 4 identical servers process in 10 minutes?",
        "options": {"A": "1,500", "B": "2,000", "C": "1,200", "D": "3,000"},
        "correct": "B"
    },
    {
        "id": 17,
        "type": "aptitude",
        "category": "math",
        "question": "What is the median of the following set of dataset scores: [14, 7, 22, 19, 3, 11, 28]?",
        "options": {"A": "14", "B": "16", "C": "19", "D": "11"},
        "correct": "A"
    },
    {
        "id": 18,
        "type": "aptitude",
        "category": "analytical",
        "question": "A dataset contains 80% training data and 20% test data. If the total dataset has 2,500 samples, how many samples are in the test set?",
        "options": {"A": "400", "B": "500", "C": "600", "D": "2000"},
        "correct": "B"
    },
    {
        "id": 19,
        "type": "aptitude",
        "category": "english",
        "question": "Complete the sentence logically: 'Despite the severe network latency, the remote developer _____ delivered the project on time.'",
        "options": {"A": "reluctantly", "B": "successfully", "C": "scarcely", "D": "adversely"},
        "correct": "B"
    },
    {
        "id": 20,
        "type": "aptitude",
        "category": "logic",
        "question": "If 'TECH' is coded as '20-5-3-8' based on alphabetical positions, how would 'DATA' be coded?",
        "options": {"A": "4-1-20-1", "B": "4-1-19-1", "C": "3-1-20-1", "D": "4-2-20-2"},
        "correct": "A"
    }
]
