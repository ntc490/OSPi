ospi - Opensource Sprinkler Controller Project
==============================================

This is a variation of OSPi.  It will leverage the web UI implementation, but
scrap much of the other Python code.  Goals include:

Features I like from OSPi:
* Ability to control zones from smart-phone
* Never have to set the time - even after power failures (thanks NTP)
* Logging

Features I'd like to have:
* Press a button to skip a day (used after it rains a lot)
* Adjust station times based on percentage or weather data
  (couldn't figure out how to do it well with OSPi).
* Simpler to use
* Simpler to extend/modify (more friendly code)

Weaknesses of OSPi source code:
* Abbreviated variable names make it hard to read and understand.  Yes, there's
  a legend.  See "Code Complete" or one of many other resources for good ideas
  on this topic.
* Logic is very deeply nested in critical areas.  The Cyclomatic complexity is
  too high.
* Use of higher level concepts in the code would make things easier to
  understand.  It reminds me of assembly code in a few places.
* The product features aren't intuitive to me as a user.  Maybe some docs would
  help?  I'd rather keep it simple.
