# Simplified High-School Level Questions (10 Interest + 10 Aptitude)

INTEREST_QUESTIONS = [
    {
        "id": 1,
        "type": "interest",
        "question": "If your school asks you to lead a group project for a science exhibition, which role would you prefer?",
        "options": {
            "A": "Create a computer program or mobile app for the display.",
            "B": "Design posters, graphics, and video presentations.",
            "C": "Manage the project budget, buy materials, and calculate costs.",
            "D": "Conduct experiments on biology, health, or environmental science."
        },
        "tag_mapping": {"A": ["coding", "automation"], "B": ["design", "creativity"], "C": ["money", "business"], "D": ["lab", "health"]}
    },
    {
        "id": 2,
        "type": "interest",
        "question": "What kind of YouTube videos or social media posts do you enjoy watching most?",
        "options": {
            "A": "Tech reviews, coding tutorials, or video game development.",
            "B": "Business stories, stock trading tips, or money tips for teenagers.",
            "C": "Graphic design tips, digital art tutorials, or video editing tricks.",
            "D": "Science experiments, medical facts, or nature discoveries."
        },
        "tag_mapping": {"A": ["technology", "coding"], "B": ["business", "money"], "C": ["creativity", "media"], "D": ["research", "nature"]}
    },
    {
        "id": 3,
        "type": "interest",
        "question": "How do you prefer spending your free time at home?",
        "options": {
            "A": "Customizing computer software, playing strategy games, or solving puzzles.",
            "B": "Drawing graphics, writing stories, or editing photos/videos.",
            "C": "Helping younger classmates study or organizing community social work.",
            "D": "Reading about business ideas, saving money, or tracking small profits."
        },
        "tag_mapping": {"A": ["hardware", "problem_solving"], "B": ["design", "writing"], "C": ["teaching", "helping"], "D": ["charts", "money"]}
    },
    {
        "id": 4,
        "type": "interest",
        "question": "When you face a daily task or problem, what is your natural reaction?",
        "options": {
            "A": "Find a smart tool or write a computer trick to do it faster.",
            "B": "Look at numbers, tables, or charts to understand what happened.",
            "C": "Talk to friends or family to understand how they feel and help them.",
            "D": "Investigate the science or mechanics behind how things work."
        },
        "tag_mapping": {"A": ["automation", "coding"], "B": ["data", "charts"], "C": ["helping", "teaching"], "D": ["lab", "nature"]}
    },
    {
        "id": 5,
        "type": "interest",
        "question": "Which dream job setting sounds most exciting to you?",
        "options": {
            "A": "Working remotely on a laptop earning in US Dollars through online freelancing.",
            "B": "Working in a modern software house or artificial intelligence studio.",
            "C": "Working in a busy corporate bank or managing investments.",
            "D": "Working in a well-equipped hospital or biological research laboratory."
        },
        "tag_mapping": {"A": ["creativity", "coding"], "B": ["technology", "problem_solving"], "C": ["business", "money"], "D": ["health", "research"]}
    },
    {
        "id": 6,
        "type": "interest",
        "question": "If you could fix one problem in your local city or village, you would choose to:",
        "options": {
            "A": "Build automated smart devices or solar technology solutions.",
            "B": "Research ways to improve crop growth and plant health.",
            "C": "Set up free online learning platforms for young students.",
            "D": "Help local shopkeepers manage sales, prices, and profits better."
        },
        "tag_mapping": {"A": ["hardware", "automation"], "B": ["lab", "research"], "C": ["teaching", "writing"], "D": ["data", "business"]}
    },
    {
        "id": 7,
        "type": "interest",
        "question": "If you and your friends started a small business, what role would you take?",
        "options": {
            "A": "Handling the website, apps, and computer systems.",
            "B": "Designing logos, advertisements, and product packaging.",
            "C": "Managing accounts, price lists, and cash flow.",
            "D": "Testing and improving product quality and science."
        },
        "tag_mapping": {"A": ["coding", "technology"], "B": ["design", "creativity"], "C": ["money", "charts"], "D": ["research", "health"]}
    },
    {
        "id": 8,
        "type": "interest",
        "question": "Which of these tasks feels fun and satisfying to complete?",
        "options": {
            "A": "Finding and fixing bugs in a program or computer error.",
            "B": "Checking internet security settings and protecting accounts.",
            "C": "Solving math equations or balancing a spreadsheet.",
            "D": "Understanding medical symptoms and learning how to treat illnesses."
        },
        "tag_mapping": {"A": ["problem_solving", "coding"], "B": ["security", "investigation"], "C": ["math", "charts"], "D": ["health", "helping"]}
    },
    {
        "id": 9,
        "type": "interest",
        "question": "Which modern trend in Pakistan interests you the most?",
        "options": {
            "A": "Artificial Intelligence tools like ChatGPT and digital helpers.",
            "B": "Earning money online through graphic design, writing, or freelancing.",
            "C": "Digital payment apps like EasyPaisa, JazzCash, Nayapay, or Sadapay.",
            "D": "New medical technology and health applications."
        },
        "tag_mapping": {"A": ["automation", "data"], "B": ["creativity", "writing"], "C": ["money", "business"], "D": ["health", "lab"]}
    },
    {
        "id": 10,
        "type": "interest",
        "question": "If you had to write a simple essay or article today, what would it be about?",
        "options": {
            "A": "How to keep your mobile phone and online accounts safe from hackers.",
            "B": "Smart ways high school students can save and earn pocket money.",
            "C": "Tips for creating eye-catching social media designs.",
            "D": "How modern science is helping fight diseases and climate change."
        },
        "tag_mapping": {"A": ["security", "coding"], "B": ["money", "business"], "C": ["design", "writing"], "D": ["nature", "research"]}
    }
]

APTITUDE_QUESTIONS = [
    {
        "id": 11,
        "type": "aptitude",
        "category": "logic",
        "question": "What is the next number in this simple pattern: 5, 10, 15, 20, ... ?",
        "options": {"A": "22", "B": "25", "C": "30", "D": "35"},
        "correct": "B"
    },
    {
        "id": 12,
        "type": "aptitude",
        "category": "math",
        "question": "If a shirt costs PKR 1,000 and has a 20% discount, what is the final price you pay?",
        "options": {"A": "PKR 700", "B": "PKR 800", "C": "PKR 850", "D": "PKR 900"},
        "correct": "B"
    },
    {
        "id": 13,
        "type": "aptitude",
        "category": "analytical",
        "question": "All doctors studied science. Ali is a doctor. What can we logically say about Ali?",
        "options": {
            "A": "Ali studied science.",
            "B": "Ali never studied science.",
            "C": "Ali is an engineer.",
            "D": "Ali studied art."
        },
        "correct": "A"
    },
    {
        "id": 14,
        "type": "aptitude",
        "category": "english",
        "question": "Which word means the OPPOSITE of 'SIMPLE'?",
        "options": {"A": "Easy", "B": "Complex", "C": "Clear", "D": "Small"},
        "correct": "B"
    },
    {
        "id": 15,
        "type": "aptitude",
        "category": "science",
        "question": "Which gas do plants absorb from the air during photosynthesis?",
        "options": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Helium"},
        "correct": "B"
    },
    {
        "id": 16,
        "type": "aptitude",
        "category": "problem_solving",
        "question": "If 1 worker can finish a task in 6 hours, how many hours will 2 workers take working at the same speed?",
        "options": {"A": "3 hours", "B": "6 hours", "C": "12 hours", "D": "2 hours"},
        "correct": "A"
    },
    {
        "id": 17,
        "type": "aptitude",
        "category": "math",
        "question": "What is the average (mean) of these three marks: 70, 80, and 90?",
        "options": {"A": "75", "B": "80", "C": "85", "D": "240"},
        "correct": "B"
    },
    {
        "id": 18,
        "type": "aptitude",
        "category": "analytical",
        "question": "A school class has 50 students. If 60% of them are girls, how many girls are in the class?",
        "options": {"A": "20", "B": "25", "C": "30", "D": "35"},
        "correct": "C"
    },
    {
        "id": 19,
        "type": "aptitude",
        "category": "english",
        "question": "Choose the correct word to complete the sentence: 'Sarah study hard every day so she _____ high marks in her exams.'",
        "options": {"A": "gets", "B": "get", "C": "getting", "D": "gotten"},
        "correct": "A"
    },
    {
        "id": 20,
        "type": "aptitude",
        "category": "logic",
        "question": "If A = 1, B = 2, C = 3, what is the total value of CAT (C + A + T where T=20)?",
        "options": {"A": "22", "B": "24", "C": "26", "D": "20"},
        "correct": "B"
    }
]
