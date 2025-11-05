# Suggested Workflow
## for discussion Nov 6


In typical git projects, the "main" branch is carefully curated. But here? Let's make it a free-for-all. Contributors should be encouraged to make changes directly in the main branch. However, if many people are touching it then it may evolve very quickly, and some changes may get stomped on by other people's changes. We'll deal with it as it comes.

If someone desires a more stable copy to work from, we have several options, in increasing order of git-difficulty:

- Make your own branch directly in the project. This branch will be created off of a certain point of the main branch, and then from that point on the branch will not directly track any further changes from the main branch. You (and others!) will be free to edit this branch directly. Once the branch it deemed ready to be integrated in the main body of work, we can merge it into the main branch. (Part of that process will be fixing any conflicts between your branch and the main branch).
- Clone the project on your local machine, and work on it as much as you like. Push up the commits when they are ready. You may want to do this in a branch, unless you intend to make the main branch more chaotic.
- Fork the project in github, and work off of the fork. Doing this gives you total control over everything. You can feel free to do this if you would rather manage the git aspects on your own, without all the chaos we are imposing in the main branch. When your stuff is ready, submit a pull request. If you know how to do this, you should be able to handle any conflicts on your own.

Eventually, as we decide individual clauses or sub-clauses are mature enough to be discussed by the wider group, we may "freeze" it by putting a tag in the repository. People should understand that the clause is now under discussion, and any changes that are made here may not make it back to the working group. If the working group drives any changes, they should be made on a branch from that tag.

Eventually, the parts of the standard that are "frozen" in this fashion can form the basis of the official submission.