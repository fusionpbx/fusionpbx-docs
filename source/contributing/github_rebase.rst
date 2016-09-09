******************************
Rebasing a branch with GitHub
******************************

Welcome to the rebasing a branch with GitHub guide. 
    
    
**1.** Open the GitHub client application and make sure you are on the branch you want to rebase
     
.. image:: ../_static/images/contributing/github_rebase_1.png

Select the setting icon and choose Open on Git Shell

.. image:: ../_static/images/contributing/github_rebase_2.png

You will be presented with a new shell

.. image:: ../_static/images/contributing/github_rebase_new_shell.png

**2.** Next execute the following two commands and notepad will appear

::

  git fetch --all
  git rebase --ignore-date --interactive fusionpbx/master

|

change the first commit to reword and the following commit(s) to fixup (similar to screenshot below)

.. image:: ../_static/images/contributing/github_rebase_3.png

Close and save the text, next it will pop up another notepad for the commit message.
Enter the commit title on the first line, leave a line blank and enter the commit message (similar to screenshot below)

.. image:: ../_static/images/contributing/github_rebase_4.png

Close and save the text again.

**3.** Switch back to the github client and switch between history/changes to make it update and check it has done what you want.

.. image:: ../_static/images/contributing/github_rebase_5.png

**4.** If the changes are correct switch back to the git shell and execute this to push the changes

::

  git push --force-with-lease
  exit

|

All done!
