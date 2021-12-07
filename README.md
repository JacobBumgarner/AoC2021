This repository contains the solutions to my first advent of code. 

My goal for this month is simply to complete each day in less than an hour of total work time.

<b>12.06.21 Log</b><br>
Part1 was easy... too easy... yep! Part2 came in as a zinger. Today we had to model exponential growth of lanternfish. For part1, we had to measure 80 days of growth. To do this I created an array where each element represented a fish and its value represented it's breeding 'timer'. When the timer hit 0, a new element was added to the array and the timer was reset. See the problem? This solution is highly limited to small day ranges of growth. For Part2, we're asked to measure growth out to 256 days... my initial solution could never solve this time range!

For Part2, I initially imagined reducing the array size by storing the fish as bool elements rather than uint8's and keeping them in different age bins. In this convoluted solution I'd move the fish from bin to bin between days. At this point though, my time was pretty limited, and feeling stuck, I decided to outsource some help. Writing this now, I can't believe I didn't converge onto the final solution with this initial idea, but I ended up peaking at a friend's solution to find that he used a dict to store aging fish. This immediately made me recognize that I should use a histogram. My implementation after this ended up being pretty simple! Lesson learned? Spend more time ponedering, if you have it?

<b>12.05.21 Log</b><br>
Not too difficult today. Rather than reworking a new solution for part 2, I just decided to add a 'diagonals:bool' paramater to the mapper function. This is inefficient when solving both part 1/2 sequentially, as the map has to be entirely remade for part2. But, I figured it was easier to add this single parameter rather than spend time writing an additional function for part2.

<b>12.04.21 Log</b><br>
I feel pretty happy with my solution for identifying bingo board winners. I'm doing better and keeping focused on tasks one at a time rather than jumping back and forth between ideas. Today I opted for an OOP approach where I stored bingo boards and row/column hits as arrays. However, this OOP approach bypasses the array reduction features of numpy that can be used to much more efficiently solve the problem. Lesson learned for the future!

<b>12.02.21 Log</b><br>
Today's solution clicked pretty easily with me. Working with vessel graphs definitely helped with visualizing the variations in space.
