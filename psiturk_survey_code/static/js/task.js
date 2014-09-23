/*
 * Requires:
 *     psiturk.js
 *     utils.js
 */

// Initalize psiturk object
var psiTurk = PsiTurk(uniqueId, adServerLoc);

var mycondition = condition;  // these two variables are passed by the psiturk server process
var mycounterbalance = counterbalance;  // they tell you which condition you have been assigned to

// All pages to be loaded
var pages = [
	"stage.html",
	"postquestionnaire.html"
];

// add as a list as many pages as you like
var instructionPages = [
	"instructions/instruct-1.html",
	"instructions/instruct-2.html",
	"instructions/instruct-3.html",
	"instructions/instruct-ready.html"
];

psiTurk.preloadPages(pages.concat(instructionPages));


// Each key should represent a set of questions
var QUESTIONS = {};


QUESTIONS.p = _.shuffle([
//Question Id's point in the direction of the label. (1-10 = + on withdrawal)

//paste this whole thing back into lines 31 – 634
//need instructions that the endpoints should be thought of as containing the words “or less”, or, “or more”
     {
     id: 'BF-F1+',
     question: "I lose my temper...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F2+',
     question: "I get upset...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F3+',
     question: "In general, my overall mood changes...",
     labels: ['Once a week or less', '3-4 times a week', 'Once per day or more']
    },
    //{id: 'BF-F3.5+',
    // question: "Compared to other people of my gender, my mood changes..."
    {
     id: 'BF-F4+',
     question: "I get agitated...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F5+',
     question: "I get stirred up...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F6-',
     question: "I find myself calm and relaxed...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F7-',
     question: "I keep my emotions under control...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F8-',
     question: "I lose my composure...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F9+',
     question: "In general, I get annoyed...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F10+',
     question: "I am filled with doubts about things...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F11-',
     question: "On average, I feel threatened...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F12+',
     question: "I worry about my future...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F13+',
     question: "I get discouraged about what I am doing...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F14+', 
     question: "I get overwhelmed...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F15+', 
     question: "I get fearful or afraid...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F16+', 
     question: "I generally feel blue... ",
    labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F17-', 
     question: " I feel alive and full of life... ",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F18+', 
     question: "I feel uncomfortable with myself...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F19-', 
     question: "I try to live in the moment...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F20+',
     question: "I get embarrassed...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']

    },
    { // Empathy/Agreeableness 
     id: 'BF-F21+', 
     question: "In general, I feel the emotions of other people...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F22+', 
     question: "I sincerely inquire about other people's well-being...",
    labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F23+',
     question: "I sympathize with other people's feelings...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F24+', 
     question: "I take an interest in other people's lives...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F25+', 
     question: "I do things for others...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F26+', 
     question: "I take an interest in other people's problems...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F27-', 
     question: "I don't prioritize other people's needs...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F28-',
     question: "I am generally indifferent to the feelings of others...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F29-',
     question: "In general, I have no time for others...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F30+', 
     question: "I express my 'soft and caring' side...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F31+', 
     question: "I respect the will of those with more authority than I...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F32+',
     question: "I try to avoid seeming pushy...",
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F33+', 
     question: "I actively avoid imposing my will on others...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F34-', 
     question: "I put people under pressure...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F35-', 
     question: "I insult people...",  
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F36-', 
     question: "I take advantage of others...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F37-', 
     question: "I seek conflict...",
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
   },
    {
     id: 'BF-F39-', 
     question: "I have an argument and/or good fight...",
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F40', 
     question: "I consider how a situation will benefit my own personal gain...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']  
  },
    {
     id: 'BF-F41+', 
     question: "I carry out the plans that I make...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
   },
    {
     id: 'BF-F42+', 
     question: "I finish the tasks that I start...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F43+', 
     question: "I get small tasks done quickly...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F44+', 
     question: "I feel like I know what I am doing...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    },
    {
     id: 'BF-F45-', 
     question: "I waste time...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F46-', 
     question: "I find it difficult to start working...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']  
  },
    {
     id: 'BF-F47-', 
     question: "I generally mess things up...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F48-', 
     question: "I don't put my mind to the task at hand...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F49-', 
     question: "I postpone making decisions...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F50-', 
     question: "I get distracted...",
     labels:['Every day', '3 times a week', 'Once every two weeks']
    },
    {
     id: 'BF-F51+', 
     question: "I make to-do lists...", 
     labels:['Once a week or less', '3 times a week', 'Every day']
    },
     {
     id: 'BF-F52-', 
     question: "I tidy up my living space...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F53+', 
     question: "I follow a regular schedule...", 
    labels:['Once a week or less', '3 times a week', 'Every day']
    },
    {
     id: 'BF-F54+', 
     question: "I find that I want everything to be 'just right'...",
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']   
 },
    {
     id: 'BF-F55+', 
     question: "I see to it that rules are observed...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F56+', 
     question: "I take care to be methodical in my work...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F57-', 
     question: "I leave my belongings lying around...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F58-', 
     question: "I misplace things...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F59-', 
     question: "I straighten up my room...", 
     labels:['Once a week or less', 'Around 3 times a week',  'Every day or more']
    },
    {
     id: 'BF-F60-', 
     question: "I forget things when I travel...", 
     labels: ['Once every 5 trips', 'Every 3 trips', 'Every trip']
    },

    {//Extroversion
     id: 'BF-F61+',
     question: "I try to be friendly towards others...",
      labels: ['A few times a month', 'Twice a week', 'Every day']
    },
    {
     id: 'BF-F62+', 
     question: "I warm up quickly to others...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
},
    {
     id: 'BF-F63+', 
     question: "I show my feelings when I'm happy...",  
      labels:['Rarely', 'Sometimes', 'Every time'] 
//might have something to do with intensity of happiness… ‘everytime I’m even remotely happy’…
    },
     {
     id: 'BF-F64+', 
     question: "I go out of my way to include people  in conversations...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
     {
     id: 'BF-F65+', 
     question: "I laugh heartily...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
    {
     id: 'BF-F66+', 
     question: "I open up to my friends...", 
     labels: ['Less than once a month', 'A few times a month', 'Once a week or more']      
  },
    {
     id: 'BF-F67-', 
     question: "I keep others at a distance...", 
      labels: ['Less than once a month', 'A few times a month', 'Once a week or more']  
        },
    {
     id: 'BF-F68-', 
     question: "I generally keep to myself...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']      
    },
    {
     id: 'BF-F69+', 
     question: "I get caught up in the excitement of what is going on...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']      
    },
    {
     id: 'BF-F70-', 
     question: " I am generally unenthusiastic...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']      
    },
    {
     id: 'BF-F71+', 
     question: "I take charge of situations...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
     {
     id: 'BF-F72+', 
     question: "I feel like I have a strong personality...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F73+', 
     question: "I captivate people during conversations...", 
     labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
},
    {
     id: 'BF-F74+', 
     question: "I interrupt people and conversations to make a point...", 
      labels: ['Once every 2 weeks or less', '3 times a week or more', 'Every day']
    },
     {
     id: 'BF-F75+', 
     question: " I talk others into doing things my way...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
    {
     id: 'BF-F76+', 
     question: "In a group, I am the first to act or decide what to do...", 
      labels:['Less than once a month', 'Once every two weeks', 'Once a week or more']    
    },
     {
     id: 'BF-F77-', 
     question: "I act in a passive manner...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
    {
     id: 'BF-F78-', 
     question: "In a group, I 'go with the low' and follow what the group decides...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
     {
     id: 'BF-F79-', 
     question: "I wait for others to lead the way...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
     {
     id: 'BF-F80-', 
     question: "I hold back my opinions...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
     {///////////OPENNESS
     id: 'BF-F81+', 
     question: "I understand new things quickly...", 
      labels:['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']    
    },
     {
     id: 'BF-F82-', 
     question: "I get overwhelmed by too much information...", 
     labels :['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
   },
     {
     id: 'BF-F83+', 
     question: "I try to solve complex problems...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
 },
    {
     id: 'BF-F84+', 
     question: "I use or make not of large / uncommon words...", 
      labels: ['Once every 2 weeks or less', 'Around 3 times a week', 'Every day']

    },
    {
     id: 'BF-F85+', 
     question: "I formulate abstract ideas clearly...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F86+', 
     question: "I learn about new things on my own time...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F87+', 
     question: "I think about abstract, cerebral ideas...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
    {
     id: 'BF-F88+', 
     question: "I have a philosophical discussion...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
   },
    {
     id: 'BF-F89-', 
    question: "Regarding books,  the words 'easy', 'light' and/or 'fun' describe...",
      labels: ['Almost none of the books I read', 'Some of the books I read', 'Nearly every book I read']
    },
     {
     id: 'BF-F90-', 
     question: "When I learn something new, it takes me a while to fully understand it...", 
      labels: ['Almost never', 'Every so often', 'Every time']
    },
    {
    id:'BF-F91+',
    question:"I read longform journalism articles...",
    labels:['Less than once a month','A few times a month','Once a week or more']
    },

     {     ///////////////////////////////////////aesthetic 
     id: 'BF-F92-', 
     question: "I notice the beauty of nature...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F93-', 
     question: "I spend time enjoying art, photography or sculpture...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F94+', 
     question: "I reflect on things and/or introspect...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F95+', 
     question: "I get deeply immersed or lost in music...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
     {
     id: 'BF-F96+', 
     question: "I see beauty in things that others might not notice...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
     {
     id: 'BF-F97+', 
     question: "I find that I need a creative outlet...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
    },
    {
     id: 'BF-F98+', 
     question: "I read poems or literature or plays...", 
     labels: ['Once every 2 weeks or less', 'A few times a month', 'Around once a week'] 
    },
  
    {
     id: 'BF-F99+', 
     question: "I get lost in thought...", 
      labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more'] 
   },
    {
     id: 'BF-F100+', 
     question: "I daydream...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    },
     {
     id: 'BF-F101+', 
     question: "I notice emotional aspects of paintings and photographs ...", 
     labels: ['Once every 2 weeks or less', 'Around once a week', '3 times a week or more']
    }
]);

QUESTIONS.mindset = _.shuffle([
    { //naming scheme : ‘construct_humilityitemnumber_direction’
        id: 'PBR_1+',
        question: "I am ______ % responsible for who I am.",
        labels: ['0', '50', '100']
    },


    {
        id: 'PBR_2-',
        question: " If I’m running late, or I mess something up, it’s usually due to unforeseeable circumstances. ",   
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'PBR_3+',
        question: " I take ______ % responsibility for what will happen to me during the next few months. ",
        labels: ['0', '50', '100']  
    },
    {
        id: 'PBR_4+',
        question: " It is ultimately my fault if I don’t end up seeing a project all the way through.",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'PBR_5+',
        question: "How well I do in life is _____ under my control." ,
        labels: ['Not really', 'Somewhat', 'Entirely']  
    },
    {
        id: 'PBR_6-',
        question: "In general, people’s personalities stop changing after a certain age.",
        labels:  ['Disagree', 'Neutral', 'Agree']
        
    },
    {
        id: 'PBR_7-',
        question: "On the whole, personal shortcomings are impossible to overcome.",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'PBR8_',
        question: "Fate has a lot to do with who a person becomes.",
        labels: ['Disagree', 'Neutral', 'Agree'] 
    },
    {
        id: 'OPG9+',
        question: "How familiar are you with the following phrase: 'The purpose of life is to learn life’s lessons'. ",
        labels: ['Unfamiliar', 'Neutral', 'Familiar']  
    },
    {
        id: 'OPG_10+',
        question: "I How much do you believe the following phrase: 'The purpose of life is to learn life’s lessons'. ",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'OPG_11+',
        question:  "There is something I can learn from every experience I have, regardless of how it makes me feel. ",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'OPG_12-',
        question: "Negative emotions and feelings should be avoided.",
        labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
        id: 'OPG_13+',
        question: "In general, I keep myself ‘open’ to criticism and feedback about my behavior.",
        labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
        id: 'OPG_14+',
        question: " I am ____ talking about my flaws with my friends.",
        labels: ['Uncomfortable', 'Neutral', 'Comfortable']
    },
    {
        id: 'OPG_15+',
        question: "I am ____trying to work on an aspect of my character.",
        labels: ['Rarely', 'Neutral', 'Frequently']
    },
    {
        id: 'OPG_16+',
        question: "There is something valuable I can learn from _______ of the people I know.",
        labels: ['Few', 'Some', 'All']
    },
    {
        id: 'OPG_17+',
        question: "In comparison to other people, I have more _______ than average.",
        labels: ['Flaws', ' ', 'Virtues'] // scored as 2x distance away from 50.
    },
{
        id: 'OPG_18-',
        question: "Negative criticism is detrimental.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
        id: 'OPG_18-',
        question: "I mentally criticize myself when I make a mistake.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
        id: 'IE_19+',
        question: "All people are of equal worth.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
    id:'IE_20+',
    question:"The people I pass by, or run into day to day are of the same status as I.",
    labels: ['Disagree', 'Neutral ', 'Agree']
},
{
    id:'IE_21+',
    question:"In general, I feel ______ than the people I interact with.",
    labels: ['Less Important', 'About the same ', 'More Important'] //2x distance from 50
},
{
    id:'IE_22-’',
    question:'Some people don’t deserve my empathy or attention.',
labels: ['Disagree', 'Neutral', 'Agree']
},

{
    id:'IE_23-',
    question:'Hitler was less than human.',
    labels:['Disagree', 'Neutral', 'Agree']
},
{
    id:'IE_23-',
    question:'I make eye contact with homeless people.',
    labels:['Rarely', 'Sometimes', 'Frequently']
},
{
    id:'IE_24-',
    question:'I get intimidated by people who are smart, or pretty, or both.',
    labels:['Rarely', 'Sometimes', 'Frequently']
},
{
    id:'IE_25-',
    question: 'I use a ‘1-10’ scale when determining whom I might date.',
    labels:['Rarely', 'Sometimes', 'Frequently']
    }
    
]);

if (!_.indexBy) {
	// DIY indexBy support, since psiTurk uses an older version of Underscore.js
	_.mixin({
		indexBy: function(indexArray, by) {
			return _.chain(indexArray)
				.groupBy(by)
				.map(function(arr, key) { return [key, _.first(arr)]; })
				.object()
				.value();
		}
	});
}

/********************
* HTML manipulation
*
* All HTML files in the templates directory are requested
* from the server when the PsiTurk object is created above. We
* need code to get those pages from the PsiTurk object and
* insert them into the document.
*
********************/

var PhasedQuestions = function() {
	var self = this;

	// NOTE: the following variables can be safely modified

	// Each set of questions, in the order they should appear
	self.phases = [QUESTIONS.p]; // , QUESTIONS.mindset];

	// The maximum number of questions per page
	self.PER_PAGE = 25;

	// WARNING: the following variables are intended for internal use

	if (!self.phases) throw new Error('No phases were set.');

	// HTML classes
	self.classes = {
		error: 'has-warning',
		answered: 'has-success',
		hidden: 'hidden'
	};

	// Which page we're on
	self.PAGE_INDEX = 0;

	// The default value for input[type=range]
	self.defaultValue = 50;

	// The options for $.noUiSlider
	self.sliderOptions = {
		start: self.defaultValue,
		range: { min: 0, max: 100 }
	};

	// The current set of questions
	self.currentPhase = null;

	// Have the validations been run at least once
	// self.hasValidated = false;

	// Load the correct HTML
	psiTurk.showPage('stage.html');

	// Ready the template function
	self.template = _.template($('#question-template').html());

	// Questions keyed by ID
	self.questionsById = _.extend.apply(_, [{}].concat(
		_.map(self.phases, function(phase) { return _.indexBy(phase, 'id'); })
	));

	// Functions

	self.nextPhase = function() {
		if (self.phases.length) {
			// Set the next phase as the current one
			self.currentPhase = self.phases.shift();

			// Reset to page #1
			self.PAGE_INDEX = 0;

			// And show it
			self.renderPage();
		} else {
			// No more questions!
			self.finish();
		}
	};

	self.validate = function() {
		// Any unanswered questions?
		var $unansweredQuestions = $('.phased-questions .form-group').not('.' + self.classes.answered);
		$unansweredQuestions.addClass(self.classes.error);
		return !$unansweredQuestions.length;
	};

	self.nextPage = function() {
		// Last page of questions; proceed to next set
		if (self.isOnLastPage()) {
			return self.nextPhase();
		}

		// Render the next page of questions
		self.PAGE_INDEX++;
		self.renderPage();
	};

	// Helpers
	self.getQuestionById = function(id) { return self.questionsById[id]; };
	self.isOnFirstPage = function() { return self.PAGE_INDEX === 0; };
	self.isOnLastPage = function() { return Math.floor(self.currentPhase.length / self.PER_PAGE) === self.PAGE_INDEX; };

	var _toggleWarning = function(bool) {
		$('.phased-questions .alert-warning').toggleClass(self.classes.hidden, !bool);
		$('.phased-questions button.continue').prop('disabled', bool);
	};

	self.showWarning = $.proxy(_toggleWarning, null, true);
	self.hideWarning = $.proxy(_toggleWarning, null, false);

	self.renderPage = function() {
		// Reset some state
		// self.hasValidated = false;
		self.hideWarning();

		var startIndex = self.PER_PAGE * self.PAGE_INDEX;

		// Run this chunk of questions through the template function
		var questions = _.map(self.currentPhase.slice(startIndex, startIndex + self.PER_PAGE), self.template);

		// Set the page number
		$('.phased-questions .page-num').text(self.PAGE_INDEX + 1);

		// Set the question # offset
		// and render the questions
		$('.phased-questions form ol')
			.attr('start', startIndex + 1)
			.html(questions.join("\n"));

		$('.phased-questions .slider').noUiSlider(self.sliderOptions);

		window.scrollTo(0,0);
	};

	// Move on to the next psiTurk situation
	self.finish = function() { currentview = new Questionnaire(); };

	// Bind the UI elements

	// When "Continue" is clicked
	$(document).on('submit', '.phased-questions form', function(e) {
		e.preventDefault();

		var $form = $(e.currentTarget);

		// Disable "Continue" button
		$form.find('button.continue').prop('disabled', true);

		if (self.validate()) {
			// All questions were answered; record them and proceed!
			var answers = _.indexBy($form.serializeArray(), 'name');
			_.each(answers, function(answer, id) {
				var question = self.getQuestionById(id);
				question.answer = answer.value;
				psiTurk.recordTrialData(question);
			});
			self.nextPage();
		} else {
			// Scroll to the top and show the warning
			$('html, body').animate({ scrollTop: 0 }, 1000, self.showWarning);
		}
	});

	// When a slider is clicked/moved
	$(document).on('change', '.phased-questions .slider', function(e) {
		var $el = $(e.currentTarget);

		$el.next('input').val($el.val());

		// Remove the warning color from this question
		$el.closest('.form-group')
			.addClass(self.classes.answered)
			.removeClass(self.classes.error);

		// No more questions have default values
		if (!$('.form-group.' + self.classes.error).length) {
			self.hideWarning();
		}
	});

	// Start 'er up!
	self.nextPhase();
};

/****************
* Questionnaire *
****************/

var Questionnaire = function() {

	var error_message = "<h1>Oops!</h1><p>Something went wrong submitting your HIT. This might happen if you lose your internet connection. Press the button to resubmit.</p><button id='resubmit'>Resubmit</button>";

	record_responses = function() {
		psiTurk.recordTrialData({ phase: 'postquestionnaire', status: 'submit' });

		$('textarea').each(function(i, val) {
			psiTurk.recordUnstructuredData(this.id, this.value);
		});
		$('select').each(function(i, val) {
			psiTurk.recordUnstructuredData(this.id, this.value);
		});
	};

	prompt_resubmit = function() {
		replaceBody(error_message);
		$("#resubmit").click(resubmit);
	};

	resubmit = function() {
		replaceBody("<h1>Trying to resubmit...</h1>");
		reprompt = setTimeout(prompt_resubmit, 10000);

		psiTurk.saveData({
			success: function() {
				clearInterval(reprompt);
				psiTurk.computeBonus('compute_bonus', finish);
			},
			error: prompt_resubmit
		});
	};

	// Load the questionnaire snippet
	psiTurk.showPage('postquestionnaire.html');
	psiTurk.recordTrialData({ phase: 'postquestionnaire', status: 'begin' });

	$("#next").click(function() {
		record_responses();
		psiTurk.saveData({
			success: function(){
				psiTurk.computeBonus('compute_bonus', function() {
					psiTurk.completeHIT(); // when finished saving compute bonus, the quit
				});
			},
			error: prompt_resubmit
		});
	});


};

// Task object to keep track of the current phase
var currentview;

/*******************
 * Run Task
 ******************/
$(window).load(function() {
	psiTurk.doInstructions(
		instructionPages, // a list of pages you want to display in sequence
		function() {
			// what you want to do when you are done with instructions
			currentview = new PhasedQuestions();
		}
	);
});
