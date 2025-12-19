#!/usr/bin/env python3
"""
Quickstart Agentic Project - A simple agent with LLM reasoning and tool execution.
"""
import os
import sys
from typing import Dict, Any, List, Callable


# Simple Tools
class Tools:
    """Collection of simple tools the agent can use."""
    
    @staticmethod
    def calculator(operation: str) -> str:
        """
        Simple calculator tool that evaluates mathematical expressions.
        
        Args:
            operation: Mathematical expression to evaluate (e.g., "2 + 2", "10 * 5")
        
        Returns:
            Result of the calculation as a string
        """
        try:
            # Safety: Only allow basic math operations
            allowed_chars = set("0123456789+-*/(). ")
            if not all(c in allowed_chars for c in operation):
                return "Error: Invalid characters in expression"
            
            result = eval(operation)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def get_time() -> str:
        """Get current date and time."""
        from datetime import datetime
        return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    @staticmethod
    def echo(message: str) -> str:
        """Echo a message back."""
        return f"Echo: {message}"


class SimpleAgent:
    """
    A simple agent that can reason using an LLM and execute tools.
    """
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initialize the agent.
        
        Args:
            model: LLM model to use (default: gpt-3.5-turbo)
        """
        self.model = model
        self.tools = Tools()
        self.available_tools = {
            "calculator": self.tools.calculator,
            "get_time": self.tools.get_time,
            "echo": self.tools.echo,
        }
        
        # Check for API key
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("⚠️  Warning: OPENAI_API_KEY not set. Running in demo mode.")
            self.demo_mode = True
        else:
            self.demo_mode = False
            try:
                import openai
                self.client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                print("⚠️  Warning: openai package not installed. Running in demo mode.")
                self.demo_mode = True
    
    def _call_llm(self, prompt: str) -> str:
        """
        Call the LLM with a prompt.
        
        Args:
            prompt: The prompt to send to the LLM
        
        Returns:
            LLM response
        """
        if self.demo_mode:
            # Demo mode: Simple rule-based responses
            if "calculate" in prompt.lower():
                # Extract numbers and operators from the prompt
                import re
                # Find pattern like "25 * 4" or "15+27"
                match = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', prompt)
                if match:
                    calc = match.group(1)
                    return f"I'll calculate that for you: calculator({calc})"
            elif "time" in prompt.lower():
                return "I'll get the current time for you: get_time()"
            else:
                # Extract message after common prefixes
                msg = prompt
                for prefix in ["echo:", "echo "]:
                    if prefix in prompt.lower():
                        msg = prompt[prompt.lower().index(prefix) + len(prefix):].strip()
                        break
                return f"I'll echo your message: echo({msg})"
        else:
            # Real LLM call
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": 
                         "You are a helpful agent. You have access to these tools: "
                         "calculator(operation), get_time(), echo(message). "
                         "When you need to use a tool, respond with the exact format: TOOL_NAME(arguments)"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=150
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                return f"Error calling LLM: {str(e)}"
    
    def _parse_tool_call(self, response: str) -> tuple[str, str] | None:
        """
        Parse tool call from LLM response.
        
        Args:
            response: LLM response that may contain a tool call
        
        Returns:
            Tuple of (tool_name, arguments) or None if no tool call found
        """
        import re
        
        # Look for pattern: tool_name(arguments)
        pattern = r'(\w+)\((.*?)\)'
        matches = re.findall(pattern, response)
        
        for tool_name, args in matches:
            if tool_name in self.available_tools:
                return tool_name, args.strip('\'"')
        
        return None
    
    def run(self, task: str) -> str:
        """
        Execute a task using the agent.
        
        Args:
            task: The task description
        
        Returns:
            Final result
        """
        print(f"\n🤖 Agent received task: {task}")
        print(f"💭 Reasoning...")
        
        # Step 1: Ask LLM to reason about the task
        llm_response = self._call_llm(task)
        print(f"🧠 Agent thinks: {llm_response}")
        
        # Step 2: Check if LLM wants to use a tool
        tool_call = self._parse_tool_call(llm_response)
        
        if tool_call:
            tool_name, args = tool_call
            print(f"🔧 Executing tool: {tool_name}({args})")
            
            # Execute the tool
            try:
                # Handle tools that don't take arguments
                if tool_name == "get_time":
                    result = self.available_tools[tool_name]()
                else:
                    result = self.available_tools[tool_name](args)
                print(f"✅ Result: {result}")
                return result
            except Exception as e:
                error_msg = f"Error executing tool: {str(e)}"
                print(f"❌ {error_msg}")
                return error_msg
        else:
            # No tool needed, return LLM response
            print(f"✅ Final answer: {llm_response}")
            return llm_response


def main():
    """Main entry point for the quickstart agent."""
    print("=" * 60)
    print("🚀 Quickstart Agentic Project")
    print("=" * 60)
    
    # Initialize agent
    agent = SimpleAgent()
    
    # Example tasks
    example_tasks = [
        "Calculate 25 * 4",
        "What time is it?",
        "Echo: Hello, Agentic World!",
    ]
    
    # Check if task provided as command line argument
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        result = agent.run(task)
    else:
        # Run example tasks
        print("\n📋 Running example tasks...\n")
        for task in example_tasks:
            result = agent.run(task)
            print()
    
    print("=" * 60)
    print("✨ Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
