import chatgpt

def evaluate_sentence_evidence(gpt_sentence, evidence):
    compare_prompt = f'''
    Using the GPT-Sentence and Evidence below, if the GPT-Sentence disagrees with the Evidence, return using the
    format below. Also, rephrase the disagreeing sentence/sentences from the Evidence into a single
    sentence called Correct-Sentence that has the same structure as our GPT-Sentence. For example, if our GPT-Sentence was
    "He went on to pursue his Ph.D. in Mathematics, which he obtained in 1997 from the University of Chicago"
    but the corresponding sentence from the Evidence was "He received his Ph.D. in 2000 from the University of California,
    Berkeley under the joint supervision of Andrew Casson and William Thurston; his dissertation concerned foliations of three-dimensional manifolds,"
    Correct-Sentence should be
    "He received his Ph.D. in 2000 from the University of California, Berkeley," which has the
    same words as the GPT-Sentence and only changes the part that disagrees (University of Chicago to University of California). It does not mention Andrew Casson, WIlliam Thurston, or manifolds because they are unrelated to our GPT-Sentence.

    Desired format:
    Likely Wrong, Evidence: <Correct-Sentence>

    If the evidence contains a statement or statements
    that agree with the GPT-Sentence, return using the format below.

    Desired format:
    Likely Correct

    If the GPT-Sentence and the Evidence are unrelated,
    just return the words "Unclear".

    GPT-Sentence: ###
    {gpt_sentence}
    ###

    Evidence: ###
    {evidence}
    ###
    '''

    return chatgpt.getGptText(compare_prompt)

test_prompt = '''Using the GPT-Sentence and Evidence below, if the GPT-Sentence says a fact that is said differently in the Evidence (such as when someone was born), return using the
format below. Also, rephrase the correct fact from the Evidence into a single
sentence called Correct-Sentence that has the same structure as our GPT-Sentence. For example, if our GPT-Sentence was
"He went on to pursue his Ph.D. in Mathematics, which he obtained in 1997 from the University of Chicago"
but there is a part of the Evidence that says "He received his Ph.D. in 2000 from the University of California,
Berkeley under the joint supervision of Andrew Casson and William Thurston; his dissertation concerned foliations of three-dimensional manifolds,"
Correct-Sentence should be
"He received his Ph.D. in 2000 from the University of California, Berkeley," which has the
same words as the GPT-Sentence and only changes the part that disagrees (University of Chicago to University of California). It does not mention Andrew Casson, WIlliam Thurston, or manifolds because they are unrelated to our GPT-Sentence.

Desired format:
Likely Wrong, Evidence: <Correct-Sentence>

If the evidence contains a statement or statements
that agree with the GPT-Sentence, return using the format below.

Desired format:
Likely Correct

If the GPT-Sentence and the Evidence are unrelated,
just return the words "Unclear".

GPT-Sentence: ###
Barack Obama was born in Indiana in 1854.

Evidence: ###
Barack Hussein Obama II (listen) bə-RAHK hoo-SAYN oh-BAH-mə;[1] born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African-American president of the United States.[2] Obama previously served as a U.S. senator representing Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004, and worked as a civil rights lawyer before holding public office.

Obama was born in Honolulu, Hawaii. After graduating from Columbia University in 1983, he worked as a community organizer in Chicago. In 1988, he enrolled in Harvard Law School, where he was the first black president of the Harvard Law Review. After graduating, he became a civil rights attorney and an academic, teaching constitutional law at the University of Chicago Law School from 1992 to 2004. Turning to elective politics, he represented the 13th district in the Illinois Senate from 1997 until 2004, when he ran for the U.S. Senate. Obama received national attention in 2004 with his March Senate primary win, his well-received keynote address at the July Democratic National Convention, and his landslide November election to the Senate. In 2008, after a close primary campaign against Hillary Clinton, he was nominated by the Democratic Party for president and chose Joe Biden as his running mate. Obama was elected over Republican nominee John McCain in the presidential election and was inaugurated on January 20, 2009. Nine months later, he was named the 2009 Nobel Peace Prize laureate, a decision that drew a mixture of praise and criticism.

Obama's first-term actions addressed the global financial crisis and included a major stimulus package, a partial extension of George W. Bush's tax cuts, legislation to reform health care, a major financial regulation reform bill, and the end of a major US military presence in Iraq. Obama also appointed Supreme Court justices Sonia Sotomayor and Elena Kagan, the former being the first Hispanic American on the Supreme Court. He ordered the counterterrorism raid which killed Osama bin Laden and downplayed Bush's counterinsurgency model, expanding air strikes and making extensive use of special forces while encouraging greater reliance on host-government militaries.'''