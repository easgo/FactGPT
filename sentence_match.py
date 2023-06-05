import chatgpt

def evaluate_sentence_evidence(gpt_sentence, evidence):
    compare_prompt = f'''Using the selected sentence and Evidence below, if the selected sentence says a fact that is said differently in the Evidence (such as when someone was born), return using the
format below. Also, produce a new sentence called "Correct-Sentence," which is the correct fact from the Evidence that is different from the selected sentence.
For example, if our selected sentence was
"He went on to pursue his Ph.D. in Mathematics, which he obtained in 1997 from the University of Chicago"
but there is a part of the Evidence that says "He received his Ph.D. in 2000 from the University of California,
Berkeley under the joint supervision of Andrew Casson and William Thurston; his dissertation concerned foliations of three-dimensional manifolds,"
Correct-Sentence should be
"He actually received his Ph.D. in 2000 from the University of California, Berkeley," which has the same
main idea as the selected sentence and only changes the part that disagrees (University of Chicago to University of California). It does not mention Andrew Casson, William Thurston, or manifolds because they are unrelated to our selected sentence.

Desired format:
Likely Wrong, Evidence: <Correct-Sentence>

If the evidence contains a statement or statements
that agree with the selected sentence, return using the format below.
"Explanation" is a sentence that explains why the selected sentence is likely correct based on the evidence.

Desired format:
Likely Correct, <Explanation>

If the GPT-Sentence and the Evidence are unrelated,
just return the words "Unclear".

    Selected sentence: ###
    {gpt_sentence}
    ###

    Evidence: ###
    {evidence}
    ###
    '''

    return chatgpt.getGptText(compare_prompt)