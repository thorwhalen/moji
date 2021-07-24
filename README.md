# moji

Developing a full emoji language.

Disclaimer: My personal belief is that would better serve to enhance existing 
writing systems by re-introducing the information that is lost when removing 
body language, facial expression and tone of voice. 
In fact, this is exactly how emojis are actually used in most cases. 

Still, out of academic curiosity, let's see what we can do. 

This is not about just replacing some text by emoji equivalent: 
We want the written system to only use unicode emojis. 

This is not about converting text to an emoji-only written system. 
That's easy. You can do it with two emoji characters -- that's called binary. 
You can do it with a mapping between letters and emojis -- 
that's lame.

Instead what we want to do here is explore how one can map english 
(for example) to emojis, and back, but through their semantic content, 
with an eye on patterns that might lead to a grammar for the "language"
-- whether this grammar emerges naturally, or is helped out a bit 
through the modeling setup.

To install:	```pip install moji```


# References

## emoji2vec

Princeton and University College London researchers doing word2vec 
with emojis. [See this article](https://arxiv.org/pdf/1609.08359.pdf).
We'll start with 
[the data](https://github.com/uclnlp/emoji2vec/tree/master/data/raw_training_data) 
they provide, 
namely the english-emoji relations and possibly the emoji vectors too.


## Emojicode

Can you believe these nerds. 
A [programming language](https://www.emojicode.org/) 
where language constructs (types, operators, etc.) are emojis. 
And they're serious! I mean, just check out at the 
[reference documentation](https://www.emojicode.org/docs/reference/)!

## Will emoji become a new language?

[This article from the BBC]
(https://www.bbc.com/future/article/20151012-will-emoji-become-a-new-language) 
explores the question.

## Emojin

In [this video](https://www.youtube.com/watch?v=2vKVv-ymBGI) 
Matt Mignogna talks about the "what makes a language" 
and proceeds in proposing a prototype. 
His prototype is not of much use for use since it's only a small 
lexicon an overly simplistic grammar, depends on non-emoji 
(in the unicode sense) diacritics, 
and is (as he later points out) just a mapping of English 
(I mean... who needs a definite article!)

Still, the first 6mn are is a nice introduction to the effort and potential.



