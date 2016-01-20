
I could hide the fact that I'm still figuring out how to git properly (ie. without a hub) but I won't bother.

So ...

* Work locally on the `mona` branch. To update Freegreentea.info/talks, do ... `git push dreamhost mona` which pushes to the remote repository configured as "dreamhost" ; from dreamhost you need to do `git merge mona` to pull mona into the active master branch.

* To push to github, you want to push this mona branch to their Master with `git push github mona:master` or `git push github HEAD:master`
