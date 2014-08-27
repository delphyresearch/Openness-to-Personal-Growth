####QUESTIONS CURRENT 8/26/2014

var QUESTIONS = {};

QUESTIONS.p = _.shuffle([
	 {
     id: 'BF-F1+',
     question: "I lose my temper...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more'] 
    },
    {
     id: 'BF-F2+',
     question: "I get upset...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F3+',
     question: "In general, my mood changes...",
     // should this be once a week?
     labels: ['A few times a month', 'A few times a week', 'A few times a day']
    },
    //{id: 'BF-F3.5+',
    // question: "Compared to other people of my gender, my mood changes...",//'''''''''/'/'/'/=/===/==/=/===/========================='
    // labels: ['Less frequently', "About as frequently other people's moods", 'More frequently ']},
    {
     id: 'BF-F4+',
     question: "I get agitated...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F5+',
     question: "I get stirred up...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F6-',
     question: "I find myself calm and relaxed...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F7-',
     question: "I keep my emotions under control...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F8-',
     question: "I lose my composure...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F9+',
     question: "In general, I get annoyed...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F10+',
     question: "I am filled with doubts about things...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F11-',
     question: "On average, I feel threatened...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F12+',
     question: "I worry about my future...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F13+',
     question: "I get discouraged about what I am doing...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F14+', 
     question: "I feel overwhelmed...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F15+', 
     question: "I find myself fearful or afraid...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F16+', 
     question: "I generally feel blue... ",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F17-', 
     question: "In general, I feel alive and full of life... ",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F18+', 
     question: "I feel uncomfortable with myself...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F19-', 
     question: "I try to live in the moment...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F20+',
     question: "I get embarrassed...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     id: 'BF-F21+', 
     question: "I feel the emotions of other people...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F22+', 
     question: "I sincerely inquire about other people's well-being...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
     //labels: [ 'A few times a month or less','1-2 times per week', '5 days a week or more']
    },
    {
     id: 'BF-F23+',
     question: "I sympathize with other people's feelings...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F24+', 
     question: "I take an interest in other people's lives...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F25+', 
     question: "I do things for others...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F26+', 
     question: "I take an interest in other people's problems...",
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F27-', 
     question: "I don't have time for other people's needs...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F28-',
     question: "I find myself indifferent to and/or unconcerned with the feelings of others...", //#####
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F29-',
     question: "I find I have no time for others...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F30+', 
     question: "I express my 'soft and caring' side...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     id: 'BF-F31+', 
     question: "I respect the will of those with more authority than I...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },//As often as possible, most of the time, not so much...
    {
     id: 'BF-F32+',
     question: "I try to avoid seeming pushy...", //#######
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F33+', 
     question: "I avoid imposing my will on others...", //#######
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F34-', 
     question: "I put people under pressure...", //#######
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F35-', 
     question: "I insult people...", //#######
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
 //   {
 //    id: 'BF-F36-', //this is an equal worth question.
//     question: "It occurs to me that I am better than certain, other people...", //
//     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
//    },
    {
     id: 'BF-F36-', 
     question: "I take advantage of others...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F37-', 
     question: "I seek conflict...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F39-', 
     question: "I have a good fight and/or argument...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F40', 
     question: "I consider how a situation will benefit my own personal gain...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {////industriousness
     id: 'BF-F41+', 
     question: "I carry out the plans I make...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F42+', 
     question: "I finish the tasks that I start...", // What does this mean here?
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F43+', 
     question: "I get small tasks done quickly...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F44+', 
     question: "I feel that know what I am doing...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F45-', 
     question: "I waste time...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F46-', 
     question: "I find it difficult to start working...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F47-', 
     question: "I mess things up...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F48-', 
     question: "I don't put my mind to the task at hand...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F49-', 
     question: "I postpone making decisions...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F50-', 
     question: "I get distracted...", //
     labels: ['A few times a month', 'A few times a week', 'Once a day or more']
    },
    {//////////////////////////////////////////////////////////////////////
     id: 'BF-F51', 
     question: "I make to-do lists...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F52-', 
     question: "I tidy things up...", ////\\//\\//\/\/\/\/\/\\\//\\//\/\\/\\/\\/\/\||\\||//||\\
     labels: ['A few times a month or less', 'Once a week', 'Three times a week or more']
    },
    {
     id: 'BF-F53+', 
     question: "I follow a regular schedule...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F54+', 
     question: "I find that I want everything to be 'just right'...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F55+', 
     question: "I see to it that rules are observed...", //
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F56+', 
     question: "I am methodical in my work...", // 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F57-', 
     question: "I leave my belongings lying around...", // 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F58-', 
     question: "I misplace things...", // '''''''''''''''''''''''''''''''''''''''''''
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F59-', 
     question: "I clean my room...", // 
     labels: ['A few times a month or less', 'Once a week', 'Three times a week or more']
    },
    {
     id: 'BF-F60-', 
     question: "I forget things when I travel...", // ***************************************************
     labels: ['Less than once every 3 trips', 'Every 2-3 trips', 'Every trip']
    },

    {///////////////////////////////////////////////////////////////////////Extroversion-Assertiveness
     id: 'BF-F61+', //=/+?+?+?-/-?-?-?-/-/-/-/-'-/-'-/----'/'/'/'''//'-'-/-/''/'/-'/-/'
     question: "I try to be friendly...", // connecting / making new friends has as much to do with empathy
      labels: ['A few times a month', 'Twice a week', 'Every day']
    },
    {
     id: 'BF-F62+', 
     question: "I quickly warm up to to others...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F63+', 
     question: "I show my feelings when I'm happy...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F64+', 
     question: "I enjoy what I happen to be doing...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F65+', 
     question: "I laugh heartily...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },

    {
     id: 'BF-F66+', 
     question: "I open up to my friends...", // 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F67-', 
     question: "I keep others at a distance...", // if this question doesn't load, it doesn't load
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F68-', 
     question: "I generally keep to myself...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F69-', 
     question: "I get caught up in the excitement of what is going on...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F70-', 
     question: "I find I am unenthusiastic...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {///////////////////////////////////////////////////////////////////////////////////////////
     id: 'BF-F71+', 
     question: "I take charge of situations...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F72+', 
     question: "I feel like I have a strong personality...", // 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F73+', 
     question: "I captivate people...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F74+', 
     question: "I interrupt people and conversations to make a point...", 
      labels: ['A few times a month', 'Twice a week', 'Every day']//if the item touches on social interaction...
    },
     {
     id: 'BF-F75+', 
     question: " I talk others into doing things my way...", //!!!!!!!!
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F76+', 
     question: "In a group, I am the first to act or decide what to do...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F77-', 
     question: "I do not act assertively...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F78-', 
     question: "In a group setting, I follow what the will of the group...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F79-', 
     question: "I wait for others to lead the way...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F80-', 
     question: "I hold back my opinions...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {/////////////////////////////////////////////////////OPENNESSS//////////////////////////////////
     id: 'BF-F81+', 
     question: "I understand new things quickly...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F82-', 
     question: "I get overwhelmed by information...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F83+', 
     question: "I try to solve complex problems...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F84+', 
     question: "I use large or uncommon words...", 
      labels: ['A few times a month or less', 'Twice a week', 'Every day']

    },
    {
     id: 'BF-F85+', 
     question: "I find that people over-explain things...", 
      labels: ['Less than once a month', 'A few times a month', 'Once a week or more']
    },
    {
     id: 'BF-F86+', 
     question: "I formulate abstract ideas clearly...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F87+', 
     question: "I try to learn about new things on my own time...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F88+', 
     question: "I think about abstract, cerebral ideas...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F89+', 
     question: "I have philosophical discussions...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F90-', 
     question: "I read light, fun books...", 
      labels: ['Hardly ever', 'About once a month', 'A few times a month or more']
    },
     {
     id: 'BF-F91-', 
     question: "It takes me a while to learn something new...", 
      labels: ['Hardly ever', 'Every so often', 'Constantly']//?????
    },
     {///////////////////////////////////////aesthetic sense///////////////////////////////////////////////////////////////////////
     id: 'BF-F92-', 
     question: "I notice the beauty of nature...", 
       labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F93-', 
     question: "I make time to enjoy art, photography or sculpture...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F94+', 
     question: "I reflect on things...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F95+', 
     question: "I get deeply immersed in music...", 
     labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F96+', 
     question: "I see beauty in things that others might not notice...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F97+', 
     question: "I find that I need a creative outlet...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F98+', 
     question: "I read poems and literature...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F99+', ////////////////////////////////////////////////////this needs work////
     question: "I go to the theater...", /// 
      labels: ['Once every 3 months', 'About once a month', 'Once a week or more']
    },
    {
     id: 'BF-F100+', 
     question: "I get lost in thought...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
    {
     id: 'BF-F101+', 
     question: "I daydream...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    },
     {
     id: 'BF-F102+', 
     question: "I notice emotional aspects of paintings and photographs ...", 
      labels: ['Less than once a month', 'A few times a month', 'Two to three times a week or more']
    }

 
]);

QUESTIONS.mindset = _.shuffle([
	{
		id: 'PBR_1_+',
		question: "Please estimate the following by selecting a number between 0 and 100:
		 I am _____ percent responsible for who I am.",
		labels: ['0', '50', '100']
	},
	{
		id: 'PBR_2_-',
		question: "If I'm running late, or I mess something up,
		 it's usually due to unforseeable circumstances.",   //more locus of control
		labels: ['Disagree', 'Neutral', 'Agree']  
	},
	{
		id: 'PBR_3_+',
		question: "In general, I take responsibility for what will happend to me,
		 regardless of external factors."
        labels: ['Disagree', 'Neither Agree nor Disagree', 'Agree'] 
	},
	{
		id: 'PBR_4_+',
		question: "No matter what happens or how I feel, it is ultimately on me to see something that I want done all of the way through. ",
		labels: ['Disagree', 'Neutral', 'Agree']  //
	},
	{
		id: 'PBR_5_+',
		question: "How well I do in life is _______ under my control.",
		labels: ['Somewhat', 'Mostly', 'Entirely']  //
	},
    {
        id: 'PBR_6+',
        question: "It is impossible for me to conciously change my personality",
        labels: ['Agree','Neutral','Disagree']
    },
    {
        id: 'PBR_7-',
        question: "Ou Personal flaws are deeply ingrained into who we are.",
        labels: ['Agree','Neutral','Disagree']
    },
	{
		id: 'OPG_1_+',
		question: "How familiar are you with the following statement: 
		'The purpose of life is to learn life's lessons.",
        labels: ['Unfamiliar', 'Neutral', 'Familiar']  //
	},
	{
		id: 'OPG_2_+',
		question: "There is something I can learn from every experience, 
		regardless of how good, bad, boring or interesting it is.",
		labels: ['Disagree', 'Neutral', 'Agree']  //
	},
	{
		id: 'OPG_3_-',
		question: "Negative emotions should be avoided entirely.",
		labels: ['Disagree', 'Neutral', 'Agree']  //
	},
	{
		id: 'OPG_4_+',
		question: "In general, I keep myself 'open' to criticism and feedback about my behavior.",
		labels: ['Disagree', 'Neutral', 'Agree']  //
	},
	{
		id: 'OPG_5_+',
		question: "I am _____ talking about my flaws with my friends.",
		labels: ['Uncomfortable', 'Neutral', 'Comfortable']  //
	},
	{
		id: 'OPG_6_+',
		question: "I am ______ trying to work on an aspect of my character.",
		labels: ['Never', 'Sometimes', 'Always']  //
	},
	{
		id: 'OPG_7_+',
		question:  "There is something that I can learn from ______ the people that I know.",
		labels: ['A few of', 'Some of', 'All of']  //
	},
	{
		id: 'IE_1_+',
		question: "All people are of equal worth.",
		labels: ['Disagree','Neutral','Agree']
	},
	{
		id: 'IE_2_+',
		question: "All people that I pass by, run into or interact with day-to-day are of equal status as I.",
		labels: ['Disagree','Neutral','Agree']
	},
    {
        id:'IE_3_NEUTRAL'
        question: "In general, I feel that I am _______ the people that I meet.",
        labels: ['Beneath', 'Equal to','Above']
    },
    //'ranking' people in a social hierarchy?
	{
		id: 'IE4_-',
		question: "Certain people don't deserve my empathy or attention.",
		labels: ['Disagree', 'Neutral', 'Agree']
	}
    {
        id: 'IE5_-',
        question: "Hitler was less than human.",
        labels: ['Disagree', 'Neutral', 'Agree']
    }

]);