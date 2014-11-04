/*
 * Requires:
 *     psiturk.js
 *     utils.js
 */

//////////////////////////////STUDY II: now with extra Humility / Personal Growth (V2) !


// Initalize psiturk object
var psiTurk = PsiTurk(uniqueId, adServerLoc);

var mycondition = condition;  // these two variables are passed by the psiturk server process
var mycounterbalance = counterbalance;  // they tell you which condition you have been assigned to

// All pages to be loaded
var pages = [
	"stage.html",
	"postquestionnaire.html",
    "complete.html"
];

// add as a list as many pages as you like
var instructionPages = [
	"instructions/instruct-1.html",
    "instructions/instruct-ready.html"
];

psiTurk.preloadPages(pages.concat(instructionPages));


// Each key should represent a set of questions
var QUESTIONS = {};

//QUESTIONS.sample = _.shuffle([
 //   {
  //   id: 'SAMPLE1+',
  //  question: "I eat chocolate cake...",
  //  / labels: ['Once every 2 weeks', 'Once a week', '3 times a week'] 
  //  },
   // {
  //   id: 'BF-F2+',
  //   question: "I go to bookstores...",
  //   labels: ['Once a month','Once every 2.5 weeks','Once a week'] 

  //  }
   // ]);


QUESTIONS.p = _.shuffle([
//QUESTIONS.p = [

  {//NOTE POSITIVELY KEYED TOWARDS NEUROTICISM, NOT STABILITY!!!!!
     id: 'BFAS-1+',
     question: "I get angry easily.",
     labels: ['Disagree', 'Neutral', 'Agree'] 
    },
    {
     id: 'BFAS-2+',
     question: "I get upset easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-3+',
     question: "I change my mood a lot.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },

    {
     id: 'BFAS-4+',
     question: "I am a person whose moods go up and down easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-5+',
     question: "I get agitated easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-6+',
     question: "I can be stirred up easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-F7-',
     question: "I rarely get irritated.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-8-',
     question: "I keep my emotions under control",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-9-',
     question: "I rarely lose my composure.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-10-',
     question: "I am not easily annoyed.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {//Withdrawal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     id: 'BFAS-11+',
     question: "I am filled with doubts about things.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-12+',
     question: "I feel threatened easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-13+',
     question: "I worry about things.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-14+', 
     question: "I am easily discouraged.", 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-15+', 
     question: "I become overwhelmed by events.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-16+', 
     question: "I am afraid of many things.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-17-', 
     question: "I seldom feel blue.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-18-', 
     question: "I feel comfortable with myself.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-19-', 
     question: "I rarely feel depressed.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-20-',
     question: "I am not embarrassed easily.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {///AGREEABLENESS///////////////////////////////////////////////////////////////////////////////////////////////////
     id: 'BFAS-21+', 
     question: "I feel others' emotions.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-22+', 
     question: "I inquire about others' well-being.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-23+',
     question: "I sympathize with others' feelings.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-24+', 
     question: "I take an interest in other people's lives.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-25+', 
     question: "I like to do things for others.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-26-', 
     question: "I am not interested in other people's problems.",
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-27-', 
     question: "I can't be bothered with other's needs.", //#####
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-28-',
     question: "I am indifferent to the feelings of others.", //#####
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    { 
     id: 'BFAS-29-',
     question: "I take no time for others.", 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-30-', 
     question: "I don't have a soft side.", 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     id: 'BFAS-31+', 
     question: "I respect authority.", 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-32+',
     question: "I hate to seem pushy.", //#######
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-33+', 
     question: "I avoid imposing my will on others.", //#######
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-34+', 
     question: "I rarely put people under pressure.", //#######
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-35-', 
     question: "I insult people.", //#######
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-36-', 
     question: "I believe that I am better than others.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-37-', 
     question: "I take advantage of others.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-38-', 
     question: "I  seek conflict.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-39-', 
     question: " I love a good fight.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-40-', 
     question: "I am out for my own personal gain.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {///conci...
     id: 'BFAS-41+', 
     question: "I carry out my plans.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-42+', 
     question: "I finish what I start.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-43+', 
     question: "I get things done quickly.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-44+', 
     question: "I always know what I am doing.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-45-', 
     question: "I waste my time.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-46-', 
     question: "I find it difficult to get down to work.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-47-', 
     question: "I mess things up.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-48-', 
     question: "I don't put my mind to the task at hand.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-49-', 
     question: "I postpone making decisions.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-50-', 
     question: "I am easily distracted.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {/////////////////////////////////////////////////////////////////////////////////////////////////////////
     id: 'BFAS-51+', 
     question: "I like order.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-52+', 
     question: "I keep things tidy.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-53+', 
     question: "I follow a schedule.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-54+', 
     question: "I want everything to be 'just right'.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-55+', 
     question: "I see that rules are observed.", //
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-56+', 
     question: "I want every detail taken care of.", // 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-57-', 
     question: "I leave my belongings around.", // 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-58-', 
     question: "I am not bothered by messy people.", // '''''''''''''''''''''''''''''''''''''''''''
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-59-', 
     question: "I am not bothered by disorder.", // 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-60-', 
     question: "I dislike routine.", // ***************************************************
     labels: ['Disagree', 'Neutral', 'Agree']
    },

    {///////////////////////////////////////////////////////////////////////Extroversion-Assertiveness
     id: 'BFAS-61+', 
     question: "I make friends easily.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-62+', 
     question: "I warm up quickly to to others.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-63+', 
     question: "I show my feelings when I'm happy.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-64+', 
     question: "I have a lot of fun.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-65+', 
     question: "I laugh a lot.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },

    {
     id: 'BFAS-66-', 
     question: "I am hard to get to know.", // 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-67-', 
     question: "I keep others at a distance.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-68-', 
     question: "I reveal little about myself.", // talking to strangers on the bus???
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-69-', 
     question: "I rarely get caught up in the excitement.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-70-', 
     question: "I am not a very enthusiastic person.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {///////////////////////////////////////////////////////////////////////////////////////////
     id: 'BFAS-71+', 
     question: "I take charge.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-72+', 
     question: "I have a strong personality.", // 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-73+', 
     question: "I know how to captivate people.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-74+', 
     question: "I see myself as a good leader.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-75+', 
     question: "I can talk others into doing things.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-76+', 
     question: "I am the first to act.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-77-', 
     question: "I do not have an assertive personality.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-78-', 
     question: "I lack the talent for influencing people.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-79-', 
     question: "I wait for others to lead the way.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-80-', 
     question: "I hold back my opinions.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {/////////////////////////////////////////////////////OPENNESSS//////////////////////////////////
     id: 'BFAS-81+', 
     question: "I am quick to understand things.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-82+', 
     question: "I can handle a lot of information.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-F83+', 
     question: "I like to solve complex problems.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-F84+', 
     question: "I have a rich vocabularly.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-F85+', 
     question: "I think quickly.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-F86+', 
     question: "I formulate ideas clearly.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-F87-', 
     question: "I have difficulty understanding abstract ideas.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-88-', 
     question: "I avoid philosophical discussions.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-89-', 
     question: "I avoid difficult reading material.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-90-', 
     question: "I learn things slowly.", 
     labels: ['Disagree', 'Neutral', 'Agree']

  },
  {//////////////////////////////////////aesthetic sense/
     id: 'BFAS-90+',
     question: "I enjoy the beauty of nature.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-91+', 
     question: "I believe in the importance of art.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-92+', 
     question: "I love to reflect on things.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-95+', 
     question: "I get deeply immersed in music.", 
     labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-96+', 
     question: "I see beauty in things that others might not notice.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
     {
     id: 'BFAS-97+', 
     question: "I need a creative outlet.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-98-', 
     question: "I do not like poetry.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-99-', 
     question: "I seldom get lost in thought.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-100-', 
     question: "I seldom daydream.    ", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-101-', 
     question: "I seldom notice the emotional aspects of paintings and pictures.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    }
 
]);
//];
QUESTIONS.mindset = _.shuffle([
    { //naming scheme : ‘construct_humilityitemnumber_direction’
        id: 'PBR_1+',
        question: "I am ______ % responsible for who I am.",
        labels: ['0', '50', '100']
    },

    {
        id: 'PBR_2-',
        question: "If I’m running late, or I mess something up, I tend to blame external circumstances. ",   
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    
    {
        id: 'PBR_3+',
        question: "I take ______ % responsibility for what will happen to me during the next few months. ",
        labels: ['0', '50', '100']  
    },
    {
        id: 'PBR_4+',
        question: "It is ultimately my fault if I don’t end up seeing a project all the way through.",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'PBR_5+',
        question: "How well I do in life is _______ under my control." ,
        labels: ['Not really', 'Somewhat', 'Entirely']  
    },
    {
        id: 'PBR_6-',
        question: "I'd rather 'play it safe' instead of getting out of my comfort zone.",
        labels:  ['Disagree', 'Neutral', 'Agree']
        
    },
    {
        id: 'PBR_7-',
        question: "On the whole, personal shortcomings are impossible to overcome.",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'PBR_8-',
        question: "Who a person becomes depends on fate or luck.",
        labels: ['Disagree', 'Neutral', 'Agree'] 
    },
    {
        id: 'OPG_9+',
        question: "How familiar are you with the concept 'The purpose of life is to learn life’s lessons'? ",
        labels: ['Unfamiliar', 'Neutral', 'Familiar']  
    },
    {
        id: 'OPG_10+',
        question:  "There is something I can learn from every experience I have, regardless of how it makes me feel. ",
        labels: ['Disagree', 'Neutral', 'Agree']  
    },
    {
        id: 'OPG_11-',
        question: "Negative emotions and feelings are bad.",
        labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
        id: 'OPG_12+',
        question: "In general, I keep myself ‘open’ to criticism and feedback about my behavior.",
        labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
        id: 'OPG_13+',
        question: "I am _________ talking about my flaws with my friends.",
        labels: ['Uncomfortable', ' Neutral', 'Comfortable']
    },
    {
        id: 'OPG_14+',
        question: "I write down goals for improving aspects of my character or my behavior.",
        labels: ['Rarely', 'Sometimes', 'Frequently']
    },
    {
        id: 'OPG_15+',
        question: "There is something valuable I can learn from ________ the people I know.",
        labels: ['A few of', 'Some of', 'All of']
    },
    {
        id: 'OPG_16+',
        question: "In general, I have more _________  than most of the people that I know.",
        labels: ['Flaws', ' ', 'Virtues'] // scored as 2x distance away from 50.
    },
{
        id: 'OPG_17-',
        question: "Criticism is detrimental and unproductive.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
        id: 'OPG_18-',
        question: "I negatively criticize myself when I make a mistake.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
        id: 'IE_19+',
        question: "All people are of equal worth.",
        labels: ['Disagree', 'Neutral ', 'Agree'] 
    },
{
    id:'IE_20+',
    question:"I am of the same status as the strangers I pass by and interact with every day.",
    labels: ['Disagree', 'Neutral ', 'Agree']
},
{
    id:'IE_21+',
    question:"I am ________ most of the people I interact with.",
    labels: ['Less important than', 'As important as', 'More important than'] //2x distance from 50
},
{
    id:'IE_22-',
    question:'Some people don’t deserve my empathy or attention.',
labels: ['Disagree', 'Neutral', 'Agree       ']
},

{
    id:'IE_23-',
    question:'Hitler was evil / less than human.',
    labels:['Disagree', 'Neutral', 'Agree']
},
{
    id:'IE_24+',
    question:'I make eye contact with homeless people when I pass them.',
    labels:['Rarely', 'Sometimes', 'Frequently']
},
{
    id:'IE_25-',
    question:'I get intimidated by people who are smart, or pretty, or both.',
    labels:['Rarely', 'Sometimes', 'Frequently']
},
{
    id:'IE_26-',
    question: 'I use a ‘1-10’ scale when thinking about potential romantic partners.',
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
	self.phases = [QUESTIONS.p, QUESTIONS.mindset];
    //self.phases = [QUESTIONS.mindset];
    //self.phases = [QUESTIONS.sample ];

	// The maximum number of questions per page
	self.PER_PAGE = 24;

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
			// questions!
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

		$('.phased-questions .slider')
            .noUiSlider(self.sliderOptions)
            .noUiSlider_pips({
                 mode: 'values',
                 values: [10,50,90], //make sure all of these numbers are divisable by the 'density value', throws bug otherwise
                 density: 5
            });
            

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

		// questions have default values
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
        $('input').each(function(i, val) {
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
				//psiTurk.computeBonus('compute_bonus', finish);
                psiTurk.completeHIT();
			},
			error: prompt_resubmit
		});
	};

	// Load the questionnaire snippet
	psiTurk.showPage('postquestionnaire.html');
	psiTurk.recordTrialData({ phase: 'postquestionnaire', status: 'begin' });

    $("#postquiz").submit(function(e){
	//$("#next").click(function() {
        e.preventDefault();
		record_responses();
		psiTurk.saveData({
			success: function(){
				//psiTurk.computeBonus('compute_bonus', function() {
                    // TO DO TOMORROW: psiturk.pageload (debrief)
					psiTurk.completeHIT(); // when finished saving compute bonus, the quit
				//psiTurk.showPage('debriefing.html')
                //});
			},
			error: prompt_resubmit
		});
	});


};

/*********************************************
//debrie

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
