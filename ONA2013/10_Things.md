Lisa Williams and I are leading a workshop on [10 Things You Missed by not majoring in CS](http://ona13.journalists.org/sessions/10-things-you-missed-in-cs-school/) and these are my (very rough) notes follow. 


+ Computer Science is not software engineering, and it definitely isn't what most of you are trying to do. 

I polled a statistically significant number of CS majors and people who hung around them in college (5) and they learned C++, C, Ada, OOPas, Java, Python, LISP, MIPS, Scheme.

You'd learn stuff like this:
http://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/

You'll notice that there is really only one thing on that list (Python) that anyone is talking about at ONA this week. CS programs don't teach R (though some statistics programs do) or Rails or GIS. I actually learned GIS working on a forestry research project. 

+ Programming is incredibly frustrating. CS programs don't offer some kind of magic holy grail, what they teach is that...

+ Errors make sense. When you run a program, and get an error, you look at the error and 
figure out what it means. When your Java program throws a 
`java.lang.OutOfMemoryError: PermGen space` error, you don't say "what the what?" you take it apart. You go look up `PermGen space` and find out that `PermGen` is the region in the VM memory that is used to load class files, and that the size of this memory region is fixed. So if your program loads a lot of classes you'll use up that corner of your memory. I'm getting a bit carried away because I don't actually know a thing about Java but my point is that there's a grammar to errors and you can look them up.  http://frankkieviet.blogspot.ca/2006/10/classloader-leaks-dreaded-permgen-space.html

And even back in the olden days, before Google, there were newsgroups where you could ask questions if you were really stuck. 

And, if you're my age (which is not really all that old, in the grand scheme of things) while you were working on your CS degree, you were learning Java and C and every time you made a change to your program you had to compile it and sometimes that took all night. 

http://xkcd.com/303/ 

And sometimes after waiting all night for your program to compile, it just threw a bunch more errors.

+ Compiled languages are not Interpreted languages
As long as we're talking about compilers, I'm guessing some of you are secretly wondering what a compiler actually means. Those of you who aren't wondering are CS majors who just showed up to troll me anyhow, so zip it. 

Loosely, computer languages exist in two forms: compiled languages are languages that have to be translated into machine code by a compiler. You write your source code, and then compile it -- run a translator application that transforms your human readable source code into machine code. Interpreted languages don't have to be compiled. You can run the human readable source. 

http://en.wikipedia.org/wiki/Compiled_language
http://en.wikipedia.org/wiki/Interpreted_language

If you think about the programs you use every day, stuff like your operating system or Firefox, that is all compiled software. I'm pretty sure Word is written in C++ You can't just go read the source code even if you want to. It is a useful thing to know, but you're not really going to write software in C++

+ I was going to say that compiled languages don't matter, but you would have learned very very good form. C++ compilers care about indentation. C++ compilers know the difference between a tab and a space, so if you'd studied CS, you would have really good practice indenting code and you'd be very comfortable spotting inconsistencies in code. Mostly because you'd have a lot of practice. Lucky for us, you can get practice. Especially if you accept that tidiness matters. 

+ Version Control
CVS, Subversion, Git, Mercurial, 

GitHub is probably the biggest community of Git users 
http://lifehacker.com/5983680/how-the-heck-do-i-use-github
http://babydatajournalism.tumblr.com/post/36954225868/learn-github-introduction-to-git

Collaboration, keeping track of what you changed and why you changed it. 

+ Asking good questions

I can't tell you how many times I get messages like this from students: 

	> Keep getting an error when I click on the link from the homework assignment page (here).
	
	> I noticed the code for the interactive chart isn't working. I tried adding "http:" before the "//" (like we did in class), but no luck.

What error are you getting? When you say the code isn't working, what do you mean? StackOverflow (which is an indispensable resource!) has a good roundoup of advice on [asking good questions](http://stackoverflow.com/questions/how-to-ask) and I offer my students [some advice](http://datadrivenjournalism.fall.2013.journalism.cuny.edu/good-questions/)

The best questions, the ones that get answered, are clear and concise.


+ Basic Programming Concepts 

There are some useful things you might have learned, though: 

++ Conditional Statements. `if` and `else` -- they seem like gibberish, but we do this all the time. "If you we have any pasta, there's pesto in the freezer; or if you feel like making corn bread we could finish that chili. Othwerwise we should probably get takeout." We've set out some conditions:

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

Which depends on a couple of other fuctions:

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
		

http://hyperpolyglot.org/scripting





One good intro: 
++ [Part 1](http://computationaltheory.tumblr.com/post/39873698957/the-building-blocks-of-code)
++ [Part 2](http://computationaltheory.tumblr.com/post/40052373796/the-building-blocks-of-code-part-2)
++ [A different list](http://www.gamasutra.com/blogs/AlexRose/20121120/181941/Making_Games_with_No_Previous_Experience__Part_1_Code.php)

    Conditionals (if, else, switch)
    Loops (for, while)
http://lifeandcode.tumblr.com/post/32221878851/for-loop-basics
    Variables (ints, floats, bools, strings)
    Functions
    How to use an IDE
    
http://holowczak.com/programming-concepts-tutorial-programmers/


+ http://blog.drewdagostino.com/post/32720890976/10-things-to-expect-when-you-learn-to-code


So ... read this and start thinking about what is possible:
http://radar.oreilly.com/2013/01/the-future-of-programming.html
http://lifeandcode.tumblr.com/post/12205086953/life-and-codes-greatest-hits
