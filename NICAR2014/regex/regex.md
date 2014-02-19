## Back of the Napkin RegEx

I am a lecturer at CUNY's Graduate School of Journalism where I teach classes on data visualization and newsgames and sometimes plain old reporting. 

I've also been worming my way earlier in the curriculum, so my colleageu Ben Lesser and I now do an extended "Got Numbers" workshop with every first semester Craft class, and everyone does a little bit of spreadsheet work and mapping in Fundamentals of Multimedia. 

Newsgames is a five week module that starts with downloading a git repository (we don't actually clone it), editing a .csv, and deploying to a web server. The game, Steve Melendez's Bingo Card generator, isn't really the point. The point is that by the end of week one "Just grab the repo" is an instruction that has meaning, though we also talk about how to write for something like this, how to be clean and consistent and use a single voice across each entry. 

Then we all build a quiz using Mother Jones' script and from there we dive into [Twine](http://twinery.org/), a tool that lets you incorporate scoring and logic into a choose your own adventure game. Last fall, we came up with a "spend a week homeless" game and another that trailed a disabled veteran. 

What we're doing is just storytelling.

## So ..okay. Regular Expressions. On a Napkin.

I spent a good 15 minutes looking at sites where you can print cocktail napkins. And about 60 seconds contemplating a Kickstarter campaign to produce customized regex napkins, but I didn't. Maybe we can work on that later. 

### RegEx

It will shock you to learn that Wikipedia has an extensive and thorough history of [regular expressions](http://en.wikipedia.org/wiki/Regular_expression). 

The first awesome thing about regular expressions is that they're not actually regular. When you start getting fancy you'll start to discover that applications can vary subtly in their implementation. 


### Get Started

I like to start with a manageable block of text, one where you can *see* what you're up against just fine. 

We're going to use two tools:

[Rubular](http://rubular.com/) and [RegEx 101](http://regex101.com/) to work through our puzzles today. 

That is player data from the Washington Nationals 2012 lineup that I stole from [Anthoney DeBarros](http://www.anthonydebarros.com/2012/10/09/excel-extract-text-find-mid-string/) who uses it to demonstrate some cool Excel functions, which will also work if you want to break this all up. I sometimes think it wouldn't kill me to get more current data, but I haven't gotten there yet.

Convert dates from 1/12/99 to 1999-12-01; find proper nouns and large currency amounts in a giant blob of text


► Regular expressions, or “regex”, are like find and replace on speed. Instead of searching for particular text strings (like “V6C”) regular expressions are used to look for particular patterns (i.e. a letter followed by a number followed by a letter). They can be very helpful when you’re trying to clean up a really dirty dataset and typical techniques, like text-to-columns, aren’t working.  <https://leanpub.com/bastards-regexes> The Bastards Book of Regular Expressions, an ebook by Dan Nguyen, and  <http://regular-expressions.info/> regular-expressions.info are two great places to start. You can text out your regex patterns at  <http://rubular.com/> rubular.com.



Here's that thing I mentioned. I scraped the .txt version of pdfs in doc
cloud for different combinations of regex's to find the detainee's transfer
in dates. I used that to calculate running totals for that background
population chart.

http://america.aljazeera.com/articles/multimedia/guantanamo-hungerstriketimeline.html

### Greed.
> ...playlist index:109 id:38522 title:Christmas in Heaven artist:B.B. King album:A Christmas Celebration of Hope playlist index:110 id:38523 title:I'll Be Home for Christmas artist:B.B. King album:A Christmas Celebration of Hope playlist index:111 id:38524 title:To Someone That I Love artist:B.B. King album:A Christmas Celebration of Hope playlist index:112 id:38525 title:Christmas Celebration artist:B.B. King album:A Christmas Celebration of Hope playlist index:113 id:38526 title:Merry Christmas, Baby artist:B.B. King album:A Christmas Celebration of Hope


## Tools
If you're already pretty good at regular expressions, check out the [Tuesday Challenge](http://callumacrae.github.io/regex-tuesday/) or [Hacker Rank's Challenges](https://www.hackerrank.com/categories/miscellaneous/regex).

The [RegEx Crosswords](http://regexcrossword.com/) are fun, if cryptic. 

And if you just want an easier format:
http://regex101.com/ or 

http://rubular.com/
