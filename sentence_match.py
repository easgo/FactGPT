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

test_prompt = '''
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
Danny Calegari received his PhD from UChicago in 1997.

Evidence: ###
In 1994, Calegari received a B.A. in Mathematics from the University of Melbourne with honors. He received his Ph.D. in 2000 from the University of California, Berkeley under the joint supervision of Andrew Casson and William Thurston; his dissertation concerned foliations of three-dimensional manifolds.[1]

From 2000–2002 he was Benjamin Peirce Assistant Professor at Harvard University, after which he joined the California Institute of Technology faculty; he became Merkin Professor in 2007. He was a University Professor of Pure Mathematics at the University of Cambridge in 2011–2012, and has been a Professor of Mathematics at the University of Chicago since 2012.[2]

Calegari is also an author of short fiction, published in Quadrant, Southerly, and Overland. His story A Green Light was a winner of a 1992 The Age Short Story Award.[3]
'''