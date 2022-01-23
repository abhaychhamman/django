#include<stdio.h>
#include<string.h>
char means[150][20]=
{   
"Fabulous","Face","Fast","Feasible","Fertile","Fluid","Foe","Forgive","Fresh","Friend",

"Gain","Gather","Gaunt","Generous",
"Gentle","Genuine","Glad","Good",
"Gorgeous","Gratitude",

"Handy","Hard","Hate","Humiliate",
"Hold","Healthy","Hesitate","Humble",
"House","Hospitable",

"Identical","Idle","Ignorant","Immature",
"Important","Innocent","Inferior",
"Intelligent","Internal","Intolerant",

"Joy","Jealous","Judicial","Judicious",
"Justify","Join","Jolly","Joke","Jublee",
"Job",

"Kind","Kill" ,"Keep","Kidnap","Kneel","Knell","Kitchen","King","Kick","Kit",

"Large","Lovely","Last","Latest","Late","Lathal","Legal","Last","Laugh","Listen",

"Maximum","Mean","Mend","Minor","Moral","Morbid","Morose","Mourn","Magnify", "Meager",

"Naughty","Neat","Negligent","Nervous","Neutral","New","Nice","Normal","Numerous","Nothing",

"Obey","Open","Optional","Ordinary","Ominous","Observe","Odd","Offend","Oblivious","Opaque",

};

char syns[150][20]=

{
"Marvelous","Confront","Rabid","Possible","Productive","Liquid","Enemy","Excuse","New","Buddy",

"Receive","Collect","Thin","Selfless","Tender","Sincere","Delighted","Nice","Dazzling",
"Thankfulness",

"Useful","Difficult","Detest","Embarrass","Grasp","Strong","Pause","Modest","Home",
"Welcoming",

"Alike","Inactive","uninformed","Inexperienced","Significant","Guiltless","Substandard","Sensible","Inside","Prejudiced",

"Delight","Envious","Legal","Sensible","Validate","Connect","Joyful","Jest","Anniversary","Work",

"type","Murder","Hold","Capture","Bowldown","Sound","Cookhouse","Roler","Giveup","Tools",

"Big","Considerate","Subsequent","After","Posterior","Fatal","Legitimate","Final","Giggle","Hear",

"Highest","Nasty","Fix","Lesser","Ethical","Awful","Gloomy","Bemoan","Expand","Poor",

"Bad","Clean","Careless","Ruffled","Impartial","Modern","Fine","Usual","Serveral","Nobody",

"Comply","Unfold","Elective","Usual","Menacing","Study","Strange","Disgust","Dazed","Unclear",
	
};
int main(int argc, char *argv[])
{
	char user_mean[20];
	printf("enter your meaning?q");
	scanf("%s",&user_mean);
	printf("   %s    %s\n",user_mean,means[9]);
		printf("    %s",syns[10]);
}