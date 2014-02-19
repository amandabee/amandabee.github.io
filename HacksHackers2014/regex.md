## Back of the Napkin RegEx

I am a lecturer at CUNY's Graduate School of Journalism where I teach classes on data visualization and newsgames and sometimes plain old reporting. 

I've also been worming my way earlier in the curriculum, so my colleageu Ben Lesser and I now do an extended "Got Numbers" workshop with every first semester Craft class, and everyone does a little bit of spreadsheet work and mapping in Fundamentals of Multimedia. 

Newsgames is a five week module that starts with downloading a git repository (we don't actually clone it), editing a .csv, and deploying to a web server. The game, Steve Melendez's Bingo Card generator, isn't really the point. The point is that by the end of week one "Just grab the repo" is an instruction that has meaning, though we also talk about how to write for something like this, how to be clean and consistent and use a single voice across each entry. 

Then we all build a quiz using Mother Jones' script and from there we dive into [Twine](http://twinery.org/), a tool that lets you incorporate scoring and logic into a choose your own adventure game. Last fall, we came up with a "spend a week homeless" game and another that trailed a disabled veteran. 

What we're doing is just storytelling.

## So ..okay. Regular Expressions. On a Napkin.

### RegEx

It will shock you to learn that Wikipedia has an extensive and thorough history of [regular expressions](http://en.wikipedia.org/wiki/Regular_expression). 

The first awesome thing about regular expressions is that they're not actually regular. When you start getting fancy you'll start to discover that applications can vary subtly in their implementation. 

Some important details: I actually spent about 20 minutes researching custom napkins before I remembered that I was supposed to be figuring out how to do a regular expressions workshop without a computer lab, not how to get napkins printed. I might start a kickstarter later. I'll keep you posted.

But also, if you're coming to NICAR, I will be doing this again in a computer lab and I'll have an hour. So if you get a headache, that's cool. That means you should come to the workshop and we can all massage our temples together. 


### Get Started

I like to start with a manageable block of text, one where you can *see* what you're up against just fine. This, for instance:

    NAME: Sean Burnett POS: RP AGE: 30 WT: 200 BORN: Dunedin, FL SALARY: 2350000
    NAME: Tyler Clippard POS: RP AGE: 27 WT: 200 BORN: Lexington, KY SALARY: 1650000
    NAME: Ross Detwiler-Smith POS: SP AGE: 26 WT: 174 BORN: St. Louis, MO SALARY: 485000
    NAME: Christian Garcia POS: RP AGE: 27 WT: 215 BORN: Miami, FL SALARY: N/A
    NAME: Gio Gonzalez POS: SP AGE: 27 WT: 205 BORN: Hialeah, FL SALARY: 3335000
    NAME: Mike Gonzalez POS: RP AGE: 34 WT: 215 BORN: Robstown, TX SALARY: N/A
    NAME: Ryan P. Mattheus POS: RP AGE: 28 WT: 215 BORN: Sacramento, CA SALARY: 481000
    NAME: Craig Stammen POS: RP AGE: 28 WT: 200 BORN: Coldwater, OH SALARY: 485000
    NAME: Drew Storen POS: RP AGE: 25 WT: 180 BORN: Indianapolis, IN SALARY: 498750
    NAME: Jordan Q. Zimmermann POS: SP AGE: 26 WT: 218 BORN: Auburndale, WI SALARY: 2300000 


That is player data from the Washington Nationals 2012 lineup that I stole from [Anthoney DeBarros](http://www.anthonydebarros.com/2012/10/09/excel-extract-text-find-mid-string/) who uses it to demonstrate some cool Excel functions, which will also work if you want to break this all up. I sometimes think it wouldn't kill me to get more current data, but I haven't yet. I did alter it subtly to make our challenge more fun. 

Let's say, hypothetically, that I want to put this in a spreadsheet. And I want all the data in columns. I can't just use `text to columns` because there's no delimiter.

So I want us to start by walking through how we can turn that into something closer to...

    Sean Burnett, RP, 30, 200, Dunedin, FL, 2350000
    Tyler Clippard, RP, 27, 200, Lexington, KY, 1650000
    Ross Detwiler-Smith, SP, 26, 174, St. Louis, MO, 485000
    Christian Garcia, RP, 27, 215, Miami, FL, N/A
    Gio Gonzalez, SP, 27, 205, Hialeah, FL, 3335000
    Mike Gonzalez, RP, 34, 215, Robstown, TX, N/A
    Ryan P. Mattheus, RP, 28, 215, Sacramento, CA, 481000
    Craig Stammen, RP, 28, 200, Coldwater, OH, 485000
    Drew Storen, RP, 25, 180, Indianapolis, IN, 498750
    Jordan Q. Zimmermann, SP, 26, 218, Auburndale, WI, 2300000 


Start with the name. We're going to walk through this together and you should sketch out on a napkin how you think we can solve each piece of the puzzle. <http://rubular.com/r/OCClBeRKQi>
    
    NAME: \w*        # Not a bad start.
    NAME: \w* \w*    # Better, but check out Jordan Q. Zimmerman, Ross Detwiler-Smith
    NAME: \w*[-\w. ]*\w* # Now we have everyone.

But we want to be able to make replacements, so we're going to start grouping the good stuff: 
    
    NAME: (\w*[-\w. ]*\w*) POS: 
    
    NAME: (\w*[-\w .]*\w*[ ]*) POS: ([A-Z][A-Z]) 
    NAME: (\w*[-\w .]*\w*[ ]*) POS: ([A-Z]{2}) 
    
    NAME: (\w*[-\w .]*\w*[ ]*) POS: ([A-Z]{2}) AGE: (\d\d) WT: (\d{3}) BORN: .* SALARY: (\d+|N\/A) 
    
Unpack the SALARY "or" statement: \d* will match 0 or more and stop. We want 1 or more. This is why I like Rubular, it shows you your matches. <http://rubular.com/r/lmLv0Igsdo>

But now is a good time to take this over to [Regex101](http://regex101.com/) to see it all colorized http://regex101.com/r/vS5eT3
    
    




[The Bastards Book of Regular Expressions](https://leanpub.com/bastards-regexes), an ebook by Dan Nguyen, and  <http://regular-expressions.info/> regular-expressions.info are two great places to start. You can text out your regex patterns at  <http://rubular.com/> rubular.com.

### More challenges:
Let us say that, hypothetically, I have a bunch of phone numbers that people entered using all kinds of different formats and I want them on one format. Actually, what I had was a list of perfectly consistent phone numbers and I wrote a little python regular expression to mangle them, but now that they're mangled, we're going to undo all my hard work:

    310-808-5243
    (415) 846-1688
    (720) 318-9049
    323.888.6200
    323-888-6237
    3238886209
    323/888.6202
    3237078576
    3232162201
    (323) 960-3100
    727-455-4538
    727-214-5862
    7274555955
    4242090017
    
    (\d{3})[-)\.\/ ]*(\d{3})[-)\.\/ ]*(\d{4})
    or in Python
    \(*(\d{3})[-)\.\/ ]*(\d{3})[-)\.\/ ]*(\d{4})
    
[Resolution](http://regex101.com/r/lP2iS6)
    
More challenges: Convert dates from 1/12/99 to 1999-12-01; find proper nouns and large currency amounts in a giant blob of text


http://ruby.bastardsbook.com/chapters/regexes/

### Where this gets interesting
Is when you've got what Michael Keller had, which was Guantanamo Bay officials who won't tell you ... anything, really, about how many people are incarcerated there. So you need to find the dates that each prisoner transfered in or out of the facility to compile your own running totals of the prison population:

[Gitmo Hunger Strike Timeline](http://america.aljazeera.com/articles/multimedia/guantanamo-hungerstriketimeline.html)

### Greed.
> ...playlist index:109 id:38522 title:Christmas in Heaven artist:B.B. King album:A Christmas Celebration of Hope playlist index:110 id:38523 title:I'll Be Home for Christmas artist:B.B. King album:A Christmas Celebration of Hope playlist index:111 id:38524 title:To Someone That I Love artist:B.B. King album:A Christmas Celebration of Hope playlist index:112 id:38525 title:Christmas Celebration artist:B.B. King album:A Christmas Celebration of Hope playlist index:113 id:38526 title:Merry Christmas, Baby artist:B.B. King album:A Christmas Celebration of Hope

    playlist index:(\d+) id:(\d+) title:([\w\s',]+) artist:([\w\s'.]+) album:([\w\s']+?)(?=$|\splaylist)
    \1, \2, \3, \4, \5, \n
    
Read up on [Lookaheads](http://www.rexegg.com/regex-lookarounds.html)

## Tools
If you are just getting started, and have time, Zed Shaw's [Learn Regex The Hard Way](http://regex.learncodethehardway.org/) will make you an expert. 

And Dan Nguyen is awesome, so I am going to go out on a limb and say that [The Bastards Book of Regular Expressions](https://leanpub.com/bastards-regexes) is probably also awesome. 

If you're already pretty good at regular expressions, check out the [Tuesday Challenge](http://callumacrae.github.io/regex-tuesday/) or [Hacker Rank's Challenges](https://www.hackerrank.com/categories/miscellaneous/regex).

The [RegEx Crosswords](http://regexcrossword.com/) are fun, if cryptic. 

### Required Reading

And if you just want an easier format:
http://regex101.com/ or 

http://rubular.com/
