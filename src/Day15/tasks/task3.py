prob_spam=0.1
prob_ham=0.9
prob_free_given_spam=0.9
prob_free_given_ham=0.05

#Formula
prob_free=(prob_free_given_spam * prob_spam) + (prob_free_given_ham * prob_ham)


prob_spam_given_free=(prob_free_given_spam*prob_spam)/prob_free

print("\nTotal Probability of 'Free'",prob_free)
print("Probability for email with 'Free' is actually Spam: ",prob_spam_given_free)
