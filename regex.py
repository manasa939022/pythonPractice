import re
para = """ While talking about the pitch, the India skipper made his point: 
“I didn't have a chance to see it today. 9.15 
was the press conference, never thought it will be so early
He said it with a smile and was joking but the match is scheduled for a 10:30 am start and that is
 30 minutes earlier than usual. If conditions remain the same – read ‘cold, overcast and windy’ --
  India’s two-spinner theory will go out of the window and they will have to play four pacers instead.
'all those factors and see what will be the right combination for us to go.
“It looks like there will be a bit of help for the seamers, definitely,” said Sharma. “With the overhead
 conditions as well, it’s going to assist seamers a fair bit. I don’t know how drastically but the 
 pitch changes quite a bit in this part of the world. Like, when we played the last Test here, it 
 looked very similar to this. And then as the game went on, as the day went on, it got better and better, slower and slower. And reverse swing came into play as well on Day 5. So, yeah, we're going to consider
 """

print(re.findall('[a-zA-Z-]+',para))



