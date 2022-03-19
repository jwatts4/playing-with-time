# Playing with time

This repo is for playing with OOP concepts in Python while also creating small programs with time-related
functionality (timers, pomodoros, etc.)

## Notes
Would it make sense for Timer to just be a queue of intervals? 


## TODO
- Add exception-handling.
- Add my own audio files for better alerts.
- Create interval timer functionality.
  - Allow the user to specify intervals and sub-intervals (e.g. pomodoro)
  - Play notifications to indicate the start/end of each interval (use different sounds for start and end).
  - Allow option for random intervals (e.g. on average, once every two minutes, start a ten-second interval).
- Implement a micro-interval timer to facilitate neuroplasticity (Andrew Huberman podcast).
- Add pause / continue functionality.
- Add the ability to set the time from the command line when running the file.
- The current beepy.beep() method halts execution until the audio track finishes, but I want the timer to
  begin as soon as the audio *starts* playing, not *after* it's finished playing.