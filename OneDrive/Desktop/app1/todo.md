# CURSOR PROMPT: Fix Quiz Question Skipping & AI French Language

## CRITICAL ISSUES TO FIX

### ISSUE 1: Quiz Questions Skipping

*Problem*: Quiz jumps from question 1 → 3 → 5, skipping questions 2, 4, 6
*Required Fix*: Force sequential progression 1→2→3→4→5→6→7

### ISSUE 2: AI Speaking English Instead of French

*Problem*: AI responds in English but should respond in French (all subjects taught in French)
*Required Fix*: AI must respond only in French using platform’s AI system

## TASK 1: FIX QUIZ QUESTION SEQUENCING

**File: src/screens/student/QuizScreen.tsx**

*Problem*: currentQuestionIndex is incrementing incorrectly, causing questions to skip
*Solution*: Fix the question navigation logic

typescript
// Fix the selectAnswer/nextQuestion function
const goToNextQuestion = () => {
  if (currentQuestionIndex < quiz.questions.length - 1) {
    setCurrentQuestionIndex(currentQuestionIndex + 1); // Increment by 1 only
  } else {
    // Show results only after ALL 7 questions
    setShowResults(true);
  }
};

// Ensure answer selection doesn't auto-advance
const selectAnswer = (answerIndex: number) => {
  setSelectedAnswer(answerIndex);
  // DO NOT auto-advance - wait for student to click Next
};

// Add Next button that student must click
const NextButton = () => (
  <TouchableOpacity 
    style={styles.nextButton}
    onPress={goToNextQuestion}
    disabled={selectedAnswer === null}
  >
    <Text style={styles.nextButtonText}>
      {currentQuestionIndex === quiz.questions.length - 1 ? 'Finish Quiz' : 'Next Question'}
    </Text>
  </TouchableOpacity>
);


*Key Requirements*:

- Student answers question 1
- Student must click “Next Question” button
- Shows question 2 (not 3)
- Student answers question 2
- Student clicks “Next Question”
- Shows question 3 (not 5)
- Continue until all 7 questions completed
- Show results only after question 7

## TASK 2: FIX AI TO RESPOND IN FRENCH

**File: src/screens/student/ChatScreen.tsx**

*Problem*: AI not using platform’s French AI system
*Solution*: Ensure AI calls platform endpoint with proper French context

typescript
const sendMessage = async (messageText: string) => {
  if (!messageText.trim() || !user?.id) return;
  
  // Add user message
  const userMessage = {
    id: Date.now().toString(),
    role: 'user',
    content: messageText.trim(),
    timestamp: new Date(),
  };
  setMessages(prev => [...prev, userMessage]);
  setInputText('');
  setIsLoading(true);

  try {
    // Call platform AI with French context
    const response = await studentAPI.sendMessage(
      messageText.trim(),
      user.id,
      selectedSubject || 'Mathématique', // Pass French subject
      'text'
    );

    if (response.success && response.data?.message) {
      const aiMessage = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: response.data.message, // Platform returns French response
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, aiMessage]);
    }
  } catch (error) {
    console.error('AI Error:', error);
  } finally {
    setIsLoading(false);
  }
};


*Key Requirements*:

- AI responds in French like: “Salut élève! Je peux t’aider avec les mathématiques…”
- Uses platform’s /api/chat endpoint (already in platform-api.ts)
- Maintains conversation memory from platform database
- Suggests quizzes in French: “Veux-tu faire un quiz sur ce sujet?”

## CRITICAL IMPLEMENTATION RULES

### DO NOT CHANGE:

- UI design or colors
- Button layouts or styles
- Subject selector appearance
- Chat bubble design
- Any visual elements

### ONLY CHANGE:

- Quiz question progression logic (prevent skipping)
- AI language response (ensure French)
- API integration to use platform system

### FILES TO MODIFY:

1. src/screens/student/QuizScreen.tsx - Fix question sequencing only
1. src/screens/student/ChatScreen.tsx - Fix AI French responses only

### DO NOT MODIFY:

- src/services/platform-api.ts (already correct)
- Any UI/styling files
- Any other components

## SUCCESS TEST

### Quiz Test:

1. Click “Quiz Game” button
1. See “Question 1 of 7”
1. Select answer A, B, C, or D
1. Click “Next Question”
1. See “Question 2 of 7” (not 3!)
1. Continue through ALL 7 questions sequentially
1. See results after question 7

### AI Test:

1. Type: “Bonjour, aide-moi avec les fractions”
1. AI responds in French: “Salut! Je peux t’expliquer les fractions…”
1. AI continues conversation in French only
1. AI suggests quiz in French: “Veux-tu faire un quiz sur les fractions?”

Fix these TWO issues only - keep everything else exactly the same!