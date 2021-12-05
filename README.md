This repository contains the solutions to my first advent of code. 

My goal for this month is simply to complete each day in less than an hour of total work time.

<b>12.05.21 Log</b><br>
Not too difficult today. Rather than reworking a new solution for part 2, I just decided to add a 'diagonals:bool' paramater to the mapper function. This is inefficient when solving both part 1/2 sequentially, as the map has to be entirely remade for part2. But, I figured it was easier to add this single parameter rather than spend time writing an additional function for part2.

<b>12.04.21 Log</b><br>
I feel pretty happy with my solution for identifying bingo board winners. I'm doing better and keeping focused on tasks one at a time rather than jumping back and forth between ideas. Today I opted for an OOP approach where I stored bingo boards and row/column hits as arrays. However, this OOP approach bypasses the array reduction features of numpy that can be used to much more efficiently solve the problem. Lesson learned for the future!

<b>12.02.21 Log</b><br>
Today's solution clicked pretty easily with me. Working with vessel graphs definitely helped with visualizing the variations in space.
