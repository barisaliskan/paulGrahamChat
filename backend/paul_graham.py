import openai
from datetime import datetime
import json

class PaulGrahamAgent:
    def __init__(self):
        self.system_prompt = self._create_system_prompt()
        self.max_tokens = 600
        self.temperature = 0.7
        
    def _create_system_prompt(self):
        """Create Paul Graham's characteristic system prompt"""
        return """You are Paul Graham, co-founder of Y Combinator and influential technology essayist.

PERSONALITY & STYLE:
- Write in a conversational, direct tone - like you're talking to a smart friend
- Use simple, clear language but provide deep insights
- Be thoughtful and nuanced, avoid black-and-white thinking
- Show genuine curiosity about ideas and people
- Sometimes disagree or challenge assumptions politely

KNOWLEDGE BASE:
- Co-founded Y Combinator (2005) - funded 1000+ startups
- Previously: founded Viaweb (sold to Yahoo for $49M), studied painting, PhD in CS
- Written influential essays on startups, programming, inequality, education
- Programming languages: Lisp enthusiast, also Python, JavaScript
- Investment philosophy: fund founders, not just ideas

COMMUNICATION PATTERNS:
- Often use analogies and concrete examples
- Reference personal experiences with startups and founders
- Ask thoughtful follow-up questions
- End with interesting observations or implications
- Keep responses focused (not too long)
- Sometimes reference your essays when relevant

TOPICS YOU CARE ABOUT:
- What makes startups succeed/fail
- Programming and technology trends  
- Writing and clear thinking
- Education and learning
- Economic inequality and fairness
- The future of work and creativity
- Silicon Valley culture and problems

RESPONSE STYLE:
- Start directly, don't announce "As Paul Graham..."
- Use "I think" or "In my experience" naturally
- Share specific examples when possible
- Be humble about predictions and uncertainties
- Show interest in the other person's perspective"""

    def generate_response(self, user_message, api_key, conversation_history=None):
        """Generate Paul Graham-style response"""
        try:
            # Set API key
            openai.api_key = api_key
            
            # Prepare messages for API
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add conversation history (last 8 messages to manage token limits)
            if conversation_history:
                recent_history = conversation_history[-8:]
                for msg in recent_history:
                    messages.append({
                        "role": msg.get("role", "user"),
                        "content": msg.get("content", "")
                    })
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=0.9,
                frequency_penalty=0.1,
                presence_penalty=0.1
            )
            
            # Extract response
            paul_response = response.choices[0].message.content.strip()
            
            return paul_response
            
        except openai.error.AuthenticationError:
            return "I'm having trouble with my API access. Could you check your OpenAI API key?"
        
        except openai.error.RateLimitError:
            return "I'm getting too many requests right now. Could you try again in a moment?"
        
        except openai.error.InvalidRequestError as e:
            return f"There seems to be an issue with the request: {str(e)}"
        
        except Exception as e:
            return f"I encountered an unexpected error: {str(e)}. This might be a temporary issue."
    
    def get_timestamp(self):
        """Get current timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_sample_questions(self):
        """Get sample questions for testing"""
        return [
            "What makes a startup successful?",
            "How should I approach learning programming?",
            "What's your advice for first-time founders?",
            "Why do you think Lisp is underrated?",
            "What's wrong with the current education system?",
            "How do you identify good startup ideas?",
            "What's the biggest mistake startups make?",
            "How has Y Combinator changed over the years?"
        ]
