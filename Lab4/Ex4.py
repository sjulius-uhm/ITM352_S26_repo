# Try to append to a tuple.  It won't work!
# Samantha Julius
# Date: Feb. 1, 2026

survey_respondents = (1012, 1035, 1021, 1053)
print("Original survey respondents tuple:", survey_respondents)
#survey_respondents.append(1054)  # This will raise an AttributeError
survey_respondents = survey_respondents + (1054,)
print("After adding 1054:", survey_respondents)