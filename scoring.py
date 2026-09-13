from careers import CAREER_DATABASE

def calculate_scores(user_answers, interest_questions, aptitude_questions):
    interest_scores = {}
    for q in interest_questions:
        q_id = q["id"]
        selected_option = user_answers.get(q_id)
        if selected_option:
            tags = q["tag_mapping"].get(selected_option, [])
            for tag in tags:
                interest_scores[tag] = interest_scores.get(tag, 0) + 1

    max_interest = max(interest_scores.values()) if interest_scores else 1
    normalized_interests = {k: v / max_interest for k, v in interest_scores.items()}

    aptitude_totals = {"logic": 0, "math": 0, "analytical": 0, "english": 0, "science": 0, "problem_solving": 0}
    aptitude_correct = {"logic": 0, "math": 0, "analytical": 0, "english": 0, "science": 0, "problem_solving": 0}

    for q in aptitude_questions:
        q_id = q["id"]
        cat = q["category"]
        aptitude_totals[cat] = aptitude_totals.get(cat, 0) + 1
        
        selected_option = user_answers.get(q_id)
        if selected_option == q["correct"]:
            aptitude_correct[cat] = aptitude_correct.get(cat, 0) + 1

    aptitude_percentages = {}
    for cat, total in aptitude_totals.items():
        if total > 0:
            aptitude_percentages[cat] = aptitude_correct[cat] / total
        else:
            aptitude_percentages[cat] = 0.5

    career_rankings = []

    for career_name, profile in CAREER_DATABASE.items():
        matching_tags = [tag for tag in profile["interest_tags"] if tag in interest_scores]
        interest_match_score = len(matching_tags) / len(profile["interest_tags"]) if profile["interest_tags"] else 0.5

        aptitude_match_score = 0.0
        for cat, weight in profile["aptitude_weights"].items():
            score = aptitude_percentages.get(cat, 0.5)
            aptitude_match_score += score * weight

        combined_score = round((interest_match_score * 0.5 + aptitude_match_score * 0.5) * 100, 1)

        career_rankings.append({
            "career": career_name,
            "suitability_score": combined_score,
            "interest_score": round(interest_match_score * 100, 1),
            "aptitude_score": round(aptitude_match_score * 100, 1),
            "details": profile
        })

    career_rankings.sort(key=lambda x: x["suitability_score"], reverse=True)

    return career_rankings[:3], aptitude_percentages, interest_scores
