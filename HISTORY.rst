.. :changelog:

Release History
---------------
0.5.3 (2014-06-08)
..................

* detect command execution status in a more robust way, fix ValueError caused during changed pipe commands when one of the command has no stdout and finishes earl.


0.5.2 (2014-06-08)
..................

* fix seekability detection bug in pypy<2.3.0-alpha0 for wr(), ap(). (brettatoms)


0.5.1 (2014-06-06)
..................

* fix target decoding error for ap() and wr() in py3. (brettatoms)


0.5.0 (2014-05-11)
..................

* expand environment variables
* set working directory using with statement (tburette)


0.4.0 (2014-05-07)
..................

* add env api
* add pypy support
* fix: support 'utf-8' encoded string as pipe input


0.3.0 (2014-05-05)
..................

* asynchronous command execution
* parallel command execution


0.2.0 (2014-05-04)
..................

* support IO redirect


0.1.1 (2014-05-01)
..................

* python 3 support


0.1.0 (2014-05-01)
..................

* overload '|' operator to simulate pipe syntax in shell (qiao)
* fix test cases for Mac (qiao)


0.0.8 (2014-05-01)
..................

* support subclass of string and list as argument for p()


0.0.7 (2014-04-30)
..................

* Register in Python index


0.0.1 (2014-04-03)
..................

* First blood
