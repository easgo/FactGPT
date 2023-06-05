import chatgpt

def evaluate_sentence_evidence(gpt_sentence, evidence):
    compare_prompt = f'''Using the selected sentence and Evidence below, if the selected sentence says a fact that is said differently in the Evidence (such as when someone was born), return using the
format below. Also, produce a new sentence called "Correct-Sentence," which is the correct fact from the Evidence that is different from the selected sentence.
For example, if our selected sentence was
"He pursued his Ph.D. in Mathematics, obtained in 1997 from UChicago"
but there is a part of the Evidence that says "He received his Ph.D. in 2000 from the University of California,
Berkeley under the joint supervision of Andrew Casson and William Thurston; his dissertation concerned foliations of three-dimensional manifolds,"
Correct-Sentence should be
"He actually received his Ph.D. in 2000 from the University of California, Berkeley," which has the same
main idea as the selected sentence and only changes the part that disagrees (University of Chicago to University of California). It does not mention Andrew Casson, William Thurston, or manifolds because they are unrelated to our selected sentence.

Everything in #Infobox# is EXTREMELY IMPORTANT AND CERTAINLY CORRECT. It is organized in key value pairs where the key is the attribute about the topic at hand and the value is the value of that attribute. For example, if it says Born: "August 18, 1973" and the sentence says "He was born on August 17, 1973," you can be confident that the sentence is inccorrect. If it says "length: x" for a road then that would mean the road is indeed x length long. 

Everything in #content# is also certainly correct. It is organized into paragraphs. Both comprise the Evidence described above.



If any part of the sentence is incorrect
Desired format:
Likely Wrong, Evidence: <Correct-Sentence>

If the evidence contains a statement or statements
that agree with the selected sentence, return using the format below.
"evidence" is the part of the Evidence that agrees with the selected sentence. If you can't find any part of the Evidence that agrees with the selected sentence, just return the words "Unclear."

Desired format:
Likely Correct, <evidence>

If the selected sentence and Evidence are unrelated,
just return the words "Unclear".

    Selected sentence: ####
    {gpt_sentence}
    ####

    Evidence: ####
    {evidence}
    ####
    '''

    return chatgpt.getGptText(compare_prompt)