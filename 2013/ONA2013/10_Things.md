Lisa Williams and I are leading a workshop on [10 Things You Missed by not majoring in CS](http://ona13.journalists.org/sessions/10-things-you-missed-in-cs-school/) and these are our notes. 

# CS is not Software Engineering
Computer Science is not software engineering, and it definitely isn't what most of you are trying to do. 

I polled a statistically significant number of CS majors and people who hung around them in college (5) and they learned C++, C, Ada, OOPas, Java, Python, LISP, MIPS, Scheme.

You'd learn stuff like this:
http://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/

You'll notice that there is really only one thing on that list (Python) that anyone is talking about at ONA this week. CS programs don't teach R (though some statistics programs do) or Rails or GIS. I actually learned GIS working on a forestry research project. 

#Programming is Frustrating
Programming is incredibly frustrating. All those languages you've never heard of? They're compiled languages. You write your code, run a compiler. It takes hours. And sometime in the middle of the night, it throws an error. And when you wake up in the morning you find out it didn't work. 

CS programs don't offer some kind of magic holy grail, what they teach is that...

#Errors make sense
Errors make sense. When you run a program, and get an error, you look at the error and figure out what it means. When your Java program throws a 
`java.lang.OutOfMemoryError: PermGen space` error, you don't say "what the what?" you take it apart. You go look up `PermGen space` and find out that `PermGen` is the region in the VM memory that is used to load class files, and that the size of this memory region is fixed. So if your program loads a lot of classes you'll use up that corner of your memory. I'm getting a bit carried away because I don't actually know a thing about Java but my point is that there's a grammar to errors and you can look them up.  http://frankkieviet.blogspot.ca/2006/10/classloader-leaks-dreaded-permgen-space.html

And even back in the olden days, before Google, there were newsgroups where you could ask questions if you were really stuck. 

And, if you're my age (which is not really all that old, in the grand scheme of things) while you were working on your CS degree, you were learning Java and C and every time you made a change to your program you had to compile it and sometimes that took all night. 

http://xkcd.com/303/ 

And sometimes after waiting all night for your program to compile, it just threw a bunch more errors.

#Good Form Matters
Compiled languages are not Interpreted languages. As long as we're talking about compilers, I'm guessing some of you are secretly wondering what a compiler actually means. Those of you who aren't wondering are CS majors who just showed up to troll me anyhow, so zip it. 

Loosely, computer languages exist in two forms: compiled languages are languages that have to be translated into machine code by a compiler. You write your source code, and then compile it -- run a translator application that transforms your human readable source code into machine code. Interpreted languages don't have to be compiled. You can run the human readable source. 

If you really want to know the difference between a [compiled language](http://en.wikipedia.org/wiki/Compiled_language) and an [interpreted language](http://en.wikipedia.org/wiki/Interpreted_language) you could start reading, but I wouldn't actually start there. 

I thought I was going to say that compiled languages don't matter, but one thing you learn from them is good form. Really good form. C++ compilers care about indentation. C++ compilers know the difference between a tab and a space, so if you'd studied CS, you would have really good practice indenting code and you'd be very comfortable spotting inconsistencies in code. Mostly because you'd have a lot of practice. Lucky for us, you can get practice. Especially if you accept that tidiness matters. 

Look over the [Python coding standards](http://www.python.org/dev/peps/pep-0008/#indentation) and start at least indenting your code.  

# Use Version Control
Or at least comment your code. Here's why: 
[my talks repo](https://gitorious.org/talks-and-teaching/talks-and-teaching/)

People often describe version control as a collaboration tool, which it is, but even if you aren't collaborating with a soul, you should be using version control.

I can see my history, I know when things changed. I can go back. When I was director of technology at Gotham Gazette one of the first things I did was I took our whole spaghetti heap mess of a hand written CMS in three languages and I put it into a Subversion repository. And then I started a staging server (another key concept! Test!) and I would make changes on my laptop, check them in, check them out on the staging server, check my work, and then check them out on the live site. And then when our editor said "you know six months ago this stopped working and I don't know why, but it should work." I can go back and see that my commit message says we disabled that functionality for a reason. And the reason is there. And so I can go back to our editor and say "this is we changed that. and this is what changing it back will do." Not because I magically remember, but because I wrote it down. 

Today, I tend to use Git, mostly because other people use git, but also because it does somethings better like let you commit incremental changes. Unless you live with someone who is a Mercurial developer and they're committed to helping you, go with Git. 

The other reason to use version control is that you can check things out. And clone them. Which we'll get to  when we get to #8. 

CVS, Subversion, Git, Mercurial, 

GitHub is probably the biggest community of Git users but git is free software and there are plenty of other git repository hosts out there, including (gitorious)[http://gitorious.org], which I like because I like to be contrary. But Lifehacker has a nice (starter guide)[http://lifehacker.com/5983680/how-the-heck-do-i-use-github] for Github. 

#Ask good questions

I can't tell you how many times I get messages like this from students: 

	> Keep getting an error when I click on the link from the homework assignment page (here).

or
	
	> I noticed the code for the interactive chart isn't working. I tried adding "http:" before the "//" (like we did in class), but no luck.

What error are you getting? When you say the code isn't working, what do you mean? StackOverflow (which is an indispensable resource!) has a good roundoup of advice on [asking good questions](http://stackoverflow.com/questions/how-to-ask) and I offer my students [some advice](http://datadrivenjournalism.fall.2013.journalism.cuny.edu/good-questions/)

The best questions, the ones that get answered, are clear and concise. It take some time to get used to what matters and what doesn't, sometimes my students try, and I get something closer to:

	> My cat threw up all over the place and I'm using Chrome but when I tried to load the page I get an error that says "403 Forbidden nginx/1.1.19" and I tried three other browers and I'm stuck.
	
And that's better. I can tell you that a `403 Forbidden` error is coming from the server (and the server is running `nginx`) and so it doesn't matter what browser you're using, the server is going to say the same thing to anyone who asks. 
	
#The Command Line Loves You
If you've never used the terminal, start. It's not what you're used to, but...when someone on Stack Exchange says "What happens when you run ..." they probably mean "when you type this command at the command line in your shell."

[Command Line the Hard Way](http://cli.learncodethehardway.org/book/)

Open the terminal. On a Mac, it is in `Utilities`. On Windows I have no idea. I run Debian when I'm not using Lisa's lovely Macbook Air. 

#Don't Start from Scratch

Actually, they don't teach you this in CS. In CS you learn to do everything from scratch. And that's bad. I'll get into a lot of overwrought cooking analogies if we have time but there's really no need to grow your own wheat and harvest it yourself and grind it into flour by hand. Do that once or twice if you're committed to a truly hands on experience, but you can make excellent spaghetti with dried pasta from the grocery store and canned tomatoes. 

Starting from scratch is great if you've got four years to really master C++ but it also makes a difference that your professor has spent years developing assignments that build naturally on one another and are doable with your current skill set. 

I can take [WNYC's bingo code](https://github.com/amandabee/bingo) and clone it and make some changes and create [my own Bingo game](http://digitalstorage.journalism.cuny.edu/amandahickman/newsgames/bingo/embed.html) (that's kind of goofy, my newsgames class put that together in class last week, just to practice cloning a repository, changing some files and putting them online. I recommend trying that if it sounds hard. 

#Start Small

You don't know you're starting small, you think you're just doing your homework. 

Write a scraper. Use [scraperwiki](https://scraperwiki.com/) to write your first one and then move on to writing something local that you can run yourself. 

Make a map.

Write something that pulls data from an API. 


#Basic Programming Concepts
CS programs probably start here. You don't have to. Just look for English and think about what it means and you'll do fine. Later, when you really want to understand a concept, you can ask more questions and do more reading. I'm personally a huge fan of Zed Shaw and when you find that you wish you understood `for` loops better, go walk through [Python the Hard Way](http://learnpythonthehardway.org/). Languages use [different syntax for the same concept](http://hyperpolyglot.org/scripting), not so different from the way that most languages have some kind of basic grammar about subject verb agreement.

    Conditionals (if, else, switch)
    Loops (for, while)
    Variables (ints, floats, bools, strings)
    Functions
    How to use an IDE
    
*Conditional Statements*  `if` and `else` -- they seem like gibberish, but we do this all the time. "If you we have any pasta, there's pesto in the freezer; or if you feel like making corn bread we could finish that chili. Othwerwise we should probably get takeout." We've set out some conditions:

	if (we have pasta):
		do this: (thaw the pesto);
	else if (you feel like making cornbread):
		do this: (make corn bread and heat up the chili)
	else:
		do this: (buy takeout)

Because we have human brains, we can interpret statements like "there's pesto in the feezer" to mean "thaw the pesto, cook the pasta, toss it with the pesto and serve that for dinner. Please." So we get away with shorthand. So computers, they're the exasperating child who says "oh, you want me to cook pasta and thaw pesto and that will be dinner? You didn't actually say that." And then you're hungry and annoyed and everyone is having a blood sugar crisis. 

Also because we have brains and some autonomy, we're likely to say "well, we do have pasta but I'd rather have cornbread, so I think I'll go for chili and cornbread." The computer, not so much. If there's pasta, our program stops right there and makes it. It only proceeds to the next choices if "we have pasta" is a false statement.

So: going back to the shorthand, another core concept is functions. If you're going to do something more than once, you want to define a function for it. Our chili and cornbread function might look something like this:

	def chili_and_cornbread() {
		make cornbread;
		heat chili;
	}

Which depends on a couple of other functions:

	def chili() {
		# do something with beans and tomatoes and mushrooms and 
		# possibly beef, but I'm a vegetarian so I don't do beef
	}

	def cornbread {
		preheat oven to 400°;
		pan = oil a 9" round cake pan;
		wet_ingredients = ["1 egg", "1/3 c oil", "1 c milk"];
		dry_ingredients = ["1c corn meal", "1c flour","1/2 t salt","1T baking powder"];
		if (southern == true) {
			dry_ingredients.append["1/4 c sugar"]
		}
		mix dry_ingredients;
		mix wet_ingredients;
		batter = dry_ingredients + wet_ingredients;
		pour batter into pan;
		bake 30 min;
	}

And because our baking programming language has pre-defined routines for things like "mix" and "pour" and "bake" we don't have to define those. Or, we might need to add a line like `import baking` to pull in a library that defines those basic culinary processes. 

[One](http://computationaltheory.tumblr.com/post/39873698957/the-building-blocks-of-code),  [another](http://computationaltheory.tumblr.com/post/40052373796/the-building-blocks-of-code-part-2), [A different list](http://www.gamasutra.com/blogs/AlexRose/20121120/181941/Making_Games_with_No_Previous_Experience__Part_1_Code.php), [Concepts](http://holowczak.com/programming-concepts-tutorial-programmers/)

#Turn it to 11

Further reading: [Life and Code's Greatest Hits](http://lifeandcode.tumblr.com/post/12205086953/life-and-codes-greatest-hits)
