/*
 * Requires:
 *  psiturk.js
 *  utils.js
 */

// Initalize psiturk object
var psiTurk = PsiTurk();

// All pages to be loaded
var pages = [
    "instruct.html",
    "test.html",
    "postquestionnaire.html"
];

psiTurk.preloadPages(pages);

//big five aspect scales:

var QUESTIONS_BFAS = _.shuffle([ //anyway to shuffle the two large blocks?/////////////////
    
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
     id: 'BFAS-F7-'
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
     question: "I rarely feel depressed."
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
     {//
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
     question: "I seldom daydream", 
      labels: ['Disagree', 'Neutral', 'Agree']
    },
    {
     id: 'BFAS-101-', 
     question: "I seldom notice the emotional aspects of paintings and pictures.", 
      labels: ['Disagree', 'Neutral', 'Agree']
    }
 
        
]);

 var QUESTIONSmindset = _.shuffle([ //anyway to shuffle the two large blocks?/////////////////
    {
     id: 'OPG1+',
     question: "Please estimate the following: On the whole, I am _____ percent responsible for who I am.",
     labels: ['0', '50', '100'] 
    },
    {
     id: 'OPG2-',
     question: "If I'm running late or I mess something up, it's usually due to forces beyond my control.",   //more locus of control     
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },
    {
     id: 'OPG3+',
     question: "I am entirely responsible for everything that happens to me, regardless of external circumstances." ,    
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },

    {
     id: 'OPG4+',
     question: "No matter what happens or how I feel, it is ultimately on me to see something that I want done all of the way through. " ,     
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },

    {
     id: 'OPG5+',
     question: "The purpose of life is to learn life's lessons."  ,      
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },
    {
     id: 'OPG6+',
     question: "There is something I can learn from every experience, regardless of how good, bad, boring or interesting it is." ,       
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },
    {
     id: 'OPG7-',
     question: "Negative emotions should be avoided as much as possible."  ,      
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },
    {
     id: 'OPG8+',
     question: "In general, I keep myself 'open' to criticism and feedback about my behaviour.",        
     labels: ['Disagree', 'Neutral', 'Agree']  // 
    },
    {
     id: 'OPG9+',
     question: "I am _____ talking about my flaws with my friends.",        
     labels: ['Uncomfortable', 'Neutral', 'Comfortable']  // 

    },
    {
     id: 'OPG10+',
     question: "I am ______ trying to work on an aspect of my character.",        
     labels: ['Never', 'Sometimes', 'Always']  // 

    },
    
    {
     id: 'OPG11+',
     question:  "There is something that I can learn from ______ the people that I know.",       
     labels: ['A few of', 'Some of', 'All of']  // 
    },
 
    {
     id: 'OPG12+',
     question: "All people are of equal worth.", 
     labels: ['Disagree','Neutral','Agree']  
    },
    {
     id: 'OPG12.5+',
     question: "All people that I pass by, run into or interact with day-to-day are of equal worth.", 
     labels: ['Disagree','Neutral','Agree']  
    },
    {
     id: 'OPG13-',//??????????
     question: "If I had to, I could rank where in the social status hierarchy my friends would be." ,   
     labels: ['Disagree', 'Neutral', 'Agree']   
    }, 
    {
     id: 'OPG14-',
     question: "Certain people don't deserve my empathy or attention." ,   
     labels: ['Disagree', 'Neutral', 'Agree']   
    },     

    ]);   


//QUESTION KEY IS: NOT CURRENT
// Task object to keep track of the current phase
var currentview;


/********************
* HTML manipulation
*
* All HTML files in the templates directory are requested
* from the server when the PsiTurk object is created above. We
* need code to get those pages from the PsiTurk object and
* insert them into the document.
*
********************/


/*************************
* INSTRUCTIONS
*************************/

var Instructions = function(pages) {
    var currentscreen = 0,
       timestamp;
       instruction_pages = pages;

    var next = function() {
     psiTurk.showPage(instruction_pages[currentscreen]);
     $('.continue').click(function() {
       buttonPress();
     });

     currentscreen = currentscreen + 1;

     // Record the time that an instructions page is presented
     timestamp = new Date().getTime();
    };

    var buttonPress = function() {

     // Record the response time
     var rt = (new Date().getTime()) - timestamp;
     psiTurk.recordTrialData(["INSTRUCTIONS", currentscreen, rt]);

     if (currentscreen == instruction_pages.length) {
       finish();
     } else {
       next();
     }

    };

    var finish = function() {
     // Record that the user has finished the instructions and
     // moved on to the experiment. This changes their status code
     // in the database.
     //psiTurk.finishInstructions();

     // Move on to the experiment
     currentview = new TestPhase();
    };

    next();
};

/********************
* DERRPY TEST     *
********************/

var TestPhase = function() {

    var PER_PAGE = 2;
    var PAGE_INDEX = 0;

    // Load the test.html snippet into the body of the page
    psiTurk.showPage('test.html');
    var template = _.template($('#question-template').html());

    // template works like this:
    /*
    template({
     question: 'This is a question',
     labels: ['right', 'center', 'left']
    });
    */

    /*
    var next = function() {
     if (stims.length === 0) {
       finish();
     } else {
       stim = stims.shift();
       show_word( stim[0], stim[1] );
       wordon = new Date().getTime();
       listening = true;
       $('#query').html(resp_prompt).show();
     }
    };
    */

    $(document).on('click', 'nav a', function(e) {
     e.preventDefault();
     var nav = $(e.currentTarget);
     if (nav.hasClass('disabled')) return;

     if (nav.hasClass('prev')) {
       PAGE_INDEX--;
       render();
     } else if (nav.hasClass('next')) {
       PAGE_INDEX++;
       render();
     }
    });

    $(document).on('click', '.finish.button', function() {
     e.preventDefault();
     // finish()...
    });

    var isFirstPage = function() { return PAGE_INDEX === 0; };
    var isLastPage = function() { return Math.floor(QUESTIONSp.length / PER_PAGE) === PAGE_INDEX; };

    var render = function() {
     // $('input[type=range]').fancyjQueryRangePlugin({
     //   options: true
     // });

     $('.test .page-num').text(PAGE_INDEX + 1);
     $('.test a.prev').toggleClass('disabled', isFirstPage());
     $('.test a.next').toggleClass('disabled', isLastPage());

     var startIndex = PER_PAGE * PAGE_INDEX;
     var questions = _.map(QUESTIONSp.slice(startIndex, startIndex + PER_PAGE), template);
     $('.test .questions').html(questions.join("\n"));
    };

    var finish = function() {
     // psiTurk.recordTrialData(["TEST", stim[0], stim[1], stim[2], response, hit, rt]);
     currentview = new Questionnaire();
    };

    // Start the test
    render();
};


/****************
* Questionnaire *
****************/

var Questionnaire = function() {

    var error_message = "<h1>Oops!</h1><p>Something went wrong submitting your HIT. This might happen if you lose your internet connection. Press the button to resubmit.</p><button id='resubmit'>Resubmit</button>";

    record_responses = function() {

     psiTurk.recordTrialData(['postquestionnaire', 'submit']);

     $('textarea').each( function(i, val) {
       psiTurk.recordUnstructuredData(this.id, this.value);
     });
     $('select').each( function(i, val) {
       psiTurk.recordUnstructuredData(this.id, this.value);
     });

    };

    finish = function() {
     debriefing();
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
         finish();
       },
       error: prompt_resubmit}
     );
    };

    // Load the questionnaire snippet
    psiTurk.showPage('postquestionnaire.html');
    psiTurk.recordTrialData(['postquestionnaire', 'begin']);

    $("#continue").click(function () {
     record_responses();
     psiTurk.teardownTask();
       psiTurk.saveData({success: finish, error: prompt_resubmit});
    });

};

var debriefing = function() { window.location="/debrief?uniqueId=" + psiTurk.taskdata.id; };

/*******************
 * Run Task
 ******************/
$(window).load(function(){
     currentview = new Instructions([
     "instruct.html"
    ]);
});

// vi: noexpandtab tabstop=4 shiftwidth=4
