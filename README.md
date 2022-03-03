This repository contains the solutions to my first advent of code. 

My goal for this project is to simply complete each day's puzzle. I'm less interested in speed of completion and more interested in taking the time to understand the puzzle and implement a solid solution

<b><strike>12.12.21</strike> 03.02.22 Log</b><br>
Today's puzzle was really fun for me to solve! We were given a map with individual path points and connections between those points. Some of these points could only be visited once or twice, and others could be visited infinitely. We then had to find the maximal number of paths that reached from the start to the end of the path that followed the visitation rules.

Since I am quite familiar with graph theory thanks to VesselVio, I decided to create my own graph classes. The first class was my main graph class (the Cave), and the second class was for the vertices (the Nodes). Then after creating these classes, I made a simple recursive search function to find the maximal number of paths. Quite fun!


<b><strike>12.11.21</strike> 02.28.22 Log</b><br>
This puzzle didn't present too much difficulty. I solved it using np.argwhere to identify the flashing points and slicing to update the N8(p) elements.

<b><strike>12.10.21</strike> 02.22.22 Log</b><br>
After a long couple of months of grinding out code for another one of my projects, I decided that I wanted to come back to these challenges. The 10th day was pretty interesting. Once I figured out exactly what the rules were, it was relatively straight forward to solve. Figuring the rules out took me much longer than I would've wished, however. I don't think that it was clearly described that any chunks inside of main chunks must be complete; instead, this had to be figured out intuitively. 

I ended up iteratively removing complete chunk markers until the line wasn't changing anymore. From here, if there was an absence of any closers, the line was defined as incomplete. This line was then reversed and tallied as instructed. If there was a closer present, I identified the first one and added it to the tally as instructed.

<b>12.09.21 Log</b><br>
Image processing!

<b>12.08.21 Log</b><br>
There's nothing clean about my solution to Day 8. I wish I could say that I developed some elegant code cracking solution, but I decided to just brute force it using sets created between the different numbers. Just glad I was able to solve it!

<b>12.07.21 Log</b><br>
I was able to complete today's challenge relatively quickly and without too much difficutly. Unfortunately, my solution to part2 isn't exactly *quick*... It took about 23 seconds to idneitfy the optimal convergence location. If I had more time, I might try to sit and consider a more optimized solution, but I'm happy with just solving it for today! I'll definitely compare my solution to others to see what I could've done better.

<b>12.06.21 Log</b><br>
Part1 was easy... too easy... yep! Part2 came in as a zinger. Today we had to model exponential growth of lanternfish. For part1, we had to measure 80 days of growth. To do this I created an array where each element represented a fish and its value represented it's breeding 'timer'. When the timer hit 0, a new element was added to the array and the timer was reset. See the problem? This solution is highly limited to small day ranges of growth. For Part2, we're asked to measure growth out to 256 days... my initial solution could never solve this time range!

For Part2, I initially imagined reducing the array size by storing the fish as bool elements rather than uint8's and keeping them in different age bins. In this convoluted solution I'd move the fish from bin to bin between days. At this point though, my time was pretty limited, and feeling stuck, I decided to outsource some help. Writing this now, I can't believe I didn't converge onto the final solution with this initial idea, but I ended up peaking at a friend's solution to find that he used a dict to store aging fish. This immediately made me recognize that I should use a histogram. My implementation after this ended up being pretty simple! Lesson learned? Spend more time pondering, if you have it?

<b>12.05.21 Log</b><br>
Not too difficult today. Rather than reworking a new solution for part 2, I just decided to add a 'diagonals:bool' paramater to the mapper function. This is inefficient when solving both part 1/2 sequentially, as the map has to be entirely remade for part2. But, I figured it was easier to add this single parameter rather than spend time writing an additional function for part2.

<b>12.04.21 Log</b><br>
I feel pretty happy with my solution for identifying bingo board winners. I'm doing better and keeping focused on tasks one at a time rather than jumping back and forth between ideas. Today I opted for an OOP approach where I stored bingo boards and row/column hits as arrays. However, this OOP approach bypasses the array reduction features of numpy that can be used to much more efficiently solve the problem. Lesson learned for the future!

<b>12.02.21 Log</b><br>
Today's solution clicked pretty easily with me. Working with vessel graphs definitely helped with visualizing the variations in space.
