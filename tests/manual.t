Setup:

  $ alias xt="python $TESTDIR/../t.py --task-dir `pwd` --list test"

Create a task file manually (no IDs):

  $ cat >> test << EOF
  > Sample one.
  > Sample two.
  > EOF
  $ xt
  7 - Sample two.
  3 - Sample one.

Add some manual tasks:

  $ echo 'Custom one. | id: custom1' >> test
  $ echo 'Custom two. | id: custom2' >> test
  $ xt
  7       - Sample two.
  custom1 - Custom one.
  3       - Sample one.
  custom2 - Custom two.

Rewrite the task file:

  $ cat > test << EOF
  > New.
  > EOF
  $ xt
  5 - New.
