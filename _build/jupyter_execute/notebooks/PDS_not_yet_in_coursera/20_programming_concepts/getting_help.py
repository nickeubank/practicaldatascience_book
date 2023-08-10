#!/usr/bin/env python
# coding: utf-8

# # Getting Help Online
# 
# The only constant in Data Science today is change. Packages are constantly being modified, and new tools emerge almost every week. As a result, you will never reach a point where you have "learned everything," and so learning to get help when you need it is a critical part of being a data scientist, and its a skill with more nuance than you might expect. 
# 
# ## Looking for Answers
# 
# When you hit a problem *by far* your best chance for finding a solution is to just google your problem. 
# 
# When googling here are a few suggestions for what search terms to use: 
# 
# - **Always include the language or package you are using:** Googling "how do I get the average of all the rows in a matrix" is much less likely to be helpful than "how do I get the average of all the rows in numpy". 
# - **If you get an error message, google the error message (along with package):** odds are someone has had the same problem you're having, and has already asked about it somewhere. 
# 
# 
# 
# ## How To Ask for Help
# 
# Unfortunately, sometimes you have a problem that google won't solve. When that happens, it's time to move from looking for help to asking for help. 
# 
# First, the good news: the internet is magic. Seriously. The amount of time people are willing to spend helping other people solve their programming problems absolutely blows my mind every time I think about it. 
# 
# Now the bad news: while people can be *incredibly* helpful, they can also get unreasonably grumpy when someone asks for help in a manner that violates community norms (which I'll discuss below). The norms that exist are there for a reason, this this isn't entirely unreasonable, but this can make it hard for a new programmer who doesn't know the "rules" of community forums. 
# 
# ### Community Norms
# 
# Here are a few of the community norms around asking for help: 
# 
# **Show your work:** 
# 
# People like to help people who are stuck, but hate spending time assisting someone with a problem they could have solved with google. So to get the best help, make sure to include in your request for help:
# 
# - Description of things you’ve tried yourself
# - Links to other sites you’ve visited that seem like might help but don’t: People are often quick to say “hey, this has been asked elsewhere” and throw a link at you, so add links to the other sites you’ve check and some information about why those solutions don’t work.
# 
# **Don't add small talk:** 
# 
# People get surprisingly bent out of shape if you add small talk ("Hi! OK, here's my problem..."). Personally, I still often add a "Thanks!" at the end of posts, but even that is a little dangerous. In general, you *only* want to state your question.
# 
# Relatedly, **don't be surprised if people are *really* curt in their comments / responses. They're not being rude, just efficient.** The people who provide help on these forums often help *dozens* of people a day, so they tend to type only the absolute minimum required to answer a question. 
# 
# **Try to provide a Minimal Working Example (MWE):** 
# 
# - If you're trying to figure out an error or problem you don't understand, try to include a reproducible example of the problem your experiencing: Nothing will make it more likely you get help than if you can post a chunk of code (5-20 lines?) that someone else can copy and paste into Python to recreate the problem. This is what's referred to as a Minimal Working Example (MWE). This isn’t always possible of course, but really do try.
#     - Writing a MWE is also great practice because the practice of trying to identify the smalled bit of code required to generate your problem often helps you understand the cause of your problem, and sometimes will even lead you to solving your own problem. 
# - If you are trying to figure out how to do something, try to give an example of the data you currently have, and an example of what you want to have in the end. By virtue of not being sure how to do it, you obviously can't provide code to accomplish your goal, but by writing out exactly what you want, it makes it easier for others to help you. 
# 

# ## Good and Bad Exampls
# 
# - [Excellent](https://stackoverflow.com/questions/48828484/pandas-reshape-dataframe-every-n-rows-to-columns) The poster gave example data, showed what they're starting with, then took the time to make a fake table showing what they wanted to achieve, *and* showed that they had tried using `numpy` (to show they had been trying to solve themselves before asking for help), but that it hadn't worked. 
# - [Pretty Good](https://stackoverflow.com/questions/18250298/how-to-check-if-a-value-is-in-the-list-in-selection-from-pandas-data-frame): Shows solution that user doesn't like, and in doing so shows that they've been trying things themselves AND shows what solution they've ruled out already. They tagged their post with `pandas` and `python` so the right people would see it. Could be better if they had provided one more line of data to generate `df_new` before trying to work with it so others could more easily replicate.
# 

# ## Places to Ask Questions
# 
# There are a few places to ask for programming help, and the quality of help you get often depends on where you go. 
# 
# **Questions Related To Big Packages or Language:** If you have a question about a really, really popular piece of software (python, R, ArcGIS, numpy, pandas, ggplot), then its often best to go to [StackOverflow](https://stackoverflow.com/). StackOverflow is... crazy. People contribute more time to helping others there than you could ever imagine. But it's also the place where the community norms discussed above are most important, so craft your request for help carefully before posting. 
# 
# - If you are posting on Stack Overflow, make sure to also tag the relevant packages. Many people who manage packages watch stackoverflow for posts that are tagged for their package. 
# 
# **Questions about Smaller Packages:** If you have a question about a package that's less developed, a question on StackOverflow is likely to get lost in the noise. In these situations, trying finding a "Get Help" section on the package's homepage or github repository, as these will often direct you to a dedicated mailing list or message board. Note that to use a mailing list you'll usually have to subscribe, which will result in a bunch of unwanted emails for a couple days. Just bite the bullet, subscribe, ask your question, wait for an answer, then unsubscribe. Examples of great mailing lists:
# 
# - [PyData](https://groups.google.com/forum/#!forum/pydata): For questions about pandas.
# - [iGraph](https://lists.nongnu.org/mailman/listinfo/igraph-help): For questions about the iGraph network analysis library.
# - [Numpy and Scipy](https://www.scipy.org/scipylib/mailing-lists.html): For numpy and scipy.
# 
# Finally, if you don't see a mailing list, try creating a new issue on the package's github repository. 
# 
# 

# ## Diversity and Inclusion Issues
# 
# A final and deeply unfortunate note about getting help online: all too often programming forums are awful to women and people of color. For example, here's a recent mea culpa from [Stack Overflow](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/). This isn't uniformally the case: many younger communities (like the community around the Julia programming language) seem to be taking inclusiveness really seriously, and do better than most groups. But on the whole, women and people of color should be aware (ok, are probably already painfully aware) that the internet is not always equally welcoming. 
# 
# With that in mind, there is a case to be made for using gender-neutral usernames and generic profile pics when posting on these forums. `randomuser123` is likely to be treated better than `lucy92`, and a user with a random geometric user icon is likely to be treated better than a person whose picture identifies the user as a person of color.
# 
# Of course, that doesn't mean you *should* use a generic name and icon. There is tremendous value in having better representation from women and people of color in these forums (women and people of color are likely to feel more comfortable participating in a forum if they see other people who look like them present). Moreover, many forums now have [Community Guidelines](https://julialang.org/community/standards/) and a process for reporting (and sanctioning) abusive behavior. Being visible and active will help ensure these communities stand behind their statements (and will help weed out bad apples). 
# 
# But whether one wishes to just use these forums as easily as white men, or risk disgusting behavior in order to induce change is a deeply personal choice. I bring this up not to advocate for one choice or the other, but rather to ensure students understand the potential consequences of each choice so each student can make the choice that is best for them personally. 
